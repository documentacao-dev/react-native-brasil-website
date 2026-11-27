---
ia-translated: true
title: Usando Native Driver para Animated
author: Janic Duplessis
authorTitle: Software Engineer at App & Flow
authorURL: 'https://twitter.com/janicduplessis'
authorImageURL: 'https://secure.gravatar.com/avatar/8d6b6c0f5b228b0a8566a69de448b9dd?s=128'
authorTwitter: janicduplessis
tags: [engineering]
---

Pelo último ano, temos trabalhado na melhoria do desempenho de animações que usam a biblioteca Animated. Animações são muito importantes para criar uma experiência de usuário bonita, mas também podem ser difíceis de fazer corretamente. Queremos facilitar para os desenvolvedores criarem animações performáticas sem ter que se preocupar com algum código causando lentidão.

## O que é isso? {#what-is-this}

A API Animated foi projetada com uma restrição muito importante em mente: ela é serializável. Isso significa que podemos enviar tudo sobre a animação para o nativo antes mesmo de ela ter começado e permite que o código nativo execute a animação na UI thread sem ter que passar pela bridge em cada frame. É muito útil porque uma vez que a animação tenha começado, a JS thread pode ser bloqueada e a animação ainda será executada suavemente. Na prática, isso pode acontecer muito porque o código do usuário é executado na JS thread e as renderizações do React também podem bloquear o JS por um longo tempo.

## Um pouco de história... {#a-bit-of-history}

