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

<<<<<<< pt
`requestAnimationFrame(fn)` não é o mesmo que `setTimeout(fn, 0)` - o primeiro disparará depois que todos os frames forem liberados, enquanto o último disparará o mais rápido possível (mais de 1000x por segundo em um iPhone 5S).
||||||| base_en
`requestAnimationFrame(fn)` is not the same as `setTimeout(fn, 0)` - the former will fire after all the frames have flushed, whereas the latter will fire as quickly as possible (over 1000x per second on a iPhone 5S).
=======
`requestAnimationFrame(fn)` is not the same as `setTimeout(fn, 0)` - the former will fire after all the frames have flushed, whereas the latter will fire as quickly as possible (over 1000x per second on an iPhone 5S).
>>>>>>> new_en

`setImmediate` é executado no final do bloco de execução JavaScript atual, logo antes de enviar a resposta em lote de volta para o nativo. Observe que se você chamar `setImmediate` dentro de um callback `setImmediate`, ele será executado imediatamente, não retornará para o nativo entre as chamadas.

A implementação de `Promise` usa `setImmediate` como sua implementação de assincronia.

:::note
Ao depurar no Android, se os horários entre o debugger e o dispositivo ficarem dessincronizados; coisas como animação, comportamento de eventos, etc., podem não funcionar corretamente ou os resultados podem não ser precisos.
Por favor, corrija isso executando ``adb shell "date `date +%m%d%H%M%Y.%S%3N`"`` na sua máquina de depuração. Acesso root é necessário para uso em dispositivos reais.
:::
<<<<<<< pt

## InteractionManager

:::warning Deprecated
O comportamento do `InteractionManager` foi alterado para ser o mesmo que `setImmediate`, que deve ser usado em vez disso.
:::

Uma razão pela qual aplicativos nativos bem construídos parecem tão suaves é evitando operações caras durante interações e animações. No React Native, atualmente temos uma limitação de que existe apenas uma única thread de execução JS, mas você pode usar `InteractionManager` para garantir que trabalhos de longa duração sejam agendados para iniciar após quaisquer interações/animações terem sido concluídas.

Aplicações podem agendar tarefas para serem executadas após interações com o seguinte:

```tsx
InteractionManager.runAfterInteractions(() => {
  // ...long-running synchronous task...
});
```

Compare isso com outras alternativas de agendamento:

- requestAnimationFrame(): para código que anima uma view ao longo do tempo.
- setImmediate/setTimeout/setInterval(): executa código mais tarde, observe que isso pode atrasar animações.
- runAfterInteractions(): executa código mais tarde, sem atrasar animações ativas.

O sistema de manipulação de toque considera um ou mais toques ativos como uma 'interação' e atrasará callbacks `runAfterInteractions()` até que todos os toques tenham terminado ou sido cancelados.

`InteractionManager` também permite que aplicações registrem animações criando um 'handle' de interação no início da animação e limpando-o ao concluir:

```tsx
const handle = InteractionManager.createInteractionHandle();
// run animation... (`runAfterInteractions` tasks are queued)
// later, on animation completion:
InteractionManager.clearInteractionHandle(handle);
// queued tasks run if all handles were cleared
```
||||||| base_en

## InteractionManager

:::warning Deprecated
The `InteractionManager` behavior has been changed to be the same as `setImmediate`, which should be used instead.
:::

One reason why well-built native apps feel so smooth is by avoiding expensive operations during interactions and animations. In React Native, we currently have a limitation that there is only a single JS execution thread, but you can use `InteractionManager` to make sure long-running work is scheduled to start after any interactions/animations have completed.

Applications can schedule tasks to run after interactions with the following:

```tsx
InteractionManager.runAfterInteractions(() => {
  // ...long-running synchronous task...
});
```

Compare this to other scheduling alternatives:

- requestAnimationFrame(): for code that animates a view over time.
- setImmediate/setTimeout/setInterval(): run code later, note this may delay animations.
- runAfterInteractions(): run code later, without delaying active animations.

The touch handling system considers one or more active touches to be an 'interaction' and will delay `runAfterInteractions()` callbacks until all touches have ended or been cancelled.

`InteractionManager` also allows applications to register animations by creating an interaction 'handle' on animation start, and clearing it upon completion:

```tsx
const handle = InteractionManager.createInteractionHandle();
// run animation... (`runAfterInteractions` tasks are queued)
// later, on animation completion:
InteractionManager.clearInteractionHandle(handle);
// queued tasks run if all handles were cleared
```
=======
>>>>>>> new_en
