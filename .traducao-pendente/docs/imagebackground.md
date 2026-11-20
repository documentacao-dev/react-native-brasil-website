---
ia-translated: true
id: imagebackground
title: '🗑️ ImageBackground'
---

<<<<<<< pt
Uma solicitação de recurso comum de desenvolvedores familiarizados com a web é `background-image`. Para lidar com este caso de uso, você pode usar o componente `<ImageBackground>`, que possui os mesmos props que `<Image>`, e adicionar quaisquer children que você desejar para sobrepor em cima dele.
||||||| base_en
A common feature request from developers familiar with the web is `background-image`. To handle this use case, you can use the `<ImageBackground>` component, which has the same props as `<Image>`, and add whatever children to it you would like to layer on top of it.
=======
:::warning[Deprecated]
Use a [`View`](view.md) with an absolutely positioned [`Image`](image.md) instead.
:::

A common feature request from developers familiar with the web is `background-image`. To handle this use case, you can use the `<ImageBackground>` component, which has the same props as `<Image>`, and add whatever children to it you would like to layer on top of it.
>>>>>>> new_en

<<<<<<< pt
Você pode não querer usar `<ImageBackground>` em alguns casos, já que a implementação é básica. Consulte o [código-fonte](https://github.com/facebook/react-native/blob/main/packages/react-native/Libraries/Image/ImageBackground.js) do `<ImageBackground>` para mais informações e crie seu próprio componente customizado quando necessário.
||||||| base_en
You might not want to use `<ImageBackground>` in some cases, since the implementation is basic. Refer to `<ImageBackground>`'s [source code](https://github.com/facebook/react-native/blob/main/packages/react-native/Libraries/Image/ImageBackground.js) for more insight, and create your own custom component when needed.
=======
You might not want to use `<ImageBackground>` in some cases, since the implementation is basic. Refer to `<ImageBackground>`'s [source code](https://github.com/react/react-native/blob/main/packages/react-native/Libraries/Image/ImageBackground.js) for more insight, and create your own custom component when needed.
>>>>>>> new_en

Note que você deve especificar alguns atributos de estilo de largura e altura.

## Exemplo

```SnackPlayer name=ImageBackground
import {ImageBackground, StyleSheet, Text} from 'react-native';
import {SafeAreaView, SafeAreaProvider} from 'react-native-safe-area-context';

const image = {uri: 'https://legacy.reactjs.org/logo-og.png'};

const App = () => (
  <SafeAreaProvider>
    <SafeAreaView style={styles.container} edges={['left', 'right']}>
      <ImageBackground source={image} resizeMode="cover" style={styles.image}>
        <Text style={styles.text}>Inside</Text>
      </ImageBackground>
    </SafeAreaView>
  </SafeAreaProvider>
);

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  image: {
    flex: 1,
    justifyContent: 'center',
  },
  text: {
    color: 'white',
    fontSize: 42,
    lineHeight: 84,
    fontWeight: 'bold',
    textAlign: 'center',
    backgroundColor: '#000000c0',
  },
});

export default App;
```

---

# Referência

## Props

### [Image Props](image.md#props)

Herda [Image Props](image.md#props).

---

### `imageStyle`

| Tipo                                |
| ----------------------------------- |
| [Image Style](image-style-props.md) |

---

### `imageRef`

Um ref setter que será atribuído ao [element node](element-nodes) do componente `Image` interno quando montado.

---

### `style`

| Tipo                              |
| --------------------------------- |
| [View Style](view-style-props.md) |
