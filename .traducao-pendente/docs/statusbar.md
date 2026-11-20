---
ia-translated: true
id: statusbar
title: StatusBar
---

import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; import constants from '@site/core/TabsConstants';

Componente para controlar a status bar do aplicativo. A status bar é a zona, tipicamente no topo da tela, que exibe a hora atual, informações de rede Wi-Fi e celular, nível de bateria e/ou outros ícones de status.

### Uso com Navigator

É possível ter múltiplos componentes `StatusBar` montados ao mesmo tempo. As props serão mescladas na ordem em que os componentes `StatusBar` foram montados.

<Tabs groupId="language" queryString defaultValue={constants.defaultSnackLanguage} values={constants.snackLanguages}>
<TabItem value="javascript">

```SnackPlayer name=StatusBar%20Component%20Example&supportedPlatforms=android,ios&ext=js
import {useState} from 'react';
import {
  Button,
  Platform,
  StatusBar,
  StyleSheet,
  Text,
  View,
} from 'react-native';
import {SafeAreaView, SafeAreaProvider} from 'react-native-safe-area-context';

const STYLES = ['default', 'auto', 'dark-content', 'light-content'];
const TRANSITIONS = ['fade', 'slide', 'none'];

const App = () => {
  const [hidden, setHidden] = useState(false);
  const [statusBarStyle, setStatusBarStyle] = useState(STYLES[0]);
  const [statusBarTransition, setStatusBarTransition] = useState(
    TRANSITIONS[0],
  );

  const changeStatusBarVisibility = () => setHidden(!hidden);

  const changeStatusBarStyle = () => {
    const styleId = STYLES.indexOf(statusBarStyle) + 1;
    if (styleId === STYLES.length) {
      setStatusBarStyle(STYLES[0]);
    } else {
      setStatusBarStyle(STYLES[styleId]);
    }
  };

  const changeStatusBarTransition = () => {
    const transition = TRANSITIONS.indexOf(statusBarTransition) + 1;
    if (transition === TRANSITIONS.length) {
      setStatusBarTransition(TRANSITIONS[0]);
    } else {
      setStatusBarTransition(TRANSITIONS[transition]);
    }
  };

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.container}>
        <StatusBar
          animated={true}
          barStyle={statusBarStyle}
          showHideTransition={statusBarTransition}
          hidden={hidden}
        />
        <Text style={styles.textStyle}>
          StatusBar Visibility:{'\n'}
          {hidden ? 'Hidden' : 'Visible'}
        </Text>
        <Text style={styles.textStyle}>
          StatusBar Style:{'\n'}
          {statusBarStyle}
        </Text>
        {Platform.OS === 'ios' ? (
          <Text style={styles.textStyle}>
            StatusBar Transition:{'\n'}
            {statusBarTransition}
          </Text>
        ) : null}
        <View style={styles.buttonsContainer}>
          <Button
            title="Toggle StatusBar"
            onPress={changeStatusBarVisibility}
          />
          <Button
            title="Change StatusBar Style"
            onPress={changeStatusBarStyle}
          />
          {Platform.OS === 'ios' ? (
            <Button
              title="Change StatusBar Transition"
              onPress={changeStatusBarTransition}
            />
          ) : null}
        </View>
      </SafeAreaView>
    </SafeAreaProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: '#ECF0F1',
  },
  buttonsContainer: {
    padding: 10,
  },
  textStyle: {
    textAlign: 'center',
    marginBottom: 8,
  },
});

export default App;
```

</TabItem>
<TabItem value="typescript">

