---
ia-translated: true
title: Referência de Bots
---

## pull-bot

<<<<<<< pt
Este bot linter de pull request realiza verificações básicas de sanidade sempre que um pull request é criado. Ele pode deixar um comentário no pull request se não conseguir encontrar um test plan ou um changelog na descrição, ou se perceber que o pull request não foi aberto contra o branch `main`. Este bot usa [Danger](https://danger.systems), e sua configuração pode ser encontrada em [`dangerfile.js`](https://github.com/facebook/react-native/blob/main/packages/react-native-bots/dangerfile.js).
||||||| base_en
This pull request linter bot performs basic sanity checks whenever a pull request is created. It might leave a comment on a pull request if it is unable to find a test plan or a changelog in the description, or if it notices that the pull request was not opened against the `main` branch. This bot uses [Danger](https://danger.systems), and its configuration can be found in the [`dangerfile.js`](https://github.com/facebook/react-native/blob/main/packages/react-native-bots/dangerfile.js).
=======
This pull request linter bot performs basic sanity checks whenever a pull request is created. It might leave a comment on a pull request if it is unable to find a test plan or a changelog in the description, or if it notices that the pull request was not opened against the `main` branch. This bot uses [Danger](https://danger.systems), and its configuration can be found in the [`dangerfile.js`](https://github.com/react/react-native/blob/main/packages/react-native-bots/dangerfile.js).
>>>>>>> new_en

## analysis-bot

<<<<<<< pt
O bot de análise de código coleta feedback de ferramentas como Prettier, eslint e Flow sempre que um commit é adicionado a um pull request. Se alguma dessas ferramentas encontrar problemas com o código, o bot adicionará esses problemas como comentários de revisão inline no pull request. Sua configuração pode ser encontrada no arquivo [`analyze_code.sh`](https://github.com/facebook/react-native/blob/main/scripts/circleci/analyze_code.sh) no repositório principal.
||||||| base_en
The code analysis bot collects feedback from tools such as Prettier, eslint, and Flow whenever a commit is added to a pull request. If any of these tools finds issues with the code, the bot will add these as inline review comments on the pull request. Its configuration can be found in the [`analyze_code.sh`](https://github.com/facebook/react-native/blob/main/scripts/circleci/analyze_code.sh) file in core repository.
=======
The code analysis bot collects feedback from tools such as Prettier, eslint, and Flow whenever a commit is added to a pull request. If any of these tools finds issues with the code, the bot will add these as inline review comments on the pull request. Its configuration can be found in the [`analyze_code.sh`](https://github.com/react/react-native/blob/main/scripts/circleci/analyze_code.sh) file in core repository.
>>>>>>> new_en

## label-actions

<<<<<<< pt
Um bot que age sobre uma issue ou pull request com base em uma label. Configurado em [`.github/workflows/on-issue-labeled.yml`](https://github.com/facebook/react-native/blob/main/.github/workflows/on-issue-labeled.yml).
||||||| base_en
A bot that acts on an issue or pull request based on a label. Configured in [`.github/workflows/on-issue-labeled.yml`](https://github.com/facebook/react-native/blob/main/.github/workflows/on-issue-labeled.yml).
=======
A bot that acts on an issue or pull request based on a label. Configured in [`.github/workflows/on-issue-labeled.yml`](https://github.com/react/react-native/blob/main/.github/workflows/on-issue-labeled.yml).
>>>>>>> new_en

## github-actions

<<<<<<< pt
Um bot que executa ações definidas em um workflow do GitHub. Workflows são configurados em [`.github/workflows`](https://github.com/facebook/react-native/tree/main/.github/workflows).
||||||| base_en
A bot that performs actions defined in a GitHub workflow. Workflows are configured in [`.github/workflows`](https://github.com/facebook/react-native/tree/main/.github/workflows).
=======
A bot that performs actions defined in a GitHub workflow. Workflows are configured in [`.github/workflows`](https://github.com/react/react-native/tree/main/.github/workflows).
>>>>>>> new_en

## facebook-github-bot

O Facebook GitHub Bot é usado em vários projetos open source na Meta. No caso do React Native, você provavelmente o encontrará quando ele fizer push de um merge commit para `main` após um pull request ser importado com sucesso para o source control interno do Facebook. Ele também informará aos autores se estiverem faltando um Contributor License Agreement.

## react-native-bot

O React Native bot é uma ferramenta que nos ajuda a automatizar vários processos descritos neste wiki. Configurado em [`hramos/react-native-bot`](https://github.com/hramos/react-native-bot).
