---
id: release-levels
title: Níveis de release
ia-translated: true
---

import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; import constants from '@site/core/TabsConstants';

O React Native oferece à comunidade a possibilidade de adotar novos recursos individualmente assim que o design e a implementação estiverem quase completos, mesmo antes de eles serem incluídos em uma versão estável. Essa abordagem é conhecida como **níveis de release**.

Você pode configurar o nível de release do React Native para que sua instância do React Native inicialize com as Feature Flags definidas nos modos `EXPERIMENTAL`, `CANARY` ou `STABLE`.

:::note
Essa abordagem é semelhante aos [releases Canary e Experimental do React](https://react.dev/blog/2023/05/03/react-canaries), mas com uma diferença importante: independentemente do nível de release, o mesmo código do React JS e do React Native é usado.  
O React Native também não usa as tags NPM `@canary` ou `@experimental`, já que os níveis de release estão disponíveis tanto para releases estáveis quanto para nightly do React Native.
:::

Além disso, definir o nível de release como `EXPERIMENTAL` ou `CANARY` **não** resulta no consumo de `react@nightly` ou `react@canary`, por causa da forma como o react-native consome a versão do React ([você pode ler mais sobre isso aqui](https://github.com/react/react-native/blob/main/packages/react-native/Libraries/Renderer/README.md#react--react-native-versions)).

## Quando usar cada nível de release {#when-to-use-each-release-level}

- **`STABLE`**:
  - Use para todos os apps e bibliotecas de produção que não precisam de acesso antecipado a recursos ainda não lançados.
  - Este é o nível padrão para releases estáveis e nightly.
- **`CANARY`:**
  - Use se você é autor de framework, desenvolvedor avançado de apps, ou precisa testar ou adotar novos recursos antes de eles serem lançados na versão estável.
  - Não recomendado para produção ou apps voltados ao usuário.
- **`EXPERIMENTAL`:**
  - Use apenas para testes e para dar feedback sobre novos recursos nos estágios iniciais de desenvolvimento
  - Não recomendado para produção ou apps voltados ao usuário.

## Como inicializar o React Native usando Canary e Experimental {#how-to-initialize-react-native-using-canary--experimental}

### Android

A classe `DefaultNewArchitectureEntryPoint` agora tem uma propriedade `releaseLevel` (padrão: `STABLE`).  
O sistema de feature flags usa essa propriedade para selecionar o conjunto apropriado de feature flags para o nível de release escolhido.

```kotlin title="Exemplo de uso"
DefaultNewArchitectureEntryPoint.releaseLevel = ReleaseLevel.CANARY
DefaultNewArchitectureEntryPoint.load()
```

O sistema de build gera classes de override de feature flags diferentes para cada nível de release, garantindo que os recursos corretos sejam habilitados em cada estágio.

### iOS

A classe `RCTReactNativeFactory` agora tem um inicializador que aceita um parâmetro `releaseLevel`. A configuração das feature flags usa esse parâmetro para selecionar os overrides corretos. Crie a factory a partir do seu `SceneDelegate` (ou do `AppDelegate`, se você não usa o ciclo de vida UIScene).

<Tabs groupId="ios-language" queryString defaultValue={constants.defaultAppleLanguage} values={constants.appleLanguages}>
<TabItem value="objc">

```objc title="SceneDelegate.m"
self.reactNativeFactory = [[RCTReactNativeFactory alloc] initWithDelegate:self releaseLevel:Canary];
```

</TabItem>
<TabItem value="swift">

```swift title="SceneDelegate.swift"
reactNativeFactory = RCTReactNativeFactory(delegate: self, releaseLevel: RCTReleaseLevel.Canary)
```

</TabItem>
</Tabs>

<details>
<summary>Apps sem o ciclo de vida UIScene</summary>

<Tabs groupId="ios-language" queryString defaultValue={constants.defaultAppleLanguage} values={constants.appleLanguages}>
<TabItem value="objc">

```objc title="AppDelegate.mm"
[[RCTReactNativeFactory alloc] initWithDelegate:delegate releaseLevel:Canary];
```

</TabItem>
<TabItem value="swift">

```swift title="AppDelegate.swift"
let factory = RCTReactNativeFactory(delegate: delegate, releaseLevel: RCTReleaseLevel.Canary)
```

</TabItem>
</Tabs>

</details>

O sistema garante que apenas um nível de release esteja ativo por instância do app, e vai dar crash se várias factories forem criadas com níveis de release diferentes.
