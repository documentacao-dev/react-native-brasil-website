# TODO de tradução — React Native Brasil

> Arquivo gerado por `python3 tool/traducao/gerar_todo.py`.
> Para mudar este cabeçalho, edite `tool/traducao/todo_cabecalho.md`.
> O processo completo (tradução e sincronização com o upstream) está em `CLAUDE.md`.

Uma página conta como traduzida quando o frontmatter tem `ia-translated: true`.
Páginas e parciais sem frontmatter usam `<!-- ia-translated: true -->` na
primeira linha.

Escopo: `docs/` (próxima versão), a versão estável em
`website/versioned_docs/version-<atual>/` (a primeira de
`website/versions.json`), `website/architecture/`, `website/contributing/`,
`website/community/` e, com baixa prioridade, `website/blog/`. As versões
antigas de `website/versioned_docs/` ficam em inglês.

Prioridade: primeiro as páginas **traduzidas cujo inglês mudou** (aparecem em
`.traducao-pendente/` depois de uma sincronização), depois as páginas novas.
A versão estável é semeada a partir de `docs/` por
`tool/traducao/semear_versao.py`; só o que sobrar vai para tradução.
