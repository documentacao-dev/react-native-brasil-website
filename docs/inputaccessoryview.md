---
id: inputaccessoryview
title: '🗑️ InputAccessoryView'
ia-translated: true
---

:::warning[Deprecated]
`InputAccessoryView` está obsoleto e será removido em uma versão futura.
:::

Um componente que permite a customização da view de acessório de entrada do teclado no iOS. A view de acessório de entrada é exibida acima do teclado sempre que um `TextInput` tem foco. Este componente pode ser usado para criar toolbars personalizadas.

Para usar este componente, envolva sua toolbar personalizada com o componente InputAccessoryView e defina um `nativeID`. Em seguida, passe esse `nativeID` como o `inputAccessoryViewID` de qualquer `TextInput` que você desejar. Um exemplo básico:

```SnackPlayer name=InputAccessoryView&supportedPlatforms=ios
import {useState} from 'react';
import {
  Button,
  InputAccessoryView,
  ScrollView,
  TextInput,
  StyleSheet,
} from 'react-native';
import {SafeAreaView, SafeAreaProvider} from 'react-native-safe-area-context';

const inputAccessoryViewID = 'uniqueID';
const initialText = '';

const App = () => {
  const [text, setText] = useState(initialText);

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.container}>
        <ScrollView keyboardDismissMode="interactive">
          <TextInput
            style={styles.textInput}
            inputAccessoryViewID={inputAccessoryViewID}
            onChangeText={setText}
            value={text}
            placeholder={'Please type here…'}
          />
        </ScrollView>
      </SafeAreaView>
      <InputAccessoryView nativeID={inputAccessoryViewID}>
        <Button onPress={() => setText(initialText)} title="Clear text" />
      </InputAccessoryView>
    </SafeAreaProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    paddingHorizontal: 20,
  },
  textInput: {
    padding: 16,
    borderColor: 'black',
    borderWidth: 1,
  },
});

export default App;
```

Este componente também pode ser usado para criar text inputs fixos (text inputs que são ancorados ao topo do teclado). Para fazer isso, envolva um `TextInput` com o componente `InputAccessoryView` e não defina um `nativeID`. Para um exemplo, veja [InputAccessoryViewExample.js](https://github.com/react/react-native/blob/main/packages/rn-tester/js/examples/InputAccessoryView/InputAccessoryViewExample.js).

---

# Referência {#reference}

## Props

### `backgroundColor`

| Type               |
| ------------------ |
| [color](colors.md) |

---

### `nativeID`

Um ID que é usado para associar este `InputAccessoryView` a TextInput(s) especificados.

| Type   |
| ------ |
| string |

---

### `style`

| Type                              |
| --------------------------------- |
| [View Style](view-style-props.md) |

# Problemas conhecidos {#known-issues}

- [react-native#18997](https://github.com/react/react-native/issues/18997): Não funciona com `TextInput` multilinha
- [react-native#20157](https://github.com/react/react-native/issues/20157): Não pode ser usado com uma tab bar inferior
