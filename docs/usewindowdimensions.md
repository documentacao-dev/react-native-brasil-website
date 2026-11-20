---
ia-translated: true
id: usewindowdimensions
title: useWindowDimensions
---

```tsx
import {useWindowDimensions} from 'react-native';
```

`useWindowDimensions` atualiza automaticamente todos os seus valores quando o tamanho da tela ou a escala de fonte muda. Você pode obter a largura e altura da janela da sua aplicação assim:

```tsx
const {height, width} = useWindowDimensions();
```

## Exemplo

```SnackPlayer name=useWindowDimensions&supportedPlatforms=ios,android
import {StyleSheet, Text, View, useWindowDimensions} from 'react-native';
import {SafeAreaView, SafeAreaProvider} from 'react-native-safe-area-context';

const App = () => {
  const {height, width, scale, fontScale} = useWindowDimensions();
  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.container}>
        <Text style={styles.header}>Window Dimension Data</Text>
        <View>
          <Text>Height: {height}</Text>
          <Text>Width: {width}</Text>
          <Text>Font scale: {fontScale}</Text>
          <Text>Pixel ratio: {scale}</Text>
        </View>
        <View
          style={{
            width: 100 * fontScale,
            padding: 16 * fontScale,
            ...styles.box,
          }}>
          <Text style={{fontSize: 14 / fontScale}}>Dynamic Box</Text>
        </View>
      </SafeAreaView>
    </SafeAreaProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    gap: 12,
  },
  header: {
    fontSize: 20,
  },
  box: {
    minWidth: 100,
    backgroundColor: '#06bcee',
  },
});

export default App;
```

## Propriedades

### `fontScale`

```tsx
useWindowDimensions().fontScale;
```

A escala da fonte atualmente usada. Alguns sistemas operacionais permitem que os usuários aumentem ou diminuam suas fontes para maior conforto de leitura. Esta propriedade informará o que está em vigor.

:::note
Changing the font size percentage can be leveraged to dynamically adjust the sizes of UI elements, such as padding, margins, and container heights, to ensure a consistent and accessible user experience. By using the fontScale property, developers can make their applications more adaptable to users' preferences for larger or smaller text, enhancing readability and usability.
:::

---

### `height`

```tsx
useWindowDimensions().height;
```

A altura em pixels da janela ou tela que sua aplicação ocupa.

---

### `scale`

```tsx
useWindowDimensions().scale;
```

A proporção de pixels do dispositivo no qual sua aplicação está sendo executada. Os valores podem ser:

- `1` que indica que um ponto é igual a um pixel (geralmente PPI/DPI de 96, 76 em algumas plataformas).
- `2` ou `3` que indica uma tela Retina ou de alto DPI.

---

### `width`

```tsx
useWindowDimensions().width;
```

A largura em pixels da janela ou tela que sua aplicação ocupa.
