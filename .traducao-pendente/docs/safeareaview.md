---
id: safeareaview
title: '🗑️ SafeAreaView'
ia-translated: true
---

<<<<<<< pt
:::warning Descontinuado
Use [react-native-safe-area-context](https://github.com/AppAndFlow/react-native-safe-area-context) em vez disso.
||||||| base_en
:::warning Deprecated
Use [react-native-safe-area-context](https://github.com/AppAndFlow/react-native-safe-area-context) instead.
=======
:::warning[Deprecated]
Use [react-native-safe-area-context](https://github.com/AppAndFlow/react-native-safe-area-context) instead.
>>>>>>> new_en
:::

O propósito do `SafeAreaView` é renderizar conteúdo dentro dos limites da área segura de um dispositivo. Atualmente, é aplicável apenas para dispositivos iOS com versão iOS 11 ou posterior.

`SafeAreaView` renderiza conteúdo aninhado e aplica automaticamente padding para refletir a porção da view que não é coberta por barras de navegação, barras de abas, barras de ferramentas e outras views ancestrais. Além disso, e mais importante, os paddings da Safe Area refletem a limitação física da tela, como cantos arredondados ou entalhes da câmera (ou seja, a área de alojamento do sensor no iPhone 13).

## Exemplo

Para usar, envolva sua view de nível superior com um `SafeAreaView` com um estilo `flex: 1` aplicado a ele. Você também pode querer usar uma cor de fundo que combine com o design da sua aplicação.

```SnackPlayer name=SafeAreaView&supportedPlatforms=ios
import {StyleSheet, Text, SafeAreaView} from 'react-native';

const App = () => {
  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.text}>Page content</Text>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  text: {
    fontSize: 25,
    fontWeight: '500',
  },
});

export default App;
```

---

# Referência

## Props

### [View Props](view.md#props)

Herda [View Props](view.md#props).

:::note
<<<<<<< pt
Como padding é usado para implementar o comportamento do componente, regras de padding em estilos aplicados a um `SafeAreaView` serão ignoradas e podem causar resultados diferentes dependendo da plataforma. Veja [#22211](https://github.com/facebook/react-native/issues/22211) para detalhes.
||||||| base_en
As padding is used to implement the behavior of the component, padding rules in styles applied to a `SafeAreaView` will be ignored and can cause different results depending on the platform. See [#22211](https://github.com/facebook/react-native/issues/22211) for details.
=======
As padding is used to implement the behavior of the component, padding rules in styles applied to a `SafeAreaView` will be ignored and can cause different results depending on the platform. See [#22211](https://github.com/react/react-native/issues/22211) for details.
>>>>>>> new_en
:::
