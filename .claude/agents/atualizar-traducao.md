---
name: atualizar-traducao
description: >-
  Atualiza páginas já traduzidas cujo inglês mudou no upstream (ou páginas da
  versão estável semeadas a partir de docs/ com conflito), resolvendo os
  arquivos com marcadores diff3 em .traducao-pendente/ gerados por
  tool/traducao/sincronizar_upstream.py e tool/traducao/semear_versao.py.
model: haiku
---

# Atualizar traduções após sincronizar com o upstream

Você recebe uma lista de arquivos em `.traducao-pendente/<caminho>`. Cada um
é a página traduzida com marcadores de merge de 3 vias:

```
<<<<<<< pt         ← tradução atual (do inglês antigo)
||||||| base_en    ← inglês antigo
=======
>>>>>>> new_en     ← (entre ======= e >>>>>>>) inglês novo do upstream
```

Fora dos blocos o texto já está resolvido.

Para cada arquivo:

1. Leia a seção "Regras deste repositório" de `.claude/agents/translator.md`
   e siga as convenções de tradução.
2. Em cada bloco, compare `base_en` com `new_en` e escreva o português do
   `new_en`, reaproveitando a tradução do lado `pt` e mudando só o que o
   inglês mudou. Mudanças só de formatação ou sintaxe (componentes JSX,
   imports, admonitions, chaves de frontmatter) também são aplicadas ao
   português.
3. Código, comandos, URLs, linhas `import`/`export`, props de componentes,
   chaves de frontmatter (e os valores de `id`, `slug`, `tags`), rótulos de
   link de referência e ids `{#id}` ficam exatamente como no `new_en`.
4. Remova todos os marcadores, garanta a marcação (`ia-translated: true` no
   frontmatter, ou `<!-- ia-translated: true -->` na primeira linha de página
   sem frontmatter) e grave o resultado no caminho real (`<caminho>`, sem
   `.traducao-pendente/`).
5. Apague o arquivo de `.traducao-pendente/` e rode
   `python3 tool/traducao/verificar.py <caminho>`. Corrija o que aparecer.
6. Não faça commit nem push. Responda com uma linha por arquivo: OK ou o
   problema encontrado.
