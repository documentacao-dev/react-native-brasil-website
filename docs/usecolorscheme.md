---
ia-translated: true
id: usecolorscheme
title: useColorScheme
---

```tsx
import {useColorScheme} from 'react-native';
```

O React hook `useColorScheme` fornece e subscreve atualizações de esquema de cores do módulo [`Appearance`](appearance). O valor de retorno indica o esquema de cores ativo. O valor pode ser atualizado posteriormente, seja através de ação direta do usuário (por exemplo, seleção de tema nas configurações do dispositivo ou estilo de interface selecionado no nível do app via [`setColorScheme`](appearance#setcolorscheme)) ou em uma programação (por exemplo, temas claro e escuro que seguem o ciclo dia/noite).

### Valores de retorno {#return-values}

- `'light'`: O esquema de cores claro é aplicado.
- `'dark'`: O esquema de cores escuro é aplicado.
- `null`: Pode ser retornado se o módulo nativo Appearance não estiver disponível.

---

## Exemplo {#example}

```SnackPlayer
import {Text, StyleSheet, useColorScheme} from 'react-native';
import {SafeAreaView, SafeAreaProvider} from 'react-native-safe-area-context';

const App = () => {
  const colorScheme = useColorScheme();
  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.container}>
        <Text>useColorScheme(): {colorScheme}</Text>
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
});

export default App;
```

Você pode encontrar um exemplo completo que demonstra o uso deste hook junto com um contexto React para adicionar suporte a temas claro e escuro à sua aplicação em [`AppearanceExample.js`](https://github.com/react/react-native/blob/main/packages/rn-tester/js/examples/Appearance/AppearanceExample.js).
