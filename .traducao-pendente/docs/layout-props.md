---
ia-translated: true
id: layout-props
title: Props de Layout
---

import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; import constants from '@site/core/TabsConstants';

:::info
Exemplos mais detalhados sobre essas propriedades podem ser encontrados na página [Layout with Flexbox](flexbox).
:::

### Exemplo

O exemplo a seguir mostra como diferentes propriedades podem afetar ou moldar um layout React Native. Você pode tentar, por exemplo, adicionar ou remover quadrados da UI enquanto altera os valores da propriedade `flexWrap`.

<Tabs groupId="language" queryString defaultValue={constants.defaultSnackLanguage} values={constants.snackLanguages}>
<TabItem value="javascript">

```SnackPlayer name=LayoutProps%20Example&ext=js
import {useState} from 'react';
import {Button, ScrollView, StyleSheet, Text, View} from 'react-native';
import {SafeAreaView, SafeAreaProvider} from 'react-native-safe-area-context';

const App = () => {
  const [flexDirection, setFlexDirection] = useState(0);
  const [justifyContent, setJustifyContent] = useState(0);
  const [alignItems, setAlignItems] = useState(0);
  const [direction, setDirection] = useState(0);
  const [wrap, setWrap] = useState(0);

  const [squares, setSquares] = useState([<Square />, <Square />, <Square />]);

  const hookedStyles = {
    flexDirection: flexDirections[flexDirection],
    justifyContent: justifyContents[justifyContent],
    alignItems: alignItemsArr[alignItems],
    direction: directions[direction],
    flexWrap: wraps[wrap],
  };

  const changeSetting = (value, options, setterFunction) => {
    if (value === options.length - 1) {
      setterFunction(0);
      return;
    }
    setterFunction(value + 1);
  };

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.container}>
        <View style={[styles.container, styles.playingSpace, hookedStyles]}>
          {squares.map(elem => elem)}
        </View>
        <ScrollView style={styles.layoutContainer}>
          <View style={styles.controlSpace}>
            <View style={styles.buttonView}>
              <Button
                title="Change Flex Direction"
                onPress={() =>
                  changeSetting(flexDirection, flexDirections, setFlexDirection)
                }
              />
              <Text style={styles.text}>{flexDirections[flexDirection]}</Text>
            </View>
            <View style={styles.buttonView}>
              <Button
                title="Change Justify Content"
                onPress={() =>
                  changeSetting(
                    justifyContent,
                    justifyContents,
                    setJustifyContent,
                  )
                }
              />
              <Text style={styles.text}>{justifyContents[justifyContent]}</Text>
            </View>
            <View style={styles.buttonView}>
              <Button
                title="Change Align Items"
                onPress={() =>
                  changeSetting(alignItems, alignItemsArr, setAlignItems)
                }
              />
              <Text style={styles.text}>{alignItemsArr[alignItems]}</Text>
            </View>
            <View style={styles.buttonView}>
              <Button
                title="Change Direction"
                onPress={() =>
                  changeSetting(direction, directions, setDirection)
                }
              />
              <Text style={styles.text}>{directions[direction]}</Text>
            </View>
            <View style={styles.buttonView}>
              <Button
                title="Change Flex Wrap"
                onPress={() => changeSetting(wrap, wraps, setWrap)}
              />
              <Text style={styles.text}>{wraps[wrap]}</Text>
            </View>
            <View style={styles.buttonView}>
              <Button
                title="Add Square"
                onPress={() => setSquares([...squares, <Square />])}
              />
            </View>
            <View style={styles.buttonView}>
              <Button
                title="Delete Square"
                onPress={() =>
                  setSquares(squares.filter((v, i) => i !== squares.length - 1))
                }
              />
            </View>
          </View>
        </ScrollView>
      </SafeAreaView>
    </SafeAreaProvider>
  );
};

const flexDirections = ['row', 'row-reverse', 'column', 'column-reverse'];
const justifyContents = [
  'flex-start',
  'flex-end',
  'center',
  'space-between',
  'space-around',
  'space-evenly',
];
const alignItemsArr = [
  'flex-start',
  'flex-end',
  'center',
  'stretch',
  'baseline',
];
const wraps = ['nowrap', 'wrap', 'wrap-reverse'];
const directions = ['inherit', 'ltr', 'rtl'];

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  layoutContainer: {
    flex: 0.5,
  },
  playingSpace: {
    backgroundColor: 'white',
    borderColor: 'blue',
    borderWidth: 3,
    overflow: 'hidden',
  },
  controlSpace: {
    flexDirection: 'row',
    flexWrap: 'wrap',
  },
  buttonView: {
    width: '50%',
    padding: 10,
  },
  text: {
    textAlign: 'center',
  },
});

const Square = () => (
  <View
    style={{
      width: 50,
      height: 50,
      backgroundColor: randomHexColor(),
    }}
  />
);

const randomHexColor = () => {
  return '#000000'.replace(/0/g, () => {
    return Math.round(Math.random() * 14).toString(16);
  });
};

export default App;
```

</TabItem>
<TabItem value="typescript">

