---
ia-translated: true
id: targetevent
title: Tipo de Objeto TargetEvent
---

O objeto `TargetEvent` é retornado no callback como resultado de uma mudança de foco, por exemplo `onFocus` ou `onBlur` no componente [TextInput](textinput).

## Exemplo {#example}

```
{
    target: 1127
}
```

## Chaves e valores {#keys-and-values}

### `target`

O node id do elemento que recebe o TargetEvent.

| Tipo                        | Opcional |
| --------------------------- | -------- |
| number, `null`, `undefined` | Não       |

## Usado por {#used-by}

- [`TextInput`](textinput)
- [`TouchableWithoutFeedback`](touchablewithoutfeedback)
