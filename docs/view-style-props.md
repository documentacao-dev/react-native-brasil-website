---
ia-translated: true
id: view-style-props
title: Props de Estilo de View
---

import ExperimentalAPIWarning from './\_experimental-api-warning.mdx';
import {getCoreBranchNameForCurrentVersion} from '@site/src/getCoreBranchNameForCurrentVersion';

### Exemplo {#example}

```SnackPlayer name=ViewStyleProps
import {View, StyleSheet} from 'react-native';
import {SafeAreaView, SafeAreaProvider} from 'react-native-safe-area-context';

const App = () => (
  <SafeAreaProvider>
    <SafeAreaView style={styles.container}>
      <View style={styles.top} />
      <View style={styles.middle} />
      <View style={styles.bottom} />
    </SafeAreaView>
  </SafeAreaProvider>
);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'space-between',
    padding: 20,
    margin: 10,
  },
  top: {
    flex: 0.3,
    backgroundColor: 'grey',
    borderWidth: 5,
    borderTopLeftRadius: 20,
    borderTopRightRadius: 20,
  },
  middle: {
    flex: 0.3,
    backgroundColor: 'beige',
    borderWidth: 5,
  },
  bottom: {
    flex: 0.3,
    backgroundColor: 'pink',
    borderWidth: 5,
    borderBottomLeftRadius: 20,
    borderBottomRightRadius: 20,
  },
});

export default App;
```

# Referência {#reference}

## Props

### `backfaceVisibility`

| Type                          |
| ----------------------------- |
| enum(`'visible'`, `'hidden'`) |

---

### `backgroundColor`

| Type               |
| ------------------ |
| [color](colors.md) |

---

### `backgroundImage`

