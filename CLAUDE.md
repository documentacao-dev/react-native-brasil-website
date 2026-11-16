# CLAUDE.md — React Native Brasil

Este repositório é a tradução para português do Brasil do site do React Native
(reactnative.dev), parte da org [`documentacao-dev`](https://github.com/documentacao-dev).
É um fork do [facebook/react-native-website](https://github.com/facebook/react-native-website)
(remote `upstream`). O site é Docusaurus 3 com páginas em Markdown/MDX.

## Começando do zero (sessão nova)

A partir da raiz do repositório:

```console
bash tool/traducao/setup.sh
```

O script confere o Python 3 e o PyYAML, adiciona o remote `upstream`
(facebook/react-native-website) e busca histórico suficiente para achar o
último commit sincronizado.

Comandos úteis:

- `python3 tool/traducao/verificar.py`: valida a estrutura das traduções.
- `python3 tool/traducao/gerar_todo.py`: regenera o `TODO-TRADUCAO.md`.
- Site local (Node 22 + Yarn via Corepack): `corepack enable && yarn install`,
  depois `yarn start` (servidor) ou `yarn build` (build completo, pesado:
  usa `NODE_OPTIONS=--max_old_space_size=8192`). Com `PREVIEW_DEPLOY=true` o
  build inclui só `docs/` e as duas últimas versões.

## Onde fica o quê

- `docs/`: páginas da próxima versão (rota `/docs/next`). É onde o upstream
  edita; parciais começam com `_` (ex.: `_experimental-api-warning.mdx`).
- `website/versioned_docs/version-X/`: cópias de `docs/` por versão. A
  primeira de `website/versions.json` é a **versão estável**, aberta em
  `/docs/` por padrão.
- `website/versioned_sidebars/`: sidebar de cada versão (rótulos de categoria).
- `website/architecture/`, `website/contributing/`, `website/community/`,
  `website/blog/`: as outras seções do site.
- `website/sidebars*.ts`, `website/docusaurus.config.ts`,
  `website/src/`: navegação, configuração e componentes (traduzidos à mão).
- `.claude/agents/translator.md`: **convenções de tradução**. A seção
  "Regras deste repositório" prevalece sobre o resto do arquivo.
- `tool/traducao/`: scripts de tradução e de sincronização (descritos abaixo).
- `plan/`: histórico da tradução inicial (fases 1 a 3). Não é mais usado; o
  status vivo é o `TODO-TRADUCAO.md`.

## Escopo do ciclo de tradução

Definido em `tool/traducao/escopo.py` (todos os scripts leem de lá):

| Entra | Por quê |
|---|---|
| `docs/` | Próxima versão; é onde as mudanças do upstream aparecem primeiro. |
| `website/versioned_docs/version-<estável>/` | É a versão que o leitor abre por padrão. Semeada a partir de `docs/` (abaixo). |
| `website/architecture/`, `contributing/`, `community/` | Seções pequenas, já traduzidas. |
| `website/blog/` | Já traduzido; baixa prioridade para páginas novas. |

Ficam **fora**: as versões antigas de `website/versioned_docs/` (continuam em
inglês; quando a estável muda, a anterior simplesmente sai do escopo) e os
arquivos TypeScript (passam pelo merge de 3 vias do sync, mas não pelo
`verificar.py` nem pelo TODO).

### Versão estável: semeadura sem tradução

Quando o upstream corta uma versão, ele copia `docs/` para
`website/versioned_docs/version-X/`. O `semear_versao.py` (chamado pelo
sync) faz, para cada página da versão estável ainda em inglês, um merge de 3
vias com a irmã traduzida em `docs/`: sem conflito, a tradução é copiada; com
conflito, vai para `.traducao-pendente/` como as páginas do sync. Também
traduz os rótulos de categoria do `version-X-sidebars.json` com os pares que o
fork já usa em `website/sidebars.ts`. No teste com a 0.82, 226 das 236 páginas
foram semeadas sem conflito.

## Regras de tradução (resumo)

As regras completas estão em `.claude/agents/translator.md`. As mais
importantes:

- Página traduzida tem `ia-translated: true` no frontmatter; página ou
  parcial sem frontmatter tem `<!-- ia-translated: true -->` na primeira
  linha.
- No frontmatter só `title`, `sidebar_label` e `description` são traduzidos;
  `id`, `slug`, `tags` e o resto ficam como no inglês.
- Títulos traduzidos levam o id do inglês no formato do Docusaurus:
  `## Começando {#getting-started}` (nunca `{:#id}`).
- Não traduza código, comandos, URLs, linhas `import`/`export`, componentes
  JSX e suas props (`value`, `className`), rótulos de link de referência nem
  ids `{#id}`. Admonitions (`:::tip`) mantêm o tipo.
- Mantenha a estrutura idêntica ao inglês: títulos, listas, cercas de código,
  admonitions e componentes.
- Termos técnicos consagrados ficam em inglês (props, state, hook, bundle,
  Turbo Module, Fabric, New Architecture etc.).

## Modelo da tradução: sempre Haiku

Toda tradução e retradução de página (tradução nova, sync com o upstream, correção de trecho) roda no **Haiku** (`model: haiku`, hoje Claude Haiku 5.5), local ou na nuvem (Claude Code na web, GitHub App, rotinas agendadas).

- Os agentes de tradução em `.claude/agents/` (`translator.md`, `atualizar-traducao.md`) declaram `model: haiku`. Não troque.
- Se um orquestrador disparar subagentes para traduzir, passe `model: "haiku"` na ferramenta Agent.
- O modelo principal da sessão fica só com a orquestração: merge do upstream, scripts de conferência, commits e PR. Ele não traduz páginas.
- Exceção: o **review** (agente `revisar-traducao`) roda em **Sonnet**. Ele só aponta problemas; quem corrige é o Haiku.

## Agentes e paralelismo

- **No máximo 5 agentes em paralelo**, em lotes equilibrados por tamanho, sem
  dois agentes no mesmo arquivo. Agentes não fazem commit nem push: quem
  orquestra confere com `verificar.py`, faz o commit por lote e o push.
- **Traduzir páginas novas:** `translator.md` (`doc-translator-pt-br`, Haiku).
  Se um arquivo falhar duas vezes no `verificar.py`, refaça-o no Haiku com o
  erro no prompt ou corrija o trecho à mão na orquestração. Não troque de
  modelo.
- **Atualizar páginas já traduzidas** (arquivos diff3 de
  `.traducao-pendente/`): `atualizar-traducao.md` (Haiku).
- **Review:** `revisar-traducao.md` (Sonnet, contexto limpo, só aponta).
- Componentes TSX, configuração e workflows: resolva diretamente, sem agente.

## Ciclo automático: skill `traduzir`

O ciclo inteiro (sync, semeadura, tradução, verificação, commit, PR, review,
correção e merge) está na skill `.claude/skills/traduzir/SKILL.md`. Rode
`/traduzir` numa sessão local ou na web.

O ciclo semanal roda por rotina agendada do Claude na nuvem, que executa a skill `traduzir`; o workflow traducao-automatica.yml fica para disparo manual (Actions → Tradução automática, com `paginas` e `sem_merge`).

No workflow, as etapas determinísticas rodam **sem Claude**, na fase
`preparar`: detectar commits novos do upstream e páginas pendentes (sem nada,
o workflow para com custo zero), sync, semeadura da versão estável,
`ancorar_titulos.py --todas`, `gerar_todo.py` e `verificar.py`. O Claude só
entra depois (`--model sonnet` orquestrando), na branch já sincronizada, para
traduzir, abrir o PR, revisar e fazer o merge.

- Tradução e correção: subagentes **Haiku**. Review: **Sonnet**.
- Merge só com `verificar.py` zerado, review sem problema grave e os checks do
  PR verdes (`Pre-merge / build` compila o MDX); senão o PR fica com o label
  `precisa-humano`.
- Labels usados: `traducao-automatica`, `revisao-ok`, `precisa-humano`.
- Os passos abaixo continuam valendo: a skill é a forma de executá-los.

## Regra principal: manter as traduções em dia com o upstream

**Traduzir páginas novas não basta: toda página já traduzida precisa ser
atualizada sempre que o inglês dela mudar no upstream.** Uma página com
`ia-translated: true` cujo conteúdo esteja defasado em relação ao inglês
atual é um bug.

Em toda sincronização com o upstream:

1. `git fetch upstream main` e crie uma branch.
2. Rode `python3 tool/traducao/sincronizar_upstream.py`. Ele:
   - faz o merge adotando a árvore do upstream (a estrutura nova do upstream
     sempre vence);
   - leva cada arquivo alterado pelo fork para o caminho novo (mesmo caminho
     ou renomeação detectada pelo git);
   - copia a tradução quando o inglês não mudou;
   - faz merge de 3 vias quando mudou. Sem conflito, grava o resultado. Com
     conflito, grava em `.traducao-pendente/<caminho>` com marcadores diff3
     e deixa o inglês novo no repositório;
   - semeia a versão estável a partir de `docs/` (`semear_versao.py`);
   - grava `.traducao-pendente/RELATORIO.md` e atualiza
     `tool/traducao/ultimo-sync-upstream.txt`.
3. Faça o commit do merge **incluindo** `.traducao-pendente/`, para nada se
   perder entre sessões.
4. Resolva **todos** os arquivos de `.traducao-pendente/`:
   - em cada bloco `<<<<<<< pt` / `||||||| base_en` / `=======` / `>>>>>>> new_en`,
     escreva o português do `new_en`, reaproveitando a tradução do lado `pt`
     e mudando só o que o inglês mudou;
   - grave o resultado no caminho real, com a marcação `ia-translated`;
   - apague o arquivo resolvido de `.traducao-pendente/` e marque-o no
     `RELATORIO.md`.
   Arquivos TSX/TS (sidebars, config, componentes) se resolvem à mão, sem
   agente.
5. Revise também os "removidos ou consolidados" do relatório: se a página que
   os substituiu ainda não está traduzida, traduza-a usando a tradução antiga
   como referência.
6. Rode `python3 tool/traducao/ancorar_titulos.py --todas --ref upstream/main`
   e `python3 tool/traducao/verificar.py` (sem argumentos ele confere todas as
   páginas traduzidas) e corrija o que aparecer.
7. Se alguma irmã em `docs/` foi traduzida agora, rode de novo
   `python3 tool/traducao/semear_versao.py --ref upstream/main`.
8. Quando `.traducao-pendente/` estiver vazio, apague a pasta, rode
   `python3 tool/traducao/gerar_todo.py` e faça o commit.
9. Só depois disso siga para as páginas novas (`TODO-TRADUCAO.md`).

**Analytics do upstream não volta.** O fork não publica o analytics nem a
telemetria do reactnative.dev oficial (Google Analytics `G-58L13S6BDP` via
`gtag`/googletagmanager, `@docusaurus/plugin-google-gtag`, o widget do
SurveyMonkey, `facebookAppId`): os visitantes daqui virariam dados das contas
da Meta/Google. Como o sync adota a árvore do upstream, ele pode trazer isso
de volta em `website/docusaurus.config.ts` ou `website/package.json`. O
`verificar.py` acusa como erro (`analytics`) qualquer um desses termos em
`website/` fora do conteúdo `.md`/`.mdx`; remova no próprio PR do sync
(e rode `yarn install` se mexer no `package.json`, para atualizar o
`yarn.lock`).

Nunca resolva um conflito trocando a página pela versão em inglês e mantendo
`ia-translated: true`, nem descartando o texto novo do upstream.

## Scripts de `tool/traducao/`

| Script | Para quê |
|---|---|
| `escopo.py` | Pastas do ciclo, versão estável e detecção da marcação (módulo comum). |
| `sincronizar_upstream.py [--alvo]` | Merge com o upstream preservando traduções (acima). |
| `semear_versao.py [--ref] [--versao]` | Copia, por merge de 3 vias, as traduções de `docs/` para a versão estável e traduz os rótulos do sidebar dela. |
| `verificar.py [--ref] [--estrito] [--resumo] [arquivos]` | **Checagens determinísticas** (abaixo). Sem argumentos confere todas as páginas marcadas do escopo. |
| `ancorar_titulos.py [--ref] (--todas \| arquivos)` | Acrescenta `{#id}` com o slug inglês aos títulos traduzidos. |
| `gerar_todo.py` | Regenera `TODO-TRADUCAO.md` (status por seção). |
| `setup.sh` | PyYAML, remote `upstream` e histórico. |

## Checagens determinísticas

```console
python3 tool/traducao/verificar.py
# só a estrutura, contra o inglês já incorporado (sem acusar defasagem):
python3 tool/traducao/verificar.py --ref $(cat tool/traducao/ultimo-sync-upstream.txt)
```

O `verificar.py` acusa como **erro**:

- `conflito`: marcadores de merge esquecidos;
- `frontmatter`: YAML inválido, `ia-translated` que não é `true` de primeiro
  nível, campo com valor no inglês que ficou vazio;
- `frontmatter-id`: `id`, `slug`, `tags`, `authors`, `date` etc. diferentes do
  inglês;
- `frontmatter-en`: `title`, `sidebar_label` ou `description` idêntico ao
  inglês e escrito em inglês;
- `flag`: marcação fora do lugar;
- `placeholder`: avisos de tradução pendente no texto;
- `ingles`: página marcada com 70% ou mais da prosa em inglês;
- `estrutura`: cercas de código, títulos, admonitions (e seus tipos),
  componentes JSX ou ids `{#id}` diferentes do inglês; linhas
  `import`/`export` diferentes; rótulo de link sem definição;
- `defasada`: o inglês da página mudou no upstream depois do último sync;
- `pendente`: `.traducao-pendente/` com arquivos não resolvidos;
- `ancora`: título traduzido sem o `{#id}` do inglês (corrija com
  `ancorar_titulos.py`);
- `link-interno`: link `](#id)` para âncora da própria página que não existe;
- `analytics`: analytics/telemetria do reactnative.dev oficial de volta no
  código do site (veja a regra do sync acima).

E como **aviso**: `parcial` (30% a 70% da prosa em inglês) e `defs-link`.

A compilação do MDX fica com o job `build` do `.github/workflows/pre-merge.yml`
(`yarn build`), que roda em todo PR. Quando uma checagem nova pegar um caso
que escapou, acrescente-a ao `verificar.py` em vez de corrigir só o arquivo.

## Personalizações do fork fora do conteúdo

### Aviso de página não traduzida

O plugin remark `website/remark/aviso-nao-traduzido.ts`, registrado em
`commonDocsOptions.remarkPlugins` do `docusaurus.config.ts`, põe no topo de
toda página de documentação **sem** a marcação `ia-translated` um aviso
("Esta página ainda está em inglês...") com link para o arquivo no GitHub. A
regra da marcação é a mesma do `tool/traducao/escopo.py`; mudou uma, mude a
outra. Vale para docs/, todas as versões e architecture/contributing/
community (os plugins de docs); não pega blog, home nem parciais `_*.mdx`. O
estilo está no fim de `website/src/css/customTheme.scss`.

Ao sincronizar, confira se continuam funcionando:

- `website/docusaurus.config.ts` (locale `pt-br`, textos da navegação),
  `website/sidebars*.ts` e `website/src/` (home, páginas e tema traduzidos);
- deploy no Firebase: `firebase.json`, `.firebaserc`,
  `.github/workflows/firebase-deploy.yml` e `firebase-preview.yml`;
- o `stale-bot.yml` e o `pre-merge.yml` do upstream continuam ativos aqui.
  Para remover uma automação do upstream a cada sync, ponha-a em
  `REMOVIDOS_NO_FORK` no `sincronizar_upstream.py`.

## Git

- Trabalhe em branch e abra PR para a `main`.
- Commits de tradução: `translate: <caminho>`; sincronização:
  `Merge upstream facebook/react-native-website main`.
