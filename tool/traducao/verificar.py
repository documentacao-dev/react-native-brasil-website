#!/usr/bin/env python3
"""Checagens determinísticas das traduções do React Native Brasil.

    python3 tool/traducao/verificar.py [--ref upstream/main] [--estrito] [arquivos...]

Sem arquivos, confere todas as páginas marcadas com ia-translated dentro do
escopo (tool/traducao/escopo.py) e as checagens globais. Erros fazem o script
sair com código 1; avisos só são listados, a menos que se passe --estrito.

O original em inglês de cada página é `git show <ref>:<caminho>` (mesmo
caminho no upstream). Para conferir só a estrutura contra o inglês que o fork
já incorporou, sem acusar defasagem, use
`--ref $(cat tool/traducao/ultimo-sync-upstream.txt)`.

Checagens:

ERROS
- conflito:     marcadores de merge (<<<<<<<, |||||||, >>>>>>>) no arquivo.
- frontmatter:  YAML inválido; `ia-translated` que não é o booleano `true` de
                primeiro nível; campo que tem valor no inglês e ficou vazio.
- frontmatter-id: `id`, `slug`, `sidebar_position`, `hide_table_of_contents`,
                `authors`, `tags`, `date` ou `image` diferente do inglês (mudar
                `id`/`slug` quebra rota, sidebar e links).
- frontmatter-en: `title`, `sidebar_label` ou `description` idêntico ao inglês
                e em inglês (3+ palavras com palavra-função inglesa).
- flag:         `ia-translated` fora do frontmatter, ou o comentário
                `<!-- ia-translated: true -->` fora da primeira linha de uma
                página sem frontmatter.
- placeholder:  avisos de "tradução pendente" deixados no texto.
- ingles:       página marcada como traduzida cuja prosa está em inglês
                (proporção de palavras-função em inglês >= 0.7).
- estrutura:    número de cercas de código, títulos, admonitions `:::` (e a
                sequência dos tipos: note, tip, info, warning, caution, danger),
                tags de componente JSX (`<Tabs>`, `<TabItem>`...) ou ids
                `{#id}` diferente do inglês; linhas `import`/`export` do MDX
                diferentes do inglês (são código); rótulo de link
                `[texto][rótulo]` sem definição.
- defasada:     o inglês da página mudou no upstream desde o último sync
                (tool/traducao/ultimo-sync-upstream.txt): rode
                sincronizar_upstream.py.
- pendente:     .traducao-pendente/ ainda tem arquivos para resolver.
- ancora:       título traduzido cujo slug difere do slug em inglês e que não
                tem `{#id}` explícito (links #ancora de outras páginas
                quebrariam). Corrija com tool/traducao/ancorar_titulos.py.
- link-interno: link para âncora da própria página (`](#id)`) que não existe
                (títulos, `id="..."` e parciais importados incluídos).
- analytics:    analytics/telemetria do reactnative.dev oficial no código do
                site (website/, fora o conteúdo .md/.mdx): gtag, G-58L13S6BDP,
                googletagmanager, plugin-google-gtag, surveymonkey.com/,
                facebookAppId. O sync traz de volta o que o upstream tem;
                remova antes do commit. Conferido em toda execução sem arquivos.

AVISOS
- parcial:      proporção de inglês entre 0.3 e 0.7 (tradução incompleta).
- defs-link:    número de definições de link diferente do original.

O que não fica aqui: a compilação do MDX, conferida pelo job `build` do
.github/workflows/pre-merge.yml (`yarn build`) em todo PR.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit('Falta o PyYAML: pip install pyyaml')

sys.path.insert(0, str(Path(__file__).resolve().parent))
from escopo import (ROOT, FLAG_COMENTARIO, FLAG_COMENTARIO_MDX, FLAG_FM,  # noqa: E402
                    frontmatter, no_escopo, pastas, traduzida)
import ancorar_titulos as anc  # noqa: E402

SYNC = ROOT / 'tool' / 'traducao' / 'ultimo-sync-upstream.txt'
PEND = ROOT / '.traducao-pendente'

CONFLITO = re.compile(r'^(<{7} |\|{7} |>{7} )', re.M)
PLACEHOLDER = re.compile(
    r'note for translators|to be translated|marked for translation'
    r'|tradu[çc][ãa]o pendente|todo:? traduzir|\[traduzir\]', re.I)
CERCA = re.compile(r'^\s*(```|~~~)', re.M)
ADMONITION = re.compile(r'^\s*:::(\w+)', re.M)
FECHA_ADMONITION = re.compile(r'^\s*:::\s*$', re.M)
JSX = re.compile(r'<([A-Z][\w.]*)')
IDS = re.compile(r'\{#[^}\s]+\}')
IMPORT_EXPORT = re.compile(r'^(?:import|export)\s.*$', re.M)
DEFS_LINK = re.compile(r'^\s*\[[^\]]+\]:\s', re.M)
CAMPOS_IGUAIS = ('id', 'slug', 'sidebar_position', 'hide_table_of_contents',
                 'authors', 'tags', 'date', 'image')
CAMPOS_TRADUZIVEIS = ('title', 'sidebar_label', 'description')

# Palavras-função para estimar o idioma da prosa.
EN = set('the and of to is are you your this that with for in it be can when '
         'which by an or as from have will not these use using'.split())
PT = set('os de do da dos das que é são um uma para com no na nos nas em por '
         'você seu sua ao como mais pode isso este esta'.split())
LIMITE_ERRO, LIMITE_AVISO, MINIMO_PALAVRAS = 0.7, 0.3, 20


def git(*args):
    r = subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def sem_codigo(texto):
    """Remove blocos de código cercados (``` ou ~~~)."""
    saida, em_codigo = [], False
    for linha in texto.split('\n'):
        if CERCA.match(linha):
            em_codigo = not em_codigo
            continue
        if not em_codigo:
            saida.append(linha)
    return '\n'.join(saida)


def proporcao_ingles(texto):
    _, corpo = frontmatter(texto)
    corpo = sem_codigo(corpo)
    corpo = IMPORT_EXPORT.sub('', corpo)
    corpo = re.sub(r'<!--.*?-->|\{/\*.*?\*/\}|<[^<>]*>', ' ', corpo, flags=re.S)
    linhas = []
    for linha in corpo.split('\n'):
        s = linha.strip()
        if not s or s.startswith(('<', '[', '|', ':::')):
            continue
        linhas.append(re.sub(r'`[^`]*`|\[[^\]]*\]\[[^\]]*\]|\([^)]*\)|\{[^}]*\}', '', s))
    palavras = re.findall(r"[a-záéíóúãõçêâô']+", ' '.join(linhas).lower())
    e = sum(p in EN for p in palavras)
    p = sum(p in PT for p in palavras)
    return (e / (e + p), e + p) if e + p else (0.0, 0)