```SnackPlayer name=StatusBar%20Component%20Example&supportedPlatforms=android,ios&ext=tsx
import {useState} from 'react';
import {
  Button,
  Platform,
  StatusBar,
  StyleSheet,
  Text,
  View,
  StatusBarStyle,
} from 'react-native';
import {SafeAreaView, SafeAreaProvider} from 'react-native-safe-area-context';

const STYLES = ['default', 'auto', 'dark-content', 'light-content'] as const;
const TRANSITIONS = ['fade', 'slide', 'none'] as const;

const App = () => {
  const [hidden, setHidden] = useState(false);
  const [statusBarStyle, setStatusBarStyle] = useState<StatusBarStyle>(
    STYLES[0],
  );
  const [statusBarTransition, setStatusBarTransition] = useState<
    'fade' | 'slide' | 'none'
  >(TRANSITIONS[0]);

  const changeStatusBarVisibility = () => setHidden(!hidden);

  const changeStatusBarStyle = () => {
    const styleId = STYLES.indexOf(statusBarStyle) + 1;
    if (styleId === STYLES.length) {
      setStatusBarStyle(STYLES[0]);
    } else {
      setStatusBarStyle(STYLES[styleId]);
    }
  };

  const changeStatusBarTransition = () => {
    const transition = TRANSITIONS.indexOf(statusBarTransition) + 1;
    if (transition === TRANSITIONS.length) {
      setStatusBarTransition(TRANSITIONS[0]);
    } else {
      setStatusBarTransition(TRANSITIONS[transition]);
    }
  };

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.container}>
        <StatusBar
          animated={true}
          barStyle={statusBarStyle}
          showHideTransition={statusBarTransition}
          hidden={hidden}
        />
        <Text style={styles.textStyle}>
          StatusBar Visibility:{'\n'}
          {hidden ? 'Hidden' : 'Visible'}
        </Text>
        <Text style={styles.textStyle}>
          StatusBar Style:{'\n'}
          {statusBarStyle}
        </Text>
        {Platform.OS === 'ios' ? (
          <Text style={styles.textStyle}>
            StatusBar Transition:{'\n'}
            {statusBarTransition}
          </Text>
        ) : null}
        <View style={styles.buttonsContainer}>
          <Button
            title="Toggle StatusBar"
            onPress={changeStatusBarVisibility}
          />
          <Button
            title="Change StatusBar Style"
            onPress={changeStatusBarStyle}
          />
          {Platform.OS === 'ios' ? (
            <Button
              title="Change StatusBar Transition"
              onPress={changeStatusBarTransition}
            />
          ) : null}
        </View>
      </SafeAreaView>
    </SafeAreaProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: '#ECF0F1',
  },
  buttonsContainer: {
    padding: 10,
  },
  textStyle: {
    textAlign: 'center',
    marginBottom: 8,
  },
});

export default App;
```

</TabItem>
</Tabs>

### API Imperativa

Para casos onde usar um componente não é ideal, também existe uma API imperativa exposta como funções estáticas no componente. No entanto, não é recomendado usar a API estática e o componente para a mesma prop porque qualquer valor definido pela API estática será sobrescrito pelo definido pelo componente na próxima renderização.

---

# Referência

## Constants

### `currentHeight` <div className="label android">Android</div>

A altura da status bar, que inclui a altura do notch, se presente.

---

## Props

### `animated`

<<<<<<< pt
Se a transição entre as mudanças de propriedades da status bar deve ser animada. Suportado para as propriedades `backgroundColor`, `barStyle` e `hidden`.
||||||| base_en
If the transition between status bar property changes should be animated. Supported for `backgroundColor`, `barStyle` and `hidden` properties.
=======
If the transition between status bar property changes should be animated. Supported for `barStyle` and `hidden` properties.
>>>>>>> new_en

| Tipo    | Obrigatório | Padrão  |
| ------- | ----------- | ------- |
| boolean | Não         | `false` |

---

<<<<<<< pt
### `backgroundColor` <div className="label android">Android</div>

A cor de fundo da status bar.

