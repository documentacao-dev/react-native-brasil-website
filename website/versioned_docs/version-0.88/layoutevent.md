---
ia-translated: true
id: layoutevent
title: Tipo de Objeto LayoutEvent
---

O objeto `LayoutEvent` é retornado no callback como resultado de uma mudança de layout do componente, por exemplo `onLayout` no componente [View](view).

## Exemplo {#example}

```js
{
    layout: {
        width: 520,
        height: 70.5,
        x: 0,
        y: 42.5
    },
    target: 1127
}
```

## Chaves e valores {#keys-and-values}

### `height`

Altura do componente após as mudanças de layout.

| Tipo   | Opcional |
| ------ | -------- |
| number | Não      |

### `width`

Largura do componente após as mudanças de layout.

| Tipo   | Opcional |
| ------ | -------- |
| number | Não      |

### `x`

Coordenada X do componente dentro do componente pai.

| Tipo   | Opcional |
| ------ | -------- |
| number | Não      |

### `y`

Coordenada Y do componente dentro do componente pai.

| Tipo   | Opcional |
| ------ | -------- |
| number | Não      |

### `target`

O node id do elemento que recebe o LayoutEvent.

| Tipo                        | Opcional |
| --------------------------- | -------- |
| number, `null`, `undefined` | Não      |

## Usado por {#used-by}

- [`Image`](image)
- [`Pressable`](pressable)
- [`ScrollView`](scrollview)
- [`Text`](text)
- [`TextInput`](textinput)
- [`TouchableWithoutFeedback`](touchablewithoutfeedback)
- [`View`](view)