def rotulos_sem_definicao(texto):
    t = sem_codigo(texto)
    defs = {m.lower() for m in re.findall(r'^\s*\[([^\]]+)\]:\s', t, re.M)}
    usados = {(lab or txt).lower()
              for txt, lab in re.findall(r'\[([^\]]+)\]\[([^\]]*)\]', t)}
    inline = ' '.join(re.findall(r'`[^`]*`', t)).lower()
    return {r for r in usados - defs if f'[{r}]' not in inline}


def checar_frontmatter(fm, en_fm):
    try:
        dados = yaml.safe_load(fm) or {}
    except yaml.YAMLError as e:
        return [('frontmatter', f'YAML inválido: {str(e).splitlines()[0]}')]
    if not isinstance(dados, dict):
        return [('frontmatter', 'frontmatter não é um mapa YAML')]
    erros = []
    if dados.get('ia-translated') is not True:
        erros.append(('frontmatter', 'ia-translated não é `true` de primeiro nível '
                                     f'(valor: {str(dados.get("ia-translated"))[:40]!r})'))
    try:
        en = yaml.safe_load(en_fm or '') or {}
    except yaml.YAMLError:
        en = {}
    if not isinstance(en, dict):
        en = {}
    for chave, valor in en.items():
        if isinstance(valor, str) and valor.strip() and \
                not str(dados.get(chave) or '').strip():
            erros.append(('frontmatter', f'campo `{chave}` vazio (o inglês tem valor)'))
    for chave in CAMPOS_IGUAIS:
        if chave in en and dados.get(chave) != en[chave]:
            erros.append(('frontmatter-id', f'`{chave}` difere do inglês '
                                            f'({str(dados.get(chave))[:30]!r} ≠ {str(en[chave])[:30]!r})'))
    for chave in CAMPOS_TRADUZIVEIS:
        valor = en.get(chave)
        if isinstance(valor, str) and dados.get(chave) == valor:
            palavras = re.findall(r"[a-z']+", valor.lower())
            if len(palavras) >= 3 and any(p in EN for p in palavras):
                erros.append(('frontmatter-en', f'`{chave}` igual ao inglês: {valor[:60]!r}'))
    return erros


