---
ia-translated: true
id: react-native-devtools
title: React Native DevTools
---

import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; import constants from '@site/core/TabsConstants';

React Native DevTools é nossa experiência moderna de debugging para React Native. Construído propositalmente do zero, visa ser fundamentalmente mais integrado, correto e confiável do que métodos de debugging anteriores.

![React Native DevTools opened to the "Welcome" pane](/docs/assets/debugging-rndt-welcome-083.jpg)

React Native DevTools foi projetado para debugging de preocupações de aplicativos React, e não para substituir ferramentas nativas. Se você quiser inspecionar as camadas de plataforma subjacentes do React Native (por exemplo, ao desenvolver um Native Module), use as ferramentas de debugging disponíveis no Android Studio e Xcode (veja [Debugging Native Code](/docs/debugging-native-code)).

<<<<<<< pt
<details>
<summary>**💡 Compatibilidade** — lançado na 0.76</summary>

React Native DevTools suporta todos os aplicativos React Native rodando Hermes. Ele substitui os frontends anteriores Flipper, Experimental Debugger e Hermes debugger (Chrome).

Não é possível configurar React Native DevTools com versões mais antigas do React Native.

- **Chrome Browser DevTools — não suportado**
  - Conectar ao React Native via `chrome://inspect` não é mais suportado. Recursos podem não funcionar corretamente, pois as versões mais recentes do Chrome DevTools (que são construídas para corresponder às capacidades e APIs mais recentes do navegador) não foram testadas, e este frontend não possui nossas personalizações. Em vez disso, fornecemos uma versão suportada com React Native DevTools.
