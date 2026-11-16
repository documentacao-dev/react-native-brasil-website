#!/usr/bin/env python3
"""Gera TODO-TRADUCAO.md com o status de tradução das páginas do escopo
(tool/traducao/escopo.py): docs/, a versão estável em
website/versioned_docs/, website/architecture, contributing, community e blog.

Uma página conta como traduzida quando o frontmatter contém
`ia-translated: true` (ou, sem frontmatter, quando a primeira linha é
`<!-- ia-translated: true -->`). Execute a partir da raiz do repositório:

    python3 tool/traducao/gerar_todo.py
"""
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from escopo import BAIXA_PRIORIDADE, ROOT, no_escopo, pastas, traduzida  # noqa: E402

SAIDA = ROOT / 'TODO-TRADUCAO.md'
CABECALHO = ROOT / 'tool' / 'traducao' / 'todo_cabecalho.md'


def arquivos():
    r = subprocess.run(['git', '-C', str(ROOT), 'ls-files', '--', *pastas()],
                       capture_output=True, text=True, check=True)
    for c in sorted(r.stdout.split()):
        if no_escopo(c) and (ROOT / c).exists():
            yield c


def secao_de(caminho):
    """Pasta do escopo + primeiro subdiretório (ex.: docs/the-new-architecture)."""
    for p in pastas():
        if caminho.startswith(p):
            resto = caminho[len(p):]
            sub = resto.split('/')[0] if '/' in resto else ''
            return (p + sub).rstrip('/')
    return '(outros)'


def main():
    ordem = {p.rstrip('/'): i for i, p in enumerate(pastas())}
    secoes = defaultdict(list)
    total = feitas = linhas_pendentes = 0
    for c in arquivos():
        texto = (ROOT / c).read_text(encoding='utf-8')
        ok = traduzida(texto)
        n = texto.count('\n')
        total += 1
        feitas += ok
        if not ok:
            linhas_pendentes += n
        secoes[secao_de(c)].append((c, ok, n))

    def chave(s):
        raiz = next((p for p in ordem if s == p or s.startswith(p + '/')), s)
        return (any(s.startswith(b.rstrip('/')) for b in BAIXA_PRIORIDADE),
                ordem.get(raiz, 99), s)

    out = [CABECALHO.read_text(encoding='utf-8').rstrip(), '']
    pct = 100 * feitas / total if total else 0
    out += ['## Progresso', '',
            f'- Páginas traduzidas: **{feitas} / {total}** ({pct:.1f}%)',
            f'- Linhas pendentes (aprox.): {linhas_pendentes}', '',
            '| Seção | Traduzidas | Total |', '|---|---:|---:|']
    for s in sorted(secoes, key=chave):
        itens = secoes[s]
        out.append(f'| `{s}` | {sum(i[1] for i in itens)} | {len(itens)} |')
    out += ['', '## Páginas por seção', '']
    for s in sorted(secoes, key=chave):
        itens = secoes[s]
        out += [f'### `{s}` ({sum(i[1] for i in itens)}/{len(itens)})', '']
        for c, ok, n in itens:
            out.append(f'- [{"x" if ok else " "}] `{c}` ({n} linhas)')
        out.append('')
    SAIDA.write_text('\n'.join(out), encoding='utf-8')
    print(f'{SAIDA.name}: {feitas}/{total} traduzidas')


if __name__ == '__main__':
    main()
