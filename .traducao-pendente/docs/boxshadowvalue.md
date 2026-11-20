---
ia-translated: true
id: boxshadowvalue
title: Tipo de Objeto BoxShadowValue
---

O objeto `BoxShadowValue` é recebido pela propriedade de estilo [`boxShadow`](./view-style-props.md#boxshadow). Ele é composto por 2-4 comprimentos, uma cor opcional e um booleano `inset` opcional. Esses valores definem coletivamente a cor, posição, tamanho e desfoque da sombra da caixa.

## Exemplo

```js
{
  offsetX: 10,
  offsetY: -3,
  blurRadius: '15px',
  spreadDistance: '10px',
  color: 'red',
  inset: true,
}
```

## Chaves e valores

### `offsetX`

O deslocamento no eixo x. Pode ser positivo ou negativo. Um valor positivo indica direita e negativo indica esquerda.

| Tipo             | Opcional |
| ---------------- | -------- |
| number \| string | Não      |

### `offsetY`

O deslocamento no eixo y. Pode ser positivo ou negativo. Um valor positivo indica cima e negativo indica baixo.

| Tipo             | Opcional |
| ---------------- | -------- |
| number \| string | Não      |

### `blurRadius`

<<<<<<< pt
Representa o raio usado no algoritmo de [Guassian blur](https://en.wikipedia.org/wiki/Gaussian_blur). Quanto maior o valor, mais desfocada fica a sombra. Apenas valores não-negativos são válidos. O padrão é 0.
||||||| base_en
Represents the radius used in the [Guassian blur](https://en.wikipedia.org/wiki/Gaussian_blur) algorithm. The larger the value the blurrier the shadow is. Only non-negative values are valid. The default is 0.
=======
Represents the radius used in the [Gaussian blur](https://en.wikipedia.org/wiki/Gaussian_blur) algorithm. The larger the value the blurrier the shadow is. Only non-negative values are valid. The default is 0.
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

### `spreadDistance`

Quanto maior ou menor a sombra cresce ou diminui. Um valor positivo aumentará a sombra, um valor negativo diminuirá a sombra.

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

### `inset`

Se a sombra é inset ou não. Sombras inset aparecerão ao redor do interior da caixa de borda do elemento, em oposição ao exterior.

| Tipo    | Opcional |
| ------- | -------- |
| boolean | Sim      |

## Usado por

- [`boxShadow`](./view-style-props.md#boxshadow)