Este projeto começou há cerca de um ano, quando a Expo construiu o aplicativo li.st no Android. [Krzysztof Magiera](https://twitter.com/kzzzf) foi contratado para construir a implementação inicial no Android. Acabou funcionando bem e li.st foi o primeiro aplicativo a ser lançado com animações native driven usando Animated. Alguns meses depois, [Brandon Withrow](https://github.com/buba447) construiu a implementação inicial no iOS. Depois disso, [Ryan Gomba](https://twitter.com/ryangomba) e eu trabalhamos na adição de recursos ausentes como suporte para `Animated.event`, bem como corrigir bugs que encontramos ao usar em aplicativos de produção. Este foi verdadeiramente um esforço da comunidade e gostaria de agradecer a todos que estiveram envolvidos, bem como a Expo por patrocinar grande parte do desenvolvimento. Agora é usado pelos componentes `Touchable` no React Native, bem como para animações de navegação na recém-lançada biblioteca [React Navigation](https://github.com/react-community/react-navigation).

## Como funciona? {#how-does-it-work}

Primeiro, vamos verificar como as animações funcionam atualmente usando Animated com o driver JS. Ao usar Animated, você declara um grafo de nós que representam as animações que deseja executar e, em seguida, usa um driver para atualizar um valor Animated usando uma curva predefinida. Você também pode atualizar um valor Animated conectando-o a um evento de uma `View` usando `Animated.event`.

![](/blog/assets/animated-diagram.png)

Aqui está um detalhamento das etapas para uma animação e onde isso acontece:

- JS: O driver de animação usa `requestAnimationFrame` para executar em cada frame e atualizar o valor que ele dirige usando o novo valor que calcula com base na curva de animação.
- JS: Valores intermediários são calculados e passados para um nó de props que está anexado a uma `View`.
- JS: A `View` é atualizada usando `setNativeProps`.
- JS to Native bridge.
- Native: A `UIView` ou `android.View` é atualizada.

Como você pode ver, a maior parte do trabalho acontece na JS thread. Se ela estiver bloqueada, a animação pulará frames. Ela também precisa passar pela JS to Native bridge em cada frame para atualizar as views nativas.

O que o native driver faz é mover todas essas etapas para o nativo. Como Animated produz um grafo de nós animados, ele pode ser serializado e enviado para o nativo apenas uma vez quando a animação começa, eliminando a necessidade de callback para a JS thread; o código nativo pode cuidar de atualizar as views diretamente na UI thread em cada frame.

Aqui está um exemplo de como podemos serializar um valor animado e um nó de interpolação (não a implementação exata, apenas um exemplo).

Criar o nó de valor nativo, este é o valor que será animado:

```
NativeAnimatedModule.createNode({
  id: 1,
  type: 'value',
  initialValue: 0,
});
```

Criar o nó de interpolação nativo, isso diz ao native driver como interpolar um valor:

```
NativeAnimatedModule.createNode({
  id: 2,
  type: 'interpolation',
  inputRange: [0, 10],
  outputRange: [10, 0],
  extrapolate: 'clamp',
});
```

Criar o nó de props nativo, isso diz ao native driver qual prop na view ele está anexado:

```
NativeAnimatedModule.createNode({
  id: 3,
  type: 'props',
  properties: ['style.opacity'],
});
```

Conectar nós juntos:

```
NativeAnimatedModule.connectNodes(1, 2);
NativeAnimatedModule.connectNodes(2, 3);
```

Conectar o nó de props a uma view:

```
NativeAnimatedModule.connectToView(3, ReactNative.findNodeHandle(viewRef));
```

Com isso, o módulo animated nativo tem todas as informações necessárias para atualizar as views nativas diretamente sem ter que ir para o JS para calcular qualquer valor.

Tudo o que resta fazer é realmente iniciar a animação especificando que tipo de curva de animação queremos e qual valor animado atualizar. Animações de timing também podem ser simplificadas calculando cada frame da animação antecipadamente em JS para tornar a implementação nativa menor.

```
NativeAnimatedModule.startAnimation({
  type: 'timing',
  frames: [0, 0.1, 0.2, 0.4, 0.65, ...],
  animatedValueId: 1,
});
```

E agora aqui está o detalhamento do que acontece quando a animação é executada:

- Native: O native driver de animação usa `CADisplayLink` ou `android.view.Choreographer` para executar em cada frame e atualizar o valor que ele dirige usando o novo valor que calcula com base na curva de animação.
- Native: Valores intermediários são calculados e passados para um nó de props que está anexado a uma view nativa.
- Native: A `UIView` ou `android.View` é atualizada.

Como você pode ver, sem mais JS thread e sem mais bridge, o que significa animações mais rápidas! 🎉🎉

## Como uso isso no meu aplicativo? {#how-do-i-use-this-in-my-app}

Para animações normais, a resposta é simples: apenas adicione `useNativeDriver: true` à configuração de animação ao iniciá-la.

Antes:

```
Animated.timing(this.state.animatedValue, {
  toValue: 1,
  duration: 500,
}).start();
```

Depois:

```
Animated.timing(this.state.animatedValue, {
  toValue: 1,
  duration: 500,
  useNativeDriver: true, // <-- Add this
}).start();
```

Valores Animated são compatíveis apenas com um driver, então se você usar o native driver ao iniciar uma animação em um valor, certifique-se de que cada animação nesse valor também use o native driver.

Também funciona com `Animated.event`, isso é muito útil se você tiver uma animação que deve seguir a posição de scroll porque sem o native driver ela sempre será executada um frame atrás do gesto por causa da natureza assíncrona do React Native.

Antes:

```
<ScrollView
  scrollEventThrottle={16}
  onScroll={Animated.event(
    [{ nativeEvent: { contentOffset: { y: this.state.animatedValue } } }]
  )}
>
  {content}
</ScrollView>
```

Depois:

```
<Animated.ScrollView // <-- Use the Animated ScrollView wrapper
  scrollEventThrottle={1} // <-- Use 1 here to make sure no events are ever missed
  onScroll={Animated.event(
    [{ nativeEvent: { contentOffset: { y: this.state.animatedValue } } }],
    { useNativeDriver: true } // <-- Add this
  )}
>
  {content}
</Animated.ScrollView>
```

## Ressalvas {#caveats}

Nem tudo que você pode fazer com Animated é atualmente suportado no Native Animated. A principal limitação é que você pode apenas animar propriedades não relacionadas a layout, coisas como `transform` e `opacity` funcionarão, mas propriedades de Flexbox e posição não. Outra é com `Animated.event`, ele só funcionará com eventos diretos e não eventos bubbling. Isso significa que não funciona com `PanResponder`, mas funciona com coisas como `ScrollView#onScroll`.

Native Animated também faz parte do React Native há um bom tempo, mas nunca foi documentado porque era considerado experimental. Por causa disso, certifique-se de que está usando uma versão recente (0.40+) do React Native se quiser usar este recurso.

## Recursos {#resources}

Para mais informações sobre animated, recomendo assistir [esta palestra](https://www.youtube.com/watch?v=xtqUJVqpKNo) por [Christopher Chedeau](https://twitter.com/Vjeux).

Se você quer um mergulho profundo em animações e como transferi-las para o nativo pode melhorar a experiência do usuário, há também [esta palestra](https://www.youtube.com/watch?v=qgSMjYWqBk4) por [Krzysztof Magiera](https://twitter.com/kzzzf).
