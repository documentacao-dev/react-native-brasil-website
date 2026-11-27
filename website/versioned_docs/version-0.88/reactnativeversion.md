---
id: reactnativeversion
title: ReactNativeVersion
ia-translated: true
---

```tsx
import {ReactNativeVersion} from 'react-native';
```

A API `ReactNativeVersion` expõe a versão do pacote `react-native` resolvido no lado JS. Apps e bibliotecas podem usá-la para verificar compatibilidade ou habilitar comportamentos específicos de cada versão.

:::note

Além disso, já temos [`Platform.constants.reactNativeVersion`](platform#constants) na nossa API pública. **No entanto**, essa é a versão do React Native _**reportada nativamente**_ por plataforma.

:::

## Exemplo {#example}

```tsx
import {ReactNativeVersion} from 'react-native';

const version = ReactNativeVersion.getVersionString(); // 0.88.1
const {major, minor, patch, prerelease} = ReactNativeVersion;
major; // 0
minor; // 88
patch; // 1
prerelease; // null
```

---

# Referência {#reference}

## Propriedades {#properties}

### `major`

```tsx
static major: number;
```

O número da versão major do pacote `react-native` resolvido.

---

### `minor`

```tsx
static minor: number;
```

O número da versão minor do pacote `react-native` resolvido.

---

### `patch`

```tsx
static patch: number;
```

O número da versão patch do pacote `react-native` resolvido.

---

### `prerelease`

```tsx
static prerelease: string | null;
```

A tag de prerelease do pacote `react-native` resolvido, ou `null` para releases estáveis.

## Métodos {#methods}

### `getVersionString()`

```tsx
static getVersionString(): string;
```

Retorna a string de versão completa no formato `major.minor.patch` ou `major.minor.patch-prerelease`.
