---
ia-translated: true
id: debugging-native-code
title: Depuração de Código Nativo
---

import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; import constants from '@site/core/TabsConstants';

<div className="banner-native-code-required">
  <h3>Apenas Projetos com Código Nativo</h3>
  <p>A seção a seguir se aplica apenas a projetos com código nativo exposto. Se você está usando o fluxo de trabalho gerenciado do Expo, consulte o guia sobre <a href="https://docs.expo.dev/workflow/prebuild/" target="_blank">prebuild</a> para usar esta API.</p>
</div>

## Acessando Logs

Você pode exibir os logs nativos de um aplicativo iOS ou Android usando os seguintes comandos em um terminal enquanto o aplicativo estiver em execução:

```shell
# For Android:
npx react-native log-android
# Or, for iOS:
npx react-native log-ios
```

Você também pode acessá-los através de Debug > Open System Log… no iOS Simulator ou executando `adb logcat "*:S" ReactNative:V ReactNativeJS:V` em um terminal enquanto um aplicativo Android estiver em execução em um dispositivo ou emulador.

<details>
<summary>**💡 Logs Nativos Personalizados**</summary>

Se você está escrevendo um Native Module e deseja adicionar logs personalizados ao seu módulo para fins de depuração, você pode usar o seguinte método:

#### Android (Java/Kotlin)

Em seu módulo nativo, use a classe `Log` para adicionar logs que podem ser visualizados no Logcat:

```java
import android.util.Log;

private void log(String message) {
    Log.d("YourModuleName", message);
}
```

Para visualizar esses logs no Logcat, use este comando, substituindo `YourModuleName` pela sua tag personalizada:

```shell
adb logcat "*:S" ReactNative:V ReactNativeJS:V YourModuleName:D
```

#### iOS (Objective-C/Swift)

Em seu módulo nativo, use `NSLog` para logs personalizados:

```objectivec
NSLog(@"YourModuleName: %@", message);
```

Ou, em Swift:

```swift
print("YourModuleName: \(message)")
```

Esses logs aparecerão no console do Xcode ao executar o aplicativo.

</details>

## Depuração em uma IDE Nativa

Ao trabalhar com código nativo, como ao escrever Native Modules, você pode iniciar o aplicativo a partir do Android Studio ou Xcode e aproveitar os recursos de depuração nativos (configuração de breakpoints, etc.) como você faria ao construir um aplicativo nativo padrão.

Outra opção é executar seu aplicativo usando o React Native CLI e anexar o debugger nativo da IDE nativa (Android Studio ou Xcode) ao processo.

### Android Studio

No Android Studio, você pode fazer isso indo na opção "Run" na barra de menu, clicando em "Attach to Process..." e selecionando o aplicativo React Native em execução.

### Xcode

No Xcode, clique em "Debug" na barra de menu superior, selecione a opção "Attach to process" e selecione o aplicativo na lista de "Likely Targets".