```SnackPlayer name=LayoutProps%20Example&ext=tsx
import {useState} from 'react';
import {
  Button,
  ScrollView,
  StyleSheet,
  Text,
  View,
  ViewStyle,
} from 'react-native';
import {SafeAreaView, SafeAreaProvider} from 'react-native-safe-area-context';

const App = () => {
  const [flexDirection, setFlexDirection] = useState(0);
  const [justifyContent, setJustifyContent] = useState(0);
  const [alignItems, setAlignItems] = useState(0);
  const [direction, setDirection] = useState(0);
  const [wrap, setWrap] = useState(0);

  const [squares, setSquares] = useState([<Square />, <Square />, <Square />]);

  const hookedStyles = {
    flexDirection: flexDirections[flexDirection],
    justifyContent: justifyContents[justifyContent],
    alignItems: alignItemsArr[alignItems],
    direction: directions[direction],
    flexWrap: wraps[wrap],
  };

  const changeSetting = (
    value: number,
    options: any[],
    setterFunction: (index: number) => void,
  ) => {
    if (value === options.length - 1) {
      setterFunction(0);
      return;
    }
    setterFunction(value + 1);
  };

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.container}>
        <View style={[styles.container, styles.playingSpace, hookedStyles]}>
          {squares.map(elem => elem)}
        </View>
        <ScrollView style={styles.layoutContainer}>
          <View style={styles.controlSpace}>
            <View style={styles.buttonView}>
              <Button
                title="Change Flex Direction"
                onPress={() =>
                  changeSetting(flexDirection, flexDirections, setFlexDirection)
                }
              />
              <Text style={styles.text}>{flexDirections[flexDirection]}</Text>
            </View>
            <View style={styles.buttonView}>
              <Button
                title="Change Justify Content"
                onPress={() =>
                  changeSetting(
                    justifyContent,
                    justifyContents,
                    setJustifyContent,
                  )
                }
              />
              <Text style={styles.text}>{justifyContents[justifyContent]}</Text>
            </View>
            <View style={styles.buttonView}>
              <Button
                title="Change Align Items"
                onPress={() =>
                  changeSetting(alignItems, alignItemsArr, setAlignItems)
                }
              />
              <Text style={styles.text}>{alignItemsArr[alignItems]}</Text>
            </View>
            <View style={styles.buttonView}>
              <Button
                title="Change Direction"
                onPress={() =>
                  changeSetting(direction, directions, setDirection)
                }
              />
              <Text style={styles.text}>{directions[direction]}</Text>
            </View>
            <View style={styles.buttonView}>
              <Button
                title="Change Flex Wrap"
                onPress={() => changeSetting(wrap, wraps, setWrap)}
              />
              <Text style={styles.text}>{wraps[wrap]}</Text>
            </View>
            <View style={styles.buttonView}>
              <Button
                title="Add Square"
                onPress={() => setSquares([...squares, <Square />])}
              />
            </View>
            <View style={styles.buttonView}>
              <Button
                title="Delete Square"
                onPress={() =>
                  setSquares(squares.filter((v, i) => i !== squares.length - 1))
                }
              />
            </View>
          </View>
        </ScrollView>
      </SafeAreaView>
    </SafeAreaProvider>
  );
};

const flexDirections: ViewStyle['flexDirection'][] = [
  'row',
  'row-reverse',
  'column',
  'column-reverse',
];
const justifyContents: ViewStyle['justifyContent'][] = [
  'flex-start',
  'flex-end',
  'center',
  'space-between',
  'space-around',
  'space-evenly',
];
const alignItemsArr: ViewStyle['alignItems'][] = [
  'flex-start',
  'flex-end',
  'center',
  'stretch',
  'baseline',
];
const wraps: ViewStyle['flexWrap'][] = ['nowrap', 'wrap', 'wrap-reverse'];
const directions: ViewStyle['direction'][] = ['inherit', 'ltr', 'rtl'];

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  layoutContainer: {
    flex: 0.5,
  },
  playingSpace: {
    backgroundColor: 'white',
    borderColor: 'blue',
    borderWidth: 3,
    overflow: 'hidden',
  },
  controlSpace: {
    flexDirection: 'row',
    flexWrap: 'wrap',
  },
  buttonView: {
    width: '50%',
    padding: 10,
  },
  text: {
    textAlign: 'center',
  },
});

const Square = () => (
  <View
    style={{
      width: 50,
      height: 50,
      backgroundColor: randomHexColor(),
    }}
  />
);

const randomHexColor = () => {
  return '#000000'.replace(/0/g, () => {
    return Math.round(Math.random() * 14).toString(16);
  });
};

export default App;
```

</TabItem>
</Tabs>

---

# Referência

## Props

### `alignContent`

<<<<<<< pt
`alignContent` controla como as linhas se alinham na direção transversal, substituindo o `alignContent` do pai. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/align-content para mais detalhes.
||||||| base_en
`alignContent` controls how rows align in the cross direction, overriding the `alignContent` of the parent. See https://developer.mozilla.org/en-US/docs/Web/CSS/align-content for more details.
=======
`alignContent` controls how rows align in the cross direction, overriding the `alignContent` of the parent.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/align-content) for more details.
>>>>>>> new_en

| Tipo                                                                                                 | Obrigatório |
| ---------------------------------------------------------------------------------------------------- | -------- |
| enum('flex-start', 'flex-end', 'center', 'stretch', 'space-between', 'space-around', 'space-evenly') | Não       |

---

### `alignItems`

<<<<<<< pt
`alignItems` alinha os filhos na direção transversal. Por exemplo, se os filhos estão fluindo verticalmente, `alignItems` controla como eles se alinham horizontalmente. Funciona como `align-items` no CSS (padrão: stretch). Veja https://developer.mozilla.org/en-US/docs/Web/CSS/align-items para mais detalhes.
||||||| base_en
`alignItems` aligns children in the cross direction. For example, if children are flowing vertically, `alignItems` controls how they align horizontally. It works like `align-items` in CSS (default: stretch). See https://developer.mozilla.org/en-US/docs/Web/CSS/align-items for more details.
=======
`alignItems` aligns children in the cross direction. For example, if children are flowing vertically, `alignItems` controls how they align horizontally. It works like `align-items` in CSS (default: stretch).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items) for more details.
>>>>>>> new_en

| Tipo                                                            | Obrigatório |
| --------------------------------------------------------------- | -------- |
| enum('flex-start', 'flex-end', 'center', 'stretch', 'baseline') | Não       |

---

### `alignSelf`

<<<<<<< pt
`alignSelf` controla como um filho se alinha na direção transversal, substituindo o `alignItems` do pai. Funciona como `align-self` no CSS (padrão: auto). Veja https://developer.mozilla.org/en-US/docs/Web/CSS/align-self para mais detalhes.
||||||| base_en
`alignSelf` controls how a child aligns in the cross direction, overriding the `alignItems` of the parent. It works like `align-self` in CSS (default: auto). See https://developer.mozilla.org/en-US/docs/Web/CSS/align-self for more details.
=======
`alignSelf` controls how a child aligns in the cross direction, overriding the `alignItems` of the parent. It works like `align-self` in CSS (default: auto).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/align-self) for more details.
>>>>>>> new_en

