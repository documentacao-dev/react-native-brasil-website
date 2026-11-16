#!/usr/bin/env python3
"""Sincroniza este repositório com o upstream (facebook/react-native-website)
preservando as traduções e marcando o que precisa ser retraduzido.

Uso (a partir da raiz do repositório, com a árvore limpa):

    git fetch upstream main
    python3 tool/traducao/sincronizar_upstream.py [--alvo upstream/main]

O que o script faz:

1. Lê o último commit do upstream já sincronizado em
   tool/traducao/ultimo-sync-upstream.txt (a "base").
2. Inicia um merge com o alvo cuja árvore é exatamente a do upstream
   (`git merge -s ours` + `git read-tree`), para que a estrutura nova do
   upstream seja sempre respeitada.
3. Para cada arquivo que o React Native Brasil alterou em relação à base
   (páginas traduzidas, sidebars, componentes e configuração do site):
   - descobre o caminho novo (mesmo caminho ou renomeação detectada pelo git);
   - se o original em inglês não mudou, copia a versão do fork;
   - se mudou, faz merge de 3 vias (versão pt, inglês base, inglês novo).
     Sem conflito, grava o resultado. Com conflito, grava o arquivo com
     marcadores diff3 em .traducao-pendente/<caminho novo> e deixa o
     inglês novo no lugar, SEM a flag ia-translated (a página volta a
     aparecer como pendente no TODO).
4. Roda semear_versao.py: se o upstream cortou uma versão nova, a versão
   estável (website/versioned_docs/version-<atual>/) é semeada a partir das
   páginas traduzidas de docs/, e os rótulos do sidebar dela são traduzidos.
5. Grava o relatório em .traducao-pendente/RELATORIO.md e atualiza
   ultimo-sync-upstream.txt para o alvo.

Depois: resolva cada arquivo de .traducao-pendente/ (veja CLAUDE.md),
rode tool/traducao/verificar.py, apague .traducao-pendente/ e faça o commit.
"""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from escopo import ROOT, versao_atual  # noqa: E402
import semear_versao  # noqa: E402

SYNC = ROOT / 'tool' / 'traducao' / 'ultimo-sync-upstream.txt'
PEND = ROOT / '.traducao-pendente'
# Arquivos exclusivos do React Native Brasil ou que não devem ser mesclados.
IGNORAR = ('tool/traducao/', '.traducao-pendente/', 'CLAUDE.md', 'plan/',
           '.claude/', 'TODO-TRADUCAO.md')
# Arquivos do upstream que o fork NÃO quer (automações que só fazem sentido no
# facebook/react-native-website). Eles voltam a cada sync com a árvore do
# upstream, então são removidos de novo. Hoje não há nenhum: o pre-merge.yml
# (lint e build) e o stale-bot.yml continuam úteis aqui.
REMOVIDOS_NO_FORK = ()


def git(*args, check=True):
    r = subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        sys.exit(f'git {" ".join(args)} falhou:\n{r.stderr}')
    return r.stdout


