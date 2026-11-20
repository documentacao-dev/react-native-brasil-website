---
ia-translated: true
id: global-intersectionobserverentry
title: IntersectionObserverEntry 🧪
---

import CanaryAPIWarning from './\_canary-channel-api-warning.mdx';

<CanaryAPIWarning />

A interface [`IntersectionObserverEntry`](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry), conforme definida nas especificações Web. Ela descreve a interseção entre o elemento alvo e seu contêiner raiz em um momento específico de transição.

Instâncias de `IntersectionObserverEntry` são entregues a um callback de [`IntersectionObserver`](global-intersectionobserver) em seu parâmetro `entries`.

---

# Reference

## Instance properties

### `boundingClientRect`

Veja a [documentação no MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/boundingClientRect).

Retorna o retângulo de limites do elemento alvo como um `DOMRectReadOnly`.

### `intersectionRatio`

Veja a [documentação no MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/intersectionRatio).

Retorna a razão do `intersectionRect` para o `boundingClientRect`.

### `intersectionRect`

Veja a [documentação no MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/intersectionRect).

Retorna um `DOMRectReadOnly` representando a área visível do alvo.

### `isIntersecting`

Veja a [documentação no MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/isIntersecting).

Um valor Boolean que é `true` se o elemento alvo se intersecta com a raiz do intersection observer. Se isso for `true`, então o `IntersectionObserverEntry` descreve uma transição para um estado de interseção; se for `false`, então você sabe que a transição é de intersectando para não-intersectando.

### `rnRootIntersectionRatio` ⚠️

:::warning[Não padrão]
Esta é uma extensão específica do React Native.
:::

Retorna a razão do `intersectionRect` para o `rootBounds`.

```ts
get rnRootIntersectionRatio(): number;
```

Isso é análogo a `intersectionRatio`, mas calculado em relação à caixa de limites da raiz em vez da caixa de limites do alvo. Isso corresponde à opção `rnRootThreshold` e permite que você determine qual porcentagem da área raiz é coberta pelo elemento alvo.

### `rootBounds`

Veja a [documentação no MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/rootBounds).

Retorna um `DOMRectReadOnly` para a raiz do intersection observer.

### `target`

Veja a [documentação no MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/target).

O `Element` cuja interseção com a raiz mudou.

### `time`

Veja a [documentação no MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/time).

Um `DOMHighResTimeStamp` indicando o momento em que a interseção foi registrada, relativo à origem de tempo do `IntersectionObserver`.