def marcados():
    saida = git('ls-files', '--', *pastas()) or ''
    for c in saida.split():
        if no_escopo(c) and (ROOT / c).exists() and \
                traduzida((ROOT / c).read_text(encoding='utf-8')):
            yield c


IMPORT_PARCIAL = re.compile(r'''^import\s+\w+\s+from\s+['"](\.[^'"]+\.mdx?)['"]''', re.M)


def ids_da_pagina(texto, pasta, profundidade=0):
    ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', texto))
    for _, _, txt in anc.titulos(texto):
        sem, explicito = anc.separar_id(txt)
        ids.add(explicito or anc.slug(sem))
    base = set(ids)
    for i in base:  # o Docusaurus deduplica ids repetidos com -1, -2...
        ids.update(f'{i}-{n}' for n in range(1, 6))
    if profundidade < 3:
        for rel in IMPORT_PARCIAL.findall(texto):
            arq = (pasta / rel.replace('\\_', '_')).resolve()
            if arq.exists():
                ids |= ids_da_pagina(arq.read_text(encoding='utf-8'), arq.parent,
                                     profundidade + 1)
    return ids


def links_internos_quebrados(texto, pasta):
    t = sem_codigo(texto)
    alvos = re.findall(r'\]\(#([^)\s]+)\)', t)
    alvos += re.findall(r'^\s*\[[^\]]+\]:\s*#(\S+)', t, re.M)
    alvos += re.findall(r'href=["\']#([^"\']+)["\']', t)
    ids = ids_da_pagina(texto, pasta)
    return {a for a in alvos if a not in ids and '{' not in a}


def contagens(texto):
    t = sem_codigo(texto)
    return {
        'cercas de código': len(CERCA.findall(texto)),
        'títulos': len(anc.titulos(texto)),
        'admonitions :::': len(ADMONITION.findall(t)) + len(FECHA_ADMONITION.findall(t)),
        'componentes JSX': len(JSX.findall(re.sub(r'`[^`]*`', '', t))),
        'ids {#}': len(IDS.findall(t)),
    }


def checar_arquivo(caminho, ref, sync):
    erros, avisos = [], []
    texto = (ROOT / caminho).read_text(encoding='utf-8')
    fm, corpo = frontmatter(texto)
    pasta = (ROOT / caminho).parent

    if CONFLITO.search(texto):
        erros.append(('conflito', 'marcadores de merge no arquivo'))

    en = git('show', f'{ref}:{caminho}')

    if fm is not None:
        erros += checar_frontmatter(fm, frontmatter(en or '')[0])
        if FLAG_FM.search(fm) is None and 'ia-translated' in corpo:
            erros.append(('flag', '`ia-translated` fora do frontmatter'))
    elif not texto.lstrip().startswith((FLAG_COMENTARIO, FLAG_COMENTARIO_MDX)):
        erros.append(('flag', 'comentário ia-translated fora da primeira linha'))

    for linha in texto.split('\n'):
        if PLACEHOLDER.search(linha):
            erros.append(('placeholder', linha.strip()[:90]))
            break

    if en is None:
        erros.append(('estrutura', f'sem original em {ref[:9]}'))
        return erros, avisos

    if not Path(caminho).name.startswith('_'):
        prop, n = proporcao_ingles(texto)
        if n >= MINIMO_PALAVRAS and prop >= LIMITE_ERRO:
            erros.append(('ingles', f'marcada como traduzida, mas {prop:.0%} da prosa está em inglês'))
        elif n >= MINIMO_PALAVRAS and prop >= LIMITE_AVISO:
            avisos.append(('parcial', f'{prop:.0%} da prosa ainda em inglês'))

    quebrados = links_internos_quebrados(texto, pasta) - links_internos_quebrados(en, pasta)
    if quebrados:
        erros.append(('link-interno', 'âncoras inexistentes: ' + ', '.join(sorted(quebrados))))

    _, n_ancoras = anc.ancorar(en, texto)
    if n_ancoras:
        erros.append(('ancora', f'{n_ancoras} título(s) sem o `{{#id}}` do inglês; '
                                'rode tool/traducao/ancorar_titulos.py'))

    ce, cp = contagens(en), contagens(texto)
    for nome in ce:
        # ids a mais são permitidos (mantêm o slug inglês de títulos traduzidos).
        if ce[nome] != cp[nome] and not (nome == 'ids {#}' and cp[nome] > ce[nome]):
            erros.append(('estrutura', f'{nome}: en={ce[nome]} pt={cp[nome]}'))
    te = ADMONITION.findall(sem_codigo(en))
    tp = ADMONITION.findall(sem_codigo(texto))
    if len(te) == len(tp) and te != tp:
        erros.append(('estrutura', f'tipos de admonition diferentes: en={te} pt={tp}'))
    ie = sorted(IMPORT_EXPORT.findall(sem_codigo(en)))
    ip = sorted(IMPORT_EXPORT.findall(sem_codigo(texto)))
    if ie != ip:
        dif = sorted(set(ie) ^ set(ip))
        erros.append(('estrutura', 'import/export diferente do inglês: ' + '; '.join(dif)[:120]))
    faltando = rotulos_sem_definicao(texto) - rotulos_sem_definicao(en)
    if faltando:
        erros.append(('estrutura', 'rótulos sem definição: ' + ', '.join(sorted(faltando))))
    ne, np_ = len(DEFS_LINK.findall(sem_codigo(en))), len(DEFS_LINK.findall(sem_codigo(texto)))
    if ne != np_:
        avisos.append(('defs-link', f'en={ne} pt={np_}'))

    if sync and sync != ref:
        en_sync = git('show', f'{sync}:{caminho}')
        if en_sync is not None and en_sync != en:
            erros.append(('defasada', f'o inglês mudou entre {sync[:9]} e {ref[:9]}; '
                                      'rode sincronizar_upstream.py'))
    return erros, avisos


