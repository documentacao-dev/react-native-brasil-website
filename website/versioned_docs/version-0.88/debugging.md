---
ia-translated: true
id: debugging
title: Fundamentos de Depuração
---

import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; import constants from '@site/core/TabsConstants';

:::note
Recursos de depuração, como o Dev Menu, LogBox e React Native DevTools são desabilitados em builds de release (produção).
:::

## Abrindo o Dev Menu {#opening-the-dev-menu}

React Native fornece um menu de desenvolvedor no aplicativo que fornece acesso a recursos de depuração. Você pode acessar o Dev Menu balançando seu dispositivo ou através de atalhos de teclado:

- iOS Simulator: <kbd>Ctrl</kbd> + <kbd>Cmd ⌘</kbd> + <kbd>Z</kbd> (ou Device > Shake)
- Android emulators: <kbd>Cmd ⌘</kbd> + <kbd>M</kbd> (macOS) ou <kbd>Ctrl</kbd> + <kbd>M</kbd> (Windows e Linux)

Alternativa (Android): `adb shell input keyevent 82`.

![The React Native Dev Menu](/docs/assets/debugging-dev-menu-083.jpg)

## Abrindo o DevTools {#opening-devtools}

[React Native DevTools](./react-native-devtools) é nosso debugger integrado para React Native. Ele permite que você inspecione e entenda como seu código JavaScript está sendo executado, semelhante a um navegador web.

Para abrir o DevTools, você pode:

- Selecionar "Open DevTools" no Dev Menu.
- Pressionar <kbd>j</kbd> no CLI.

![React Native DevTools opened to the "Welcome" pane](/docs/assets/debugging-rndt-welcome-083.jpg)

No primeiro lançamento, o DevTools abrirá em um painel de boas-vindas, junto com uma gaveta de console aberta onde você pode visualizar logs e interagir com o runtime JavaScript. No topo da janela, você pode navegar para outros painéis, incluindo o React Components Inspector e Profiler integrados.

Saiba mais em nosso [guia do React Native DevTools](./react-native-devtools).

## LogBox

LogBox é uma ferramenta no aplicativo que é exibida quando avisos ou erros são registrados pelo seu aplicativo.

![A LogBox warning and an expanded LogBox syntax error](/docs/assets/debugging-logbox-076.jpg)

### Erros Fatais {#fatal-errors}

Quando ocorre um erro irrecuperável, como um erro de sintaxe JavaScript, LogBox abrirá com a localização do erro. Neste estado, LogBox não pode ser descartado, pois seu código não pode ser executado. LogBox será descartado automaticamente assim que o erro de sintaxe for corrigido — seja via Fast Refresh ou após um reload manual.

### Erros e Avisos do Console {#console-errors-and-warnings}

Erros e avisos do console são exibidos como notificações na tela com um badge vermelho ou amarelo.

- **Errors** serão exibidos com uma contagem de notificações. Toque na notificação para ver uma visualização expandida e para paginar através de outros logs.
- **Warnings** exibirão um banner de notificação sem detalhes, solicitando que você abra o React Native DevTools.

Quando o React Native DevTools está aberto, todos os erros, exceto erros fatais, serão ocultados do LogBox. Recomendamos usar o painel Console dentro do React Native DevTools como fonte da verdade, devido às várias opções do LogBox que podem ocultar ou ajustar o nível de certos logs.

<details>
<summary>**💡 Ignorando logs**</summary>

LogBox pode ser configurado via a API `LogBox`.

```js
import {LogBox} from 'react-native';
```

#### Ignorar todos os logs {#ignore-all-logs}

Notificações do LogBox podem ser desabilitadas usando `LogBox.ignoreAllLogs()`. Isso pode ser útil em situações como demonstrações de produtos.

```js
LogBox.ignoreAllLogs();
```

#### Ignorar logs específicos {#ignore-specific-logs}

Notificações podem ser desabilitadas em uma base por log via `LogBox.ignoreLogs()`. Isso pode ser útil para avisos barulhentos ou aqueles que não podem ser corrigidos, por exemplo, em uma dependência de terceiros.

```js
LogBox.ignoreLogs([
  // Exact message
  'Warning: componentWillReceiveProps has been renamed',

  // Substring or regex match
  /GraphQL error: .*/,
]);
```

:::note

LogBox tratará certos erros do React como avisos, o que significa que eles não serão exibidos como uma notificação de erro no aplicativo. Usuários avançados podem alterar esse comportamento personalizando o filtro de avisos do LogBox usando [`LogBoxData.setWarningFilter()`](https://github.com/react/react-native/blob/d334f4d77eea538dff87fdcf2ebc090246cfdbb0/packages/react-native/Libraries/LogBox/Data/LogBoxData.js#L338).

:::

</details>

## Performance Monitor

No Android e iOS, uma sobreposição de desempenho no aplicativo pode ser alternada durante o desenvolvimento selecionando **"Perf Monitor"** no Dev Menu. Saiba mais sobre este recurso [aqui](/docs/performance).

![The Performance Monitor overlay on iOS and Android](/docs/assets/debugging-performance-monitor.jpg)

:::info
O Performance Monitor é executado no aplicativo e é um guia. Recomendamos investigar as ferramentas nativas no Android Studio e Xcode para medições de desempenho precisas.
:::
