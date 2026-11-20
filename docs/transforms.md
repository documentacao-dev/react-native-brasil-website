---
ia-translated: true
id: transforms
title: Transformações
---

Transformações são propriedades de estilo que ajudam você a modificar a aparência e a posição de seus components usando transformações 2D ou 3D. No entanto, uma vez que você aplica transformações, os layouts permanecem os mesmos ao redor do component transformado, o que pode fazer com que ele se sobreponha aos components próximos. Você pode aplicar margem ao component transformado, aos components próximos ou padding ao container para evitar tais sobreposições.

## Example

```SnackPlayer name=Transforms%20Example
import {ScrollView, StyleSheet, Text, View} from 'react-native';
import {SafeAreaView, SafeAreaProvider} from 'react-native-safe-area-context';

const App = () => (
  <SafeAreaProvider>
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContentContainer}>
        <View style={styles.box}>
          <Text style={styles.text}>Original Object</Text>
        </View>

        <View
          style={[
            styles.box,
            {
              transform: [{scale: 2}],
            },
          ]}>
          <Text style={styles.text}>Scale by 2</Text>
        </View>

        <View
          style={[
            styles.box,
            {
              transform: [{scaleX: 2}],
            },
          ]}>
          <Text style={styles.text}>ScaleX by 2</Text>
        </View>

        <View
          style={[
            styles.box,
            {
              transform: [{scaleY: 2}],
            },
          ]}>
          <Text style={styles.text}>ScaleY by 2</Text>
        </View>

        <View
          style={[
            styles.box,
            {
              transform: [{rotate: '45deg'}],
            },
          ]}>
          <Text style={styles.text}>Rotate by 45 deg</Text>
        </View>

        <View
          style={[
            styles.box,
            {
              transform: [{rotateX: '45deg'}, {rotateZ: '45deg'}],
            },
          ]}>
          <Text style={styles.text}>Rotate X&Z by 45 deg</Text>
        </View>

        <View
          style={[
            styles.box,
            {
              transform: [{rotateY: '45deg'}, {rotateZ: '45deg'}],
            },
          ]}>
          <Text style={styles.text}>Rotate Y&Z by 45 deg</Text>
        </View>

        <View
          style={[
            styles.box,
            {
              transform: [{skewX: '45deg'}],
            },
          ]}>
          <Text style={styles.text}>SkewX by 45 deg</Text>
        </View>

        <View
          style={[
            styles.box,
            {
              transform: [{skewY: '45deg'}],
            },
          ]}>
          <Text style={styles.text}>SkewY by 45 deg</Text>
        </View>

        <View
          style={[
            styles.box,
            {
              transform: [{skewX: '30deg'}, {skewY: '30deg'}],
            },
          ]}>
          <Text style={styles.text}>Skew X&Y by 30 deg</Text>
        </View>

        <View
          style={[
            styles.box,
            {
              transform: [{translateX: -50}],
            },
          ]}>
          <Text style={styles.text}>TranslateX by -50 </Text>
        </View>

        <View
          style={[
            styles.box,
            {
              transform: [{translateY: 50}],
            },
          ]}>
          <Text style={styles.text}>TranslateY by 50 </Text>
        </View>

        <View
          style={[
            styles.box,
            {
              transform: [
                {
                  matrix: [1, 0.5, 0, 0, 0.5, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                },
              ],
            },
          ]}>
          <Text style={styles.text}>Matrix Transform</Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  </SafeAreaProvider>
);

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContentContainer: {
    alignItems: 'center',
    paddingBottom: 60,
  },
  box: {
    height: 100,
    width: 100,
    borderRadius: 5,
    marginVertical: 40,
    backgroundColor: '#61dafb',
    alignItems: 'center',
    justifyContent: 'center',
  },
  text: {
    fontSize: 14,
    fontWeight: 'bold',
    margin: 8,
    color: '#000',
    textAlign: 'center',
  },
});

export default App;
```

---

# Referência {#reference}

## Transform

`transform` aceita um array de objetos de transformação ou valores em string separados por espaços. Cada objeto especifica a propriedade que será transformada como a chave, e o valor a ser usado na transformação. Os objetos não devem ser combinados. Use um único par chave/valor por objeto.

As transformações de rotação requerem uma string para que a transformação possa ser expressa em graus (deg) ou radianos (rad). Por exemplo:

```js
{
  transform: [{rotateX: '45deg'}, {rotateZ: '0.785398rad'}],
}
```

O mesmo também pode ser alcançado usando uma string separada por espaços:

```js
{
  transform: 'rotateX(45deg) rotateZ(0.785398rad)',
}
```

As transformações de inclinação requerem uma string para que a transformação possa ser expressa em graus (deg). Por exemplo:

```js
{
  transform: [{skewX: '45deg'}],
}
```

As transformações de translação (`translateX` e `translateY`) aceitam números (pontos) ou strings de porcentagem (por exemplo, `'50%'`, `'100%'`). Ao usar porcentagens, o deslocamento é relativo à largura do elemento (para `translateX`) ou à altura (para `translateY`). A translação com porcentagem é suportada na [New Architecture](/architecture/landing-page). Por exemplo:

