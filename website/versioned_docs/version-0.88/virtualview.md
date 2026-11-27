---
ia-translated: true
id: virtualview
title: VirtualView 🧪
---

import ExperimentalAPIWarning from './\_experimental-api-warning.mdx';

<ExperimentalAPIWarning />

`VirtualView` é um componente principal que se comporta de forma similar a [`View`](view).

Quando é descendente de um [`ScrollView`](scrollview), ele ganha capacidades adicionais de virtualização para reduzir seu consumo de memória quando obscurecido pelo viewport de scroll.

```tsx
<ScrollView>
  <VirtualView>
    <Text>Hello world!</Text>
  </VirtualView>
</ScrollView>
```

Um `VirtualView` sem um ancestral [`ScrollView`](scrollview) não possui nenhuma capacidade de virtualização.

## Virtualization

Quando um `VirtualView` sai da região visível de um [`ScrollView`](scrollview), ele se torna oculto. Quando oculto, um `VirtualView` armazenará em cache seu layout mais recente e pode desmontar seus filhos — um processo chamado virtualização.

Quando um `VirtualView` retorna à região visível de um [`ScrollView`](scrollview), ele se torna visível. Quando visível, seus filhos são _garantidamente_ renderizados. Esta garantia é mantida bloqueando a thread principal de renderizar o próximo frame que revelaria o `VirtualView` até que seus filhos possam ser renderizados.

<img src="/docs/assets/d_virtualview_modes.svg" width="700" alt="Diagram of VirtualView modes and thresholds." />

