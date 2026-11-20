---
ia-translated: true
id: strict-typescript-api
title: Strict TypeScript API
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import RNRepoLink from '@site/core/RNRepoLink';

:::info[Novidade na 0.87]

**A Strict API agora vem habilitada por padrão** (antes era opt-in a partir da 0.80). Esta é uma **mudança breaking**, detalhada no guia abaixo.

:::

A Strict TypeScript API é a API TypeScript moderna do React Native, substituindo as definições TypeScript mantidas manualmente das versões anteriores.

### Mudanças principais (breaking) {#key-changes-breaking}

1. **Sem deep imports.** A API está restrita ao arquivo index do `react-native`. Este é um contrato de API pública mais restrito e intencional. Também garante que mudanças internas de caminhos de arquivo no código-fonte do React Native não sejam breaking.
2. **Gerada diretamente do código-fonte.** Antes, o React Native usava tipos mantidos manualmente, separadamente. Gerar a partir do código-fonte agora significa que melhoramos a cobertura, a correção e as garantias de compatibilidade.

### Como desativar <div className="label primary">Desde a 0.87</div> {#opting-out-since-087}

A Strict API é uma **mudança breaking**, e nem todos os apps e bibliotecas conseguem migrar imediatamente.

Continuamos a distribuir nossos tipos manuais anteriores, que podem ser restaurados pelo seu `tsconfig.json`. Observe que, em uma versão futura, removeremos essa opção de desativação.

```diff title="tsconfig.json"
  {
    "extends": "@react-native/typescript-config",
    "compilerOptions": {
      ...
+     "customConditions": ["react-native", "react-native-legacy-deep-imports"]
    }
  }
```

:::info[Problemas / Feedback?]

A ativação da Strict API por padrão na 0.87 é uma mudança para todo o ecossistema, e uma que precisamos fazer para ter garantias de API estáveis para o React Native no futuro.

As escolhas de design sobre quais APIs são exportadas na raiz, e as atualizações intencionais de nomes e formatos de tipos, foram discutidas com a comunidade e os parceiros desde a prévia original da 0.80.

