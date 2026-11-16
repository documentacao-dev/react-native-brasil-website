#!/usr/bin/env python3
"""Semeia a tradução da versão estável (website/versioned_docs/version-<atual>/)
a partir das páginas já traduzidas de docs/, sem modelo nenhum.

    python3 tool/traducao/semear_versao.py [--ref <commit do upstream>] [--versao 0.88]

Quando o upstream corta uma versão, ele copia docs/ para
website/versioned_docs/version-X/. Então, para cada página da versão que ainda
está em inglês e cuja irmã em docs/ já está traduzida, o script faz um merge
de 3 vias:

- pt:      docs/<página> traduzida (árvore de trabalho);
- base_en: docs/<página> em inglês no commit do upstream que essa tradução
           acompanha (`--ref`, padrão: tool/traducao/ultimo-sync-upstream.txt);
- new_en:  a página da versão em inglês (árvore de trabalho).

Sem conflito, grava a página traduzida na versão. Com conflito, grava os
marcadores diff3 em .traducao-pendente/<caminho da versão> (resolvido pelo
agente atualizar-traducao, como no sync) e deixa o inglês no lugar.

Também traduz os rótulos de categoria de
website/versioned_sidebars/version-X-sidebars.json com os mesmos pares
inglês → português que o fork já usa em website/sidebars.ts.

O sincronizar_upstream.py chama este script no fim de todo sync.
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from escopo import ROOT, EXTENSOES, pasta_versao, traduzida, versao_atual  # noqa: E402

SYNC = ROOT / 'tool' / 'traducao' / 'ultimo-sync-upstream.txt'
PEND = ROOT / '.traducao-pendente'


def show(ref, caminho):
    r = subprocess.run(['git', '-C', str(ROOT), 'show', f'{ref}:{caminho}'],
                       capture_output=True)
    return r.stdout if r.returncode == 0 else None


def rotulos_sidebar(ref, antes=None):
    """Pares {rótulo inglês: rótulo português} tirados do diff entre o
    website/sidebars.ts do upstream e o do fork (linhas trocadas uma a uma).
    `antes=(ref_pt, ref_en)` acrescenta os pares de um commit anterior do fork
    (usado pelo sync quando o sidebars.ts ficou em conflito)."""
    pares = {}
    if antes:
        pares.update(_pares(show(antes[1], 'website/sidebars.ts'),
                            show(antes[0], 'website/sidebars.ts')))
    pt_arq = ROOT / 'website' / 'sidebars.ts'
    if pt_arq.exists():
        pares.update(_pares(show(ref, 'website/sidebars.ts'), pt_arq.read_bytes()))
    return pares


def _pares(en, pt):
    if not en or not pt:
        return {}
    en = en.decode('utf-8').split('\n')
    pt = pt.decode('utf-8').split('\n')
    chave = re.compile(r"""^\s*(?:label:\s*)?(['"]?)([^'":]+)\1\s*[:,]""")
    import difflib
    pares = {}
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=en, b=pt, autojunk=False).get_opcodes():
        if op != 'replace' or i2 - i1 != j2 - j1:
            continue
        for le, lp in zip(en[i1:i2], pt[j1:j2]):
            me, mp = chave.match(le), chave.match(lp)
            if me and mp and me.group(2) != mp.group(2):
                pares[me.group(2).strip()] = mp.group(2).strip()
    return pares


def traduzir_sidebar(versao, ref, antes=None):
    arq = ROOT / 'website' / 'versioned_sidebars' / f'version-{versao}-sidebars.json'
    pares = rotulos_sidebar(ref, antes)
    if not arq.exists() or not pares:
        return 0
    texto = arq.read_text(encoding='utf-8')
    n = 0
    # Troca no texto (sem reformatar o JSON): chaves de categoria `"X": [` e
    # valores de `"label": "X"`.
    for en, pt in pares.items():
        e, p = json.dumps(en), json.dumps(pt, ensure_ascii=False)
        texto, k1 = re.subn(rf'{re.escape(e)}(\s*:\s*[\[{{])', lambda m: p + m.group(1), texto)
        texto, k2 = re.subn(rf'("label"\s*:\s*){re.escape(e)}', lambda m: m.group(1) + p, texto)
        n += k1 + k2
    if n:
        arq.write_text(texto, encoding='utf-8')
    return n