`backgroundImage` permite desenhar um [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient) e um [`radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient) usando uma sintaxe semelhante à da web.

```tsx
// Simple usage:
<View style={{ backgroundImage: 'linear-gradient(45deg, blue, red)' }} />

<View style={{ backgroundImage: 'radial-gradient(ellipse farthest-corner at 30% 40%, red, blue)' }} />

// Also with PlatformColor:
<View
style={{
  backgroundImage: [
    {
      type: 'linear-gradient',
      direction: 'to bottom',
      colorStops: [
        {
          color: Platform.select({
            ios: PlatformColor('systemTealColor'),
            android: PlatformColor('@android:color/holo_purple'),
            default: 'blue',
          }),
          positions: ['0%'],
        },
        {color: 'green', positions: ['100%']},
      ],
    },
  ],
}}
/>
```

Exemplos mais complexos de uso podem ser encontrados no app RNTester (com suporte a `PlatformColor`):

- <a href={`https://github.com/react/react-native/blob/${getCoreBranchNameForCurrentVersion()}/packages/rn-tester/js/examples/LinearGradient/LinearGradientExample.js`}>LinearGradientExample.js</a>
- <a href={`https://github.com/react/react-native/blob/${getCoreBranchNameForCurrentVersion()}/packages/rn-tester/js/examples/RadialGradient/RadialGradientExample.js`}>RadialGradientExample.js</a>

| Type                                                                                                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| string, array of objects: `{type: 'linear-gradient', direction: string, colorStops: object[] }`, `{type: 'radial-gradient', shape: string, position: object, size: string, colorStops: object[] }` |

---

### `backgroundPosition`

Controla onde o gradiente de fundo é posicionado dentro da view. Isso é útil quando `backgroundImage` está definido e você quer deslocar ou centralizar o gradiente em vez de preenchê-lo em toda a área.

```tsx
<View
  style={{
    backgroundImage: 'radial-gradient(circle, #ff6b6b, #4ecdc4)',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
    backgroundSize: '50px 50px',
  }}
/>
```

| Type                                                                                    |
| --------------------------------------------------------------------------------------- |
| string \| array of objects `{top: string, left: string, right: string, bottom: string}` |

---

### `backgroundRepeat`

Controla se o gradiente de fundo é repetido, e como. Funciona junto com `backgroundImage` para repetir gradientes por toda a view.

```tsx
<View
  style={{
    backgroundImage: 'linear-gradient(45deg, #ff6b6b, #4ecdc4)',
    backgroundRepeat: 'repeat',
    backgroundSize: '20px 20px',
  }}
/>
```

| Type                                                                                               |
| -------------------------------------------------------------------------------------------------- |
| enum(`'repeat'`, `'space'`, `'round'`, `'no-repeat'`) \| array of objects `{x: string, y: string}` |

---

### `backgroundSize`

Controla o tamanho do gradiente de fundo. Isso é mais útil quando `backgroundImage` está definido e o gradiente não deve preencher a view inteira por padrão.

```tsx
<View
  style={{
    backgroundImage: 'linear-gradient(90deg, #a8edea, #fed6e3)',
    backgroundRepeat: 'no-repeat',
    backgroundSize: '100px 100px',
  }}
/>
```

| Type                                                |
| --------------------------------------------------- |
| string \| array of objects `{x: number, y: number}` |

---

### `borderBottomColor`

| Type               |
| ------------------ |
| [color](colors.md) |

---

### `borderBlockColor`

| Type               |
| ------------------ |
| [color](colors.md) |

---

### `borderBlockEndColor`

| Type               |
| ------------------ |
| [color](colors.md) |

---

### `borderBlockStartColor`

| Type               |
| ------------------ |
| [color](colors.md) |

---

### `borderBottomEndRadius`

| Type                              |
| --------------------------------- |
| number, string (percentage value) |

---

### `borderBottomLeftRadius`

| Type                              |
| --------------------------------- |
| number, string (percentage value) |

---

### `borderBottomRightRadius`

| Type                              |
| --------------------------------- |
| number, string (percentage value) |

---

### `borderBottomStartRadius`

| Type                              |
| --------------------------------- |
| number, string (percentage value) |

---

### `borderStartEndRadius`

| Type                              |
| --------------------------------- |
| number, string (percentage value) |

---

### `borderStartStartRadius`

| Type                              |
| --------------------------------- |
| number, string (percentage value) |

---

### `borderEndEndRadius`

| Type                              |
| --------------------------------- |
| number, string (percentage value) |

---

### `borderEndStartRadius`

| Type                              |
| --------------------------------- |
| number, string (percentage value) |

---

### `borderBottomWidth`

| Type   |
| ------ |
| number |

---

### `borderColor`

| Type               |
| ------------------ |
| [color](colors.md) |

---

### `borderCurve` <div className="label ios">iOS</div>

No iOS 13+, é possível alterar a curvatura dos cantos das bordas.

| Type                               |
| ---------------------------------- |
| enum(`'circular'`, `'continuous'`) |

---

### `borderEndColor`

| Type               |
| ------------------ |
| [color](colors.md) |

---

### `borderLeftColor`

| Type               |
| ------------------ |
| [color](colors.md) |

---

### `borderLeftWidth`

| Type   |
| ------ |
| number |

---

### `borderRadius`

Se a borda arredondada não estiver visível, tente aplicar `overflow: 'hidden'` também.

| Type                              |
| --------------------------------- |
| number, string (percentage value) |

---

### `borderRightColor`

| Type               |
| ------------------ |
| [color](colors.md) |

---

### `borderRightWidth`

| Type   |
| ------ |
| number |

---

### `borderStartColor`

| Type               |
| ------------------ |
| [color](colors.md) |

---

### `borderStyle`

| Type                                    |
| --------------------------------------- |
| enum(`'solid'`, `'dotted'`, `'dashed'`) |

---

### `borderTopColor`

| Type               |
| ------------------ |
| [color](colors.md) |

---

### `borderTopEndRadius`

| Type                              |
| --------------------------------- |
| number, string (percentage value) |

---

### `borderTopLeftRadius`

| Type                              |
| --------------------------------- |
| number, string (percentage value) |

---

### `borderTopRightRadius`

| Type                              |
| --------------------------------- |
| number, string (percentage value) |

---

### `borderTopStartRadius`

| Type                              |
| --------------------------------- |
| number, string (percentage value) |

---

### `borderTopWidth`

| Type                              |
| --------------------------------- |
| number, string (percentage value) |

---

### `borderWidth`

| Type   |
| ------ |
| number |

### `boxShadow`

:::note
`boxShadow` está disponível apenas na [Nova Arquitetura](/architecture/landing-page). Sombras externas são suportadas apenas no **Android 9+**. Sombras internas são suportadas apenas no **Android 10+**.
:::

Adiciona um efeito de sombra a um elemento, com a capacidade de controlar a posição, cor, tamanho e desfoque da sombra. Esta sombra aparece ao redor do lado externo ou interno da caixa de borda do elemento, dependendo se a sombra é _inset_ ou não. Esta é uma implementação compatível com a especificação da [propriedade de estilo web de mesmo nome](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow). Leia mais sobre todos os argumentos disponíveis na documentação de [BoxShadowValue](./boxshadowvalue).

Essas sombras podem ser compostas juntas para que um único `boxShadow` possa ser composto de múltiplas sombras diferentes.

`boxShadow` aceita uma string que imita a [sintaxe web](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow#syntax) ou um array de objetos [BoxShadowValue](./boxshadowvalue).

| Type                                      |
| ----------------------------------------- |
| array of BoxShadowValue objects \| string |

### `cursor` <div className="label ios">iOS</div>

No iOS 17+, definir como `pointer` permite efeitos de hover quando um ponteiro (como um trackpad ou stylus no iOS, ou o olhar do usuário no visionOS) está sobre a view.

| Type                        |
| --------------------------- |
| enum(`'auto'`, `'pointer'`) |

---

### `elevation` <div className="label android">Android</div>

Define a elevação de uma view, usando a [API de elevação](https://developer.android.com/develop/ui/views/theming/shadows-clipping#Elevation) subjacente do Android. Isso adiciona uma sombra projetada ao item e afeta a ordem z para views sobrepostas. Suportado apenas no Android 5.0+, não tem efeito em versões anteriores.

| Type   |
| ------ |
| number |

---

### `filter`

:::note
`filter` está disponível apenas na [Nova Arquitetura](/architecture/landing-page)
:::

Adiciona um filtro gráfico à `View`. Este filtro é composto por qualquer número de _funções de filtro_, cada uma representando alguma mudança atômica na composição gráfica da `View`. A lista completa de funções de filtro válidas é definida abaixo. `filter` será aplicado aos descendentes da `View` assim como à própria `View`. `filter` implica em `overflow: hidden`, então os descendentes serão cortados para caber nos limites da `View`.

As seguintes funções de filtro funcionam em todas as plataformas:

- `brightness`: Altera o brilho da `View`. Aceita um número não negativo ou porcentagem.
- `opacity`: Altera a opacidade, ou alfa, da `View`. Aceita um número não negativo ou porcentagem.

:::note
Devido a problemas com desempenho e conformidade com a especificação, essas são as únicas duas funções de filtro disponíveis no iOS. Há planos para explorar algumas soluções alternativas potenciais usando SwiftUI em vez de UIKit para esta implementação.
:::

<div className="label basic android">Android</div>

As seguintes funções de filtro funcionam apenas no Android:

- `blur`: Desfoca a `View` com um [desfoque Gaussiano](https://en.wikipedia.org/wiki/Gaussian_blur), onde o comprimento especificado representa o raio usado no algoritmo de desfoque. Qualquer valor DIP não negativo é válido (sem porcentagens). Quanto maior o valor, mais desfocado o resultado.
- `contrast`: Altera o contraste da `View`. Aceita um número não negativo ou porcentagem.
- `dropShadow`: Adiciona uma sombra ao redor da máscara alfa da `View` (apenas pixels com alfa diferente de zero na `View` irão projetar uma sombra). Aceita uma cor opcional representando a cor da sombra e 2 ou 3 comprimentos. Se 2 comprimentos forem especificados, eles são interpretados como `offsetX` e `offsetY` que irão transladar a sombra nas dimensões X e Y respectivamente. Se um terceiro comprimento for fornecido, ele é interpretado como o desvio padrão do desfoque Gaussiano usado na sombra - então um valor maior irá desfocar a sombra mais. Leia mais sobre os argumentos em [DropShadowValue](./dropshadowvalue.md).
- `grayscale`: Converte a `View` para [escala de cinza](https://en.wikipedia.org/wiki/Grayscale) pela quantidade especificada. Aceita um número não negativo ou porcentagem, onde `1` ou `100%` representa escala de cinza completa.
- `hueRotate`: Altera a [matiz](https://en.wikipedia.org/wiki/Hue) da View. O argumento desta função define o ângulo de uma roda de cores ao redor da qual a matiz será rotacionada, então, por exemplo, `360deg` não teria efeito. Este ângulo pode ter unidades `deg` ou `rad`.
- `invert`: Inverte as cores na `View`. Aceita um número não negativo ou porcentagem, onde `1` ou `100%` representa inversão completa.
- `sepia`: Converte a `View` para [sépia](<https://en.wikipedia.org/wiki/Sepia_(color)>). Aceita um número não negativo ou porcentagem, onde `1` ou `100%` representa sépia completo.
- `saturate`: Altera a [saturação](https://en.wikipedia.org/wiki/Colorfulness) da `View`. Aceita um número não negativo ou porcentagem.

:::note
`blur` e `dropShadow` são suportados apenas no **Android 12+**
:::

`filter` aceita um array de objetos compreendendo as funções de filtro acima ou uma string que imita a [sintaxe web](https://developer.mozilla.org/en-US/docs/Web/CSS/filter#syntax).

| Type                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| array of objects: `{brightness: number\|string}`, `{opacity: number\|string}`, `{blur: number\|string}`, `{contrast: number\|string}`, `{dropShadow: DropShadowValue\|string}`, `{grayscale: number\|string}`, `{hueRotate: number\|string}`, `{invert: number\|string}`, `{sepia: number\|string}`, `{saturate: number\|string}` or string |

---

### `mixBlendMode`

:::note
`mixBlendMode` está disponível apenas na [Nova Arquitetura](/architecture/landing-page) e no **Android 10+**
:::

Controla como a `View` mescla suas cores com os outros elementos do seu **contexto de empilhamento**. Confira a [documentação do MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/mix-blend-mode) para uma visão completa de cada função de mesclagem.

Para um controle mais granular sobre o que deve ser mesclado, veja [isolation](layout-props#isolation).

##### Valores de mixBlendMode {#mixblendmode-values}

- `normal`: O elemento é desenhado por cima do fundo, sem mesclagem.
- `multiply`: A cor de origem é multiplicada pela cor de destino e substitui o destino.
- `screen`: Multiplica os complementos das cores do fundo e da origem e, em seguida, calcula o complemento do resultado.
- `overlay`: Multiplica ou aplica `screen` às cores, dependendo do valor da cor do fundo.
- `darken`: Seleciona a mais escura entre as cores do fundo e da origem.
- `lighten`: Seleciona a mais clara entre as cores do fundo e da origem.
- `color-dodge`: Clareia a cor do fundo para refletir a cor de origem. Pintar com preto não produz nenhuma mudança.
- `color-burn`: Escurece a cor do fundo para refletir a cor de origem. Pintar com branco não produz nenhuma mudança.
- `hard-light`: Multiplica ou aplica `screen` às cores, dependendo do valor da cor de origem. O efeito é semelhante a iluminar o fundo com um holofote forte.
- `soft-light`: Escurece ou clareia as cores, dependendo do valor da cor de origem. O efeito é semelhante a iluminar o fundo com um holofote difuso.
- `difference`: Subtrai a mais escura das duas cores da mais clara.
- `exclusion`: Produz um efeito semelhante ao do modo Difference, mas com menor contraste.
- `hue`: Cria uma cor com a matiz da cor de origem e a saturação e a luminosidade da cor do fundo.
- `saturation`: Cria uma cor com a saturação da cor de origem e a matiz e a luminosidade da cor do fundo.
- `color`: Cria uma cor com a matiz e a saturação da cor de origem e a luminosidade da cor do fundo. Isso preserva os tons de cinza do fundo e é útil para colorir imagens monocromáticas ou tingir imagens coloridas.
- `luminosity`: Cria uma cor com a luminosidade da cor de origem e a matiz e a saturação da cor do fundo. Produz o efeito inverso ao do modo Color.
- `plus-lighter`: Soma os canais de cor de origem e de destino, limitando cada um ao valor máximo.

| Type                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum(`'normal'`, `'multiply'`, `'screen'`, `'overlay'`, `'darken'`, `'lighten'`, `'color-dodge'`, `'color-burn'`, `'hard-light'`, `'soft-light'`, `'difference'`, `'exclusion'`, `'hue'`, `'saturation'`, `'color'`, `'luminosity'`, `'plus-lighter'`) |

---

### `opacity`

| Type   |
| ------ |
| number |

---

### `outlineColor`

:::note
`outlineColor` está disponível apenas na [Nova Arquitetura](/architecture/landing-page)
:::

Define a cor do contorno de um elemento. Veja a [documentação web](https://developer.mozilla.org/en-US/docs/Web/CSS/outline-color) para mais detalhes.

| Type               |
| ------------------ |
| [color](colors.md) |

---

### `outlineOffset`

:::note
`outlineOffset` está disponível apenas na [Nova Arquitetura](/architecture/landing-page)
:::

Define a quantidade de espaço entre um contorno e os limites de um elemento. Não afeta o layout. Veja a [documentação web](https://developer.mozilla.org/en-US/docs/Web/CSS/outline-offset) para mais detalhes.

| Type   |
| ------ |
| number |

---

### `outlineStyle`

:::note
`outlineStyle` está disponível apenas na [Nova Arquitetura](/architecture/landing-page)
:::

Define o estilo do contorno de um elemento. Veja a [documentação web](https://developer.mozilla.org/en-US/docs/Web/CSS/outline-style) para mais detalhes.

| Type                                    |
| --------------------------------------- |
| enum(`'solid'`, `'dotted'`, `'dashed'`) |

---

### `outlineWidth`

:::note
`outlineWidth` está disponível apenas na [Nova Arquitetura](/architecture/landing-page)
:::

A largura de um contorno que é desenhado ao redor de um elemento, fora da borda. Não afeta o layout. Veja a [documentação web](https://developer.mozilla.org/en-US/docs/Web/CSS/outline-width) para mais detalhes.

| Type   |
| ------ |
| number |

---

### `pointerEvents`

Controla se a `View` pode ser o alvo de eventos de toque.

- `'auto'`: A View pode ser o alvo de eventos de toque.
- `'none'`: A View nunca é o alvo de eventos de toque.
- `'box-none'`: A View nunca é o alvo de eventos de toque, mas suas subviews podem ser.
- `'box-only'`: A view pode ser o alvo de eventos de toque, mas suas subviews não podem ser.

| Type                                                  |
| ----------------------------------------------------- |
| enum(`'auto'`, `'box-none'`, `'box-only'`, `'none'` ) |
