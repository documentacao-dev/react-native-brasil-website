---
ia-translated: true
id: usecolorscheme
title: useColorScheme
---

```tsx
import {useColorScheme} from 'react-native';
```

<<<<<<< pt
O React hook `useColorScheme` fornece e subscreve atualizações de esquema de cores do módulo [`Appearance`](appearance). O valor de retorno indica o esquema de cores preferido do usuário atual. O valor pode ser atualizado posteriormente, seja através de ação direta do usuário (por exemplo, seleção de tema nas configurações do dispositivo) ou em uma programação (por exemplo, temas claro e escuro que seguem o ciclo dia/noite).
||||||| base_en
The `useColorScheme` React hook provides and subscribes to color scheme updates from the [`Appearance`](appearance) module. The return value indicates the current user preferred color scheme. The value may be updated later, either through direct user action (e.g. theme selection in device settings) or on a schedule (e.g. light and dark themes that follow the day/night cycle).
=======
The `useColorScheme` React hook provides and subscribes to color scheme updates from the [`Appearance`](appearance) module. The return value indicates the active color scheme. The value may be updated later, either through direct user action (e.g. theme selection in device settings or application-level selected user interface style via [`setColorScheme`](appearance#setcolorscheme)) or on a schedule (e.g. light and dark themes that follow the day/night cycle).
>>>>>>> new_en

<<<<<<< pt
### Esquemas de cores suportados
||||||| base_en
### Supported color schemes
=======
### Return values
>>>>>>> new_en

<<<<<<< pt
- `"light"`: O usuário prefere um tema de cor claro.
- `"dark"`: O usuário prefere um tema de cor escuro.
- `null`: O usuário não indicou um tema de cor preferido.
||||||| base_en
- `"light"`: The user prefers a light color theme.
- `"dark"`: The user prefers a dark color theme.
- `null`: The user has not indicated a preferred color theme.
=======
- `'light'`: The light color scheme is applied.
- `'dark'`: The dark color scheme is applied.
- `null`: May be returned if the native Appearance module is not available.
>>>>>>> new_en

---

## Exemplo

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

<<<<<<< pt
Você pode encontrar um exemplo completo que demonstra o uso deste hook junto com um contexto React para adicionar suporte a temas claro e escuro à sua aplicação em [`AppearanceExample.js`](https://github.com/facebook/react-native/blob/main/packages/rn-tester/js/examples/Appearance/AppearanceExample.js).
||||||| base_en
You can find a complete example that demonstrates the use of this hook alongside a React context to add support for light and dark themes to your application in [`AppearanceExample.js`](https://github.com/facebook/react-native/blob/main/packages/rn-tester/js/examples/Appearance/AppearanceExample.js).
=======
You can find a complete example that demonstrates the use of this hook alongside a React context to add support for light and dark themes to your application in [`AppearanceExample.js`](https://github.com/react/react-native/blob/main/packages/rn-tester/js/examples/Appearance/AppearanceExample.js).
>>>>>>> new_en