| Tipo                                                                    | Obrigatório |
| ----------------------------------------------------------------------- | -------- |
| enum('auto', 'flex-start', 'flex-end', 'center', 'stretch', 'baseline') | Não       |

---

### `aspectRatio`

<<<<<<< pt
Aspect ratio controla o tamanho da dimensão indefinida de um nó. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/aspect-ratio para mais detalhes.
||||||| base_en
Aspect ratio controls the size of the undefined dimension of a node. See https://developer.mozilla.org/en-US/docs/Web/CSS/aspect-ratio for more details.
=======
Aspect ratio controls the size of the undefined dimension of a node.
>>>>>>> new_en

- Em um nó com width/height definida, aspect ratio controla o tamanho da dimensão não definida
- Em um nó com flex basis definida, aspect ratio controla o tamanho do nó no eixo transversal se não estiver definido
- Em um nó com uma função de medida, aspect ratio funciona como se a função de medida medisse o flex basis
- Em um nó com flex grow/shrink, aspect ratio controla o tamanho do nó no eixo transversal se não estiver definido
- Aspect ratio leva em conta as dimensões min/max

<<<<<<< pt
| Tipo           | Obrigatório |
||||||| base_en
| Type           | Required |
=======
See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/aspect-ratio) for more details.

| Type           | Required |
>>>>>>> new_en
| -------------- | -------- |
| number, string | Não       |

---

### `borderBottomWidth`

<<<<<<< pt
`borderBottomWidth` funciona como `border-bottom-width` no CSS. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/border-bottom-width para mais detalhes.
||||||| base_en
`borderBottomWidth` works like `border-bottom-width` in CSS. See https://developer.mozilla.org/en-US/docs/Web/CSS/border-bottom-width for more details.
=======
`borderBottomWidth` works like `border-bottom-width` in CSS.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/border-bottom-width) for more details.
>>>>>>> new_en

| Tipo   | Obrigatório |
| ------ | -------- |
| number | Não       |

---

### `borderEndWidth`

Quando direction é `ltr`, `borderEndWidth` é equivalente a `borderRightWidth`. Quando direction é `rtl`, `borderEndWidth` é equivalente a `borderLeftWidth`.

| Tipo   | Obrigatório |
| ------ | -------- |
| number | Não       |

---

### `borderLeftWidth`

<<<<<<< pt
`borderLeftWidth` funciona como `border-left-width` no CSS. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/border-left-width para mais detalhes.
||||||| base_en
`borderLeftWidth` works like `border-left-width` in CSS. See https://developer.mozilla.org/en-US/docs/Web/CSS/border-left-width for more details.
=======
`borderLeftWidth` works like `border-left-width` in CSS.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/border-left-width) for more details.
>>>>>>> new_en

| Tipo   | Obrigatório |
| ------ | -------- |
| number | Não       |

---

### `borderRightWidth`

<<<<<<< pt
`borderRightWidth` funciona como `border-right-width` no CSS. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/border-right-width para mais detalhes.
||||||| base_en
`borderRightWidth` works like `border-right-width` in CSS. See https://developer.mozilla.org/en-US/docs/Web/CSS/border-right-width for more details.
=======
`borderRightWidth` works like `border-right-width` in CSS.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/border-right-width) for more details.
>>>>>>> new_en

| Tipo   | Obrigatório |
| ------ | -------- |
| number | Não       |

---

### `borderStartWidth`

Quando direction é `ltr`, `borderStartWidth` é equivalente a `borderLeftWidth`. Quando direction é `rtl`, `borderStartWidth` é equivalente a `borderRightWidth`.

| Tipo   | Obrigatório |
| ------ | -------- |
| number | Não       |

---

### `borderTopWidth`

<<<<<<< pt
`borderTopWidth` funciona como `border-top-width` no CSS. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/border-top-width para mais detalhes.
||||||| base_en
`borderTopWidth` works like `border-top-width` in CSS. See https://developer.mozilla.org/en-US/docs/Web/CSS/border-top-width for more details.
=======
`borderTopWidth` works like `border-top-width` in CSS.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/border-top-width) for more details.
>>>>>>> new_en

| Tipo   | Obrigatório |
| ------ | -------- |
| number | Não       |

---

### `borderWidth`

<<<<<<< pt
`borderWidth` funciona como `border-width` no CSS. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/border-width para mais detalhes.
||||||| base_en
`borderWidth` works like `border-width` in CSS. See https://developer.mozilla.org/en-US/docs/Web/CSS/border-width for more details.
=======
`borderWidth` works like `border-width` in CSS.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/border-width) for more details.
>>>>>>> new_en

| Tipo   | Obrigatório |
| ------ | -------- |
| number | Não       |

---

### `bottom`

`bottom` é o número de pixels lógicos para deslocar a borda inferior deste componente.

Funciona de forma similar a `bottom` no CSS, mas no React Native você deve usar pontos ou porcentagens. Ems e outras unidades não são suportadas.

<<<<<<< pt
Veja https://developer.mozilla.org/en-US/docs/Web/CSS/bottom para mais detalhes sobre como `bottom` afeta o layout.
||||||| base_en
See https://developer.mozilla.org/en-US/docs/Web/CSS/bottom for more details of how `bottom` affects layout.
=======
See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/bottom) for more details of how `bottom` affects layout.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `boxSizing`

`boxSizing` define como as várias props de dimensionamento do elemento (`width`, `height`, `minWidth`, `minHeight`, etc.) são calculadas. Se `boxSizing` for `border-box`, esses tamanhos se aplicam à border box do elemento. Se for `content-box`, eles se aplicam à content box do elemento. O valor padrão é `border-box`. A [documentação web](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing) é uma boa fonte de informação se você deseja aprender mais sobre como essa prop funciona.

| Tipo                              | Obrigatório |
| --------------------------------- | -------- |
| enum('border-box', 'content-box') | Não       |

---

### `columnGap`

<<<<<<< pt
`columnGap` funciona como `column-gap` no CSS. Apenas unidades de pixel são suportadas no React Native. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/column-gap para mais detalhes.
||||||| base_en
`columnGap` works like `column-gap` in CSS. Only pixel units are supported in React Native. See https://developer.mozilla.org/en-US/docs/Web/CSS/column-gap for more details.
=======
`columnGap` works like `column-gap` in CSS. It accepts numbers (in points) or percentage strings (e.g. `'10%'`). Percentage values are supported on the [New Architecture](/architecture/landing-page).
>>>>>>> new_en