Acreditamos ter resolvido todas as arestas, mas ainda podem existir casos extremos. Se você optar por desativar a Strict API na 0.87 ou posterior, adoraríamos saber o motivo: [**thread de discussão**](https://github.com/react-native-community/discussions-and-proposals/discussions/1015).

:::

---

## Guia de migração {#migration-guide}

:::tip

Use a skill [**/migrate-to-strict-api**](https://www.skills.sh/react-native-community/skills/migrate-to-strict-api) para migrar seu projeto com um agente.

```sh
npx skills add react-native-community/skills --skill migrate-to-strict-api
```

:::

### Antes de começar {#before-you-start}

Ativar a Strict API — atualizando para a 0.87 ou optando por ela em uma versão anterior — afeta apenas a análise de TypeScript do seu próprio projeto, delimitada pelo seu `tsconfig.json`.

Na maioria dos casos, cada projeto pode migrar de forma independente: desenvolvedores de apps não precisam esperar dependências específicas para ativar a Strict API, e autores de bibliotecas não precisam esperar seus usuários.

#### Mantenha o `skipLibCheck` habilitado {#keep-skiplibcheck-enabled}

O processo acima depende do `skipLibCheck`, que o `@react-native/typescript-config` habilita por padrão. Ele impede que erros originados dentro de arquivos `.d.ts` de terceiros apareçam nos seus resultados. Se seu projeto sobrescreve essa opção, habilite-a novamente antes de começar; caso contrário, você verá erros em dependências que não pode corrigir.

#### Atualize suas dependências {#update-your-dependencies}

Às vezes, suas dependências podem ter arestas sob a Strict API. Sempre que erros de tipo envolverem uma biblioteca, procure e atualize primeiro para uma versão corrigida.

Uma aresta específica: algumas bibliotecas publicam código-fonte TypeScript bruto que o seu projeto importa, por exemplo arquivos de setup do Jest. Eles são checados como parte do seu projeto. Bibliotecas populares já reempacotaram esses pontos de entrada:

- `@expensify/react-native-live-markdown` — corrigido na [0.1.335](https://github.com/Expensify/react-native-live-markdown/pull/771)
- `react-native-safe-area-context` — corrigido na [5.8.1](https://github.com/AppAndFlow/react-native-safe-area-context/pull/745)

<details>
<summary>**Avançado: excluindo uma biblioteca incompatível**</summary>

Se uma biblioteca incompatível estiver gerando erros em `node_modules` (normalmente `TS2307: Cannot find module 'react-native/Libraries/...'`), você pode excluí-la da análise de TypeScript como correção local, redirecionando o subcaminho importado para um stub sem tipos:

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

Também reporte a incompatibilidade à biblioteca; as correções linkadas acima são um bom modelo.

</details>

### Novo namespace `CodegenTypes` {#new-codegentypes-namespace}

Tipos usados para codegen, como `Int32`, `Double`, `WithDefault`, etc., agora estão disponíveis sob um único namespace `CodegenTypes`. Da mesma forma, `codegenNativeComponent` e `codegenNativeCommands` agora estão disponíveis para importar do pacote react-native em vez de usar o deep import.

O `CodegenTypes` com namespace, bem como `codegenNativeCommands` e `codegenNativeComponent`, também estão disponíveis no pacote `react-native` quando a Strict API não está habilitada para facilitar a adoção para bibliotecas de terceiros.

#### Migração {#migration}

<Tabs defaultValue="after">
<TabItem value="before" label="Antes">

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
<TabItem value="after" label="Depois">

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

### Refs agora usam tipos `*Instance` <div className="label primary">Desde a 0.87</div> {#refs-now-use-instance-types-since-087}

Cada componente nativo agora tem um tipo `*Instance` dedicado para uso com refs, por exemplo `ViewInstance`, `TextInputInstance`, `ScrollViewInstance`. Esta é a **forma recomendada de tipar refs** na Strict TypeScript API.

Antes, `useRef<View>` funcionava porque `View` e os outros componentes eram tipados como classe. Na Strict API, os componentes nativos são tipados como funções, então `View` se refere à própria função — **nomes de tipo de componente não funcionam mais como tipos de ref**.

<Tabs defaultValue="after">
<TabItem value="before" label="Antes">

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
<TabItem value="after" label="Depois">

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

Os tipos `*Instance` também funcionam de forma transparente com as variantes `Animated`; não é preciso um tipo separado:

```tsx title=""
const viewRef = useRef<ViewInstance>(null);

<View ref={viewRef} />
<Animated.View ref={viewRef} />
```

Isso também substitui o tipo `Animated.LegacyRef`, que foi removido. Código que usa `ref={ref as React.Ref<Animated.LegacyRef<View>>}` pode ser simplificado para `ref={ref}` com uma ref tipada como `ViewInstance`.

<details>
<summary>**Tipos de instância disponíveis**</summary>

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

Componentes sem suporte a ref (`InputAccessoryView`, `TouchableWithoutFeedback`, `experimental_LayoutConformance`) não têm tipos de instância.

</details>

**Migração**

| Antes                                                   | Depois                       |
| ------------------------------------------------------- | ---------------------------- |
| `useRef<View>(null)`                                    | `useRef<ViewInstance>(null)` |
| `useRef<React.ComponentRef<typeof View>>(null)`         | `useRef<ViewInstance>(null)` |
| `useRef<HostInstance>(null)` (for a specific component) | `useRef<ViewInstance>(null)` |
| `Ref<Animated.LegacyRef<View>>`                         | `Ref<ViewInstance>`          |

:::note

`React.ComponentRef<typeof View>` continua válido e produz o mesmo tipo que `ViewInstance`. Os tipos `*Instance` são aliases práticos; as duas abordagens funcionam.

:::

### Remoção dos tipos `*Static` {#removal-of-static-types}

#### Migração {#migration}

<Tabs defaultValue="after">
<TabItem value="before" label="Antes">

```tsx title=""
import {Linking, LinkingStatic} from 'react-native';

function foo(linking: LinkingStatic) {}
foo(Linking);
```

</TabItem>
<TabItem value="after" label="Depois">

```tsx title=""
import {Linking} from 'react-native';

function foo(linking: Linking) {}
foo(Linking);
```

</TabItem>
</Tabs>

As seguintes APIs eram anteriormente nomeadas como `*Static` mais uma declaração de variável desse tipo. Na maioria dos casos havia um alias para que o valor e o tipo fossem exportados sob o mesmo identificador, mas alguns estavam faltando.

<details>
<summary>**APIs afetadas**</summary>

- `AlertStatic`
- `ActionSheetIOSStatic`
- `ToastAndroidStatic`
- `InteractionManagerStatic` (Neste caso não havia um alias de tipo `InteractionManager` relevante)
- `UIManagerStatic`
- `PlatformStatic`
- `SectionListStatic`
- `PixelRatioStatic` (Neste caso não havia um alias de tipo `PixelRatio` relevante)
- `AppStateStatic`
- `AccessibilityInfoStatic`
- `ImageResizeModeStatic`
- `BackHandlerStatic`
- `DevMenuStatic` (Neste caso não havia um alias de tipo `DevMenu` relevante)
- `ClipboardStatic`
- `PermissionsAndroidStatic`
- `ShareStatic`
- `DeviceEventEmitterStatic`
- `LayoutAnimationStatic`
- `KeyboardStatic` (Neste caso não havia um alias de tipo `Keyboard` relevante)
- `DevSettingsStatic` (Neste caso não havia um alias de tipo `DevSettings` relevante)
- `I18nManagerStatic`
- `EasingStatic`
- `PanResponderStatic`
- `NativeModulesStatic` (Neste caso não havia um alias de tipo `NativeModules` relevante)
- `LogBoxStatic`
- `PushNotificationIOSStatic`
- `SettingsStatic`
- `VibrationStatic`

</details>

### Atualizando mocks de teste {#updating-test-mocks}

Na maioria dos projetos, nenhuma mudança é necessária aqui. As chamadas `jest.mock()` existentes contra caminhos `react-native/*` continuam funcionando: a Strict API não muda como os caminhos de módulo são resolvidos no Jest ou no Metro, e a string de caminho de `jest.mock()` não é checada por tipos.

Se um arquivo de teste importa um caminho profundo como módulo (por exemplo, para envolver a implementação real de `jest.requireActual()`), o TypeScript vai reportar o import como sem tipos. Quando nenhuma exportação na raiz cobre o caso de uso, você pode manter o import e silenciar o erro:

```ts
// @ts-expect-error - React Native internal, untyped under the Strict API
import NativeAppState from 'react-native/Libraries/AppState/NativeAppState';
```

Além disso, se o seu setup do Jest importa `react-native/Libraries/Core/InitializeCore`, atualize-o — veja [`InitializeCore` agora é `react-native/setup-env`](#initializecore-is-now-react-nativesetup-env-since-087).

## Outras mudanças breaking {#other-breaking-changes}

### `InitializeCore` agora é `react-native/setup-env` <div className="label primary">Desde a 0.87</div> {#initializecore-is-now-react-nativesetup-env-since-087}

Diferente de outros deep imports, este módulo é um ponto de entrada com efeitos colaterais, sem equivalente na raiz do `react-native`. O `InitializeCore` está descontinuado desde a 0.87.

```diff title=""
- import 'react-native/Libraries/Core/InitializeCore';
+ import 'react-native/setup-env';
```

A maioria dos apps nunca importa isso diretamente; normalmente ele aparece em arquivos de setup do Jest e em pontos de entrada personalizados.

### Mudanças nos tipos de Animated {#changes-to-animated-types}

Nodes de Animated eram anteriormente tipos genéricos baseados em sua saída de interpolação. Agora, eles são tipos não genéricos com um método `interpolate` genérico.

`Animated.LegacyRef` não está mais disponível. Use o tipo `*Instance` apropriado (por exemplo, `ViewInstance` para `Animated.View`).

### Tipos unificados para props opcionais {#unified-types-for-optional-props}

Nos novos tipos, toda prop opcional será tipada como `type | undefined`.

### Remoção de alguns tipos descontinuados {#removal-of-some-deprecated-types}

Os aliases `*Properties`, descontinuados há muito tempo, são inacessíveis na Strict API. Eles vêm de uma renomeação antiga dos tipos de props para os nomes modernos `*Props`, e cada alias tem um substituto direto: `ViewProperties` vira `ViewProps`, `TextInputProperties` vira `TextInputProps`, e assim por diante (além de `ImagePropertiesSourceOptions`, que vira `ImageSourcePropType`).

Para a lista completa de aliases, veja <RNRepoLink href="/packages/react-native/types/public/DeprecatedPropertiesAlias.d.ts">`DeprecatedPropertiesAlias.d.ts`</RNRepoLink>.

### Remoção de props de componentes que sobraram {#removal-of-leftover-component-props}

Algumas propriedades que foram definidas nas definições de tipo mas não foram usadas pelo componente ou estavam sem definição foram removidas (por exemplo: `lineBreakMode` em `Text`, `scrollWithoutAnimationTo` em `ScrollView`, estilos transform definidos fora do array transform).

### Remoção de tipos auxiliares de uso interno {#removal-of-internal-only-helper-types}

Devido à configuração das definições de tipo anteriores, todo tipo definido era acessível a partir do pacote `react-native`. Isso incluía tipos que não foram explicitamente exportados e tipos helper que deveriam ser usados apenas internamente.

Exemplos notáveis disso são tipos relacionados ao StyleSheet (como `RecursiveArray`, `RegisteredStyle` e `Falsy`) e Animated (como `WithAnimatedArray` e `WithAnimatedObject`).

## Perguntas frequentes {#faqs}

<details>
<summary>**Isso muda algo em tempo de execução?**</summary>

Não. A Strict API muda quais definições de tipo o TypeScript resolve; os dois modos resolvem o mesmo JavaScript, e o seu bundle não é afetado.

Observe que a 0.87 também remove `react-native/src/private/*` das exportações do pacote, o que afeta o runtime. Essa mudança é independente da Strict API.

</details>

<details>
<summary>**Eu mantenho uma biblioteca. Preciso migrar antes que meus usuários possam atualizar?**</summary>

Não. Bibliotecas e apps devem conseguir migrar de forma independente. A Strict API é habilitada por projeto, pelo `tsconfig.json` de cada um: um app que a adota não afeta sua biblioteca, e sua biblioteca que a adota não afeta seus usuários. Os consumidores veem apenas as definições de tipo que o seu pacote distribui.

Duas ressalvas: qualquer código-fonte TypeScript bruto que você distribui para os consumidores importarem (como um ponto de entrada de mock do Jest) é checado dentro dos projetos deles, então não pode depender de deep imports. Distribua a saída compilada com arquivos `.d.ts` (veja [Atualize suas dependências](#update-your-dependencies)). E você ainda deve planejar migrar o seu próprio código: a opção de desativar os tipos legados é temporária.

</details>

<details>
<summary>**Uma API que eu uso não é exportada pelo `react-native`. Isso é um bug?**</summary>

Na maioria dos casos isso é intencional, e não um descuido. Nossa [RFC](https://github.com/react-native-community/discussions-and-proposals/pull/894) delimitou a API pública ao que o arquivo index do `react-native` exporta, então alguns internos antes acessíveis agora são privados.

Se você depende de algo sem equivalente na raiz, conte pra gente na [thread de discussão](https://github.com/react-native-community/discussions-and-proposals/discussions/1015). Quando justificado, podemos promover APIs para a exportação do index.

</details>

<details>
<summary>**Por que os tipos manuais do React Native foram substituídos?**</summary>

O React Native é escrito em [Flow](https://flow.org/), não em TypeScript. Seus tipos TypeScript eram antes contribuídos pela comunidade e mantidos à mão (com origem em `@types/react-native`, no DefinitelyTyped), deixando lacunas de correção. Gerá-los a partir do nosso código-fonte garante que os tipos sempre correspondam à implementação.

Veja [Caminhando para uma API JavaScript estável](/blog/2025/06/12/moving-towards-a-stable-javascript-api) para a motivação completa.

</details>

:::note[Saiba mais]

<div style={{display: 'flex', alignItems: 'center', gap: 40}}>
  <div style={{flex: 1, gap: 8}}>
    <strong style={{display: 'block', marginBottom: 8}}>
      Assista à palestra!
    </strong>
    <span>
      Compartilhamos um mergulho nas nossas motivações e no trabalho por trás
      da Strict TypeScript API na{' '}
      <strong>App.js 2025</strong>.
    </span>
    <a
      href="https://www.youtube.com/live/UTaJlqhTk2g?si=SDRmj80kss7hXuGG&t=6520"
      target="_blank">
      <strong>Assista no YouTube</strong>
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
    alt="Palestra App.js 2025"
  />
</div>

:::
