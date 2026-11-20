---
ia-translated: true
id: strict-typescript-api
title: Strict TypeScript API
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import RNRepoLink from '@site/core/RNRepoLink';

<<<<<<< pt
A Strict TypeScript API é uma prévia da nossa futura API JavaScript estável para React Native.
||||||| base_en
The Strict TypeScript API is a preview of our future, stable JavaScript API for React Native.
=======
:::info[New in 0.87]
>>>>>>> new_en

<<<<<<< pt
Especificamente, este é um novo conjunto de tipos TypeScript para o pacote npm `react-native`, disponível a partir da versão 0.80. Eles fornecem maior precisão de tipos e maior prova de futuro, e nos permitirão evoluir com confiança a API do React Native para uma forma estável. Optar pela Strict TypeScript API traz algumas diferenças estruturais de tipos e, portanto, é uma mudança breaking de uma só vez.
||||||| base_en
Specifically, this is a new set of TypeScript types for the `react-native` npm package, available from 0.80 onwards. These provide stronger and more futureproof type accuracy, and will allow us to confidently evolve React Native's API into a stable shape. Opting in to the Strict TypeScript API brings some structural type differences, and is therefore a one-time breaking change.
=======
**The Strict API is now enabled by default** (previously an opt-in from 0.80+). This is a **breaking change**, detailed in the guide below.
>>>>>>> new_en

<<<<<<< pt
Os novos tipos são:
||||||| base_en
The new types are:
=======
:::
>>>>>>> new_en

<<<<<<< pt
1. **Gerados diretamente do nosso código-fonte** — melhorando a cobertura e correção, para que você possa esperar garantias de compatibilidade mais fortes.
2. **Restritos ao arquivo index do `react-native`** — definindo mais rigorosamente nossa API pública, e significando que não quebraremos a API ao fazer mudanças internas nos arquivos.
||||||| base_en
1. **Generated directly from our source code** — improving coverage and correctness, so you can expect stronger compatibility guarantees.
2. **Restricted to `react-native`'s index file** — more tightly defining our public API, and meaning we won't break the API when making internal file changes.
=======
The Strict TypeScript API is React Native's modern TypeScript API, replacing the previous hand-maintained TypeScript definitions from earlier versions.
>>>>>>> new_en

<<<<<<< pt
Quando a comunidade estiver pronta, a Strict TypeScript API se tornará nossa API padrão no futuro — sincronizada com a remoção de deep imports.
||||||| base_en
When the community is ready, the Strict TypeScript API will become our default API in future — synchronized with deep imports removal.
=======
### Key changes (breaking)
>>>>>>> new_en

1. **No deep imports.** The API is restricted to `react-native`'s index file. This is a tighter and more intentional public API contract. It also ensures that internal file path changes in React Native's source code won't be breaking.
2. **Generated directly from source.** Previously, React Native used separately maintained manual types. Generating from source now means we improve coverage, correctness, and compatibility guarantees.

<<<<<<< pt
Estamos fornecendo esses novos tipos ao lado de nossos tipos existentes, o que significa que você pode escolher migrar quando estiver pronto. Encorajamos early adopters e aplicativos recém-criados a optar através do seu arquivo `tsconfig.json`.
||||||| base_en
We're shipping these new types alongside our existing types, meaning you can choose to migrate when ready. We encourage early adopters and newly created apps to opt in via your `tsconfig.json` file.
=======
### Opting out <div className="label primary">Since 0.87</div>
>>>>>>> new_en

<<<<<<< pt
Optar é uma **breaking change**, já que alguns de nossos novos tipos têm nomes e formas atualizados, embora muitos aplicativos não sejam afetados. Você pode aprender sobre cada breaking change na próxima seção.
||||||| base_en
Opting in is a **breaking change**, since some of our new types have updated names and shapes, although many apps won't be affected. You can learn about each breaking change in the next section.
=======
The Strict API is a **breaking change**, and not all apps and libraries may be able to migrate immediately.
>>>>>>> new_en

We continue to ship our previous manual types, which can be reverted to via your `tsconfig.json` config. Please note that in a future release we will remove this opt out.

```diff title="tsconfig.json"
  {
    "extends": "@react-native/typescript-config",
    "compilerOptions": {
      ...
+     "customConditions": ["react-native", "react-native-legacy-deep-imports"]
    }
  }
```

