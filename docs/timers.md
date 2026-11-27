---
ia-translated: true
id: timers
title: Timers
---

Timers são uma parte importante de uma aplicação e o React Native implementa os [timers do navegador](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Timeouts_and_intervals).

## Timers

- `setTimeout` e `clearTimeout`
- `setInterval` e `clearInterval`
- `setImmediate` e `clearImmediate`
- `requestAnimationFrame` e `cancelAnimationFrame`

`requestAnimationFrame(fn)` não é o mesmo que `setTimeout(fn, 0)` - o primeiro disparará depois que todos os frames forem liberados, enquanto o último disparará o mais rápido possível (mais de 1000x por segundo em um iPhone 5S).

`setImmediate` é executado no final do bloco de execução JavaScript atual, logo antes de enviar a resposta em lote de volta para o nativo. Observe que se você chamar `setImmediate` dentro de um callback `setImmediate`, ele será executado imediatamente, não retornará para o nativo entre as chamadas.

A implementação de `Promise` usa `setImmediate` como sua implementação de assincronia.

:::note
Ao depurar no Android, se os horários entre o debugger e o dispositivo ficarem dessincronizados; coisas como animação, comportamento de eventos, etc., podem não funcionar corretamente ou os resultados podem não ser precisos.
Por favor, corrija isso executando ``adb shell "date `date +%m%d%H%M%Y.%S%3N`"`` na sua máquina de depuração. Acesso root é necessário para uso em dispositivos reais.
:::