def irmas(rel):
    """Caminhos possíveis da irmã em docs/ (o upstream troca .md por .mdx)."""
    raiz, ext = rel.rsplit('.', 1)
    return [f'docs/{rel}'] + [f'docs/{raiz}.{e}' for e in ('md', 'mdx') if e != ext]


def fonte(rel, ref, antes):
    """(pt, base_en) para semear `rel`, ou None. Primeiro a irmã traduzida na
    árvore (inglês em `ref`); depois, com `antes=(ref_pt, ref_en)`, a tradução
    de um commit anterior do fork contra o inglês daquele momento."""
    if any((PEND / c).exists() for c in irmas(rel)):
        return 'aguardar'  # a irmã será retraduzida; semeie depois dela
    for c in irmas(rel):
        arq = ROOT / c
        if arq.exists() and \
                traduzida(arq.read_text(encoding='utf-8')):
            base = show(ref, c)
            if base is not None:
                return arq.read_bytes(), base
    if antes:
        for c in irmas(rel):
            pt, base = show(antes[0], c), show(antes[1], c)
            if pt is not None and base is not None and traduzida(pt.decode('utf-8', 'replace')):
                return pt, base
    return None


def semear(versao, ref, antes=None):
    """Retorna (semeadas, conflitos, sem_irma). Páginas cuja irmã em docs/
    está em .traducao-pendente/ entram em sem_irma: rode de novo depois que a
    irmã for resolvida."""
    pasta = ROOT / pasta_versao(versao)
    semeadas, conflitos, sem_irma = [], [], []
    if not pasta.is_dir():
        return semeadas, conflitos, sem_irma
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for arq in sorted(p for p in pasta.rglob('*') if p.suffix in EXTENSOES):
            rel = arq.relative_to(pasta).as_posix()
            destino = arq.relative_to(ROOT).as_posix()
            novo = arq.read_bytes()
            if traduzida(novo.decode('utf-8', 'replace')) or (PEND / destino).exists():
                continue
            f = fonte(rel, ref, antes)
            if f is None or f == 'aguardar':
                sem_irma.append(destino)
                continue
            (tmp / 'pt').write_bytes(f[0])
            (tmp / 'base').write_bytes(f[1])
            (tmp / 'novo').write_bytes(novo)
            r = subprocess.run(['git', 'merge-file', '-p', '--diff3', '-L', 'pt',
                                '-L', 'base_en', '-L', 'new_en', str(tmp / 'pt'),
                                str(tmp / 'base'), str(tmp / 'novo')],
                               capture_output=True)
            if r.returncode == 0:
                arq.write_bytes(r.stdout)
                semeadas.append(destino)
            else:
                p = PEND / destino
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(r.stdout)
                conflitos.append((destino, r.stdout.count(b'\n<<<<<<< pt')))
    return semeadas, conflitos, sem_irma


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ref', help='commit do upstream que docs/ traduzido acompanha')
    ap.add_argument('--versao', help='padrão: a primeira de website/versions.json')
    a = ap.parse_args()
    ref = a.ref or SYNC.read_text().strip()
    versao = a.versao or versao_atual()
    if not versao:
        sys.exit('Nenhuma versão em website/versions.json')
    semeadas, conflitos, sem_irma = semear(versao, ref)
    rotulos = traduzir_sidebar(versao, ref)
    print(f'Versão {versao}: {len(semeadas)} semeada(s), {len(conflitos)} com conflito '
          f'(em .traducao-pendente/), {len(sem_irma)} sem irmã traduzida em docs/ (ou com a irmã em .traducao-pendente/); '
          f'{rotulos} rótulo(s) do sidebar traduzido(s).')


if __name__ == '__main__':
    main()
