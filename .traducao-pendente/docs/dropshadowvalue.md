---
ia-translated: true
id: dropshadowvalue
title: Tipo de Objeto DropShadowValue
---

O objeto `DropShadowValue` é aceito pela propriedade de estilo [`filter`](./view-style-props.md#filter) para a função `dropShadow`. Ele é composto por 2 ou 3 comprimentos e uma cor opcional. Esses valores definem coletivamente a cor, posição e desfoque da sombra projetada.

## Exemplo

```js
{
  offsetX: 10,
  offsetY: -3,
  standardDeviation: '15px',
  color: 'blue',
}
```

## Chaves e valores

### `offsetX`

O deslocamento no eixo x. Pode ser positivo ou negativo. Um valor positivo indica direita e negativo indica esquerda.

| Tipo             | Opcional |
| ---------------- | -------- |
| number \| string | Não      |

### `offsetY`

O deslocamento no eixo y. Pode ser positivo ou negativo. Um valor positivo indica para cima e negativo indica para baixo.

| Tipo             | Opcional |
| ---------------- | -------- |
| number \| string | Não      |

### `standardDeviation`

<<<<<<< pt
Representa o desvio padrão usado no algoritmo de [desfoque gaussiano](https://en.wikipedia.org/wiki/Gaussian_blur). Quanto maior o valor, mais desfocada será a sombra. Apenas valores não negativos são válidos. O padrão é 0.
||||||| base_en
Represents the standard deviation used in the [Guassian blur](https://en.wikipedia.org/wiki/Gaussian_blur) algorithm. The larger the value the blurrier the shadow is. Only non-negative values are valid. The default is 0.
=======
Represents the standard deviation used in the [Gaussian blur](https://en.wikipedia.org/wiki/Gaussian_blur) algorithm. The larger the value the blurrier the shadow is. Only non-negative values are valid. The default is 0.
>>>>>>> new_en

<<<<<<< pt
| Tipo            | Opcional |
| --------------- | -------- |
| numer \| string | Sim      |
||||||| base_en
| Type            | Optional |
| --------------- | -------- |
| numer \| string | Yes      |
=======
| Type             | Optional |
| ---------------- | -------- |
| number \| string | Yes      |
>>>>>>> new_en

### `color`

A cor da sombra. O padrão é `black`.

| Tipo                 | Opcional |
| -------------------- | -------- |
| [color](./colors.md) | Sim      |

## Usado por

- [`filter`](./view-style-props.md#filter)
