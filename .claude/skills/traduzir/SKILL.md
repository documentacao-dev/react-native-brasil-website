---
name: traduzir
description: >-
  Roda o ciclo completo de tradução do React Native Brasil de ponta a ponta:
  sync com o upstream (facebook/react-native-website), semeadura da versão
  estável a partir de docs/, retradução das páginas que mudaram e tradução das
  páginas novas em subagentes Haiku, verificação determinística, commit, PR,
  review independente em Sonnet, correção em Haiku e merge quando tudo fica
  verde. Use quando pedirem "traduzir", "sincronizar com o upstream", "rodar o
  sync", "atualizar a tradução", "o inglês mudou", "tem página defasada", "saiu
  versão nova do React Native", ou quando o workflow semanal
  traducao-automatica.yml chamar. Também serve para traduzir só um conjunto de
  páginas: passe os caminhos como argumento.
---

# Ciclo de tradução do React Native Brasil

Você é o **orquestrador**. Quem traduz é sempre um subagente **Haiku**; quem
revisa é um subagente **Sonnet** de contexto limpo. Você não escreve tradução:
cuida de git, scripts, lotes, commits, PR e da decisão de merge.

Argumentos opcionais (`$ARGUMENTS`): caminhos de páginas para traduzir só
elas, ou `sem-merge` para parar no PR pronto, sem merge.

Leia antes: `CLAUDE.md` (escopo, processo e scripts de `tool/traducao/`) e a
seção "Regras deste repositório" de `.claude/agents/translator.md`.

## 0. Ambiente

```console
bash tool/traducao/setup.sh          # PyYAML, remote upstream, histórico
git fetch upstream main
```

**Branch já preparada pelo workflow.** No Actions, a fase `preparar` do
`traducao-automatica.yml` já detectou o trabalho, rodou o sync (com a
semeadura da versão estável), o `ancorar_titulos.py --todas`, o
`gerar_todo.py` e o `verificar.py`, e publicou a branch
`traducao/AAAA-MM-DD`. Nesse caso, comece na etapa 3 e não rode o
`sincronizar_upstream.py` de novo.

Árvore limpa e `main` atualizada. Se já existir um PR aberto com o label
`traducao-automatica`, **não abra outro**: continue nele (faça checkout da
branch dele e pule para a etapa que faltar).

## 1. Detectar o que fazer

- `git rev-list --count $(cat tool/traducao/ultimo-sync-upstream.txt)..upstream/main`
  diz quantos commits do upstream entraram desde o último sync.
- `TODO-TRADUCAO.md` lista as páginas ainda não traduzidas do escopo.
- Se não há commit novo do upstream nem página pendente (e nenhum caminho foi
  passado), **pare aqui** e responda "nada a traduzir". Não abra PR vazio.

Crie a branch `traducao/AAAA-MM-DD` a partir da `main`.

## 2. Sync com o upstream

Siga a "Regra principal" do `CLAUDE.md`, passos 2 e 3: rode
`python3 tool/traducao/sincronizar_upstream.py` e faça o commit do merge
**incluindo** `.traducao-pendente/`. Depois,
`python3 tool/traducao/ancorar_titulos.py --todas --ref upstream/main`.

Arquivos que não são prosa (componentes TSX, `docusaurus.config.ts`,
`sidebars*.ts`, `package.json`, workflows) você resolve direto, sem agente,
como diz o `CLAUDE.md`.

## 3. Traduzir em Haiku

Monte lotes equilibrados por tamanho, **no máximo 5 subagentes em paralelo**,
nunca dois no mesmo arquivo. Sempre com `model: "haiku"` na ferramenta Agent:

- Páginas em `.traducao-pendente/` (inglês mudou, ou semeadura da versão
  estável com conflito) → subagente com o prompt de
  `.claude/agents/atualizar-traducao.md`.
- Páginas novas (do `TODO-TRADUCAO.md` ou dos argumentos) → subagente com o
  prompt de `.claude/agents/translator.md`. Prioridade: `docs/`, depois a
  versão estável, depois architecture/contributing/community, blog por último.