:::info[Issues / Feedback?]

<<<<<<< pt
Isso instruirá o TypeScript a resolver os tipos do `react-native` a partir do nosso novo diretório [`types_generated/`](https://www.npmjs.com/package/react-native?activeTab=code), em vez do diretório anterior [`types/`](https://www.npmjs.com/package/react-native?activeTab=code) (mantido manualmente). Nenhum restart do TypeScript ou do seu editor é necessário.
||||||| base_en
This will instruct TypeScript to resolve `react-native` types from our new [`types_generated/`](https://www.npmjs.com/package/react-native?activeTab=code) dir, instead of the previous [`types/`](https://www.npmjs.com/package/react-native?activeTab=code) dir (manually maintained). No restart of TypeScript or your editor is required.
=======
The 0.87 rollout of the Strict API by default is an ecosystem-wide change, and one we need to make in order to have stable API guarantees for React Native in future.

Design choices about which APIs are exported at root, and intentional updates to type names/shapes have been worked on with the community and partners since the original 0.80 preview.

We believe we've ironed out all rough edges, but there may still be edge cases. If you're choosing to opt out of the Strict API in 0.87 or later, we'd love to know why: [**discussion thread**](https://github.com/react-native-community/discussions-and-proposals/discussions/1015).
>>>>>>> new_en

:::

<<<<<<< pt
A Strict TypeScript API segue nossa [RFC](https://github.com/react-native-community/discussions-and-proposals/pull/894) para remover deep imports do React Native. Portanto, algumas APIs não são mais exportadas na raiz. Isso é intencional, para reduzir a superfície geral da API do React Native.
||||||| base_en
The Strict TypeScript API follows our [RFC](https://github.com/react-native-community/discussions-and-proposals/pull/894) to remove deep imports from React Native. Therefore, some APIs are no longer exported at root. This is intentional, in order to reduce the overall surface area of React Native's API.
=======
---

## Migration guide
>>>>>>> new_en

:::tip

<<<<<<< pt
**Enviando feedback**: Trabalharemos com a comunidade para finalizar quais APIs exportamos ao longo de (pelo menos) as próximas duas versões do React Native. Por favor, compartilhe seu feedback em nossa [feedback thread](https://github.com/react-native-community/discussions-and-proposals/discussions/893).
||||||| base_en
**Sending feedback**: We will be working with the community to finalize which APIs we export over (at least) the next two React Native releases. Please share your feedback in our [feedback thread](https://github.com/react-native-community/discussions-and-proposals/discussions/893).
=======
Use the [**/migrate-to-strict-api**](https://www.skills.sh/react-native-community/skills/migrate-to-strict-api) skill to migrate your codebase via an agent.
>>>>>>> new_en

<<<<<<< pt
Veja também nossa [announcement blog post](/blog/2025/06/12/moving-towards-a-stable-javascript-api) para mais informações sobre nossa motivação e cronogramas.
||||||| base_en
See also our [announcement blog post](/blog/2025/06/12/moving-towards-a-stable-javascript-api) for more info on our motivation and timelines.
=======
```sh
npx skills add react-native-community/skills --skill migrate-to-strict-api
```
>>>>>>> new_en

:::

### Before you start

Enabling the Strict API — by upgrading to 0.87, or by opting in on an earlier release — affects TypeScript analysis of your own project only, scoped by its `tsconfig.json`.

In most cases, codebases can migrate independently — app developers don't need to wait for specific dependencies to opt in, and library authors don't need to wait for their users.

#### Keep `skipLibCheck` enabled

The above depends on `skipLibCheck`, which `@react-native/typescript-config` enables by default. This keeps errors originating inside third-party `.d.ts` files out of your results. If your project overrides it, turn it back on before you start — otherwise you will see errors in dependencies that you can't fix.

#### Update your dependencies

Occasionally, your dependencies can have rough edges under the Strict API. Whenever type errors involve a library, check for and update to a fixed release first.

One specific rough edge: Some libraries ship raw TypeScript source that your project imports, e.g. Jest setup files. These are typechecked as part of your project. Popular libraries have already repackaged these entry points:

- `@expensify/react-native-live-markdown` — fixed in [0.1.335](https://github.com/Expensify/react-native-live-markdown/pull/771)
- `react-native-safe-area-context` — fixed in [5.8.1](https://github.com/AppAndFlow/react-native-safe-area-context/pull/745)

<details>
<summary>**Advanced: Excluding an incompatible library**</summary>

If an incompatible library is producing errors under `node_modules` (typically `TS2307: Cannot find module 'react-native/Libraries/...'`), you can exclude it from TypeScript analysis as a local fix, by redirecting the imported subpath to an untyped stub:

```json title="tsconfig.json"
{
  "compilerOptions": {
    "paths": {
      "some-library/jest/mock": ["./untyped-module.d.ts"]
    }
  }
}
```

```ts title="untyped-module.d.ts"
declare const anyExport: unknown;
export default anyExport;
```

Please also report the incompatibility to the library — the fixes linked above are a good template.

</details>

### New `CodegenTypes` namespace

Tipos usados para codegen, como `Int32`, `Double`, `WithDefault`, etc., agora estão disponíveis sob um único namespace `CodegenTypes`. Da mesma forma, `codegenNativeComponent` e `codegenNativeCommands` agora estão disponíveis para importar do pacote react-native em vez de usar o deep import.

O `CodegenTypes` com namespace, bem como `codegenNativeCommands` e `codegenNativeComponent`, também estão disponíveis no pacote `react-native` quando a Strict API não está habilitada para facilitar a adoção para bibliotecas de terceiros.

#### Migration

<Tabs defaultValue="after">
<TabItem value="before" label="Before">

```ts title=""
import codegenNativeComponent from 'react-native/Libraries/Utilities/codegenNativeComponent';
import type {
  Int32,
  WithDefault,
} from 'react-native/Libraries/Types/CodegenTypes';

interface NativeProps extends ViewProps {
  enabled?: WithDefault<boolean, true>;
  size?: Int32;
}

export default codegenNativeComponent<NativeProps>(
  'RNCustomComponent',
);
```

</TabItem>
<TabItem value="after" label="After">

```ts title=""
import {CodegenTypes, codegenNativeComponent} from 'react-native';

interface NativeProps extends ViewProps {
  enabled?: CodegenTypes.WithDefault<boolean, true>;
  size?: CodegenTypes.Int32;
}

export default codegenNativeComponent<NativeProps>(
  'RNCustomComponent',
);
```

</TabItem>
</Tabs>

### Refs now use `*Instance` types <div className="label primary">Since 0.87</div>

Each built-in component now has a dedicated `*Instance` type for use with refs — for example, `ViewInstance`, `TextInputInstance`, `ScrollViewInstance`. These are the **recommended way to type refs** under the Strict TypeScript API.

Previously, `useRef<View>` worked because `View` and other components were typed as a class. Under the Strict API, built-in components are typed as functions, so `View` refers to the function itself — **component type names no longer work as ref types**.

<Tabs defaultValue="after">
<TabItem value="before" label="Before">

```tsx title=""
import {useRef} from 'react';
import {View, TextInput} from 'react-native';

function MyComponent() {
  const viewRef = useRef<View>(null);
  const inputRef = useRef<TextInput>(null);

  return (
    <>
      <View ref={viewRef} />
      <TextInput ref={inputRef} />
    </>
  );
}
```

</TabItem>
<TabItem value="after" label="After">

```tsx title=""
import {useRef} from 'react';
import type {
  TextInput,
  TextInputInstance,
  View,
  ViewInstance,
} from 'react-native';

function MyComponent() {
  const viewRef = useRef<ViewInstance>(null);
  const inputRef = useRef<TextInputInstance>(null);

  return (
    <>
      <View ref={viewRef} />
      <TextInput ref={inputRef} />
    </>
  );
}
```

</TabItem>
</Tabs>

`*Instance` types also work transparently with `Animated` variants — no separate type is needed:

```tsx title=""
const viewRef = useRef<ViewInstance>(null);

<View ref={viewRef} />
<Animated.View ref={viewRef} />
```

This also replaces the removed `Animated.LegacyRef` type. Code using `ref={ref as React.Ref<Animated.LegacyRef<View>>}` can be simplified to `ref={ref}` with a `ViewInstance`-typed ref.

<details>
<summary>**Available instance types**</summary>

| Component                 | Instance type                     |
| ------------------------- | --------------------------------- |
| `ActivityIndicator`       | `ActivityIndicatorInstance`       |
| `Button`                  | `ButtonInstance`                  |
| `DrawerLayoutAndroid`     | `DrawerLayoutAndroidInstance`     |
| `FlatList`                | `FlatListInstance`                |
| `Image`                   | `ImageInstance`                   |
| `ImageBackground`         | `ImageBackgroundInstance`         |
| `KeyboardAvoidingView`    | `KeyboardAvoidingViewInstance`    |
| `Modal`                   | `ModalInstance`                   |
| `Pressable`               | `PressableInstance`               |
| `ProgressBarAndroid`      | `ProgressBarAndroidInstance`      |
| `RefreshControl`          | `RefreshControlInstance`          |
| `SafeAreaView`            | `SafeAreaViewInstance`            |
| `ScrollView`              | `ScrollViewInstance`              |
| `SectionList`             | `SectionListInstance`             |
| `StatusBar`               | `StatusBarInstance`               |
| `Switch`                  | `SwitchInstance`                  |
| `Text`                    | `TextInstance`                    |
| `TextInput`               | `TextInputInstance`               |
| `TouchableHighlight`      | `TouchableHighlightInstance`      |
| `TouchableNativeFeedback` | `TouchableNativeFeedbackInstance` |
| `TouchableOpacity`        | `TouchableOpacityInstance`        |
| `View`                    | `ViewInstance`                    |
| `VirtualizedList`         | `VirtualizedListInstance`         |
| `VirtualizedSectionList`  | `VirtualizedSectionListInstance`  |

Components without ref support (`InputAccessoryView`, `TouchableWithoutFeedback`, `experimental_LayoutConformance`) do not have instance types.

</details>

**Migration**

| Before                                                  | After                        |
| ------------------------------------------------------- | ---------------------------- |
| `useRef<View>(null)`                                    | `useRef<ViewInstance>(null)` |
| `useRef<React.ComponentRef<typeof View>>(null)`         | `useRef<ViewInstance>(null)` |
| `useRef<HostInstance>(null)` (for a specific component) | `useRef<ViewInstance>(null)` |
| `Ref<Animated.LegacyRef<View>>`                         | `Ref<ViewInstance>`          |

:::note

`React.ComponentRef<typeof View>` remains valid and produces the same type as `ViewInstance`. The `*Instance` types are convenient aliases — both approaches work.

:::

### Removal of `*Static` types

#### Migration

<Tabs defaultValue="after">
<TabItem value="before" label="Before">

```tsx title=""
import {Linking, LinkingStatic} from 'react-native';

function foo(linking: LinkingStatic) {}
foo(Linking);
```

</TabItem>
<TabItem value="after" label="After">

```tsx title=""
import {Linking} from 'react-native';

function foo(linking: Linking) {}
foo(Linking);
```

<<<<<<< pt
As seguintes APIs eram anteriormente nomeadas como `*Static` mais uma declaração de variável desse tipo. Na maioria dos casos havia um alias para que o valor e o tipo fossem exportados sob o mesmo identificador, mas alguns estavam faltando.
||||||| base_en
The following APIs were previously named as `*Static` plus a variable declaration of said type. In most cases there was an alias so that value and the type were exported under the same identifier, but some were missing.
=======
</TabItem>
</Tabs>
>>>>>>> new_en

<<<<<<< pt
(Por exemplo, havia um tipo `AlertStatic`, variável `Alert` do tipo `AlertStatic` e tipo `Alert` que era um alias para `AlertStatic`. Mas no caso de `PixelRatio` havia um tipo `PixelRatioStatic` e uma variável `PixelRatio` desse tipo sem aliases de tipo adicionais.)
||||||| base_en
(For example there was an `AlertStatic` type, `Alert` variable of type `AlertStatic` and type `Alert` which was an alias for `AlertStatic`. But in the case of `PixelRatio` there was a `PixelRatioStatic` type and a `PixelRatio` variable of that type without additional type aliases.)
=======
The following APIs were previously named as `*Static` plus a variable declaration of said type. In most cases there was an alias so that value and the type were exported under the same identifier, but some were missing.
>>>>>>> new_en

<details>
<summary>**Affected APIs**</summary>

- `AlertStatic`
- `ActionSheetIOSStatic`
- `ToastAndroidStatic`
- `InteractionManagerStatic` (In this case there was no relevant `InteractionManager` type alias)
- `UIManagerStatic`
- `PlatformStatic`
- `SectionListStatic`
- `PixelRatioStatic` (In this case there was no relevant `PixelRatio` type alias)
- `AppStateStatic`
- `AccessibilityInfoStatic`
- `ImageResizeModeStatic`
- `BackHandlerStatic`
- `DevMenuStatic` (In this case there was no relevant `DevMenu` type alias)
- `ClipboardStatic`
- `PermissionsAndroidStatic`
- `ShareStatic`
- `DeviceEventEmitterStatic`
- `LayoutAnimationStatic`
- `KeyboardStatic` (In this case there was no relevant `Keyboard` type alias)
- `DevSettingsStatic` (In this case there was no relevant `DevSettings` type alias)
- `I18nManagerStatic`
- `EasingStatic`
- `PanResponderStatic`
- `NativeModulesStatic` (In this case there was no relevant `NativeModules` type alias)
- `LogBoxStatic`
- `PushNotificationIOSStatic`
- `SettingsStatic`
- `VibrationStatic`

</details>

### Updating test mocks

<<<<<<< pt
Devido a essa mudança, acessar tipos de ref dessas views requer usar o padrão `React.ComponentRef<typeof View>`, que funciona conforme esperado para componentes de classe e de função, por exemplo:
||||||| base_en
Due to this change, accessing ref types of these views requires using `React.ComponentRef<typeof View>` pattern which works as expected for both class and function components, e.g.:
=======
In most projects, no changes are needed here. Existing `jest.mock()` calls against `react-native/*` paths keep working — the Strict API doesn't change how module paths resolve in Jest or Metro, and a `jest.mock()` path string isn't type-checked.
>>>>>>> new_en

If a test file imports a deep path as a module (for example, to wrap the real implementation from `jest.requireActual()`), TypeScript will report the import as untyped. Where no root export covers the use case, you can keep the import and quiet the error:

```ts
// @ts-expect-error - React Native internal, untyped under the Strict API
import NativeAppState from 'react-native/Libraries/AppState/NativeAppState';
```

Separately, if your Jest setup imports `react-native/Libraries/Core/InitializeCore`, update it — see [`InitializeCore` is now `react-native/setup-env`](#initializecore-is-now-react-nativesetup-env-since-087).

## Other breaking changes

### `InitializeCore` is now `react-native/setup-env` <div className="label primary">Since 0.87</div>

Unlike other deep imports, this module is a side-effect entry point with no root `react-native` equivalent. `InitializeCore` is deprecated since 0.87.

```diff title=""
- import 'react-native/Libraries/Core/InitializeCore';
+ import 'react-native/setup-env';
```

Most apps never import this directly — it's typically found in Jest setup files and custom entry points.

### Changes to Animated types

Animated nodes eram anteriormente tipos genéricos baseados em sua saída de interpolação. Agora, eles são tipos não genéricos com um método `interpolate` genérico.

<<<<<<< pt
`Animated.LegacyRef` não está mais disponível.
||||||| base_en
`Animated.LegacyRef` is no longer available.
=======
`Animated.LegacyRef` is no longer available. Use the appropriate `*Instance` type instead (e.g. `ViewInstance` for `Animated.View`).
>>>>>>> new_en

### Unified types for optional props

Nos novos tipos, toda prop opcional será tipada como `type | undefined`.

### Removal of some deprecated types

<<<<<<< pt
Todos os tipos listados em <RNRepoLink href="/packages/react-native/types/public/DeprecatedPropertiesAlias.d.ts">`DeprecatedPropertiesAlias.d.ts`</RNRepoLink> estão inacessíveis sob a Strict API.
||||||| base_en
All types listed in <RNRepoLink href="/packages/react-native/types/public/DeprecatedPropertiesAlias.d.ts">`DeprecatedPropertiesAlias.d.ts`</RNRepoLink> are inaccessible under the Strict API.
=======
The long-deprecated `*Properties` aliases are inaccessible under the Strict API. These date from an early rename of the props types to their modern `*Props` names, and each alias has a direct replacement: `ViewProperties` becomes `ViewProps`, `TextInputProperties` becomes `TextInputProps`, and so on (plus `ImagePropertiesSourceOptions`, which becomes `ImageSourcePropType`).

For the full list of aliases, see <RNRepoLink href="/packages/react-native/types/public/DeprecatedPropertiesAlias.d.ts">`DeprecatedPropertiesAlias.d.ts`</RNRepoLink>.
>>>>>>> new_en

### Removal of leftover component props

Algumas propriedades que foram definidas nas definições de tipo mas não foram usadas pelo componente ou estavam sem definição foram removidas (por exemplo: `lineBreakMode` em `Text`, `scrollWithoutAnimationTo` em `ScrollView`, estilos transform definidos fora do array transform).

### Removal of internal-only helper types

Devido à configuração das definições de tipo anteriores, todo tipo definido era acessível a partir do pacote `react-native`. Isso incluía tipos que não foram explicitamente exportados e tipos helper que deveriam ser usados apenas internamente.

<<<<<<< pt
Exemplos notáveis disso são tipos relacionados ao StyleSheet (como `RecursiveArray`, `RegisteredStyle` e `Falsy`) e Animated (como `WithAnimatedArray` e `WithAnimatedObject`).
||||||| base_en
Notable examples of this are types related to StyleSheet (like `RecursiveArray`, `RegisteredStyle` and `Falsy`) and Animated (like `WithAnimatedArray` and `WithAnimatedObject`).
=======
Notable examples of this are types related to StyleSheet (like `RecursiveArray`, `RegisteredStyle` and `Falsy`) and Animated (like `WithAnimatedArray` and `WithAnimatedObject`).

## FAQs

<details>
<summary>**Does this change anything at runtime?**</summary>

No. The Strict API changes which type definitions TypeScript resolves — both modes resolve the same JavaScript, and your bundle is unaffected.

Note that 0.87 separately removes `react-native/src/private/*` from the package's exports, which does affect runtime. That change is independent of the Strict API.

</details>

<details>
<summary>**I maintain a library. Do I need to migrate before my users can upgrade?**</summary>

No — libraries and apps should be able to migrate independently. The Strict API is enabled per project, through each project's own `tsconfig.json`: an app adopting it doesn't affect your library, and your library adopting it doesn't affect your users. Consumers only ever see the type definitions your package ships.

Two caveats: any raw TypeScript source you ship for consumers to import (such as a Jest mock entry point) is typechecked inside their projects, so it must not rely on deep imports — ship compiled output with `.d.ts` files instead (see [Update your dependencies](#update-your-dependencies)). And you should still plan to migrate your own source: the legacy types opt-out is temporary.

</details>

<details>
<summary>**An API I use isn't exported from `react-native`. Is that a bug?**</summary>

In most cases this is intentional rather than an oversight. Our [RFC](https://github.com/react-native-community/discussions-and-proposals/pull/894) scoped the public API to what `react-native`'s index file exports, so some previously reachable internals are now private.

If you depend on something with no root equivalent, please tell us in the [discussion thread](https://github.com/react-native-community/discussions-and-proposals/discussions/1015). Where justified, we may promote APIs to the index export.

</details>

<details>
<summary>**Why were React Native's manual types replaced?**</summary>

React Native is authored in [Flow](https://flow.org/), not TypeScript. Its TypeScript types were previously community-contributed and hand-maintained (originating from `@types/react-native` on DefinitelyTyped), leaving correctness gaps — generating them from our source code ensures the types always match the implementation.

See [Moving Towards a Stable JavaScript API](/blog/2025/06/12/moving-towards-a-stable-javascript-api) for the full rationale.

</details>

:::note[Learn more]

<div style={{display: 'flex', alignItems: 'center', gap: 40}}>
  <div style={{flex: 1, gap: 8}}>
    <strong style={{display: 'block', marginBottom: 8}}>
      Watch the talk!
    </strong>
    <span>
      We shared a deep dive into our motivations and the work
      behind the Strict TypeScript API at{' '}
      <strong>App.js 2025</strong>.
    </span>
    <a
      href="https://www.youtube.com/live/UTaJlqhTk2g?si=SDRmj80kss7hXuGG&t=6520"
      target="_blank">
      <strong>View on YouTube</strong>
    </a>
  </div>
  <img
    src="/blog/assets/0.80-js-stable-api-appjs.jpg"
    style={{
      flexShrink: 0,
      maxWidth: '200px',
      aspectRatio: '16/9',
      borderRadius: 10,
    }}
    alt="App.js 2025 Talk"
  />
</div>

:::
>>>>>>> new_en
