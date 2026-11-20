---
ia-translated: true
id: dimensions
title: Dimensions
---

:::info
[`useWindowDimensions`](usewindowdimensions) é a API preferida para componentes React. Diferentemente de `Dimensions`, ela atualiza conforme as dimensões da janela mudam. Isso funciona bem com o paradigma React.
:::

```tsx
import {Dimensions} from 'react-native';
```

Você pode obter a largura e altura da janela do aplicativo usando o seguinte código:

```tsx
const windowWidth = Dimensions.get('window').width;
const windowHeight = Dimensions.get('window').height;
```

:::note
Embora as dimensões estejam disponíveis imediatamente, elas podem mudar (por exemplo, devido à rotação do dispositivo, dispositivos dobráveis etc), portanto qualquer lógica de renderização ou estilos que dependam dessas constantes devem tentar chamar esta função a cada renderização, ao invés de armazenar o valor em cache (por exemplo, usando estilos inline ao invés de definir um valor em um `StyleSheet`).
:::

Se você está mirando dispositivos dobráveis ou dispositivos que podem mudar o tamanho da tela ou o tamanho da janela do aplicativo, você pode usar o event listener disponível no módulo Dimensions conforme mostrado no exemplo abaixo.

## Example

```SnackPlayer name=Dimensions%20Example&ext=tsx
import {useState, useEffect} from 'react';
import {
  StyleSheet,
  Text,
  Dimensions,
  type DimensionsPayload,
} from 'react-native';
import {SafeAreaView, SafeAreaProvider} from 'react-native-safe-area-context';

const windowDimensions = Dimensions.get('window');
const screenDimensions = Dimensions.get('screen');

const App = () => {
  const [dimensions, setDimensions] = useState({
    window: windowDimensions,
    screen: screenDimensions,
  });

  useEffect(() => {
    const subscription = Dimensions.addEventListener(
      'change',
      ({window, screen}: DimensionsPayload) => {
        if (window && screen) {
          setDimensions({window, screen});
        }
      },
    );
    return () => subscription?.remove();
  });

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.container}>
        <Text style={styles.header}>Window Dimensions</Text>
        {Object.entries(dimensions.window).map(([key, value]) => (
          <Text>
            {key} - {value}
          </Text>
        ))}
        <Text style={styles.header}>Screen Dimensions</Text>
        {Object.entries(dimensions.screen).map(([key, value]) => (
          <Text>
            {key} - {value}
          </Text>
        ))}
      </SafeAreaView>
    </SafeAreaProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  header: {
    fontSize: 16,
    marginVertical: 10,
  },
});

export default App;
```

# Reference

## Methods

### `addEventListener()`

```tsx
static addEventListener(
  type: 'change',
  handler: ({
    window,
    screen,
  }: DimensionsPayload) => void,
): EventSubscription;
```

Adiciona um event handler. Eventos suportados:

<<<<<<< pt
- `change`: Dispara quando uma propriedade dentro do objeto `Dimensions` muda. O argumento para o event handler é um objeto do tipo [`DimensionsValue`](#dimensionsvalue).
||||||| base_en
- `change`: Fires when a property within the `Dimensions` object changes. The argument to the event handler is a [`DimensionsValue`](#dimensionsvalue) type object.
=======
- `change`: Fires when a property within the `Dimensions` object changes. The argument to the event handler is a [`DimensionsPayload`](#dimensionspayload) object.
>>>>>>> new_en

---

### `get()`

```tsx
static get(dim: string): DisplayMetrics | DisplayMetricsAndroid;
```

As dimensões iniciais são definidas antes de `runApplication` ser chamado, então elas devem estar disponíveis antes de qualquer outro require ser executado, mas podem ser atualizadas posteriormente.

Exemplo: `const {height, width} = Dimensions.get('window');`

**Parameters:**

| Name                                                               | Type   | Description                                                                                    |
| ------------------------------------------------------------------ | ------ | ---------------------------------------------------------------------------------------------- |
| dim <div className="label basic required two-lines">Required</div> | string | Nome da dimensão conforme definido ao chamar `set`. Retorna o valor para a dimensão. |

:::note
No Android, a dimensão `window` será reduzida pelo tamanho da barra de status (se não for translúcida) e pela barra de navegação inferior.
:::

## Type Definitions

### DimensionsPayload

**Properties:**

<<<<<<< pt
| Name   | Type                                | Description                                  |
| ------ | ----------------------------------- | -------------------------------------------- |
| window | [ScaledSize](dimensions#scaledsize) | Tamanho da janela do Application visível. |
| screen | [ScaledSize](dimensions#scaledsize) | Tamanho da tela do dispositivo.            |
||||||| base_en
| Name   | Type                                | Description                             |
| ------ | ----------------------------------- | --------------------------------------- |
| window | [ScaledSize](dimensions#scaledsize) | Size of the visible Application window. |
| screen | [ScaledSize](dimensions#scaledsize) | Size of the device's screen.            |
=======
| Name                 | Type                                                      | Description                             |
| -------------------- | --------------------------------------------------------- | --------------------------------------- |
| window               | [DisplayMetrics](dimensions#displaymetrics)               | Size of the visible application window. |
| screen               | [DisplayMetrics](dimensions#displaymetrics)               | Size of the device's screen.            |
| windowPhysicalPixels | [DisplayMetricsAndroid](dimensions#displaymetricsandroid) | Physical pixels for the Android window. |
| screenPhysicalPixels | [DisplayMetricsAndroid](dimensions#displaymetricsandroid) | Physical pixels for the Android screen. |
>>>>>>> new_en

### DisplayMetrics

| Type   |
| ------ |
| object |

**Properties:**

| Name      | Type   |
| --------- | ------ |
| width     | number |
| height    | number |
| scale     | number |
| fontScale | number |

### DisplayMetricsAndroid

`DisplayMetricsAndroid` includes all [`DisplayMetrics`](dimensions#displaymetrics) properties and the following property:

| Name       | Type   |
| ---------- | ------ |
| densityDpi | number |
