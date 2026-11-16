"""Definições comuns aos scripts de tool/traducao/: o que entra no ciclo de
tradução do React Native Brasil e como uma página é marcada como traduzida.

O que entra no ciclo (páginas .md e .mdx):

- `docs/`: a próxima versão (rota /docs/next). É onde o upstream edita.
- `website/versioned_docs/version-<atual>/`: a versão estável, a primeira de
  `website/versions.json` (rota /docs/, a que o leitor abre por padrão).
  Quando o upstream corta uma versão nova, ela passa a ser a atual e é semeada
  a partir de `docs/` por `semear_versao.py`, sem tradução.
- `website/architecture/`, `website/contributing/`, `website/community/`.
- `website/blog/` (baixa prioridade: posts históricos).

Fica de fora: as versões antigas de `website/versioned_docs/` (continuam em
inglês) e os componentes/configuração em TypeScript (traduzidos à mão, passam
pelo merge de 3 vias do sync como qualquer arquivo alterado pelo fork).

Marcação de página traduzida:

- com frontmatter: `ia-translated: true` no frontmatter;
- sem frontmatter (parciais `_*.mdx` e algumas páginas): o comentário
  `<!-- ia-translated: true -->` na primeira linha.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO_FORK = 'documentacao-dev/react-native-brasil-website'
REPO_UPSTREAM = 'facebook/react-native-website'

PASTAS_FIXAS = ('docs/', 'website/architecture/', 'website/contributing/',
                'website/community/', 'website/blog/')
BAIXA_PRIORIDADE = ('website/blog/',)
EXTENSOES = ('.md', '.mdx')

FLAG_FM = re.compile(r'^ia-translated:\s*true\s*$', re.M)
FLAG_COMENTARIO = '<!-- ia-translated: true -->'
FLAG_COMENTARIO_MDX = '{/* ia-translated: true */}'


def versao_atual(root=ROOT):
    """Primeira versão de website/versions.json (a estável), ou None."""
    arq = Path(root) / 'website' / 'versions.json'
    try:
        versoes = json.loads(arq.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return None
    return versoes[0] if versoes else None


def pasta_versao(versao):
    return f'website/versioned_docs/version-{versao}/'


def pastas(root=ROOT):
    v = versao_atual(root)
    extra = (pasta_versao(v),) if v else ()
    return PASTAS_FIXAS[:1] + extra + PASTAS_FIXAS[1:]


def no_escopo(caminho, root=ROOT):
    return caminho.endswith(EXTENSOES) and caminho.startswith(pastas(root))


def frontmatter(texto):
    """(frontmatter, corpo), ou (None, texto) se não houver frontmatter."""
    m = re.match(r'^---\n(.*?)\n---[ \t]*(?:\n|$)', texto, re.S)
    return (m.group(1), texto[m.end():]) if m else (None, texto)


def traduzida(texto):
    fm, _ = frontmatter(texto)
    if fm is not None:
        return FLAG_FM.search(fm) is not None
    inicio = texto.lstrip()
    return inicio.startswith(FLAG_COMENTARIO) or inicio.startswith(FLAG_COMENTARIO_MDX)
