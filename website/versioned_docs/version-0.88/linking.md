---
ia-translated: true
id: linking
title: Linking
---

import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; import constants from '@site/core/TabsConstants';

`Linking` fornece uma interface geral para interagir com links de aplicativos, tanto recebidos quanto enviados.

Todo Link (URL) possui um URL Scheme, alguns sites são prefixados com `https://` ou `http://` e o `http` é o URL Scheme. Vamos chamá-lo de scheme de forma resumida.

Além de `https`, você provavelmente também está familiarizado com o scheme `mailto`. Quando você abre um link com o scheme mailto, seu sistema operacional abrirá um aplicativo de e-mail instalado. Da mesma forma, existem schemes para fazer chamadas telefônicas e enviar SMS. Leia mais sobre [schemes de URL integrados](#built-in-url-schemes) abaixo.

Como ao usar o scheme mailto, é possível criar links para outros aplicativos usando schemes de URL personalizados. Por exemplo, quando você recebe um e-mail de **Magic Link** do Slack, o botão **Launch Slack** é uma âncora com um href que se parece com algo assim: `slack://secret/magic-login/other-secret`. Assim como com o Slack, você pode informar ao sistema operacional que deseja manipular um scheme personalizado. Quando o aplicativo Slack abre, ele recebe a URL que foi usada para abri-lo. Isso é frequentemente chamado de deep linking. Leia mais sobre como [obter o deep link](#get-the-deep-link) no seu aplicativo.

Um scheme de URL personalizado não é a única maneira de abrir seu aplicativo em dispositivos móveis. Por exemplo, se você quiser enviar um link por e-mail para alguém abrir no celular, usar um scheme de URL personalizado não é ideal porque o usuário pode abrir o e-mail em um desktop, onde o link não funcionaria. Em vez disso, você deve usar links `https` padrão, como `https://www.myapp.io/records/1234546`. Em dispositivos móveis, esses links podem ser configurados para abrir seu aplicativo. No Android, esse recurso é chamado de **Deep Links**, enquanto no iOS é conhecido como **Universal Links**.

### Esquemas de URL nativos {#built-in-url-schemes}

Conforme mencionado na introdução, existem alguns schemes de URL para funcionalidades principais que existem em todas as plataformas. A seguir está uma lista não exaustiva, mas que cobre os schemes mais comumente usados.

| Scheme           | Description                                              | iOS | Android |
| ---------------- | -------------------------------------------------------- | --- | ------- |
| `mailto`         | Abre o aplicativo de e-mail, ex: mailto: hello@world.dev | ✅  | ✅      |
| `tel`            | Abre o aplicativo de telefone, ex: tel:+123456789        | ✅  | ✅      |
| `sms`            | Abre o aplicativo de SMS, ex: sms:+123456789             | ✅  | ✅      |
| `https` / `http` | Abre o aplicativo do navegador web, ex: https://expo.dev | ✅  | ✅      |

### Habilitando deep links {#enabling-deep-links}

<div className="banner-native-code-required">
  <h3>Projetos somente com código nativo</h3>
  <p>A seção a seguir se aplica apenas a projetos com código nativo exposto. Se você estiver usando o fluxo gerenciado do Expo, veja o guia sobre <a href="https://docs.expo.dev/guides/linking/">Linking</a> na documentação do Expo para a alternativa adequada.</p>
</div>

Se você deseja habilitar deep links no seu aplicativo, leia o guia abaixo:

<Tabs groupId="syntax" queryString defaultValue={constants.defaultPlatform} values={constants.platforms}>
<TabItem value="android">

:::info
Para obter instruções sobre como adicionar suporte para deep linking no Android, consulte [Enabling Deep Links for App Content - Add Intent Filters for Your Deep Links](https://developer.android.com/training/app-indexing/deep-linking.html#adding-filters).
:::

Se você deseja receber o intent em uma instância existente da MainActivity, pode definir o `launchMode` da MainActivity como `singleTask` no `AndroidManifest.xml`. Consulte a documentação de [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element.html) para mais informações.

```xml
<activity
  android:name=".MainActivity"
  android:launchMode="singleTask">
```

</TabItem>
<TabItem value="ios">

No iOS, você precisará adicionar a pasta `LinkingIOS` aos seus caminhos de pesquisa de cabeçalho, conforme descrito na etapa 3 [aqui](linking-libraries-ios#step-3). Se você também quiser ouvir links de aplicativos recebidos durante a execução do seu aplicativo, encaminhe os deep links a partir do seu `SceneDelegate`. Se o seu aplicativo declara `UIApplicationSceneManifest` no `Info.plist`, o `RCTLinkingManager` ignora os métodos de linking do `AppDelegate` abaixo - você deve encaminhar os links a partir do `SceneDelegate`.

<Tabs groupId="ios-language" queryString defaultValue={constants.defaultAppleLanguage} values={constants.appleLanguages}>
<TabItem value="objc">

```objc title="SceneDelegate.m"
#import <React/RCTLinkingManager.h>

- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts
{
  [RCTLinkingManager scene:scene openURLContexts:URLContexts];
}
```

Se seu aplicativo estiver usando [Universal Links](https://developer.apple.com/ios/universal-links/), adicione também o seguinte:

```objc title="SceneDelegate.m"
- (void)scene:(UIScene *)scene continueUserActivity:(NSUserActivity *)userActivity
{
  [RCTLinkingManager scene:scene continueUserActivity:userActivity];
}
```

</TabItem>
<TabItem value="swift">

```swift title="SceneDelegate.swift"
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
  RCTLinkingManager.scene(scene, openURLContexts: URLContexts)
}
```

Se seu aplicativo estiver usando [Universal Links](https://developer.apple.com/ios/universal-links/), adicione também o seguinte:

```swift title="SceneDelegate.swift"
func scene(_ scene: UIScene, continue userActivity: NSUserActivity) {
  RCTLinkingManager.scene(scene, continue: userActivity)
}
```

</TabItem>
</Tabs>

Esses callbacks cobrem apenas os links que chegam enquanto a scene está conectada. Para tratar links em um cold start (o aplicativo sendo aberto por um scheme de URL personalizado ou por um Universal Link), você também precisa passar o `UIScene.ConnectionOptions` da scene para o React Native ao inicializá-lo; caso contrário, [`getInitialURL()`](#getinitialurl) resolve para `null`:

<Tabs groupId="ios-language" queryString defaultValue={constants.defaultAppleLanguage} values={constants.appleLanguages}>
<TabItem value="objc">

```objc title="SceneDelegate.m"
- (void)scene:(UIScene *)scene
    willConnectToSession:(UISceneSession *)session
                 options:(UISceneConnectionOptions *)connectionOptions
{
  // ...
  [self.reactNativeFactory startReactNativeWithModuleName:@"HelloWorld"
                                                 inWindow:self.window
                                        connectionOptions:connectionOptions];
}
```

</TabItem>
<TabItem value="swift">

```swift title="SceneDelegate.swift"
func scene(
  _ scene: UIScene,
  willConnectTo session: UISceneSession,
  options connectionOptions: UIScene.ConnectionOptions
) {
  // ...
  reactNativeFactory?.startReactNative(
    withModuleName: "HelloWorld",
    in: window,
    connectionOptions: connectionOptions
  )
}
```

</TabItem>
</Tabs>

Veja [Inicialização com SceneDelegate](integration-with-existing-apps#6-bootstrapping-with-scenedelegate) para a configuração completa do `SceneDelegate`.

<details>
<summary>Apps sem o ciclo de vida UIScene</summary>

Se seu aplicativo não usa `SceneDelegate`, adicione as seguintes linhas ao `AppDelegate`:

<Tabs groupId="ios-language" queryString defaultValue={constants.defaultAppleLanguage} values={constants.appleLanguages}>
<TabItem value="objc">

```objc title="AppDelegate.mm"
// iOS 9.x or newer
#import <React/RCTLinkingManager.h>

- (BOOL)application:(UIApplication *)application
   openURL:(NSURL *)url
   options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options
{
  return [RCTLinkingManager application:application openURL:url options:options];
}
```

Se seu aplicativo estiver usando [Universal Links](https://developer.apple.com/ios/universal-links/), você precisará adicionar o seguinte código também:

```objc title="AppDelegate.mm"
- (BOOL)application:(UIApplication *)application continueUserActivity:(nonnull NSUserActivity *)userActivity
 restorationHandler:(nonnull void (^)(NSArray<id<UIUserActivityRestoring>> * _Nullable))restorationHandler
{
 return [RCTLinkingManager application:application
                  continueUserActivity:userActivity
                    restorationHandler:restorationHandler];
}
```

</TabItem>
<TabItem value="swift">

```swift title="AppDelegate.swift"
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  return RCTLinkingManager.application(app, open: url, options: options)
}
```

Se seu aplicativo estiver usando [Universal Links](https://developer.apple.com/ios/universal-links/), você precisará adicionar o seguinte código também:

```swift title="AppDelegate.swift"
func application(
  _ application: UIApplication,
  continue userActivity: NSUserActivity,
  restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    return RCTLinkingManager.application(
      application,
      continue: userActivity,
      restorationHandler: restorationHandler
    )
  }
```

</TabItem>
</Tabs>

</details>

</TabItem>
</Tabs>

---

### Lidando com deep links {#handling-deep-links}

Existem duas maneiras de manipular URLs que abrem seu aplicativo.

#### 1. Se o app já estiver aberto, ele vai para o primeiro plano e um evento 'url' de Linking é disparado {#1-if-the-app-is-already-open-the-app-is-foregrounded-and-a-linking-url-event-is-fired}

Você pode manipular esses eventos com `Linking.addEventListener('url', callback)` - ele chama `callback({url})` com a URL vinculada

#### 2. Se o app não estiver aberto, ele é iniciado e a url é passada como initialURL {#2-if-the-app-is-not-already-open-it-is-opened-and-the-url-is-passed-in-as-the-initialurl}

Você pode manipular esses eventos com `Linking.getInitialURL()` - ele retorna uma Promise que resolve para a URL, se houver uma.

---

## Exemplo {#example}

### Abrir links e deep links (Universal Links) {#open-links-and-deep-links-universal-links}

<Tabs groupId="language" queryString defaultValue={constants.defaultSnackLanguage} values={constants.snackLanguages}>
<TabItem value="javascript">

```SnackPlayer name=Linking%20Example&supportedPlatforms=ios,android&ext=js
import {useCallback} from 'react';
import {Alert, Button, Linking, StyleSheet, View} from 'react-native';

const supportedURL = 'https://google.com';

const unsupportedURL = 'slack://open?team=123456';

const OpenURLButton = ({url, children}) => {
  const handlePress = useCallback(async () => {
    // Checking if the link is supported for links with custom URL scheme.
    const supported = await Linking.canOpenURL(url);

    if (supported) {
      // Opening the link with some app, if the URL scheme is "http" the web link should be opened
      // by some browser in the mobile
      await Linking.openURL(url);
    } else {
      Alert.alert(`Don't know how to open this URL: ${url}`);
    }
  }, [url]);

  return <Button title={children} onPress={handlePress} />;
};

const App = () => {
  return (
    <View style={styles.container}>
      <OpenURLButton url={supportedURL}>Open Supported URL</OpenURLButton>
      <OpenURLButton url={unsupportedURL}>Open Unsupported URL</OpenURLButton>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
```

</TabItem>
<TabItem value="typescript">

```SnackPlayer name=Linking%20Example&supportedPlatforms=ios,android&ext=tsx
import {useCallback} from 'react';
import {Alert, Button, Linking, StyleSheet, View} from 'react-native';

const supportedURL = 'https://google.com';

const unsupportedURL = 'slack://open?team=123456';

type OpenURLButtonProps = {
  url: string;
  children: string;
};

const OpenURLButton = ({url, children}: OpenURLButtonProps) => {
  const handlePress = useCallback(async () => {
    // Checking if the link is supported for links with custom URL scheme.
    const supported = await Linking.canOpenURL(url);

    if (supported) {
      // Opening the link with some app, if the URL scheme is "http" the web link should be opened
      // by some browser in the mobile
      await Linking.openURL(url);
    } else {
      Alert.alert(`Don't know how to open this URL: ${url}`);
    }
  }, [url]);

  return <Button title={children} onPress={handlePress} />;
};

const App = () => {
  return (
    <View style={styles.container}>
      <OpenURLButton url={supportedURL}>Open Supported URL</OpenURLButton>
      <OpenURLButton url={unsupportedURL}>Open Unsupported URL</OpenURLButton>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
```

</TabItem>
</Tabs>

### Abrir configurações personalizadas {#open-custom-settings}

<Tabs groupId="language" queryString defaultValue={constants.defaultSnackLanguage} values={constants.snackLanguages}>
<TabItem value="javascript">

```SnackPlayer name=Linking%20Example&supportedPlatforms=ios,android&ext=js
import {useCallback} from 'react';
import {Button, Linking, StyleSheet, View} from 'react-native';

const OpenSettingsButton = ({children}) => {
  const handlePress = useCallback(async () => {
    // Open the custom settings if the app has one
    await Linking.openSettings();
  }, []);

  return <Button title={children} onPress={handlePress} />;
};

const App = () => {
  return (
    <View style={styles.container}>
      <OpenSettingsButton>Open Settings</OpenSettingsButton>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
```

</TabItem>
<TabItem value="typescript">

```SnackPlayer name=Linking%20Example&supportedPlatforms=ios,android&ext=tsx
import {useCallback} from 'react';
import {Button, Linking, StyleSheet, View} from 'react-native';

type OpenSettingsButtonProps = {
  children: string;
};

const OpenSettingsButton = ({children}: OpenSettingsButtonProps) => {
  const handlePress = useCallback(async () => {
    // Open the custom settings if the app has one
    await Linking.openSettings();
  }, []);

  return <Button title={children} onPress={handlePress} />;
};

const App = () => {
  return (
    <View style={styles.container}>
      <OpenSettingsButton>Open Settings</OpenSettingsButton>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
```

</TabItem>
</Tabs>

### Obter o deep link {#get-the-deep-link}

<Tabs groupId="language" queryString defaultValue={constants.defaultSnackLanguage} values={constants.snackLanguages}>
<TabItem value="javascript">

```SnackPlayer name=Linking%20Example&supportedPlatforms=ios,android&ext=js
import {useState, useEffect} from 'react';
import {Linking, StyleSheet, Text, View} from 'react-native';

const useInitialURL = () => {
  const [url, setUrl] = useState(null);
  const [processing, setProcessing] = useState(true);

  useEffect(() => {
    const getUrlAsync = async () => {
      // Get the deep link used to open the app
      const initialUrl = await Linking.getInitialURL();

      // The setTimeout is just for testing purpose
      setTimeout(() => {
        setUrl(initialUrl ?? null);
        setProcessing(false);
      }, 1000);
    };

    getUrlAsync();
  }, []);

  return {url, processing};
};

const App = () => {
  const {url: initialUrl, processing} = useInitialURL();

  return (
    <View style={styles.container}>
      <Text>
        {processing
          ? 'Processing the initial url from a deep link'
          : `The deep link is: ${initialUrl || 'None'}`}
      </Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
```

</TabItem>
<TabItem value="typescript">

```SnackPlayer name=Linking%20Example&supportedPlatforms=ios,android&ext=tsx
import {useState, useEffect} from 'react';
import {Linking, StyleSheet, Text, View} from 'react-native';

const useInitialURL = () => {
  const [url, setUrl] = useState<string | null>(null);
  const [processing, setProcessing] = useState(true);

  useEffect(() => {
    const getUrlAsync = async () => {
      // Get the deep link used to open the app
      const initialUrl = await Linking.getInitialURL();

      // The setTimeout is just for testing purpose
      setTimeout(() => {
        setUrl(initialUrl ?? null);
        setProcessing(false);
      }, 1000);
    };

    getUrlAsync();
  }, []);

  return {url, processing};
};

const App = () => {
  const {url: initialUrl, processing} = useInitialURL();

  return (
    <View style={styles.container}>
      <Text>
        {processing
          ? 'Processing the initial url from a deep link'
          : `The deep link is: ${initialUrl || 'None'}`}
      </Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
```

</TabItem>
</Tabs>

### Enviar intents (Android) {#send-intents-android}

<Tabs groupId="language" queryString defaultValue={constants.defaultSnackLanguage} values={constants.snackLanguages}>
<TabItem value="javascript">

```SnackPlayer name=Linking%20Example&supportedPlatforms=android&ext=js
import {useCallback} from 'react';
import {Alert, Button, Linking, StyleSheet, View} from 'react-native';

const SendIntentButton = ({action, extras, children}) => {
  const handlePress = useCallback(async () => {
    try {
      await Linking.sendIntent(action, extras);
    } catch (e) {
      Alert.alert(e.message);
    }
  }, [action, extras]);

  return <Button title={children} onPress={handlePress} />;
};

const App = () => {
  return (
    <View style={styles.container}>
      <SendIntentButton action="android.intent.action.POWER_USAGE_SUMMARY">
        Power Usage Summary
      </SendIntentButton>
      <SendIntentButton
        action="android.settings.APP_NOTIFICATION_SETTINGS"
        extras={[
          {
            key: 'android.provider.extra.APP_PACKAGE',
            value: 'com.facebook.katana',
          },
        ]}>
        App Notification Settings
      </SendIntentButton>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
```

</TabItem>
<TabItem value="typescript">

```SnackPlayer name=Linking%20Example&ext=tsx
import {useCallback} from 'react';
import {Alert, Button, Linking, StyleSheet, View} from 'react-native';

type SendIntentButtonProps = {
  action: string;
  children: string;
  extras?: Array<{
    key: string;
    value: string | number | boolean;
  }>;
};

const SendIntentButton = ({
  action,
  extras,
  children,
}: SendIntentButtonProps) => {
  const handlePress = useCallback(async () => {
    try {
      await Linking.sendIntent(action, extras);
    } catch (e: any) {
      Alert.alert(e.message);
    }
  }, [action, extras]);

  return <Button title={children} onPress={handlePress} />;
};

const App = () => {
  return (
    <View style={styles.container}>
      <SendIntentButton action="android.intent.action.POWER_USAGE_SUMMARY">
        Power Usage Summary
      </SendIntentButton>
      <SendIntentButton
        action="android.settings.APP_NOTIFICATION_SETTINGS"
        extras={[
          {
            key: 'android.provider.extra.APP_PACKAGE',
            value: 'com.facebook.katana',
          },
        ]}>
        App Notification Settings
      </SendIntentButton>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
```

</TabItem>
</Tabs>

# Referência {#reference}

## Métodos {#methods}

### `addEventListener()`

```tsx
static addEventListener(
  type: 'url',
  handler: (event: {url: string}) => void,
): EventSubscription;
```

Adiciona um manipulador para mudanças de Linking ouvindo o tipo de evento `url` e fornecendo o manipulador.

---

### `canOpenURL()`

```tsx
static canOpenURL(url: string): Promise<boolean>;
```

Determina se um aplicativo instalado pode ou não manipular uma determinada URL.

O método retorna um objeto `Promise`. Quando é determinado se a URL fornecida pode ou não ser manipulada, a promise é resolvida e o primeiro parâmetro indica se ela pode ou não ser aberta.

A `Promise` será rejeitada no Android se for impossível verificar se a URL pode ser aberta ou quando estiver visando o Android 11 (SDK 30) se você não especificou as consultas de intent relevantes no `AndroidManifest.xml`. Da mesma forma, no iOS, a promise será rejeitada se você não adicionou o scheme específico na chave `LSApplicationQueriesSchemes` dentro do `Info.plist` (veja abaixo).

**Parâmetros:**

| Name                                                     | Type   | Description       |
| -------------------------------------------------------- | ------ | ----------------- |
| url <div className="label basic required">Required</div> | string | A URL para abrir. |

:::note
Para URLs web, o protocolo (`"http://"`, `"https://"`) deve ser definido de acordo!
:::

:::warning
Este método tem limitações no iOS 9+. Da [documentação oficial da Apple](https://developer.apple.com/documentation/uikit/uiapplication/1622952-canopenurl):

- Se seu aplicativo está vinculado a uma versão anterior do iOS, mas está sendo executado no iOS 9.0 ou posterior, você pode chamar este método até 50 vezes. Após atingir esse limite, chamadas subsequentes sempre resolverão para `false`. Se o usuário reinstalar ou atualizar o aplicativo, o iOS redefine o limite.
- A partir do iOS 9, seu aplicativo também precisa fornecer a chave `LSApplicationQueriesSchemes` dentro do `Info.plist` ou `canOpenURL()` sempre resolverá para `false`.
  :::

:::info
Ao visar o Android 11 (SDK 30), você deve especificar os intents para os schemes que deseja manipular no `AndroidManifest.xml`. Uma lista de intents comuns pode ser encontrada [aqui](https://developer.android.com/guide/components/intents-common).

Por exemplo, para manipular schemes `https`, o seguinte precisa ser adicionado ao seu manifest:

```
<manifest ...>
  <queries>
    <intent>
      <action android:name="android.intent.action.VIEW" />
      <data android:scheme="https"/>
    </intent>
  </queries>
</manifest>
```

:::

---

### `getInitialURL()`

```tsx
static getInitialURL(): Promise<string | null>;
```

Se o lançamento do aplicativo foi acionado por um link de aplicativo, ele fornecerá a URL do link, caso contrário, fornecerá `null`.

:::info
Para dar suporte a deep linking no Android, consulte https://developer.android.com/training/app-indexing/deep-linking.html#handling-intents.
:::

:::tip
`getInitialURL` pode retornar `null` quando a Depuração Remota de JS está ativa. Desative o depurador para garantir que seja passada.
:::

---

### `openSettings()`

```tsx
static openSettings(): Promise<void>;
```

Abre o aplicativo Settings e exibe as configurações personalizadas do aplicativo, se houver alguma.

---

### `openURL()`

```tsx
static openURL(url: string): Promise<any>;
```

Tenta abrir a `url` fornecida com qualquer um dos aplicativos instalados.

Você pode usar outras URLs, como uma localização (por exemplo, "geo:37.484847,-122.148386" no Android ou "https://maps.apple.com/?ll=37.484847,-122.148386" no iOS), um contato ou qualquer outra URL que possa ser aberta com os aplicativos instalados.

O método retorna um objeto `Promise`. Se o usuário confirmar a caixa de diálogo de abertura ou a URL abrir automaticamente, a promise é resolvida. Se o usuário cancelar a caixa de diálogo de abertura ou não houver aplicativos registrados para a URL, a promise é rejeitada.

**Parâmetros:**

| Name                                                     | Type   | Description       |
| -------------------------------------------------------- | ------ | ----------------- |
| url <div className="label basic required">Required</div> | string | A URL para abrir. |

:::note
Este método falhará se o sistema não souber como abrir a URL especificada. Se você estiver passando uma URL que não seja http(s), é melhor verificar `canOpenURL()` primeiro. Para URLs web, o protocolo (`"http://"`, `"https://"`) deve ser definido de acordo!
:::

:::warning
Este método pode se comportar de maneira diferente em um simulador, por exemplo, links `"tel:"` não podem ser manipulados no simulador iOS, pois não há acesso ao aplicativo de discagem.
:::

---

### `sendIntent()` <div className="label android">Android</div>

```tsx
static sendIntent(
  action: string,
  extras?: Array<{key: string; value: string | number | boolean}>,
): Promise<void>;
```

Inicia um intent do Android com extras.

**Parâmetros:**

| Name                                                        | Type                                                       |
| ----------------------------------------------------------- | ---------------------------------------------------------- |
| action <div className="label basic required">Required</div> | string                                                     |
| extras                                                      | `Array<{key: string, value: string ｜ number ｜ boolean}>` |
