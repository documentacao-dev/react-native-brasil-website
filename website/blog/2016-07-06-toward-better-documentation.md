---
ia-translated: true
title: Rumo a uma Melhor Documentação
author: Kevin Lacker
authorTitle: Engineering Manager at Facebook
authorURL: 'https://twitter.com/lacker'
authorImageURL: 'https://www.gravatar.com/avatar/9b790592be15d4f55a5ed7abb5103304?s=128'
authorTwitter: lacker
tags: [announcement]
---

Parte de ter uma ótima experiência de desenvolvedor é ter uma ótima documentação. Muitas coisas fazem parte da criação de bons documentos - a documentação ideal é concisa, útil, precisa, completa e encantadora. Recentemente temos trabalhado duro para melhorar os documentos com base no seu feedback, e queríamos compartilhar algumas das melhorias que fizemos.

## Exemplos Inline {#inline-examples}

Quando você aprende uma nova biblioteca, uma nova linguagem de programação ou um novo framework, há um momento lindo quando você primeiro escreve um pouco de código, testa, vê se funciona... e _funciona_. Você criou algo real. Queríamos colocar essa experiência visceral direto em nossos documentos. Assim:

```ReactNativeWebPlayer
import React, { Component } from 'react';
import { AppRegistry, Text, View } from 'react-native';

class ScratchPad extends Component {
  render() {
    return (
      <View style={{flex: 1}}>
        <Text style={{fontSize: 30, flex: 1, textAlign: 'center'}}>
          Isn't this cool?
        </Text>
        <Text style={{fontSize: 100, flex: 1, textAlign: 'center'}}>
          👍
        </Text>
      </View>
    );
  }
}

AppRegistry.registerComponent('ScratchPad', () => ScratchPad);
```

Achamos que esses exemplos inline, usando o módulo [`react-native-web-player`](https://github.com/dabbott/react-native-web-player) com ajuda de [Devin Abbott](https://twitter.com/devinaabbott), são uma ótima maneira de aprender o básico do React Native, e atualizamos nosso [tutorial para novos desenvolvedores React Native](/docs/tutorial) para usá-los sempre que possível. Confira - se você já teve curiosidade de ver o que aconteceria se você modificasse apenas um pequeno pedaço do código de exemplo, esta é uma maneira realmente boa de explorar.

O motor de simulação principal é fornecido pelo projeto [`react-native-web`](https://github.com/necolas/react-native-web) de [Nicolas Gallagher](https://twitter.com/necolas), que fornece uma maneira de exibir componentes React Native como `Text` e `View` na web. Confira o [`react-native-web`](https://github.com/necolas/react-native-web) se você está interessado em construir experiências mobile e web que compartilham uma grande parte da base de código.

## Melhores Guias {#better-guides}

Em algumas partes do React Native, existem várias maneiras de fazer as coisas, e ouvimos feedback de que poderíamos fornecer uma melhor orientação.

Temos um novo [guia de Navegação](/docs/navigation) que compara as diferentes abordagens e aconselha sobre o que você deve usar - `Navigator`, `NavigatorIOS`, `NavigationExperimental`. A médio prazo, estamos trabalhando para melhorar e consolidar essas interfaces. A curto prazo, esperamos que um guia melhor torne sua vida mais fácil.

Também temos um novo [guia para lidar com toques](/docs/handling-touches) que explica alguns dos conceitos básicos de criação de interfaces semelhantes a botões e um breve resumo das diferentes maneiras de lidar com eventos de toque.

Outra área em que trabalhamos é Flexbox. Isso inclui tutoriais sobre como [lidar com layout com Flexbox](/docs/flexbox) e como controlar [o tamanho dos componentes](/docs/height-and-width). Também inclui uma [lista não tão atraente mas esperamos útil de todos os props que controlam layout no React Native](/docs/layout-props).

## Começando {#getting-started}

Quando você começa a configurar um ambiente de desenvolvimento React Native em sua máquina, você tem que fazer um monte de instalação e configuração de coisas. É difícil tornar a instalação uma experiência realmente divertida e emocionante, mas podemos pelo menos torná-la o mais rápida e indolor possível.

Construímos um [novo fluxo de trabalho de Começando](/docs/next/getting-started) que permite selecionar seu sistema operacional de desenvolvimento e seu sistema operacional móvel antecipadamente, para fornecer um lugar conciso com todas as instruções de configuração. Também passamos pelo processo de instalação para ter certeza de que tudo funcionou e garantir que cada ponto de decisão tivesse uma recomendação clara. Depois de testar em nossos colegas inocentes, temos bastante certeza de que isso é uma melhoria.

Também trabalhamos no [guia para integrar React Native em um aplicativo existente](/docs/integration-with-existing-apps). Muitos dos maiores aplicativos que usam React Native, como o próprio aplicativo do Facebook, na verdade constroem parte do aplicativo em React Native e parte usando ferramentas de desenvolvimento regulares. Esperamos que este guia torne mais fácil para mais pessoas construir aplicativos desta maneira.

## Precisamos da Sua Ajuda {#we-need-your-help}

Seu feedback nos permite saber o que devemos priorizar. Sei que algumas pessoas lerão este post do blog e pensarão "Melhor documentação? Pffft. A documentação para X ainda está péssima!". Isso é ótimo - precisamos dessa energia. A melhor maneira de nos dar feedback depende do tipo de feedback.

Se você encontrar um erro na documentação, como descrições imprecisas ou código que não funciona de fato, [registre um issue](https://github.com/facebook/react-native/issues). Marque-o com "Documentation", para que seja mais fácil encaminhá-lo para as pessoas certas.

Se não houver um erro específico, mas algo na documentação é fundamentalmente confuso, não é uma boa opção para um issue do GitHub. Em vez disso, poste no [Canny](https://react-native.canny.io/feature-requests) sobre a área dos documentos que poderia usar ajuda. Isso nos ajuda a priorizar quando estamos fazendo trabalhos mais gerais, como escrever guias.

Obrigado por ler até aqui, e obrigado por usar React Native!