- Uma página da versão estável que ficou em inglês e cuja irmã em `docs/` foi
  traduzida neste ciclo: rode de novo `python3 tool/traducao/semear_versao.py
  --ref upstream/main` em vez de traduzir.

Num ciclo com muitas páginas novas, traduza no máximo ~40 por execução (o
resto fica para a semana seguinte) para o PR caber num review.

Depois: `python3 tool/traducao/ancorar_titulos.py <arquivos traduzidos>` e,
com `.traducao-pendente/` vazio, apague a pasta e rode
`python3 tool/traducao/gerar_todo.py`.

## 4. Verificar

```console
python3 tool/traducao/verificar.py
```

Zero erros é obrigatório. Erro num arquivo traduzido volta para um subagente
Haiku com a saída do `verificar.py` no prompt (no máximo 2 tentativas por
arquivo; depois corrija o trecho você mesmo, sem trocar de modelo). Procure
também prosa em inglês que escapou do limite de 30% do `verificar.py`
(seções novas inteiras em inglês) e mande para o Haiku.

A compilação do MDX não é conferida aqui: ela acontece no job `build` do
`pre-merge.yml`, no PR.

## 5. Commit e PR

- Commits por lote, mensagens em português (`chore: sync com upstream <sha>`,
  `translate: <caminho ou seção>`, `fix: ...`).
- `git push -u origin traducao/AAAA-MM-DD`
- `gh pr create --base main --label traducao-automatica` com o corpo:
  commits do upstream (de → para), versão estável (e quantas páginas foram
  semeadas), páginas retraduzidas, páginas novas, e o que ficou de fora.

## 6. Review em Sonnet (contexto limpo)

Dispare o subagente `revisar-traducao` (`.claude/agents/revisar-traducao.md`,
`model: "sonnet"`) passando **só** a lista de arquivos traduzidos ou
retraduzidos neste ciclo e o commit do upstream. Não passe sua opinião nem o
resumo do que foi feito. Até 5 revisores em paralelo para listas grandes.
Páginas semeadas sem conflito (cópia de `docs/` já revisado) não precisam de
review.

O revisor devolve, por arquivo, `OK` ou problemas classificados como
**grave** (sentido trocado, trecho faltando, código/link/âncora/import
alterado, inglês sem tradução) ou **leve** (estilo, escolha de palavra).

Publique o resultado como um comentário no PR (`gh pr comment`), uma linha
por arquivo com problema.

## 7. Corrigir em Haiku

Problemas **graves** voltam para subagentes Haiku com o apontamento do
revisor no prompt. Leves só se forem baratos. Depois, `verificar.py` de novo,
commit `fix: correções do review`, push, e um **novo review só dos arquivos
corrigidos**. No máximo 2 voltas de review + correção.

## 8. Aprovação e merge

Merge **só** se as quatro condições valerem:

1. `verificar.py` com 0 erros;
2. o último review sem nenhum problema grave em aberto;
3. os checks do PR verdes: `gh pr checks <n> --watch --fail-fast`
   (o `Pre-merge / build` compila o MDX de todas as páginas);
4. o argumento `sem-merge` não foi passado.

Então:

```console
gh pr edit <n> --add-label revisao-ok
gh pr merge <n> --auto --squash --delete-branch
```

Espere os checks com `gh pr checks --watch` **antes** do `gh pr merge`: a
`main` deste repositório pode não ter checks obrigatórios configurados, e sem
eles o `--auto` faz o merge na hora.

Se alguma condição falhar: `gh pr edit <n> --add-label precisa-humano`, um
comentário dizendo exatamente o que ficou pendente, e **sem** merge.

## 9. Resposta final

Uma mensagem curta: link do PR, de qual para qual commit do upstream, versão
estável, quantas páginas retraduzidas / novas / semeadas, resultado do review
(graves e leves), e se foi para merge ou ficou com `precisa-humano`.