<<<<<<< pt
| Tipo   | Obrigatório |
| ------ | -------- |
| number | Não       |
||||||| base_en
| Type   | Required |
| ------ | -------- |
| number | No       |
=======
See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/column-gap) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |
>>>>>>> new_en

---

### `direction`

<<<<<<< pt
`direction` especifica o fluxo direcional da interface do usuário. O padrão é `inherit`, exceto para o nó raiz que terá valor baseado no locale atual. Veja https://www.yogalayout.dev/docs/styling/layout-direction para mais detalhes.
||||||| base_en
`direction` specifies the directional flow of the user interface. The default is `inherit`, except for root node which will have value based on the current locale. See https://www.yogalayout.dev/docs/styling/layout-direction for more details.
=======
`direction` specifies the directional flow of the user interface. The default is `inherit`, except for root node which will have value based on the current locale.
>>>>>>> new_en

<<<<<<< pt
| Tipo                          | Obrigatório | Plataforma |
| ----------------------------- | -------- | -------- |
| enum('inherit', 'ltr', 'rtl') | Não       | iOS      |
||||||| base_en
| Type                          | Required | Platform |
| ----------------------------- | -------- | -------- |
| enum('inherit', 'ltr', 'rtl') | No       | iOS      |
=======
See [MDN CSS Reference](https://www.yogalayout.dev/docs/styling/layout-direction) for more details.

| Type                          | Required |
| ----------------------------- | -------- |
| enum('inherit', 'ltr', 'rtl') | No       |
>>>>>>> new_en

---

### `display`

`display` define o tipo de exibição deste componente.

Funciona de forma similar a `display` no CSS, mas suporta apenas os valores 'flex', 'none' e 'contents'. O padrão é `flex`.

| Tipo                             | Obrigatório |
| -------------------------------- | -------- |
| enum('none', 'flex', 'contents') | Não       |

---

### `end`

Quando direction é `ltr`, `end` é equivalente a `right`. Quando direction é `rtl`, `end` é equivalente a `left`.

Este estilo tem precedência sobre os estilos `left` e `right`.

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `flex`

No React Native, `flex` não funciona da mesma forma que funciona no CSS. `flex` é um número ao invés de uma string, e funciona de acordo com o layout engine [Yoga](https://github.com/facebook/yoga).

<<<<<<< pt
Quando `flex` é um número positivo, ele torna o componente flexível, e ele será dimensionado proporcionalmente ao seu valor flex. Assim, um componente com `flex` definido como 2 ocupará o dobro do espaço de um componente com `flex` definido como 1. `flex: <positive number>` equivale a `flexGrow: <positive number>, flexShrink: 1, flexBasis: 0`.
||||||| base_en
When `flex` is a positive number, it makes the component flexible, and it will be sized proportional to its flex value. So a component with `flex` set to 2 will take twice the space as a component with `flex` set to 1. `flex: <positive number>` equates to `flexGrow: <positive number>, flexShrink: 1, flexBasis: 0`.
=======
When `flex` is a positive number, it makes the component flexible, and it will be sized proportional to its flex value. So a component with `flex` set to `2` will take twice the space as a component with `flex` set to 1. `flex: <positive number>` equates to `flexGrow: <positive number>, flexShrink: 1, flexBasis: 0`.
>>>>>>> new_en

<<<<<<< pt
Quando `flex` é 0, o componente é dimensionado de acordo com `width` e `height`, e é inflexível.
||||||| base_en
When `flex` is 0, the component is sized according to `width` and `height`, and it is inflexible.
=======
When `flex` is `0`, the component is sized according to `width` and `height`, and it is inflexible.
>>>>>>> new_en

<<<<<<< pt
Quando `flex` é -1, o componente normalmente é dimensionado de acordo com `width` e `height`. No entanto, se não houver espaço suficiente, o componente encolherá para seu `minWidth` e `minHeight`.
||||||| base_en
When `flex` is -1, the component is normally sized according to `width` and `height`. However, if there's not enough space, the component will shrink to its `minWidth` and `minHeight`.
=======
When `flex` is `-1`, the component is normally sized according to `width` and `height`. However, if there's not enough space, the component will shrink to its `minWidth` and `minHeight`.
>>>>>>> new_en

`flexGrow`, `flexShrink` e `flexBasis` funcionam da mesma forma que no CSS.

| Tipo   | Obrigatório |
| ------ | -------- |
| number | Não       |

---

### `flexBasis`

`flexBasis` é uma forma independente de eixo de fornecer o tamanho padrão de um item ao longo do eixo principal. Definir o `flexBasis` de um filho é similar a definir o `width` desse filho se seu pai é um container com `flexDirection: row` ou definir o `height` de um filho se seu pai é um container com `flexDirection: column`. O `flexBasis` de um item é o tamanho padrão desse item, o tamanho do item antes que quaisquer cálculos de `flexGrow` e `flexShrink` sejam realizados.

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `flexDirection`

<<<<<<< pt
`flexDirection` controla em quais direções os filhos de um container vão. `row` vai da esquerda para a direita, `column` vai de cima para baixo, e você pode conseguir adivinhar o que os outros dois fazem. Funciona como `flex-direction` no CSS, exceto que o padrão é `column`. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction para mais detalhes.
||||||| base_en
`flexDirection` controls which directions children of a container go. `row` goes left to right, `column` goes top to bottom, and you may be able to guess what the other two do. It works like `flex-direction` in CSS, except the default is `column`. See https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction for more details.
=======
`flexDirection` controls which directions children of a container go. `row` goes left to right, `column` goes top to bottom, and you may be able to guess what the other two do. It works like `flex-direction` in CSS, except the default is `column`.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction) for more details.
>>>>>>> new_en

| Tipo                                                   | Obrigatório |
| ------------------------------------------------------ | -------- |
| enum('row', 'row-reverse', 'column', 'column-reverse') | Não       |

---

### `flexGrow`

`flexGrow` descreve como qualquer espaço dentro de um container deve ser distribuído entre seus filhos ao longo do eixo principal. Depois de posicionar seus filhos, um container distribuirá qualquer espaço restante de acordo com os valores de flex grow especificados por seus filhos.

`flexGrow` aceita qualquer valor de ponto flutuante >= 0, sendo 0 o valor padrão. Um container distribuirá qualquer espaço restante entre seus filhos ponderado pelos valores de `flexGrow` dos filhos.

| Tipo   | Obrigatório |
| ------ | -------- |
| number | Não       |

---

### `flexShrink`

[`flexShrink`](layout-props#flexshrink) descreve como encolher filhos ao longo do eixo principal no caso em que o tamanho total dos filhos excede o tamanho do container no eixo principal. `flexShrink` é muito similar a `flexGrow` e pode ser pensado da mesma forma se qualquer tamanho excedente for considerado espaço restante negativo. Essas duas propriedades também funcionam bem juntas, permitindo que os filhos cresçam e encolham conforme necessário.

`flexShrink` aceita qualquer valor de ponto flutuante >= 0, sendo 0 o valor padrão. Um container encolherá seus filhos ponderado pelos valores de `flexShrink` dos filhos.

| Tipo   | Obrigatório |
| ------ | -------- |
| number | Não       |

---

### `flexWrap`

<<<<<<< pt
`flexWrap` controla se os filhos podem envolver depois de atingir o fim de um flex container. Funciona como `flex-wrap` no CSS (padrão: nowrap). Veja https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap para mais detalhes. Note que não funciona mais com `alignItems: stretch` (o padrão), então você pode querer usar `alignItems: flex-start` por exemplo (detalhes da mudança: https://github.com/facebook/react-native/releases/tag/v0.28.0).
||||||| base_en
`flexWrap` controls whether children can wrap around after they hit the end of a flex container. It works like `flex-wrap` in CSS (default: nowrap). See https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap for more details. Note it does not work anymore with `alignItems: stretch` (the default), so you may want to use `alignItems: flex-start` for example (breaking change details: https://github.com/facebook/react-native/releases/tag/v0.28.0).
=======
`flexWrap` controls whether children can wrap around after they hit the end of a flex container. It works like `flex-wrap` in CSS (default: nowrap).

Note it does not work anymore with `alignItems: stretch` (the default), so you may want to use `alignItems: flex-start` for example (breaking change details: https://github.com/react/react-native/releases/tag/v0.28.0).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap) for more details.
>>>>>>> new_en

| Tipo                                   | Obrigatório |
| -------------------------------------- | -------- |
| enum('wrap', 'nowrap', 'wrap-reverse') | Não       |

---

### `gap`

<<<<<<< pt
`gap` funciona como `gap` no CSS. Apenas unidades de pixel são suportadas no React Native. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/gap para mais detalhes.
||||||| base_en
`gap` works like `gap` in CSS. Only pixel units are supported in React Native. See https://developer.mozilla.org/en-US/docs/Web/CSS/gap for more details.
=======
`gap` works like `gap` in CSS. It is a shorthand for `rowGap` and `columnGap`. It accepts numbers (in points) or percentage strings (e.g. `'10%'`). Percentage values are supported on the [New Architecture](/architecture/landing-page).
>>>>>>> new_en

<<<<<<< pt
| Tipo   | Obrigatório |
| ------ | -------- |
| number | Não       |
||||||| base_en
| Type   | Required |
| ------ | -------- |
| number | No       |
=======
See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/gap) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |
>>>>>>> new_en

---

### `height`

`height` define a altura deste componente.

<<<<<<< pt
Funciona de forma similar a `height` no CSS, mas no React Native você deve usar pontos ou porcentagens. Ems e outras unidades não são suportadas. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/height para mais detalhes.
||||||| base_en
It works similarly to `height` in CSS, but in React Native you must use points or percentages. Ems and other units are not supported. See https://developer.mozilla.org/en-US/docs/Web/CSS/height for more details.
=======
It works similarly to `height` in CSS, but in React Native you must use points or percentages. Ems and other units are not supported.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/height) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `inset`

:::note
`inset` is only available on the [New Architecture](/architecture/landing-page)
:::

Setting `inset` has the same effect as setting each of `top`, `bottom`, `right` and `left` props.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `insetBlock`

:::note
`insetBlock` is only available on the [New Architecture](/architecture/landing-page)
:::

Equivalent to [`top`](layout-props#top) and [`bottom`](layout-props#bottom).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/inset-block) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `insetBlockEnd`

:::note
`insetBlockEnd` is only available on the [New Architecture](/architecture/landing-page)
:::

Equivalent to [`bottom`](layout-props#bottom).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/inset-block-end) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `insetBlockStart`

:::note
`insetBlockStart` is only available on the [New Architecture](/architecture/landing-page)
:::

Equivalent to [`top`](layout-props#top).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/inset-block-start) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `insetInline`

:::note
`insetInline` is only available on the [New Architecture](/architecture/landing-page)
:::

Equivalent to [`right`](layout-props#right) and [`left`](layout-props#left).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/inset-inline) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `insetInlineEnd`

:::note
`insetInlineEnd` is only available on the [New Architecture](/architecture/landing-page)
:::

When direction is `ltr`, `insetInlineEnd` is equivalent to [`right`](layout-props#right). When direction is `rtl`, `insetInlineEnd` is equivalent to [`left`](layout-props#left).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/inset-inline-end) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `insetInlineStart`

:::note
`insetInlineStart` is only available on the [New Architecture](/architecture/landing-page)
:::

When direction is `ltr`, `insetInlineStart` is equivalent to [`left`](layout-props#left). When direction is `rtl`, `insetInlineStart` is equivalent to [`right`](layout-props#right).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/inset-inline-start) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `isolation`

<<<<<<< pt
`isolation` permite formar um [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Stacking_context). Esta prop está disponível apenas na [Nova Arquitetura](/architecture/landing-page).
||||||| base_en
`isolation` lets you form a [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Stacking_context). This prop is only available on the [New Architecture](/architecture/landing-page).
=======
:::note
`isolation` is only available on the [New Architecture](/architecture/landing-page)
:::

`isolation` lets you form a [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Stacking_context).
>>>>>>> new_en

Existem dois valores:

- `auto` (padrão): Não faz nada.
- `isolate`: Forma um stacking context.

| Tipo                    | Obrigatório |
| ----------------------- | -------- |
| enum('auto', 'isolate') | Não       |

---

### `justifyContent`

<<<<<<< pt
`justifyContent` alinha os filhos na direção principal. Por exemplo, se os filhos estão fluindo verticalmente, `justifyContent` controla como eles se alinham verticalmente. Funciona como `justify-content` no CSS (padrão: flex-start). Veja https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content para mais detalhes.
||||||| base_en
`justifyContent` aligns children in the main direction. For example, if children are flowing vertically, `justifyContent` controls how they align vertically. It works like `justify-content` in CSS (default: flex-start). See https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content for more details.
=======
`justifyContent` aligns children in the main direction. For example, if children are flowing vertically, `justifyContent` controls how they align vertically. It works like `justify-content` in CSS (default: flex-start).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content) for more details.
>>>>>>> new_en

| Tipo                                                                                      | Obrigatório |
| ----------------------------------------------------------------------------------------- | -------- |
| enum('flex-start', 'flex-end', 'center', 'space-between', 'space-around', 'space-evenly') | Não       |

---

### `left`

`left` é o número de pixels lógicos para deslocar a borda esquerda deste componente.

Funciona de forma similar a `left` no CSS, mas no React Native você deve usar pontos ou porcentagens. Ems e outras unidades não são suportadas.

<<<<<<< pt
Veja https://developer.mozilla.org/en-US/docs/Web/CSS/left para mais detalhes sobre como `left` afeta o layout.
||||||| base_en
See https://developer.mozilla.org/en-US/docs/Web/CSS/left for more details of how `left` affects layout.
=======
See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/left) for more details of how `left` affects layout.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `margin`

<<<<<<< pt
Definir `margin` tem o mesmo efeito que definir cada um de `marginTop`, `marginLeft`, `marginBottom` e `marginRight`. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/margin para mais detalhes.
||||||| base_en
Setting `margin` has the same effect as setting each of `marginTop`, `marginLeft`, `marginBottom`, and `marginRight`. See https://developer.mozilla.org/en-US/docs/Web/CSS/margin for more details.
=======
Setting `margin` has the same effect as setting each of `marginTop`, `marginLeft`, `marginBottom`, and `marginRight`.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/margin) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `marginBottom`

<<<<<<< pt
`marginBottom` funciona como `margin-bottom` no CSS. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/margin-bottom para mais detalhes.
||||||| base_en
`marginBottom` works like `margin-bottom` in CSS. See https://developer.mozilla.org/en-US/docs/Web/CSS/margin-bottom for more details.
=======
`marginBottom` works like `margin-bottom` in CSS. See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-bottom) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `marginBlock`

Equivalent to [`marginVertical`](layout-props#marginvertical).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `marginBlockEnd`

Equivalent to [`marginBottom`](layout-props#marginbottom).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-end) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `marginBlockStart`

Equivalent to [`marginTop`](layout-props#margintop).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-start) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `marginEnd`

Quando direction é `ltr`, `marginEnd` é equivalente a `marginRight`. Quando direction é `rtl`, `marginEnd` é equivalente a `marginLeft`.

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `marginHorizontal`

Definir `marginHorizontal` tem o mesmo efeito que definir ambos `marginLeft` e `marginRight`.

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `marginInline`

Equivalent to [`marginHorizontal`](layout-props#marginhorizontal).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `marginInlineEnd`

When direction is `ltr`, `marginInlineEnd` is equivalent to [`marginEnd`](layout-props#marginend) (i.e. `marginRight`). When direction is `rtl`, `marginInlineEnd` is equivalent to [`marginEnd`](layout-props#marginend) (i.e. `marginLeft`).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `marginInlineStart`

When direction is `ltr`, `marginInlineStart` is equivalent to [`marginStart`](layout-props#marginstart) (i.e. `marginLeft`). When direction is `rtl`, `marginInlineStart` is equivalent to [`marginStart`](layout-props#marginstart) (i.e. `marginRight`).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `marginLeft`

<<<<<<< pt
`marginLeft` funciona como `margin-left` no CSS. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/margin-left para mais detalhes.
||||||| base_en
`marginLeft` works like `margin-left` in CSS. See https://developer.mozilla.org/en-US/docs/Web/CSS/margin-left for more details.
=======
`marginLeft` works like `margin-left` in CSS. See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-left) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `marginRight`

<<<<<<< pt
`marginRight` funciona como `margin-right` no CSS. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/margin-right para mais detalhes.
||||||| base_en
`marginRight` works like `margin-right` in CSS. See https://developer.mozilla.org/en-US/docs/Web/CSS/margin-right for more details.
=======
`marginRight` works like `margin-right` in CSS.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-right) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `marginStart`

Quando direction é `ltr`, `marginStart` é equivalente a `marginLeft`. Quando direction é `rtl`, `marginStart` é equivalente a `marginRight`.

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `marginTop`

<<<<<<< pt
`marginTop` funciona como `margin-top` no CSS. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/margin-top para mais detalhes.
||||||| base_en
`marginTop` works like `margin-top` in CSS. See https://developer.mozilla.org/en-US/docs/Web/CSS/margin-top for more details.
=======
`marginTop` works like `margin-top` in CSS.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-top) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `marginVertical`

Definir `marginVertical` tem o mesmo efeito que definir ambos `marginTop` e `marginBottom`.

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `maxHeight`

`maxHeight` é a altura máxima para este componente, em pixels lógicos.

Funciona de forma similar a `max-height` no CSS, mas no React Native você deve usar pontos ou porcentagens. Ems e outras unidades não são suportadas.

<<<<<<< pt
Veja https://developer.mozilla.org/en-US/docs/Web/CSS/max-height para mais detalhes.
||||||| base_en
See https://developer.mozilla.org/en-US/docs/Web/CSS/max-height for more details.
=======
See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/max-height) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `maxWidth`

`maxWidth` é a largura máxima para este componente, em pixels lógicos.

Funciona de forma similar a `max-width` no CSS, mas no React Native você deve usar pontos ou porcentagens. Ems e outras unidades não são suportadas.

<<<<<<< pt
Veja https://developer.mozilla.org/en-US/docs/Web/CSS/max-width para mais detalhes.
||||||| base_en
See https://developer.mozilla.org/en-US/docs/Web/CSS/max-width for more details.
=======
See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/max-width) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `minHeight`

`minHeight` é a altura mínima para este componente, em pixels lógicos.

Funciona de forma similar a `min-height` no CSS, mas no React Native você deve usar pontos ou porcentagens. Ems e outras unidades não são suportadas.

<<<<<<< pt
Veja https://developer.mozilla.org/en-US/docs/Web/CSS/min-height para mais detalhes.
||||||| base_en
See https://developer.mozilla.org/en-US/docs/Web/CSS/min-height for more details.
=======
See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/min-height) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `minWidth`

`minWidth` é a largura mínima para este componente, em pixels lógicos.

Funciona de forma similar a `min-width` no CSS, mas no React Native você deve usar pontos ou porcentagens. Ems e outras unidades não são suportadas.

<<<<<<< pt
Veja https://developer.mozilla.org/en-US/docs/Web/CSS/min-width para mais detalhes.
||||||| base_en
See https://developer.mozilla.org/en-US/docs/Web/CSS/min-width for more details.
=======
See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/min-width) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `overflow`

<<<<<<< pt
`overflow` controla como os filhos são medidos e exibidos. `overflow: hidden` faz com que as views sejam cortadas enquanto `overflow: scroll` faz com que as views sejam medidas independentemente do eixo principal de seus pais. Funciona como `overflow` no CSS (padrão: visible). Veja https://developer.mozilla.org/en/docs/Web/CSS/overflow para mais detalhes.
||||||| base_en
`overflow` controls how children are measured and displayed. `overflow: hidden` causes views to be clipped while `overflow: scroll` causes views to be measured independently of their parents' main axis. It works like `overflow` in CSS (default: visible). See https://developer.mozilla.org/en/docs/Web/CSS/overflow for more details.
=======
`overflow` controls how children are measured and displayed. `overflow: hidden` causes views to be clipped while `overflow: scroll` causes views to be measured independently of their parents' main axis. It works like `overflow` in CSS (default: visible).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/overflow) for more details.
>>>>>>> new_en

| Tipo                                | Obrigatório |
| ----------------------------------- | -------- |
| enum('visible', 'hidden', 'scroll') | Não       |

---

### `padding`

<<<<<<< pt
Definir `padding` tem o mesmo efeito que definir cada um de `paddingTop`, `paddingBottom`, `paddingLeft` e `paddingRight`. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/padding para mais detalhes.
||||||| base_en
Setting `padding` has the same effect as setting each of `paddingTop`, `paddingBottom`, `paddingLeft`, and `paddingRight`. See https://developer.mozilla.org/en-US/docs/Web/CSS/padding for more details.
=======
Setting `padding` has the same effect as setting each of `paddingTop`, `paddingBottom`, `paddingLeft`, and `paddingRight`.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/padding) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `paddingBottom`

<<<<<<< pt
`paddingBottom` funciona como `padding-bottom` no CSS. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/padding-bottom para mais detalhes.
||||||| base_en
`paddingBottom` works like `padding-bottom` in CSS. See https://developer.mozilla.org/en-US/docs/Web/CSS/padding-bottom for more details.
=======
`paddingBottom` works like `padding-bottom` in CSS.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/padding-bottom) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `paddingBlock`

Equivalent to [`paddingVertical`](layout-props#paddingvertical).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `paddingBlockEnd`

Equivalent to [`paddingBottom`](layout-props#paddingbottom).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block-end) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `paddingBlockStart`

Equivalent to [`paddingTop`](layout-props#paddingtop).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block-start) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `paddingEnd`

Quando direction é `ltr`, `paddingEnd` é equivalente a `paddingRight`. Quando direction é `rtl`, `paddingEnd` é equivalente a `paddingLeft`.

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `paddingHorizontal`

Definir `paddingHorizontal` é como definir ambos `paddingLeft` e `paddingRight`.

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `paddingInline`

Equivalent to [`paddingHorizontal`](layout-props#paddinghorizontal).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `paddingInlineEnd`

When direction is `ltr`, `paddingInlineEnd` is equivalent to [`paddingEnd`](layout-props#paddingend) (i.e. `paddingRight`). When direction is `rtl`, `paddingInlineEnd` is equivalent to [`paddingEnd`](layout-props#paddingend) (i.e. `paddingLeft`).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-end) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `paddingInlineStart`

When direction is `ltr`, `paddingInlineStart` is equivalent to [`paddingStart`](layout-props#paddingstart) (i.e. `paddingLeft`). When direction is `rtl`, `paddingInlineStart` is equivalent to [`paddingStart`](layout-props#paddingstart) (i.e. `paddingRight`).

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-start) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |

---

### `paddingLeft`

<<<<<<< pt
`paddingLeft` funciona como `padding-left` no CSS. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/padding-left para mais detalhes.
||||||| base_en
`paddingLeft` works like `padding-left` in CSS. See https://developer.mozilla.org/en-US/docs/Web/CSS/padding-left for more details.
=======
`paddingLeft` works like `padding-left` in CSS.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/padding-left) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `paddingRight`

<<<<<<< pt
`paddingRight` funciona como `padding-right` no CSS. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/padding-right para mais detalhes.
||||||| base_en
`paddingRight` works like `padding-right` in CSS. See https://developer.mozilla.org/en-US/docs/Web/CSS/padding-right for more details.
=======
`paddingRight` works like `padding-right` in CSS.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/padding-right) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `paddingStart`

Quando direction é `ltr`, `paddingStart` é equivalente a `paddingLeft`. Quando direction é `rtl`, `paddingStart` é equivalente a `paddingRight`.

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `paddingTop`

<<<<<<< pt
`paddingTop` funciona como `padding-top` no CSS. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/padding-top para mais detalhes.
||||||| base_en
`paddingTop` works like `padding-top` in CSS. See https://developer.mozilla.org/en-US/docs/Web/CSS/padding-top for more details.
=======
`paddingTop` works like `padding-top` in CSS.
>>>>>>> new_en

<<<<<<< pt
| Tipo            | Obrigatório |
| --------------- | -------- |
| number, ,string | Não       |
||||||| base_en
| Type            | Required |
| --------------- | -------- |
| number, ,string | No       |
=======
See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/padding-top) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |
>>>>>>> new_en

---

### `paddingVertical`

Definir `paddingVertical` é como definir ambos `paddingTop` e `paddingBottom`.

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `position`

`position` no React Native é similar ao [CSS regular](https://developer.mozilla.org/en-US/docs/Web/CSS/position), mas tudo é definido como `relative` por padrão.

`relative` posicionará um elemento de acordo com o fluxo normal do layout. Insets (`top`, `bottom`, `left`, `right`) serão deslocados em relação a este layout.

`absolute` retira o elemento do fluxo normal do layout. Insets serão deslocados em relação ao seu [containing block](./flexbox.md#the-containing-block).

`static` posicionará um elemento de acordo com o fluxo normal do layout. Insets não terão efeito.
Elementos `static` não formam um containing block para descendentes absolutos.

Para mais informações, veja os [documentos de Layout com Flexbox](./flexbox.md#position). Além disso, [a documentação do Yoga](https://www.yogalayout.dev/docs/styling/position) tem mais detalhes sobre como `position` difere entre React Native e CSS.

| Tipo                                   | Obrigatório |
| -------------------------------------- | -------- |
| enum('absolute', 'relative', 'static') | Não       |

---

### `right`

`right` é o número de pixels lógicos para deslocar a borda direita deste componente.

Funciona de forma similar a `right` no CSS, mas no React Native você deve usar pontos ou porcentagens. Ems e outras unidades não são suportadas.

<<<<<<< pt
Veja https://developer.mozilla.org/en-US/docs/Web/CSS/right para mais detalhes sobre como `right` afeta o layout.
||||||| base_en
See https://developer.mozilla.org/en-US/docs/Web/CSS/right for more details of how `right` affects layout.
=======
See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/right) for more details of how `right` affects layout.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `rowGap`

<<<<<<< pt
`rowGap` funciona como `row-gap` no CSS. Apenas unidades de pixel são suportadas no React Native. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/row-gap para mais detalhes.
||||||| base_en
`rowGap` works like `row-gap` in CSS. Only pixel units are supported in React Native. See https://developer.mozilla.org/en-US/docs/Web/CSS/row-gap for more details.
=======
`rowGap` works like `row-gap` in CSS. It accepts numbers (in points) or percentage strings (e.g. `'10%'`). Percentage values are supported on the [New Architecture](/architecture/landing-page).
>>>>>>> new_en

<<<<<<< pt
| Tipo   | Obrigatório |
| ------ | -------- |
| number | Não       |
||||||| base_en
| Type   | Required |
| ------ | -------- |
| number | No       |
=======
See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/row-gap) for more details.

| Type           | Required |
| -------------- | -------- |
| number, string | No       |
>>>>>>> new_en

---

### `start`

Quando direction é `ltr`, `start` é equivalente a `left`. Quando direction é `rtl`, `start` é equivalente a `right`.

Este estilo tem precedência sobre os estilos `left`, `right` e `end`.

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `top`

`top` é o número de pixels lógicos para deslocar a borda superior deste componente.

Funciona de forma similar a `top` no CSS, mas no React Native você deve usar pontos ou porcentagens. Ems e outras unidades não são suportadas.

<<<<<<< pt
Veja https://developer.mozilla.org/en-US/docs/Web/CSS/top para mais detalhes sobre como `top` afeta o layout.
||||||| base_en
See https://developer.mozilla.org/en-US/docs/Web/CSS/top for more details of how `top` affects layout.
=======
See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/top) for more details of how `top` affects layout.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `width`

`width` define a largura deste componente.

<<<<<<< pt
Funciona de forma similar a `width` no CSS, mas no React Native você deve usar pontos ou porcentagens. Ems e outras unidades não são suportadas. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/width para mais detalhes.
||||||| base_en
It works similarly to `width` in CSS, but in React Native you must use points or percentages. Ems and other units are not supported. See https://developer.mozilla.org/en-US/docs/Web/CSS/width for more details.
=======
It works similarly to `width` in CSS, but in React Native you must use points or percentages. Ems and other units are not supported.

See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/width) for more details.
>>>>>>> new_en

| Tipo           | Obrigatório |
| -------------- | -------- |
| number, string | Não       |

---

### `zIndex`

`zIndex` controla quais componentes são exibidos em cima de outros. Normalmente, você não usa `zIndex`. Componentes renderizam de acordo com sua ordem na árvore do documento, então componentes posteriores são desenhados sobre os anteriores. `zIndex` pode ser útil se você tiver animações ou interfaces modais customizadas onde você não deseja esse comportamento.

<<<<<<< pt
Funciona como a propriedade CSS `z-index` - componentes com um `zIndex` maior renderizarão em cima. Pense na direção z como se estivesse apontando do telefone para seu olho. Veja https://developer.mozilla.org/en-US/docs/Web/CSS/z-index para mais detalhes.
||||||| base_en
It works like the CSS `z-index` property - components with a larger `zIndex` will render on top. Think of the z-direction like it's pointing from the phone into your eyeball. See https://developer.mozilla.org/en-US/docs/Web/CSS/z-index for more details.
=======
It works like the CSS `z-index` property - components with a larger `zIndex` will render on top. Think of the z-direction like it's pointing from the phone into your eyeball.
>>>>>>> new_en

No iOS, `zIndex` pode requerer que `View`s sejam irmãs umas das outras para funcionar como esperado.

<<<<<<< pt
| Tipo   | Obrigatório |
||||||| base_en
| Type   | Required |
=======
See [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index) for more details.

| Type   | Required |
>>>>>>> new_en
| ------ | -------- |
<<<<<<< pt
| number | Não       |

---
||||||| base_en
| number | No       |

---
=======
| number | No       |
>>>>>>> new_en