# Analytics e telemetria do reactnative.dev oficial que o fork não publica: os
# visitantes do React Native Brasil virariam dados das contas da Meta/Google.
ANALYTICS = r'gtag|G-58L13S6BDP|googletagmanager|plugin-google-gtag|surveymonkey\.com/|facebookAppId'


def analytics_herdado():
    saida = git('grep', '-nIE', ANALYTICS, '--', 'website', ':!*.md', ':!*.mdx') or ''
    return saida.splitlines()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ref', default='upstream/main')
    ap.add_argument('--estrito', action='store_true', help='avisos também falham')
    ap.add_argument('--resumo', action='store_true',
                    help='mostra só a contagem por tipo de erro/aviso')
    ap.add_argument('arquivos', nargs='*')
    a = ap.parse_args()

    ref = git('rev-parse', a.ref)
    if ref is None:
        sys.exit(f'Ref {a.ref} não encontrada. Rode: git fetch upstream main')
    ref = ref.strip()
    sync = SYNC.read_text().strip() if SYNC.exists() else None
    if sync and git('cat-file', '-e', sync) is None:
        sync = None  # histórico raso: pula a checagem de defasagem

    arquivos = a.arquivos or list(marcados())
    total_erros = total_avisos = 0
    por_tipo = {}
    for arq in arquivos:
        p = Path(arq)
        caminho = p.resolve().relative_to(ROOT).as_posix() if p.exists() else arq
        erros, avisos = checar_arquivo(caminho, ref, sync)
        for tipo, _ in erros:
            por_tipo[f'erro  {tipo}'] = por_tipo.get(f'erro  {tipo}', 0) + 1
        for tipo, _ in avisos:
            por_tipo[f'aviso {tipo}'] = por_tipo.get(f'aviso {tipo}', 0) + 1
        if (erros or avisos) and not a.resumo:
            print(f'{"✗" if erros else "!"} {caminho}')
            for tipo, msg in erros:
                print(f'    erro  [{tipo}] {msg}')
            for tipo, msg in avisos:
                print(f'    aviso [{tipo}] {msg}')
        total_erros += bool(erros)
        total_avisos += bool(avisos) and not erros

    if not a.arquivos and PEND.exists() and any(
            f.name != 'RELATORIO.md' for f in PEND.rglob('*') if f.is_file()):
        print('✗ .traducao-pendente/\n    erro  [pendente] ainda há conflitos para resolver')
        total_erros += 1

    if not a.arquivos:
        achados = analytics_herdado()
        if achados:
            print('✗ analytics herdado do upstream')
            for l in achados[:20]:
                print(f'    erro  [analytics] {l[:140]}')
            print('    É analytics/telemetria do reactnative.dev oficial que voltou com o sync: '
                  'remova (ver CLAUDE.md, regra do sync).')
            total_erros += 1
            por_tipo['erro  analytics'] = len(achados)

    if a.resumo:
        for k in sorted(por_tipo):
            print(f'  {k}: {por_tipo[k]} arquivo(s)')
    print(f'{len(arquivos)} arquivo(s) conferido(s): {total_erros} com erro, '
          f'{total_avisos} só com aviso.')
    sys.exit(1 if total_erros or (a.estrito and total_avisos) else 0)


if __name__ == '__main__':
    main()