:::note
Em desenvolvimentos futuros, um `VirtualView` oculto pode em vez disso renderizar seus filhos em um [`<Activity mode="hidden">`](https://react.dev/reference/react/Activity) para preservar o estado pelo maior tempo possível enquanto equilibra a sobrecarga de memória.
:::

### Blocking the Main Thread

Esta é a primeira vez no conjunto de recursos do React Native onde renderizar um componente React pode bloquear a thread principal. Esta é uma nova capacidade habilitada pela [New Architecture](/architecture/landing-page)!

Bloquear a thread principal pode fornecer uma melhor experiência do usuário prevenindo flashes de frames em branco que às vezes ocorrem ao usar componentes como [`FlatList`](flatlist). Também pode habilitar melhor desempenho usando prioridade de thread principal, que também é tipicamente executada em cores de maior desempenho.

No entanto, bloquear a thread principal também vem com trade-offs. Se uma operação de atualização, como montar os filhos de um `VirtualView`, levar muito tempo para terminar, agora pode perder frames. Perder mais de alguns frames pode levar a uma pior experiência do usuário tornando o app lento e não responsivo. Perder muitos frames pode fazer com que o sistema operacional exiba um modal indicando que o app não está respondendo, ou pode até terminar seu app!

:::warning
DevTools atualmente não suporta debugging de JavaScript na thread principal. Isso significa que se você estiver usando breakpoints para debugar código chamado de `onModeChange`, que é executado na thread principal, seu debugger pode congelar.

Debugar todas as outras partes do seu código JavaScript deve funcionar como esperado. Estamos trabalhando para fechar esta lacuna antes de lançar `VirtualView` para canais estáveis do React Native.
:::

### Prerendering

`VirtualView` permite que você se beneficie da renderização de thread principal enquanto mitiga as desvantagens de frames perdidos renderizando mais cedo antes de ser necessário. Isso é chamado de "prerendering".

Por padrão, cada `VirtualView` irá pré-renderizar seus filhos quando se aproximar da região visível de um [`ScrollView`](scrollview). Quando isso acontece, seus filhos serão renderizados em uma thread de background com prioridade menor (usando uma [transition](https://react.dev/reference/react/startTransition)). Isso garante que a thread principal e o React estejam disponíveis para lidar com outras interações críticas do usuário com maior prioridade.

:::note
A lógica de prerender do `VirtualView` atualmente não é configurável. O algoritmo para determinar isso está passando por iteração de design ativa e provavelmente mudará em uma versão futura.
:::

---

## Props

### `children`

Conteúdo a ser renderizado dentro deste `VirtualView`.

| Type                     |
| ------------------------ |
| [React Node](react-node) |

---

### `onModeChange`

Invocado quando o `VirtualView` muda como renderiza seus filhos.

Se um callback for fornecido, ele pode ser invocado de diferentes threads e prioridades dependendo da mudança de estado interno. Isso pode ser detectado verificando a propriedade `mode` no evento:

- Se `mode` for [`VirtualViewMode.Visible`](#virtualviewmode), o callback está sendo invocado da thread principal com prioridade imediata.
- Se `mode` for [`VirtualViewMode.Prerender`](#virtualviewmode) ou [`VirtualViewMode.Hidden`](#virtualviewmode), o callback está sendo invocado de uma thread de background com prioridade de transition.

O callback nunca será invocado consecutivamente com o mesmo valor de `mode`. No entanto, há poucas garantias sobre o sequenciamento de eventos. Além disso, o callback pode nunca ser invocado com [`VirtualViewMode.Visible`](#virtualviewmode) mesmo se se tornar visível, se os filhos foram pré-renderizados com sucesso.

| Type                                               |
| -------------------------------------------------- |
| `md ([ModeChangeEvent](#modechangeevent)) => void` |

---

### `nativeID`

Um identificador para localizar esta view de classes nativas.

| Type   |
| ------ |
| string |

---

### `style`

| Type                           |
| ------------------------------ |
| [View Style](view-style-props) |

---

## Type Definitions

### `ModeChangeEvent`

Argumento fornecido para [`onModeChange`](#onmodechange).

| Type   |
| ------ |
| object |

**Properties:**

| Name          | Type                                | Description                                                                                    |
| ------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------- |
| mode          | [VirtualViewMode](#virtualviewmode) | Novo modo do `VirtualView`.                                                                    |
| target        | element                             | `VirtualView` emitindo este evento.                                                            |
| targetRect    | [Rect](rect)                        | Layout de `target` relativo ao ancestral `ScrollView` mais próximo.                            |
| thresholdRect | [Rect](rect)                        | Layout do threshold que disparou este evento, relativo ao ancestral `ScrollView` mais próximo. |

:::note
Por exemplo, se um `VirtualView` entrar na região visível de um [`ScrollView`](scrollview)...

- `mode` seria [`VirtualViewMode.Visible`](#virtualviewmode)
- `thresholdRect` descreveria o viewport visível do ancestral [`ScrollView`](scrollview) mais próximo
- `targetRect` seria o layout de `target` que sobrepõe com `thresholdRect` (ou seja, está dentro da região visível do [`ScrollView`](scrollview))

:::

### `VirtualViewMode`

Modos possíveis de um `VirtualView`.

| Name      | Value | Description                                          |
| --------- | ----- | ---------------------------------------------------- |
| Visible   | `0`   | View alvo está visível.                              |
| Prerender | `1`   | View alvo está oculta, mas pode ser pré-renderizada. |
| Hidden    | `2`   | View alvo está oculta.                               |

---

## Static Methods

### `createHiddenVirtualView()`

```tsx
static createHiddenVirtualView(height: number): typeof VirtualView;
```

`VirtualView` inicialmente renderiza seus filhos como visíveis, mesmo se estiver inicialmente obscurecido por um ancestral [`ScrollView`](scrollview). Isso ocorre porque quando um componente é inicialmente renderizado, a presença de um ancestral [`ScrollView`](scrollview) — muito menos seu tamanho e posição de scroll — são desconhecidos.

Para casos de uso avançados, `createHiddenVirtualView()` cria um componente que renderiza um `VirtualView` inicialmente oculto com o layout estimado fornecido.

```tsx
const HiddenVirtualView = createHiddenVirtualView(100);

<ScrollView>
  <HiddenVirtualView>
    <Text>Hello world!</Text>
  </HiddenVirtualView>
</ScrollView>;
```

**Parameters:**

| Name                                                        | Type   | Description                                               |
| ----------------------------------------------------------- | ------ | --------------------------------------------------------- |
| height <div className="label basic required">Required</div> | number | Altura estimada da renderização inicial de `VirtualView`. |