def show(ref, caminho):
    r = subprocess.run(['git', '-C', str(ROOT), 'show', f'{ref}:{caminho}'],
                       capture_output=True)
    return r.stdout if r.returncode == 0 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--alvo', default='upstream/main')
    a = ap.parse_args()

    if git('status', '--porcelain').strip():
        sys.exit('A árvore de trabalho precisa estar limpa.')
    base = SYNC.read_text().strip()
    alvo = git('rev-parse', a.alvo).strip()
    if base == alvo:
        sys.exit('Já sincronizado com ' + alvo)
    head = git('rev-parse', 'HEAD').strip()
    versao_antes = versao_atual()

    arquivos_alvo = set(git('ls-tree', '-r', '--name-only', alvo).split())

    renomes = {}
    for linha in git('-c', 'diff.renameLimit=50000', 'diff', '-M70%',
                     '--name-status', base, alvo).splitlines():
        partes = linha.split('\t')
        if partes[0].startswith('R'):
            renomes[partes[1]] = partes[2]

    def area(c):
        """Pasta que delimita uma renomeação válida: cada versão de
        versioned_docs é uma área; docs/ é outra; o resto, a pasta de topo."""
        partes = c.split('/')
        if c.startswith('website/versioned_docs/') and len(partes) > 2:
            return '/'.join(partes[:3])
        return partes[0] if partes[0] != 'website' else '/'.join(partes[:2])

    def caminho_novo(p):
        if p in arquivos_alvo:
            return p
        # O upstream converte páginas de .md para .mdx (e vice-versa).
        raiz, ext = p.rsplit('.', 1) if '.' in p else (p, '')
        for outra in {'md': ('mdx',), 'mdx': ('md',)}.get(ext, ()):
            if f'{raiz}.{outra}' in arquivos_alvo:
                return f'{raiz}.{outra}'
        # Renomeação detectada pelo git, desde que fique na mesma área: o git
        # costuma parear uma página apagada de docs/ com a cópia dela numa
        # versão de versioned_docs/, o que não é renomeação.
        n = renomes.get(p)
        if n in arquivos_alvo and area(n) == area(p):
            return n
        return None

    alterados = [l.split('\t') for l in git('diff', '--name-status', '--no-renames',
                                             base, head).splitlines()]
    alterados = [(s, p) for s, p in alterados
                 if s in ('M', 'A') and not p.startswith(IGNORAR)]

    print(f'Base {base[:9]} → alvo {alvo[:9]}; {len(alterados)} arquivos do fork.')
    exclusivos_br = [p for p in git('ls-tree', '-r', '--name-only', head).split()
                     if p.startswith(IGNORAR)]
    git('merge', '-q', '--no-commit', '--no-ff', '-s', 'ours', alvo)
    git('read-tree', '-u', '--reset', alvo)
    # Arquivos exclusivos do fork que não passam pelo merge (CLAUDE.md,
    # .claude/, plan/, tool/traducao/...): o read-tree os apaga porque não
    # existem no upstream, então restaura do HEAD.
    if exclusivos_br:
        git('checkout', head, '--', *exclusivos_br)
    for p in REMOVIDOS_NO_FORK:
        if (ROOT / p).exists():
            git('rm', '-qf', '--', p)

    copiados, mesclados, conflitos, sem_destino, exclusivos = [], [], [], [], []
    mapeados = set()
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for status, p in alterados:
            br = show(head, p)
            en_base = show(base, p)
            n = caminho_novo(p)
            if n is None:
                if en_base is None:  # arquivo exclusivo do fork (firebase.json...)
                    (ROOT / p).parent.mkdir(parents=True, exist_ok=True)
                    (ROOT / p).write_bytes(br)
                    exclusivos.append(p)
                else:
                    sem_destino.append(p)
                continue
            mapeados.add(p)
            en_novo = show(alvo, n)
            if en_base == en_novo or en_base is None:
                (ROOT / n).write_bytes(br)
                copiados.append(n)
                continue
            (tmp / 'br').write_bytes(br)
            (tmp / 'base').write_bytes(en_base)
            (tmp / 'novo').write_bytes(en_novo)
            r = subprocess.run(['git', 'merge-file', '-p', '--diff3', '-L', 'pt',
                                '-L', 'base_en', '-L', 'new_en', str(tmp / 'br'),
                                str(tmp / 'base'), str(tmp / 'novo')],
                               capture_output=True)
            if r.returncode == 0:
                (ROOT / n).write_bytes(r.stdout)
                mesclados.append(n)
            else:
                destino = PEND / n
                destino.parent.mkdir(parents=True, exist_ok=True)
                destino.write_bytes(r.stdout)
                conflitos.append((n, r.stdout.count(b'\n<<<<<<< pt')))

    # Nenhum arquivo que só existe no fork pode desaparecer sem ter sido tratado.
    arquivos_base = set(git('ls-tree', '-r', '--name-only', base).split())
    sumidos = [p for p in git('ls-tree', '-r', '--name-only', head).split()
               if p not in arquivos_alvo and p not in arquivos_base
               and not (ROOT / p).exists()
               and p not in sem_destino and p not in mapeados]
    if sumidos:
        print('ATENÇÃO: arquivos do fork que sumiram no merge '
              '(restaure com git checkout HEAD -- <arquivo> se forem necessários):')
        for p in sumidos[:50]:
            print('   ', p)

    # Versão estável nova (ou ainda em inglês): semeia a partir de docs/.
    versao = versao_atual()
    # Irmã de docs/ em conflito neste sync: semeia com a tradução de antes do
    # sync (HEAD) contra o inglês da base.
    semeadas, conflitos_v, sem_irma = (semear_versao.semear(versao, alvo, antes=(head, base))
                                       if versao else ([], [], []))
    rotulos = semear_versao.traduzir_sidebar(versao, alvo, antes=(head, base)) if versao else 0

    SYNC.write_text(alvo + '\n')
    PEND.mkdir(exist_ok=True)
    todos_conflitos = conflitos + conflitos_v
    rel = [f'# Sincronização {base[:9]} → {alvo[:9]}', '',
           f'- Copiados sem mudança no inglês: {len(copiados)}',
           f'- Mesclados automaticamente: {len(mesclados)}',
           f'- **Com conflito (retraduzir)**: {len(todos_conflitos)}',
           f'- Removidos ou consolidados no upstream: {len(sem_destino)}',
           f'- Exclusivos do fork (restaurados): {len(exclusivos)}',
           f'- Versão estável: {versao_antes} → {versao}; semeadas a partir de docs/: '
           f'{len(semeadas)}, aguardando a irmã em docs/ (rode semear_versao.py depois de resolver .traducao-pendente/) ou sem irmã: {len(sem_irma)}, '
           f'rótulos do sidebar traduzidos: {rotulos}', '',
           '## Com conflito', '',
           'Cada arquivo abaixo está em `.traducao-pendente/<caminho>` com marcadores',
           'diff3 (`pt` / `base_en` / `new_en`). No repositório ficou o inglês novo.', '']
    rel += [f'- [ ] `{n}` ({c} bloco(s))' for n, c in sorted(todos_conflitos)]
    rel += ['', '## Removidos ou consolidados no upstream', '',
            'Não existem mais com o mesmo conteúdo. Se a página nova que os',
            'substitui ainda não está traduzida, a tradução antiga pode servir de',
            'referência (`git show <commit-anterior>:<caminho>`).', '']
    rel += [f'- `{p}`' for p in sorted(sem_destino)]
    (PEND / 'RELATORIO.md').write_text('\n'.join(rel) + '\n')
    print('\n'.join(rel[:9]))
    print('\nRelatório: .traducao-pendente/RELATORIO.md')


if __name__ == '__main__':
    main()
