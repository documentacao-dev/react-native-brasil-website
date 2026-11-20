---
ia-translated: true
id: react-native-devtools
title: React Native DevTools
---

import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'; import constants from '@site/core/TabsConstants';

React Native DevTools é nossa experiência moderna de debugging para React Native. Construído propositalmente do zero, visa ser fundamentalmente mais integrado, correto e confiável do que métodos de debugging anteriores.

![React Native DevTools opened to the "Welcome" pane](/docs/assets/debugging-rndt-welcome-083.jpg)

React Native DevTools foi projetado para debugging de preocupações de aplicativos React, e não para substituir ferramentas nativas. Se você quiser inspecionar as camadas de plataforma subjacentes do React Native (por exemplo, ao desenvolver um Native Module), use as ferramentas de debugging disponíveis no Android Studio e Xcode (veja [Debugging Native Code](/docs/debugging-native-code)).

## Recursos principais {#core-features}

React Native DevTools é baseado no frontend Chrome DevTools. Se você tem experiência em desenvolvimento web, seus recursos devem ser familiares. Como ponto de partida, recomendamos navegar nos [docs do Chrome DevTools](https://developer.chrome.com/docs/devtools) que contêm guias completos, bem como recursos de vídeo.

### Console

![A series of logs React Native DevTools Sources view, alongside a device](/docs/assets/debugging-rndt-console.jpg)

O painel Console permite visualizar e filtrar mensagens, avaliar JavaScript, inspecionar propriedades de objetos e mais.

[Console features reference | Chrome DevTools](https://developer.chrome.com/docs/devtools/console/reference)

#### Dicas úteis {#useful-tips}

- Se seu aplicativo tem muitos logs, use a caixa de filtro ou altere os níveis de log que são mostrados.
- Observe valores ao longo do tempo com [Live Expressions](https://developer.chrome.com/docs/devtools/console/live-expressions).
- Persista mensagens através de reloads com [Preserve Logs](https://developer.chrome.com/docs/devtools/console/reference#persist).
- Use <kbd>Ctrl</kbd> + <kbd>L</kbd> para limpar a view do console.

### Sources & breakpoints

![A paused breakpoint in the React Native DevTools Sources view, alongside a device](/docs/assets/debugging-rndt-sources-paused-with-device.jpg)

O painel Sources permite visualizar os arquivos fonte em seu aplicativo e registrar breakpoints. Use um breakpoint para definir uma linha de código onde seu aplicativo deve pausar — permitindo que você inspecione o estado vivo do programa e incremente através do código.

[Pause your code with breakpoints | Chrome DevTools](https://developer.chrome.com/docs/devtools/javascript/breakpoints)

:::tip

#### Mini-guia {#mini-guide}

Breakpoints são uma ferramenta fundamental em seu kit de debugging!

1. Navegue até um arquivo fonte usando a barra lateral ou <kbd>Cmd ⌘</kbd>+<kbd>P</kbd> / <kbd>Ctrl</kbd>+<kbd>P</kbd>.
2. Clique na coluna de números de linha ao lado de uma linha de código para adicionar um breakpoint.
3. Use os controles de navegação no canto superior direito para [step through code](https://developer.chrome.com/docs/devtools/javascript/reference#stepping) quando pausado.

:::

#### Dicas úteis {#useful-tips}

- Um overlay "Paused in Debugger" aparece quando seu aplicativo está pausado. Toque nele para retomar.
- Preste atenção aos painéis do lado direito quando em um breakpoint, que permitem inspecionar o escopo atual e call stack, e definir watch expressions.
- Use uma declaração `debugger;` para rapidamente definir um breakpoint do seu editor de texto. Isso chegará ao dispositivo imediatamente via Fast Refresh.
- Existem múltiplos tipos de breakpoints! Por exemplo, [Conditional Breakpoints e Logpoints](https://developer.chrome.com/docs/devtools/javascript/breakpoints#overview).

### Network <div className="label primary">Since 0.83</div>

![Uma requisição de rede no painel Network do React Native DevTools](/docs/assets/debugging-rndt-network.jpg)

O painel Network permite visualizar e inspecionar as requisições de rede feitas pelo seu app. As requisições registradas trazem metadados detalhados, como tempos e headers enviados e recebidos, além de prévias das respostas.

As requisições são registradas automaticamente enquanto o DevTools está aberto. Oferecemos suporte à maioria dos recursos do Chrome, com algumas exceções. Veja mais abaixo.

<details>
<summary><strong>💡 Cobertura de eventos de rede, suporte ao Expo</strong></summary>

**Quais eventos de rede são capturados?**

Hoje, registramos todas as chamadas de rede feitas por `fetch()`, `XMLHttpRequest` e `<Image>`, com suporte a bibliotecas de rede customizadas, como o Expo Fetch, previsto para depois.

**Diferenças do Expo Network**

Por causa disso, apps que usam Expo continuarão vendo o painel "Expo Network", uma implementação separada do framework Expo que registra essas fontes de requisição adicionais, mas com alguns recursos ligeiramente reduzidos.

- Cobertura para eventos de rede específicos do Expo.
- Sem suporte a initiator de requisições.
- Sem integração com o painel Performance.

Estamos trabalhando com o Expo para integrar o Expo Fetch e bibliotecas de rede de terceiros ao nosso novo pipeline de inspeção de rede em versões futuras.

**Recursos não implementados**

No lançamento, estes são os recursos de rede que ainda não são suportados no React Native:

- Eventos de WebSocket
- Mock de respostas de rede
- Simulação de throttling de rede

</details>

<details>
<summary><strong>💡 Tamanho do buffer de prévias de respostas</strong></summary>

Se você estiver inspecionando um grande volume de dados de resposta, saiba que as prévias de respostas são armazenadas em cache em um buffer no dispositivo, com tamanho máximo de 100MB. Isso significa que podemos descartar prévias de respostas (mas não os metadados) se o cache ficar grande demais, começando pela requisição mais antiga.

</details>

#### Dicas úteis {#useful-tips}

- Use a aba Initiator para ver a call stack do ponto em que uma requisição de rede foi iniciada no seu app.
- Eventos de rede também aparecem na faixa Network do painel Performance.

### Performance <div className="label primary">Since 0.83</div>

![Um trace de performance no painel Performance do React Native DevTools](/docs/assets/debugging-rndt-performance.jpg)

O rastreamento de performance permite gravar uma sessão de performance dentro do seu app, para entender como o seu código JavaScript está sendo executado e quais operações levaram mais tempo. No React Native, mostramos a execução de JavaScript, as faixas de performance do React, eventos de rede e [User Timings](https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/User_timing) personalizados, tudo renderizado em uma única linha do tempo de performance.

#### Dicas úteis {#useful-tips}

- Use [Annotations](https://developer.chrome.com/docs/devtools/performance/annotations) (shift + arrastar) para rotular e marcar um trace de performance, o que é útil antes de [baixar e compartilhar](https://developer.chrome.com/docs/devtools/performance/save-trace) o trace com alguém da equipe. As anotações também oferecem uma forma rápida de medir intervalos de tempo em **segundos**.
- Use a [API `PerformanceObserver`](./global-PerformanceObserver.md) no seu app para observar eventos de performance em tempo de execução, o que é útil se você quiser capturar telemetria de performance.

#### Saiba mais {#learn-more}

- [Faixas de performance do React](https://react.dev/reference/dev-tools/react-performance-tracks)
- [Performance APIs > User Timings | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/User_timing)
- ["Debug Like a Senior — React Native Performance Panel" | Software Mansion](https://blog.swmansion.com/react-native-debugging-new-performance-panel-in-react-native-0-83-21ca90871f6d)

### Memory

![Inspecting a heap snapshot in the Memory panel](/docs/assets/debugging-rndt-memory.jpg)

O painel Memory permite tirar um heap snapshot e visualizar o uso de memória do seu código JavaScript ao longo do tempo.

[Record heap snapshots | Chrome DevTools](https://developer.chrome.com/docs/devtools/memory-problems/heap-snapshots)

#### Dicas úteis {#useful-tips}

- Use <kbd>Cmd ⌘</kbd>+<kbd>F</kbd> / <kbd>Ctrl</kbd>+<kbd>F</kbd> para filtrar por objetos específicos no heap.
- Tirar um [allocation timeline report](https://developer.chrome.com/docs/devtools/memory-problems/allocation-profiler) pode ser útil para ver o uso de memória ao longo do tempo como um gráfico, para identificar possíveis memory leaks.

## Recursos do React DevTools {#react-devtools-features}

Nos painéis integrados Components e Profiler, você encontrará todos os recursos da extensão de navegador [React DevTools](https://react.dev/learn/react-developer-tools). Esses funcionam perfeitamente no React Native DevTools.

### React Components

![Selecting and locating elements using the React Components panel](/docs/assets/debugging-rndt-react-components.gif)

O painel React Components permite inspecionar e atualizar a árvore de componentes React renderizada.

- Passe o mouse ou selecione um elemento no DevTools para destacá-lo no dispositivo.
- Para localizar um elemento no DevTools, clique no botão "Select element" no canto superior esquerdo, depois toque em qualquer elemento no aplicativo.

#### Dicas úteis {#useful-tips}

- Props e state em um componente podem ser visualizados e modificados em tempo de execução usando o painel do lado direito.
- Componentes otimizados com [React Compiler](https://react.dev/learn/react-compiler) serão anotados com um badge "Memo ✨".

:::tip

#### Dica profissional: Destacar re-renders {#protip-highlight-re-renders}

Re-renders podem ser um contribuidor significativo para problemas de performance em aplicativos React. DevTools pode destacar re-renders de componentes à medida que acontecem.

- Para habilitar, clique no ícone View Settings (`⚙︎`) e marque "Highlight updates when components render".

![Location of the "highlight updates" setting, next to a recording of the live render overlay](/docs/assets/debugging-rndt-highlight-renders.gif)

:::

### React Profiler

![A profile rendered as a flame graph](/docs/assets/debugging-rndt-react-profiler.jpg)

O painel React Profiler permite gravar perfis de performance para entender o timing de renderizações de componentes e commits do React.

Para mais informações, veja o [guia original de 2018](https://legacy.reactjs.org/blog/2018/09/10/introducing-the-react-profiler.html#reading-performance-data) (note que partes disso podem estar desatualizadas).

## Reconectando DevTools {#reconnecting-devtools}

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