```js
{
  transform: [{translateX: '50%'}, {translateY: 100}],
}
```

### Transformação de matriz {#matrix-transform}

A transformação `matrix` aceita uma matriz de transformação 4x4 como um array de 16 números. Isso permite aplicar transformações complexas que combinam translação, rotação, escala e inclinação em uma única operação.

A matriz é especificada na ordem column-major:

```js
{
  transform: [
    {
      matrix: [
        scaleX,
        skewY,
        0,
        0,
        skewX,
        scaleY,
        0,
        0,
        0,
        0,
        1,
        0,
        translateX,
        translateY,
        0,
        1,
      ],
    },
  ];
}
```

Por exemplo, para aplicar uma combinação de escala e inclinação:

```js
{
  transform: [
    {
      matrix: [
        1, 0.5, 0, 0, 0.5, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
      ],
    },
  ];
}
```

:::note
Transformações de matriz são úteis quando você precisa aplicar matrizes de transformação pré-calculadas, como as de bibliotecas de animação ou ao criar aplicativos de editor de UI. Para transformações básicas, recomenda-se usar as propriedades de transformação individuais (scale, rotate, translate etc.), pois são mais legíveis.
:::

| Tipo                                                                                                                                                                                                                                                                                                                              | Obrigatório |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| array de objetos: `{matrix: number[]}`, `{perspective: number}`, `{rotate: string}`, `{rotateX: string}`, `{rotateY: string}`, `{rotateZ: string}`, `{scale: number}`, `{scaleX: number}`, `{scaleY: number}`, `{translateX: number \| string}`, `{translateY: number \| string}`, `{skewX: string}`, `{skewY: string}` ou string | Não       |

---

### 🗑️ `decomposedMatrix`, `rotation`, `scaleX`, `scaleY`, `transformMatrix`, `translateX`, `translateY`

:::warning[Deprecated]
Use a prop [`transform`](transforms#transform) no lugar.
:::

## Transform Origin

A propriedade `transformOrigin` define a origem para as transformações de uma view. A origem da transformação é o ponto ao redor do qual uma transformação é aplicada. Por padrão, a origem de uma transformação é `center`.

# Exemplo {#example-1}

```SnackPlayer name=TransformOrigin%20Example
import {useEffect, useRef} from 'react';
import {Animated, View, StyleSheet, Easing} from 'react-native';
import {SafeAreaView, SafeAreaProvider} from 'react-native-safe-area-context';

const App = () => {
  const rotateAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.loop(
      Animated.timing(rotateAnim, {
        toValue: 1,
        duration: 5000,
        easing: Easing.linear,
        useNativeDriver: true,
      }),
    ).start();
  }, [rotateAnim]);

  const spin = rotateAnim.interpolate({
    inputRange: [0, 1],
    outputRange: ['0deg', '360deg'],
  });

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.container}>
        <View style={styles.transformOriginWrapper}>
          <Animated.View
            style={[
              styles.transformOriginView,
              {
                transform: [{rotate: spin}],
              },
            ]}
          />
        </View>
      </SafeAreaView>
    </SafeAreaProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  transformOriginWrapper: {
    borderWidth: 1,
    borderColor: 'rgba(0, 0, 0, 0.5)',
  },
  transformOriginView: {
    backgroundColor: 'pink',
    width: 100,
    height: 100,
    transformOrigin: 'top',
  },
});

export default App;
```

### Values

Transform origin suporta valores em `px`, `percentage` e as palavras-chave `top`, `left`, `right`, `bottom`, `center`.

A propriedade `transformOrigin` pode ser especificada usando um, dois ou três valores, onde cada valor representa um deslocamento.

#### One-value syntax:

- O valor deve ser um `px`, uma `percentage`, ou uma das palavras-chave `left`, `center`, `right`, `top` e `bottom`.

```js
{
  transformOrigin: '20px',
  transformOrigin: 'bottom',
}
```

#### Two-value syntax:

- O primeiro valor (x-offset) deve ser um `px`, uma `percentage`, ou uma das palavras-chave `left`, `center` e `right`.
- O segundo valor (y-offset) deve ser um `px`, uma `percentage`, ou uma das palavras-chave `top`, `center` e `bottom`.

```js
{
  transformOrigin: '10px 2px',
  transformOrigin: 'left top',
  transformOrigin: 'top right',
}
```

#### Three-value syntax:

- Os primeiros dois valores são os mesmos que para a sintaxe de dois valores.
- O terceiro valor (z-offset) deve ser um `px`. Ele sempre representa o deslocamento Z.

```js
{
  transformOrigin: '2px 30% 10px',
  transformOrigin: 'right bottom 20px',
}
```

#### Array syntax

`transformOrigin` também suporta uma sintaxe de array. Isso torna conveniente usá-la com APIs Animated. Também evita análise de strings, então deve ser mais eficiente.

```js
{
  // Using numeric values
  transformOrigin: [10, 30, 40],
  // Mixing numeric and percentage values
  transformOrigin: [10, '20%', 0],
}
```

Você pode consultar o guia do MDN sobre [Transform origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin) para informações adicionais.
