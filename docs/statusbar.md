---
ia-translated: true
id: statusbar
title: StatusBar
---

import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; import constants from '@site/core/TabsConstants';

Componente para controlar a status bar do aplicativo. A status bar é a zona, tipicamente no topo da tela, que exibe a hora atual, informações de rede Wi-Fi e celular, nível de bateria e/ou outros ícones de status.

### Uso com Navigator {#usage-with-navigator}

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

### API Imperativa {#imperative-api}

Para casos onde usar um componente não é ideal, também existe uma API imperativa exposta como funções estáticas no componente. No entanto, não é recomendado usar a API estática e o componente para a mesma prop porque qualquer valor definido pela API estática será sobrescrito pelo definido pelo componente na próxima renderização.

---

# Referência {#reference}

## Constants

### `currentHeight` <div className="label android">Android</div>

A altura da status bar, que inclui a altura do notch, se presente.

---

## Props

### `animated`

Se a transição entre as mudanças de propriedades da status bar deve ser animada. Suportado para as propriedades `barStyle` e `hidden`.

| Tipo    | Obrigatório | Padrão  |
| ------- | ----------- | ------- |
| boolean | Não         | `false` |

---

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

### `showHideTransition` <div className="label ios">iOS</div>

O efeito de transição ao mostrar e ocultar a status bar usando a prop `hidden`.

| Tipo                                               | Padrão   |
| -------------------------------------------------- | -------- |
| [StatusBarAnimation](statusbar#statusbaranimation) | `'fade'` |

## Methods

### `popStackEntry()`

```tsx
static popStackEntry(entry: StatusBarProps);
```

Obtém e remove a última entrada de StatusBar da pilha.

**Parâmetros:**

| Nome                                                       | Tipo | Descrição                              |
| ---------------------------------------------------------- | ---- | -------------------------------------- |
| entry <div className="label basic required">Required</div> | any  | Entrada retornada de `pushStackEntry`. |

---

### `pushStackEntry()`

```tsx
static pushStackEntry(props: StatusBarProps): StatusBarProps;
```

Adiciona uma entrada de StatusBar na pilha. O valor de retorno deve ser passado para `popStackEntry` quando concluído.

**Parâmetros:**

| Nome                                                       | Tipo | Descrição                                                            |
| ---------------------------------------------------------- | ---- | -------------------------------------------------------------------- |
| props <div className="label basic required">Required</div> | any  | Objeto contendo as props de StatusBar para usar na entrada da pilha. |

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

| Nome                                                       | Tipo | Descrição                                                                            |
| ---------------------------------------------------------- | ---- | ------------------------------------------------------------------------------------ |
| entry <div className="label basic required">Required</div> | any  | Entrada retornada de `pushStackEntry` para substituir.                               |
| props <div className="label basic required">Required</div> | any  | Objeto contendo as props de StatusBar para usar na entrada de pilha de substituição. |

---

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

| Nome                                                        | Tipo                                               | Descrição                                             |
| ----------------------------------------------------------- | -------------------------------------------------- | ----------------------------------------------------- |
| hidden <div className="label basic required">Required</div> | boolean                                            | Ocultar a status bar.                                 |
| animation <div className="label ios">iOS</div>              | [StatusBarAnimation](statusbar#statusbaranimation) | Animação ao mudar a propriedade hidden da status bar. |

---

## Type Definitions

### StatusBarAnimation

Tipo de animação de status bar para transições no iOS.

| Tipo |
| ---- |
| enum |

**Constants:**

| Valor     | Tipo   | Descrição      |
| --------- | ------ | -------------- |
| `'fade'`  | string | Animação fade  |
| `'slide'` | string | Animação slide |
| `'none'`  | string | Sem animação   |

---

### StatusBarStyle

Tipo de estilo de status bar.

| Tipo |
| ---- |
| enum |

**Constants:**

| Valor             | Tipo   | Descrição                                                                                                                                 |
| ----------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `'default'`       | string | Estilo de status bar padrão (claro para Android, escuro para iOS)                                                                         |
| `'auto'`          | string | Escolhe automaticamente `light-content` ou `dark-content` conforme o esquema de cores atual. Atualiza sempre que o esquema de cores muda. |
| `'light-content'` | string | Textos e ícones brancos                                                                                                                   |
| `'dark-content'`  | string | Textos e ícones escuros (requer API>=23 no Android)                                                                                       |
