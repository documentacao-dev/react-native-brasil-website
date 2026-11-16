#!/usr/bin/env python3
"""Adiciona ids explícitos `{#slug}` aos títulos traduzidos, usando o slug
que o Docusaurus gera a partir do título correspondente em inglês (mesma
posição).

Assim os links `pagina#ancora` vindos de outras páginas (e do próprio
upstream) continuam funcionando depois da tradução.

    python3 tool/traducao/ancorar_titulos.py [--ref upstream/main] arquivos...
    python3 tool/traducao/ancorar_titulos.py --todas   # todas as marcadas

Com `--todas`, o inglês de referência é o do último sync
(tool/traducao/ultimo-sync-upstream.txt), a não ser que se passe `--ref`.
Páginas cujos títulos não correspondem ao inglês (em quantidade e nível) são
ignoradas.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from escopo import ROOT, no_escopo, traduzida  # noqa: E402

TITULO = re.compile(r'^(#{2,6})\s+(.*?)\s*$')
ID_EXPLICITO = re.compile(r'\s*\{#([^}\s]+)\}\s*$')
CERCA = re.compile(r'^\s*(```|~~~)')


def titulos(texto):
    """Retorna [(índice_da_linha, nível, texto)] fora de blocos de código."""
    res, em_codigo = [], False
    for i, linha in enumerate(texto.split('\n')):
        if CERCA.match(linha):
            em_codigo = not em_codigo
            continue
        if not em_codigo:
            m = TITULO.match(linha)
            if m:
                res.append((i, len(m.group(1)), m.group(2)))
    return res


def separar_id(texto):
    """(texto_sem_id, id ou None)."""
    m = ID_EXPLICITO.search(texto)
    if not m:
        return texto.rstrip(), None
    return texto[:m.start()].rstrip(), m.group(1)


def slug(texto):
    """Aproxima o github-slugger usado pelo Docusaurus, aplicado ao texto
    visível do título (tags HTML/JSX somem, o texto entre elas fica)."""
    t = re.sub(r'<[^>]+>', '', texto)
    t = re.sub(r'\[([^\]]*)\]\[[^\]]*\]|\[([^\]]*)\]\([^)]*\)',
               lambda m: m.group(1) or m.group(2) or '', t)
    t = re.sub(r'[*`]|(?<!\w)_|_(?!\w)', '', t)
    t = t.lower().strip()
    t = re.sub(r'[^\w\- ]', '', t)
    return t.replace(' ', '-')


def ancorar(en, pt):
    """Retorna (texto_pt_com_ids, n_ajustes), ou (None, 0) se os títulos de en
    e pt não correspondem em quantidade e nível.

    Se o inglês já tem `{#id}`, a tradução precisa ter o mesmo id; senão o id
    do slug inglês é acrescentado quando o slug do título traduzido difere."""
    te, tp = titulos(en), titulos(pt)
    if [n for _, n, _ in te] != [n for _, n, _ in tp]:
        return None, 0
    linhas = pt.split('\n')
    n = 0
    for (_, nivel, txt_en), (i, _, txt_pt) in zip(te, tp):
        texto_en, id_en = separar_id(txt_en)
        texto_pt, _ = separar_id(txt_pt)
        alvo = id_en or slug(texto_en)
        if not alvo:
            continue
        precisa = id_en is not None or alvo != slug(texto_pt)
        novo = f'{"#" * nivel} {texto_pt}' + (f' {{#{alvo}}}' if precisa else '')
        if novo != linhas[i]:
            linhas[i] = novo
            n += 1
    return '\n'.join(linhas), n


def marcadas():
    r = subprocess.run(['git', '-C', str(ROOT), 'ls-files'], capture_output=True,
                       text=True, check=True)
    for c in r.stdout.split():
        if no_escopo(c) and (ROOT / c).exists() and \
                traduzida((ROOT / c).read_text(encoding='utf-8')):
            yield c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ref')
    ap.add_argument('--todas', action='store_true')
    ap.add_argument('arquivos', nargs='*')
    a = ap.parse_args()
    if a.todas:
        ref = a.ref or (ROOT / 'tool' / 'traducao' / 'ultimo-sync-upstream.txt').read_text().strip()
        arquivos = list(marcadas())
    else:
        ref = a.ref or 'upstream/main'
        arquivos = [Path(x).resolve().relative_to(ROOT).as_posix() for x in a.arquivos]
    total = 0
    for caminho in arquivos:
        r = subprocess.run(['git', '-C', str(ROOT), 'show', f'{ref}:{caminho}'],
                           capture_output=True, text=True)
        if r.returncode != 0:
            continue  # exclusivo do fork
        pt = (ROOT / caminho).read_text(encoding='utf-8')
        novo, n = ancorar(r.stdout, pt)
        if novo is None:
            print(f'✗ {caminho}: títulos não correspondem ao inglês; ignorado')
            continue
        if n:
            (ROOT / caminho).write_text(novo, encoding='utf-8')
            total += 1
        if n or not a.todas:
            print(f'✓ {caminho}: {n} título(s) ajustado(s)')
    if a.todas:
        print(f'{total} arquivo(s) alterado(s) de {len(arquivos)} marcados.')


if __name__ == '__main__':
    main()