:::warning
Devido à imposição de edge-to-edge introduzida no Android 15, definir a cor de fundo da status bar está obsoleto no nível de API 35 e defini-la não terá efeito. Você pode ler mais sobre nossas [recomendações de edge-to-edge aqui](https://github.com/react-native-community/discussions-and-proposals/discussions/827).
:::

| Tipo            | Obrigatório | Padrão                                                                          |
| --------------- | ----------- | ------------------------------------------------------------------------------- |
| [color](colors) | Não         | cor de fundo padrão do sistema para StatusBar, ou `'black'` se não for definida |

---

||||||| base_en
### `backgroundColor` <div className="label android">Android</div>

The background color of the status bar.

:::warning
Due to edge-to-edge enforcement introduced in Android 15, setting background color of the status bar is deprecated in API level 35 and setting it will have no effect. You can read more about our [edge-to-edge recommendations here](https://github.com/react-native-community/discussions-and-proposals/discussions/827).
:::

| Type            | Required | Default                                                                |
| --------------- | -------- | ---------------------------------------------------------------------- |
| [color](colors) | No       | default system StatusBar background color, or `'black'` if not defined |

---

=======
>>>>>>> new_en
### `barStyle`

Define a cor do texto da status bar.

No Android, isso só terá impacto nas versões de API 23 e superiores.

| Tipo                                       | Obrigatório | Padrão      |
| ------------------------------------------ | ----------- | ----------- |
| [StatusBarStyle](statusbar#statusbarstyle) | Não         | `'default'` |

---

### `hidden`

Se a status bar está oculta.

| Tipo    | Obrigatório | Padrão  |
| ------- | ----------- | ------- |
| boolean | Não         | `false` |

---

<<<<<<< pt
### `networkActivityIndicatorVisible` <div className="label ios">iOS</div>

Se o indicador de atividade de rede deve ser visível.

| Tipo    | Padrão  |
| ------- | ------- |
| boolean | `false` |

---

||||||| base_en
### `networkActivityIndicatorVisible` <div className="label ios">iOS</div>

If the network activity indicator should be visible.

| Type    | Default |
| ------- | ------- |
| boolean | `false` |

---

=======
>>>>>>> new_en
### `showHideTransition` <div className="label ios">iOS</div>

O efeito de transição ao mostrar e ocultar a status bar usando a prop `hidden`.

| Tipo                                               | Padrão   |
| -------------------------------------------------- | -------- |
| [StatusBarAnimation](statusbar#statusbaranimation) | `'fade'` |

<<<<<<< pt
---

### `translucent` <div className="label android">Android</div>

Se a status bar é translúcida. Quando translucent é definido como `true`, o aplicativo desenhará sob a status bar. Isso é útil ao usar uma cor de status bar semi-transparente.

:::warning
Devido à imposição de edge-to-edge introduzida no Android 15, definir a status bar como translúcida está obsoleto no nível de API 35 e defini-la não terá efeito. Você pode ler mais sobre nossas [recomendações de edge-to-edge aqui](https://github.com/react-native-community/discussions-and-proposals/discussions/827).
:::

| Tipo    | Padrão  |
| ------- | ------- |
| boolean | `false` |

||||||| base_en
---

### `translucent` <div className="label android">Android</div>

If the status bar is translucent. When translucent is set to `true`, the app will draw under the status bar. This is useful when using a semi transparent status bar color.

:::warning
Due to edge-to-edge enforcement introduced in Android 15, setting the status bar as translucent is deprecated in API level 35 and setting it will have no effect. You can read more about our [edge-to-edge recommendations here](https://github.com/react-native-community/discussions-and-proposals/discussions/827).
:::

| Type    | Default |
| ------- | ------- |
| boolean | `false` |

=======
>>>>>>> new_en
## Methods

### `popStackEntry()`

```tsx
static popStackEntry(entry: StatusBarProps);
```

Obtém e remove a última entrada de StatusBar da pilha.

**Parâmetros:**

| Nome                                                       | Tipo | Descrição                                 |
| ---------------------------------------------------------- | ---- | ----------------------------------------- |
| entry <div className="label basic required">Required</div> | any  | Entrada retornada de `pushStackEntry`.    |

---

### `pushStackEntry()`

```tsx
static pushStackEntry(props: StatusBarProps): StatusBarProps;
```

Adiciona uma entrada de StatusBar na pilha. O valor de retorno deve ser passado para `popStackEntry` quando concluído.

**Parâmetros:**

| Nome                                                       | Tipo | Descrição                                                                  |
| ---------------------------------------------------------- | ---- | -------------------------------------------------------------------------- |
| props <div className="label basic required">Required</div> | any  | Objeto contendo as props de StatusBar para usar na entrada da pilha.      |

---

### `replaceStackEntry()`

```tsx
static replaceStackEntry(
  entry: StatusBarProps,
  props: StatusBarProps
): StatusBarProps;
```

Substitui uma entrada de pilha de StatusBar existente por novas props.

**Parâmetros:**

| Nome                                                       | Tipo | Descrição                                                                                |
| ---------------------------------------------------------- | ---- | ---------------------------------------------------------------------------------------- |
| entry <div className="label basic required">Required</div> | any  | Entrada retornada de `pushStackEntry` para substituir.                                   |
| props <div className="label basic required">Required</div> | any  | Objeto contendo as props de StatusBar para usar na entrada de pilha de substituição.    |

---

<<<<<<< pt
### `setBackgroundColor()` <div className="label android">Android</div>

```tsx
static setBackgroundColor(color: ColorValue, animated?: boolean);
```

Define a cor de fundo para a status bar.

:::warning
Devido à imposição de edge-to-edge introduzida no Android 15, definir a cor de fundo da status bar está obsoleto no nível de API 35 e defini-la não terá efeito. Você pode ler mais sobre nossas [recomendações de edge-to-edge aqui](https://github.com/react-native-community/discussions-and-proposals/discussions/827).
:::

**Parâmetros:**

| Nome                                                       | Tipo    | Descrição                       |
| ---------------------------------------------------------- | ------- | ------------------------------- |
| color <div className="label basic required">Required</div> | string  | Cor de fundo.                   |
| animated                                                   | boolean | Animar a mudança de estilo.     |

---

||||||| base_en
### `setBackgroundColor()` <div className="label android">Android</div>

```tsx
static setBackgroundColor(color: ColorValue, animated?: boolean);
```

Set the background color for the status bar.

:::warning
Due to edge-to-edge enforcement introduced in Android 15, setting background color of the status bar is deprecated in API level 35 and setting it will have no effect. You can read more about our [edge-to-edge recommendations here](https://github.com/react-native-community/discussions-and-proposals/discussions/827).
:::

**Parameters:**

| Name                                                       | Type    | Description               |
| ---------------------------------------------------------- | ------- | ------------------------- |
| color <div className="label basic required">Required</div> | string  | Background color.         |
| animated                                                   | boolean | Animate the style change. |

---

=======
>>>>>>> new_en
### `setBarStyle()`

```tsx
static setBarStyle(style: StatusBarStyle, animated?: boolean);
```

Define o estilo da status bar.

**Parâmetros:**

| Nome                                                       | Tipo                                       | Descrição                       |
| ---------------------------------------------------------- | ------------------------------------------ | ------------------------------- |
| style <div className="label basic required">Required</div> | [StatusBarStyle](statusbar#statusbarstyle) | Estilo de status bar a definir. |
| animated                                                   | boolean                                    | Animar a mudança de estilo.     |

---

### `setHidden()`

```tsx
static setHidden(hidden: boolean, animation?: StatusBarAnimation);
```

Mostra ou oculta a status bar.

**Parâmetros:**

| Nome                                                        | Tipo                                               | Descrição                                                      |
| ----------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------- |
| hidden <div className="label basic required">Required</div> | boolean                                            | Ocultar a status bar.                                          |
| animation <div className="label ios">iOS</div>              | [StatusBarAnimation](statusbar#statusbaranimation) | Animação ao mudar a propriedade hidden da status bar.          |

---

<<<<<<< pt
### `setNetworkActivityIndicatorVisible()` <div className="label ios">iOS</div>

```tsx
static setNetworkActivityIndicatorVisible(visible: boolean);
```

Controla a visibilidade do indicador de atividade de rede.

**Parâmetros:**

| Nome                                                         | Tipo    | Descrição           |
| ------------------------------------------------------------ | ------- | ------------------- |
| visible <div className="label basic required">Required</div> | boolean | Mostra o indicador. |

---

### `setTranslucent()` <div className="label android">Android</div>

```tsx
static setTranslucent(translucent: boolean);
```

Controla a translucidez da status bar.

:::warning
Devido à imposição de edge-to-edge introduzida no Android 15, definir a status bar como translúcida está obsoleto no nível de API 35 e defini-la não terá efeito. Você pode ler mais sobre nossas [recomendações de edge-to-edge aqui](https://github.com/react-native-community/discussions-and-proposals/discussions/827).
:::

**Parâmetros:**

| Nome                                                             | Tipo    | Descrição              |
| ---------------------------------------------------------------- | ------- | ---------------------- |
| translucent <div className="label basic required">Required</div> | boolean | Definir como translúcida. |

||||||| base_en
### `setNetworkActivityIndicatorVisible()` <div className="label ios">iOS</div>

```tsx
static setNetworkActivityIndicatorVisible(visible: boolean);
```

Control the visibility of the network activity indicator.

**Parameters:**

| Name                                                         | Type    | Description         |
| ------------------------------------------------------------ | ------- | ------------------- |
| visible <div className="label basic required">Required</div> | boolean | Show the indicator. |

---

### `setTranslucent()` <div className="label android">Android</div>

```tsx
static setTranslucent(translucent: boolean);
```

Control the translucency of the status bar.

:::warning
Due to edge-to-edge enforcement introduced in Android 15, setting the status bar as translucent is deprecated in API level 35 and setting it will have no effect. You can read more about our [edge-to-edge recommendations here](https://github.com/react-native-community/discussions-and-proposals/discussions/827).
:::

**Parameters:**

| Name                                                             | Type    | Description         |
| ---------------------------------------------------------------- | ------- | ------------------- |
| translucent <div className="label basic required">Required</div> | boolean | Set as translucent. |

=======
>>>>>>> new_en
## Type Definitions

### StatusBarAnimation

Tipo de animação de status bar para transições no iOS.

| Tipo |
| ---- |
| enum |

**Constants:**

| Valor     | Tipo   | Descrição       |
| --------- | ------ | --------------- |
| `'fade'`  | string | Animação fade   |
| `'slide'` | string | Animação slide  |
| `'none'`  | string | Sem animação    |

---

### StatusBarStyle

Tipo de estilo de status bar.

| Tipo |
| ---- |
| enum |

**Constants:**

<<<<<<< pt
| Valor             | Tipo   | Descrição                                                     |
| ----------------- | ------ | ------------------------------------------------------------- |
| `'default'`       | string | Estilo de status bar padrão (escuro para iOS, claro para Android) |
| `'light-content'` | string | Textos e ícones brancos                                       |
| `'dark-content'`  | string | Textos e ícones escuros (requer API>=23 no Android)           |
||||||| base_en
| Value             | Type   | Description                                                |
| ----------------- | ------ | ---------------------------------------------------------- |
| `'default'`       | string | Default status bar style (dark for iOS, light for Android) |
| `'light-content'` | string | White texts and icons                                      |
| `'dark-content'`  | string | Dark texts and icons (requires API>=23 on Android)         |
=======
| Value             | Type   | Description                                                                                                                         |
| ----------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| `'default'`       | string | Default status bar style (light for Android, dark for iOS)                                                                          |
| `'auto'`          | string | Automatically picks `light-content` or `dark-content` based on the current color scheme. Updates whenever the color scheme changes. |
| `'light-content'` | string | White texts and icons                                                                                                               |
| `'dark-content'`  | string | Dark texts and icons (requires API>=23 on Android)                                                                                  |
>>>>>>> new_en
