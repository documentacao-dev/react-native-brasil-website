---
id: viewtoken
title: ViewToken Object Type
ia-translated: true
---

<<<<<<< pt
O objeto `ViewToken` é retornado como uma das propriedades no callback `onViewableItemsChanged` (por exemplo, no componente [FlatList](flatlist)). Ele é exportado pelo [`ViewabilityHelper.js`](https://github.com/facebook/react-native/blob/main/packages/react-native/Libraries/Lists/ViewabilityHelper.js).
||||||| base_en
`ViewToken` object is returned as one of the properties in the `onViewableItemsChanged` callback (for example, in the [FlatList](flatlist) component). It is exported by [`ViewabilityHelper.js`](https://github.com/facebook/react-native/blob/main/packages/react-native/Libraries/Lists/ViewabilityHelper.js).
=======
`ViewToken` object is returned as one of the properties in the `onViewableItemsChanged` callback (for example, in the [FlatList](flatlist) component). It is exported by [`ViewabilityHelper.js`](https://github.com/react/react-native/blob/main/packages/react-native/Libraries/Lists/ViewabilityHelper.js).
>>>>>>> new_en

## Exemplo

```js
{
  item: {key: "key-12"},
  key: "key-12",
  index: 11,
  isViewable: true
}
```

## Chaves e valores

### `index`

Identificador numérico único atribuído ao elemento de dados.

<<<<<<< pt
| Tipo   | Opcional |
||||||| base_en
| Type   | Optional |
=======
This property may be `null` when the viewable element is not an item from the data array, for example when a section header or section footer becomes viewable in [`SectionList`](sectionlist).

| Type   | Optional |
>>>>>>> new_en
| ------ | -------- |
| number | Sim      |

### `isViewable`

Especifica se pelo menos alguma parte do elemento da lista está visível no viewport.

| Tipo    | Opcional |
| ------- | -------- |
| boolean | Não      |

### `item`

Dados do item

| Tipo | Opcional |
| ---- | -------- |
| any  | Não      |

### `key`

Identificador de chave atribuído ao elemento de dados extraído para o nível superior.

| Tipo   | Opcional |
| ------ | -------- |
| string | Não      |

### `section`

Dados da seção do item quando usado com `SectionList`.

| Tipo | Opcional |
| ---- | -------- |
| any  | Sim      |

## Usado por

- [`FlatList`](flatlist)
- [`SectionList`](sectionlist)
- [`VirtualizedList`](virtualizedlist)