- **Visual Studio Code — não suportado** (pré-existente)
  - Extensões de terceiros como [Expo Tools](https://github.com/expo/vscode-expo) e [Radon IDE](https://ide.swmansion.com/) podem ter compatibilidade melhorada, mas não são diretamente suportadas pela equipe React.

</details>
<details>
<summary>**💡 Feedback & FAQs**</summary>

Queremos que as ferramentas que você usa para debugar React em todas as plataformas sejam confiáveis, familiares, simples e coesas. Todos os recursos descritos nesta página são construídos com esses princípios em mente, e também queremos oferecer mais capacidades no futuro.

Estamos ativamente iterando sobre o futuro do React Native DevTools, e criamos uma [discussão GitHub](https://github.com/react-native-community/discussions-and-proposals/discussions/819) centralizada para acompanhar problemas, perguntas frequentes e feedback.

</details>

## Recursos principais
||||||| base_en
<details>
<summary>**💡 Compatibility** — released in 0.76</summary>

React Native DevTools supports all React Native apps running Hermes. It replaces the previous Flipper, Experimental Debugger, and Hermes debugger (Chrome) frontends.

It is not possible to set up React Native DevTools with any older versions of React Native.

- **Chrome Browser DevTools — unsupported**
  - Connecting to React Native via `chrome://inspect` is no longer supported. Features may not work correctly, as the latest versions of Chrome DevTools (which are built to match the latest browser capabilities and APIs) have not been tested, and this frontend lacks our customisations. Instead, we ship a supported version with React Native DevTools.
- **Visual Studio Code — unsupported** (pre-existing)
  - Third party extensions such as [Expo Tools](https://github.com/expo/vscode-expo) and [Radon IDE](https://ide.swmansion.com/) may have improved compatibility, but are not directly supported by the React team.

</details>
<details>
<summary>**💡 Feedback & FAQs**</summary>

We want the tooling you use to debug React across all platforms to be reliable, familiar, simple, and cohesive. All the features described on this page are built with these principles in mind, and we also want to offer more capabilities in future.

We are actively iterating on the future of React Native DevTools, and have created a centralized [GitHub discussion](https://github.com/react-native-community/discussions-and-proposals/discussions/819) to keep track of issues, frequently asked questions, and feedback.

</details>

## Core features
=======
## Core features
>>>>>>> new_en

React Native DevTools é baseado no frontend Chrome DevTools. Se você tem experiência em desenvolvimento web, seus recursos devem ser familiares. Como ponto de partida, recomendamos navegar nos [docs do Chrome DevTools](https://developer.chrome.com/docs/devtools) que contêm guias completos, bem como recursos de vídeo.

### Console

![A series of logs React Native DevTools Sources view, alongside a device](/docs/assets/debugging-rndt-console.jpg)

O painel Console permite visualizar e filtrar mensagens, avaliar JavaScript, inspecionar propriedades de objetos e mais.

[Console features reference | Chrome DevTools](https://developer.chrome.com/docs/devtools/console/reference)

#### Dicas úteis

- Se seu aplicativo tem muitos logs, use a caixa de filtro ou altere os níveis de log que são mostrados.
- Observe valores ao longo do tempo com [Live Expressions](https://developer.chrome.com/docs/devtools/console/live-expressions).
- Persista mensagens através de reloads com [Preserve Logs](https://developer.chrome.com/docs/devtools/console/reference#persist).
- Use <kbd>Ctrl</kbd> + <kbd>L</kbd> para limpar a view do console.

### Sources & breakpoints

![A paused breakpoint in the React Native DevTools Sources view, alongside a device](/docs/assets/debugging-rndt-sources-paused-with-device.jpg)

O painel Sources permite visualizar os arquivos fonte em seu aplicativo e registrar breakpoints. Use um breakpoint para definir uma linha de código onde seu aplicativo deve pausar — permitindo que você inspecione o estado vivo do programa e incremente através do código.

[Pause your code with breakpoints | Chrome DevTools](https://developer.chrome.com/docs/devtools/javascript/breakpoints)

:::tip

#### Mini-guia

Breakpoints são uma ferramenta fundamental em seu kit de debugging!

1. Navegue até um arquivo fonte usando a barra lateral ou <kbd>Cmd ⌘</kbd>+<kbd>P</kbd> / <kbd>Ctrl</kbd>+<kbd>P</kbd>.
2. Clique na coluna de números de linha ao lado de uma linha de código para adicionar um breakpoint.
3. Use os controles de navegação no canto superior direito para [step through code](https://developer.chrome.com/docs/devtools/javascript/reference#stepping) quando pausado.

:::

#### Dicas úteis

- Um overlay "Paused in Debugger" aparece quando seu aplicativo está pausado. Toque nele para retomar.
- Preste atenção aos painéis do lado direito quando em um breakpoint, que permitem inspecionar o escopo atual e call stack, e definir watch expressions.
- Use uma declaração `debugger;` para rapidamente definir um breakpoint do seu editor de texto. Isso chegará ao dispositivo imediatamente via Fast Refresh.
- Existem múltiplos tipos de breakpoints! Por exemplo, [Conditional Breakpoints e Logpoints](https://developer.chrome.com/docs/devtools/javascript/breakpoints#overview).

### Network <div className="label primary">Since 0.83</div>

![A network request in the React Native DevTools Network panel](/docs/assets/debugging-rndt-network.jpg)

The Network panel allows you to view and inspect the network requests made by your app. Logged requests provide detailed metadata such as timings and headers sent/received, as well as response previews.

Network requests are recorded automatically when DevTools is open. We support most features from Chrome, with some exceptions. See more below.

<details>
<summary><strong>💡 Network event coverage, Expo support</strong></summary>

**Which network events are captured?**

Today, we record all network calls through `fetch()`, `XMLHttpRequest`, and `<Image>` — with support for custom networking libraries, such as Expo Fetch, coming later.

**Expo Network differences**

Because of this, apps using Expo will continue to see the "Expo Network" panel — a separate implementation by the Expo framework which will log these additional request sources but has slightly reduced features.

- Coverage for Expo-specific network events.
- No request initiator support.
- No Performance panel integration.

We're working with Expo to integrate Expo Fetch and third party networking libraries with our new Network inspection pipeline in future releases.

**Unimplemented features**

At launch, these are the features we don't yet support in React Native:

- WebSocket events
- Network response mocking
- Simulated network throttling

</details>

<details>
<summary><strong>💡 Response previews buffer size</strong></summary>

If you are inspecting a large volume of response data, please note that response previews are cached in an on-device buffer with a maximum size of 100MB. This means we may evict response previews (but not metadata) if the cache becomes too large, oldest request first.

</details>

#### Useful tips

- Use the Initiator tab to see the call stack of where a network request was initiated in your app.
- Network events will also be shown in the Network track in the Performance panel.

### Performance <div className="label primary">Since 0.83</div>

![A performance trace in the React Native DevTools Performance panel](/docs/assets/debugging-rndt-performance.jpg)

Performance tracing allows you to record a performance session within your app to understand how your JavaScript code is running and what operations took the most time. In React Native, we show JavaScript execution, React Performance tracks, Network events, and custom [User Timings](https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/User_timing), rendered in a single performance timeline.

#### Useful tips

- Use [Annotations](https://developer.chrome.com/docs/devtools/performance/annotations) (shift-drag) to label and mark up a performance trace — useful before [downloading and sharing](https://developer.chrome.com/docs/devtools/performance/save-trace) a trace with a teammate. Annotations also provide a quick way to gauge time spans in **seconds**.
- Use the [`PerformanceObserver` API](./global-PerformanceObserver.md) in your app to observe performance events at runtime — useful if you want to capture performance telemetry.

#### Learn more

- [React Performance tracks](https://react.dev/reference/dev-tools/react-performance-tracks)
- [Performance APIs > User Timings | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/User_timing)
- ["Debug Like a Senior — React Native Performance Panel" | Software Mansion](https://blog.swmansion.com/react-native-debugging-new-performance-panel-in-react-native-0-83-21ca90871f6d)

### Memory

![Inspecting a heap snapshot in the Memory panel](/docs/assets/debugging-rndt-memory.jpg)

O painel Memory permite tirar um heap snapshot e visualizar o uso de memória do seu código JavaScript ao longo do tempo.

[Record heap snapshots | Chrome DevTools](https://developer.chrome.com/docs/devtools/memory-problems/heap-snapshots)

#### Dicas úteis

- Use <kbd>Cmd ⌘</kbd>+<kbd>F</kbd> / <kbd>Ctrl</kbd>+<kbd>F</kbd> para filtrar por objetos específicos no heap.
- Tirar um [allocation timeline report](https://developer.chrome.com/docs/devtools/memory-problems/allocation-profiler) pode ser útil para ver o uso de memória ao longo do tempo como um gráfico, para identificar possíveis memory leaks.

## Recursos do React DevTools

<<<<<<< pt
Nos painéis integrados Components e Profiler, você encontrará todos os recursos da extensão de navegador [React DevTools](https://react.dev/learn/react-developer-tools). Esses funcionam perfeitamente no React Native DevTools.
||||||| base_en
In the integrated Components and Profiler panels, you'll find all the features of the [React DevTools](https://react.dev/learn/react-developer-tools) browser extension. These work seamlessly in React Native DevTools.
=======
In the integrated Components, Profiler, and Suspense panels, you'll find all the features of the [React DevTools](https://react.dev/learn/react-developer-tools) browser extension. These work seamlessly in React Native DevTools.
>>>>>>> new_en

### React Components

![Selecting and locating elements using the React Components panel](/docs/assets/debugging-rndt-react-components.gif)

O painel React Components permite inspecionar e atualizar a árvore de componentes React renderizada.

- Passe o mouse ou selecione um elemento no DevTools para destacá-lo no dispositivo.
- Para localizar um elemento no DevTools, clique no botão "Select element" no canto superior esquerdo, depois toque em qualquer elemento no aplicativo.

#### Dicas úteis

- Props e state em um componente podem ser visualizados e modificados em tempo de execução usando o painel do lado direito.
- Componentes otimizados com [React Compiler](https://react.dev/learn/react-compiler) serão anotados com um badge "Memo ✨".

:::tip

#### Dica profissional: Destacar re-renders

Re-renders podem ser um contribuidor significativo para problemas de performance em aplicativos React. DevTools pode destacar re-renders de componentes à medida que acontecem.

- Para habilitar, clique no ícone View Settings (`⚙︎`) e marque "Highlight updates when components render".

![Location of the "highlight updates" setting, next to a recording of the live render overlay](/docs/assets/debugging-rndt-highlight-renders.gif)

:::

### React Profiler

![A profile rendered as a flame graph](/docs/assets/debugging-rndt-react-profiler.jpg)

O painel React Profiler permite gravar perfis de performance para entender o timing de renderizações de componentes e commits do React.

Para mais informações, veja o [guia original de 2018](https://legacy.reactjs.org/blog/2018/09/10/introducing-the-react-profiler.html#reading-performance-data) (note que partes disso podem estar desatualizadas).

<<<<<<< pt
## Reconectando DevTools
||||||| base_en
## Reconnecting DevTools
=======
### React Suspense <div className="label primary">Since 0.90</div>

![Selecting a Suspense boundary in the React Suspense panel, alongside a device](/docs/assets/debugging-rndt-react-suspense.jpg)

The React Suspense panel allows you to inspect the [`<Suspense>`](https://react.dev/reference/react/Suspense) boundaries in your app, and see what caused each one to suspend.

- The boundary map lays out each boundary as it appears on screen, and the timeline below it steps through the order in which they revealed their content.
- Select a boundary to see what it was suspended by, such as a `React.lazy()` component or a promise read with `use()`.

## Reconnecting DevTools
>>>>>>> new_en

Ocasionalmente, DevTools pode desconectar do dispositivo alvo. Isso pode acontecer se:

- O aplicativo é fechado.
- O aplicativo é recompilado (uma nova build nativa é instalada).
- O aplicativo trava no lado nativo.
- O dev server (Metro) é encerrado.
- Um dispositivo físico é desconectado.

Na desconexão, um diálogo será mostrado com a mensagem "Debugging connection was closed".

![A reconnect dialog shown when a device is disconnected](/docs/assets/debugging-reconnect-menu.jpg)

Daqui, você pode:

- **Dismiss**: Selecione o ícone fechar (`×`) ou clique fora do diálogo para retornar à UI do DevTools no último estado antes da desconexão.
- **Reconnect**: Selecione "Reconnect DevTools", tendo resolvido o motivo da desconexão.
