---
ia-translated: true
title: Lançamento do React Native 0.59
author: Ryan Turner
authorTitle: Mantenedor Principal & Desenvolvedor React Native
authorURL: 'https://twitter.com/turnrye'
authorImageURL: 'https://avatars0.githubusercontent.com/u/701035?s=460&v=4'
authorTwitter: turnrye
tags: [announcement, release]
---

Bem-vindo ao lançamento 0.59 do React Native! Este é mais um grande lançamento com 644 commits de 88 contribuidores. As contribuições também vêm de outras formas, então _obrigado_ por manter issues, fomentar comunidades e ensinar as pessoas sobre React Native. Este mês traz uma série de mudanças muito aguardadas, e esperamos que você as aproveite.

## 🎣 Hooks chegaram {#-hooks-are-here}

React Hooks fazem parte deste lançamento, o que permite reutilizar lógica com estado entre componentes. Há muito buzz sobre hooks, mas se você ainda não ouviu falar, dê uma olhada em alguns dos recursos maravilhosos abaixo:

> - [Introducing Hooks](https://reactjs.org/docs/hooks-intro.html) explica por que estamos adicionando Hooks ao React.
> - [Hooks at a Glance](https://reactjs.org/docs/hooks-overview.html) é uma visão geral acelerada dos Hooks integrados.
> - [Building Your Own Hooks](https://reactjs.org/docs/hooks-custom.html) demonstra a reutilização de código com Hooks personalizados.
> - [Making Sense of React Hooks](https://medium.com/@dan_abramov/making-sense-of-react-hooks-fdbde8803889) explora as novas possibilidades desbloqueadas pelos Hooks.
> - [useHooks.com](https://usehooks.com/) apresenta receitas e demonstrações de Hooks mantidos pela comunidade.

Certifique-se de experimentar isso em seus aplicativos. Esperamos que você ache a reutilização tão empolgante quanto nós.

## 📱 JSC atualizado significa ganhos de performance e suporte a 64 bits no Android {#-updated-jsc-means-performance-gains-and-64-bit-support-on-android}

React Native usa JSC ([JavaScriptCore](https://webkit.org/)) para alimentar sua aplicação. O JSC no Android tinha alguns anos de idade, o que significava que muitos recursos modernos de JavaScript não eram suportados. Pior ainda, seu desempenho era ruim em comparação com o JSC moderno do iOS. Com este lançamento, tudo isso muda.

Graças ao trabalho incrível de [@DanielZlotin](https://github.com/danielzlotin), [@dulmandakh](https://github.com/dulmandakh), [@gengjiawen](https://github.com/gengjiawen), [@kmagiera](https://github.com/kmagiera) e [@kudo](https://github.com/kudo), o JSC alcançou os últimos anos. Isso traz consigo suporte a 64 bits, suporte a JavaScript moderno e [grandes melhorias de performance](https://github.com/react-native-community/jsc-android-buildscripts/tree/master/measure). Parabéns também por tornar este um processo sustentável agora, para que possamos aproveitar futuras melhorias do WebKit sem tanto trabalho braçal, e obrigado Software Mansion e Expo por tornar este trabalho possível.

## 💨 Inicialização mais rápida de apps com inline requires {#-faster-app-launches-with-inline-requires}

Queremos ajudar as pessoas a terem aplicativos React Native performáticos por padrão e estamos trabalhando para trazer as otimizações do Facebook para a comunidade. As aplicações carregam recursos conforme necessário, em vez de desacelerar a inicialização. Este recurso é chamado de "inline requires", pois permite que o Metro identifique componentes para serem carregados preguiçosamente. Aplicativos com uma arquitetura de componentes profunda e variada verão a maior melhoria.

![source of the `metro.config.js` file in the 0.59 template, demonstrating where to enable `inlineRequires`](/blog/assets/inline-requires.png)

Precisamos que a comunidade nos informe como funciona antes de ativarmos por padrão. Quando você atualizar para 0.59, haverá um novo arquivo `metro.config.js`; mude as opções para true e nos dê [seu feedback](https://twitter.com/hashtag/inline-requires)! Leia mais sobre inline requires [na documentação de performance](/docs/performance#inline-requires) para fazer benchmark do seu aplicativo.

## 🚅 Lean core está em andamento {#-lean-core-is-underway}

React Native é um projeto grande e complexo com um repositório complicado. Isso torna a base de código menos acessível para contribuidores, difícil de testar e inchada como dependência de desenvolvimento. [Lean Core](https://github.com/react-native-community/discussions-and-proposals/issues/6) é nosso esforço para resolver esses problemas migrando código para bibliotecas separadas para melhor gerenciamento. Os últimos lançamentos viram os primeiros passos disso, mas [vamos ficar sérios](https://www.youtube.com/watch?v=FMLKb4or8yg).

Você pode notar que componentes adicionais agora estão oficialmente depreciados. Esta é uma ótima notícia, pois agora existem mantenedores para esses recursos que os mantêm ativamente. Preste atenção às mensagens de aviso e migre para as novas bibliotecas para esses recursos, porque eles serão removidos em um lançamento futuro. Abaixo está uma tabela indicando o componente, seu status e para onde você pode migrar seu uso.

| Component            | Depreciado? | Nova localização                                                                                                                                         |
| -------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AsyncStorage**     | 0.59        | [@react-native-community/react-native-async-storage](https://github.com/react-native-community/react-native-async-storage)                               |
| **ImageStore**       | 0.59        | [expo-file-system](https://github.com/expo/expo/tree/master/packages/expo-file-system) or [react-native-fs](https://github.com/itinance/react-native-fs) |
| **MaskedViewIOS**    | 0.59        | [@react-native-community/react-native-masked-view](https://github.com/react-native-community/react-native-masked-view)                                   |
| **NetInfo**          | 0.59        | [@react-native-community/react-native-netinfo](https://github.com/react-native-community/react-native-netinfo)                                           |
| **Slider**           | 0.59        | [@react-native-community/react-native-slider](https://github.com/react-native-community/react-native-slider)                                             |
| **ViewPagerAndroid** | 0.59        | [@react-native-community/react-native-viewpager](https://github.com/react-native-community/react-native-viewpager)                                       |

Nos próximos meses, haverá muitos mais componentes seguindo este caminho para um core mais enxuto. Estamos procurando ajuda com isso &mdash; vá até o [umbrella do lean core](https://github.com/facebook/react-native/issues/23313) para contribuir.

## 👩🏽‍💻 Melhorias no CLI {#-cli-improvements}

As ferramentas de linha de comando do React Native são o ponto de entrada do desenvolvedor para o ecossistema, mas tinham problemas de longa data e faltava suporte oficial. As ferramentas CLI foram movidas para um [novo repositório](https://github.com/react-native-community/react-native-cli), e um [grupo dedicado de mantenedores](https://blog.callstack.io/the-react-native-cli-has-a-new-home-79b63838f0e6) já fez algumas melhorias empolgantes.

Os logs estão muito melhor formatados agora. Os comandos agora são executados quase instantaneamente &mdash; você notará imediatamente a diferença:

![0.58's CLI is slow to start](/blog/assets/0.58-cli-speed.png)![0.58's CLI is nearly instantaneous](/blog/assets/0.59-cli-speed.png)

## 🚀 Atualizando para 0.59 {#-upgrading-to-059}

Ouvimos seu feedback sobre o [processo de atualização do React Native](https://github.com/react-native-community/discussions-and-proposals/issues/68) e estamos tomando medidas para melhorar a experiência em [lançamentos futuros](https://github.com/react-native-community/discussions-and-proposals/issues/64#issuecomment-444775432). Para atualizar para 0.59, recomendamos usar [`rn-diff-purge`](https://github.com/react-native-community/rn-diff-purge) para determinar o que mudou entre sua versão atual do React Native e 0.59, e então aplicar essas alterações manualmente. Depois de atualizar seu projeto para 0.59, você poderá usar o comando `react-native upgrade` recém-melhorado (baseado em `rn-diff-purge`!) para atualizar para 0.60 e versões posteriores conforme novos lançamentos se tornarem disponíveis.

## 🔨 Breaking Changes

O suporte ao Android em 0.59 foi limpo seguindo as últimas recomendações do Google, o que pode resultar em potencial quebra de aplicativos existentes. Este problema pode se apresentar como uma falha em tempo de execução e uma mensagem, "You need to use a Theme.AppCompat theme (or descendant) with this activity". Recomendamos atualizar o arquivo `AndroidManifest.xml` do seu projeto, certificando-se de que o valor `android:theme` seja um tema `AppCompat` (como `@style/Theme.AppCompat.Light.NoActionBar`).

O comando `react-native-git-upgrade` foi removido em 0.59, em favor do comando `react-native upgrade` recém-melhorado.

## 🤗 Agradecimentos {#-thanks}

Muitos novos contribuidores ajudaram com [habilitação de geração de código nativo a partir de tipos flow](https://github.com/facebook/react-native/issues/22990) e [resolução de avisos do Xcode](https://github.com/facebook/react-native/issues/22609) - estas são ótimas maneiras de aprender como o React Native funciona e contribuir para o bem maior. Obrigado! Fique de olho em issues similares no futuro.

Embora estes sejam os destaques que notamos, há muitos outros para se entusiasmar. Para ver todas as atualizações, dê uma olhada no [changelog](https://github.com/react-native-community/react-native-releases/blob/master/CHANGELOG.md). 0.59 é um lançamento enorme – mal podemos esperar para você experimentá-lo.

Temos ainda mais melhorias chegando durante o resto do ano. Fique ligado!

[Ryan](https://github.com/turnrye) e toda a [equipe principal do React Native](https://twitter.com/reactnative)
