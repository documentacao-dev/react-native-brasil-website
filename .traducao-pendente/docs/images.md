---
ia-translated: true
id: images
title: Imagens
---

## Recursos de Imagem Estática

React Native fornece uma maneira unificada de gerenciar imagens e outros recursos de mídia em seus apps Android e iOS. Para adicionar uma imagem estática ao seu app, coloque-a em algum lugar na sua árvore de código-fonte e referencie-a assim:

```tsx
<Image source={require('./my-icon.png')} />
```

O nome da imagem é resolvido da mesma forma que os módulos JS são resolvidos. No exemplo acima, o bundler procurará por `my-icon.png` na mesma pasta que o componente que o requer.

Você pode usar os sufixos `@2x` e `@3x` para fornecer imagens para diferentes densidades de tela. Se você tiver a seguinte estrutura de arquivo:

```
.
├── button.js
└── img
    ├── check.png
    ├── check@2x.png
    └── check@3x.png
```

...e o código de `button.js` contém:

```tsx
<Image source={require('./img/check.png')} />
```

<<<<<<< pt
...o bundler empacotará e servirá a imagem correspondente à densidade de tela do dispositivo. Por exemplo, `check@2x.png` será usado em um iPhone 7, enquanto `check@3x.png` será usado em um iPhone 7 Plus ou um Nexus 5. Se não houver imagem correspondente à densidade de tela, a melhor opção mais próxima será selecionada.
||||||| base_en
...the bundler will bundle and serve the image corresponding to device's screen density. For example, `check@2x.png`, will be used on an iPhone 7, while`check@3x.png` will be used on an iPhone 7 Plus or a Nexus 5. If there is no image matching the screen density, the closest best option will be selected.
=======
...the bundler will bundle and serve the image corresponding to device's screen density. For example, `check@2x.png`, will be used on an iPhone 7, while `check@3x.png` will be used on an iPhone 7 Plus or a Nexus 5. If there is no image matching the screen density, the closest best option will be selected.
>>>>>>> new_en

No Windows, você pode precisar reiniciar o bundler se adicionar novas imagens ao seu projeto.

Aqui estão alguns benefícios que você obtém:

1. Mesmo sistema no Android e iOS.
2. Imagens vivem na mesma pasta que seu código JavaScript. Componentes são autocontidos.
3. Nenhum namespace global, ou seja, você não precisa se preocupar com colisões de nome.
4. Apenas as imagens que são realmente usadas serão empacotadas no seu app.
5. Adicionar e alterar imagens não requer recompilação do app, você pode atualizar o simulador como normalmente faz.
6. O bundler conhece as dimensões da imagem, não há necessidade de duplicá-las no código.
7. Imagens podem ser distribuídas via pacotes [npm](https://www.npmjs.com/).

Para que isso funcione, o nome da imagem em `require` deve ser conhecido estaticamente.

```tsx
// GOOD
<Image source={require('./my-icon.png')} />;

// BAD
const icon = this.props.active
  ? 'my-icon-active'
  : 'my-icon-inactive';
<Image source={require('./' + icon + '.png')} />;

// GOOD
const icon = this.props.active
  ? require('./my-icon-active.png')
  : require('./my-icon-inactive.png');
<Image source={icon} />;
```

Note que fontes de imagem requeridas dessa forma incluem informações de tamanho (width, height) para o Image. Se você precisar escalar a imagem dinamicamente (ou seja, via flex), você pode precisar definir manualmente `{width: undefined, height: undefined}` no atributo de estilo.

<<<<<<< pt
## Recursos Estáticos Não-Imagem
||||||| base_en
## Static Non-Image Resources
=======
### Bundling images in an asset catalog (iOS)

By default the bundler copies each required image, along with every `@2x` and `@3x` variant, into your iOS app as a loose file next to the JavaScript bundle. On iOS you can instead have them compiled into an [asset catalog](https://developer.apple.com/documentation/xcode/managing-assets-with-asset-catalogs), so the system ships only the scale a device needs.

To opt in, set the `RCTUseAssetCatalog` key to `true` in your app's `Info.plist`:

```xml
<key>RCTUseAssetCatalog</key>
<true/>
```

With this enabled, the iOS build script compiles your bundled images into an `RNAssets.bundle` asset catalog at build time. Your `require('./my-icon.png')` calls stay exactly the same, and no changes to your Xcode project are needed.

After changing this setting, make sure to do a clean build.

## Static Non-Image Resources
>>>>>>> new_en

<<<<<<< pt
A sintaxe `require` descrita acima pode ser usada para incluir estaticamente arquivos de áudio, vídeo ou documento em seu projeto também. A maioria dos tipos de arquivo comuns são suportados incluindo `.mp3`, `.wav`, `.mp4`, `.mov`, `.html` e `.pdf`. Veja [padrões do bundler](https://github.com/facebook/metro/blob/master/packages/metro-config/src/defaults/defaults.js#L14-L44) para a lista completa.
||||||| base_en
The `require` syntax described above can be used to statically include audio, video or document files in your project as well. Most common file types are supported including `.mp3`, `.wav`, `.mp4`, `.mov`, `.html` and `.pdf`. See [bundler defaults](https://github.com/facebook/metro/blob/master/packages/metro-config/src/defaults/defaults.js#L14-L44) for the full list.
=======
The `require` syntax described above can be used to statically include audio, video or document files in your project as well. Most common file types are supported including `.mp3`, `.wav`, `.mp4`, `.mov`, `.html`, `.pdf` and more. See [bundler defaults](https://github.com/facebook/metro/blob/main/packages/metro-config/src/defaults/defaults.js#L16-L51) for the full list.
>>>>>>> new_en

Você pode adicionar suporte para outros tipos adicionando uma opção de resolver [`assetExts`](https://metrobundler.dev/docs/configuration#resolver-options) em sua [configuração do Metro](https://metrobundler.dev/docs/configuration).

Uma ressalva é que vídeos devem usar posicionamento absoluto em vez de `flexGrow`, já que informações de tamanho não são atualmente passadas para recursos não-imagem. Esta limitação não ocorre para vídeos que são linkados diretamente no Xcode ou na pasta Assets para Android.

## Imagens de Recursos de App Híbrido

Se você está construindo um app híbrido (algumas UIs em React Native, algumas UIs em código de plataforma) você ainda pode usar imagens que já estão empacotadas no app.

Para imagens incluídas via catálogos de assets do Xcode ou na pasta drawable do Android, use o nome da imagem sem a extensão:

```tsx
<Image
  source={{uri: 'app_icon'}}
  style={{width: 40, height: 40}}
/>
```

Para imagens na pasta assets do Android, use o esquema `asset:/`:

```tsx
<Image
  source={{uri: 'asset:/app_icon.png'}}
  style={{width: 40, height: 40}}
/>
```

Essas abordagens não fornecem verificações de segurança. Cabe a você garantir que essas imagens estejam disponíveis na aplicação. Além disso, você deve especificar as dimensões da imagem manualmente.

## Imagens de Rede

<<<<<<< pt
Muitas das imagens que você exibirá em seu app não estarão disponíveis em tempo de compilação, ou você vai querer carregar algumas dinamicamente para manter o tamanho binário baixo. Diferentemente de recursos estáticos, _você precisará especificar manualmente as dimensões de sua imagem_. É altamente recomendado que você use https também para satisfazer os requisitos de [App Transport Security](publishing-to-app-store.md#1-enable-app-transport-security) no iOS.
||||||| base_en
Many of the images you will display in your app will not be available at compile time, or you will want to load some dynamically to keep the binary size down. Unlike with static resources, _you will need to manually specify the dimensions of your image_. It's highly recommended that you use https as well in order to satisfy [App Transport Security](publishing-to-app-store.md#1-enable-app-transport-security) requirements on iOS.
=======
Many of the images you will display in your app will not be available at compile time, or you will want to load some dynamically to keep the binary size down. Unlike with static resources, _you will need to manually specify the dimensions of your image_. It's highly recommended that you use https as well in order to satisfy [App Transport Security](https://developer.apple.com/documentation/security/preventing_insecure_network_connections) requirements on iOS.
>>>>>>> new_en

```tsx
// GOOD
<Image source={{uri: 'https://reactjs.org/logo-og.png'}}
       style={{width: 400, height: 400}} />

// BAD
<Image source={{uri: 'https://reactjs.org/logo-og.png'}} />
```

### Requisições de Rede para Imagens

Se você quiser definir coisas como HTTP-Verb, Headers ou um Body junto com a requisição de imagem, você pode fazer isso definindo essas propriedades no objeto source:

```tsx
<Image
  source={{
    uri: 'https://reactjs.org/logo-og.png',
    method: 'POST',
    headers: {
      Pragma: 'no-cache',
    },
    body: 'Your Body goes here',
  }}
  style={{width: 400, height: 400}}
/>
```

## Imagens URI Data

Às vezes, você pode estar obtendo dados de imagem codificados de uma chamada de API REST. Você pode usar o esquema URI `'data:'` para usar essas imagens. Assim como para recursos de rede, _você precisará especificar manualmente as dimensões de sua imagem_.

:::info
Isso é recomendado apenas para imagens muito pequenas e dinâmicas, como ícones em uma lista de um BD.
:::

```tsx
// include at least width and height!
<Image
  style={{
    width: 51,
    height: 51,
    resizeMode: 'contain',
  }}
  source={{
    uri: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADMAAAAzCAYAAAA6oTAqAAAAEXRFWHRTb2Z0d2FyZQBwbmdjcnVzaEB1SfMAAABQSURBVGje7dSxCQBACARB+2/ab8BEeQNhFi6WSYzYLYudDQYGBgYGBgYGBgYGBgYGBgZmcvDqYGBgmhivGQYGBgYGBgYGBgYGBgYGBgbmQw+P/eMrC5UTVAAAAABJRU5ErkJggg==',
  }}
/>
```

### Controle de Cache

Em alguns casos você pode querer exibir uma imagem apenas se ela já estiver no cache local, ou seja, um placeholder de baixa resolução até que uma resolução maior esteja disponível. Em outros casos você não se importa se a imagem está desatualizada e está disposto a exibir uma imagem desatualizada para economizar largura de banda. A propriedade `cache` da source dá a você controle sobre como a camada de rede interage com o cache.

- `default`: Use a estratégia padrão da plataforma nativa.
- `reload`: Os dados para a URL serão carregados da fonte de origem. Nenhum dado de cache existente deve ser usado para satisfazer uma requisição de carregamento de URL.
- `force-cache`: Os dados de cache existentes serão usados para satisfazer a requisição, independentemente de sua idade ou data de expiração. Se não houver dados existentes no cache correspondentes à requisição, os dados são carregados da fonte de origem.
- `only-if-cached`: Os dados de cache existentes serão usados para satisfazer uma requisição, independentemente de sua idade ou data de expiração. Se não houver dados existentes no cache correspondentes a uma requisição de carregamento de URL, nenhuma tentativa é feita para carregar os dados da fonte de origem, e o carregamento é considerado como tendo falhado.

```tsx
<Image
  source={{
    uri: 'https://reactjs.org/logo-og.png',
    cache: 'only-if-cached',
  }}
  style={{width: 400, height: 400}}
/>
```

## Imagens do Sistema de Arquivos Local

Veja [CameraRoll](https://github.com/react-native-community/react-native-cameraroll) para um exemplo de uso de recursos locais que estão fora de `Images.xcassets`.

### Recursos Drawable

Android suporta carregar [recursos drawable](https://developer.android.com/guide/topics/resources/drawable-resource) via o tipo de arquivo `xml`. Isso significa que você pode usar [vector drawables](https://developer.android.com/develop/ui/views/graphics/vector-drawable-resources) para renderizar ícones ou [shape drawables](https://developer.android.com/guide/topics/resources/drawable-resource#Shape) para, bem, desenhar formas! Você pode importar e usar esses tipos de recurso da mesma forma que qualquer outro [recurso estático](#static-image-resources) ou [recurso híbrido](#images-from-hybrid-apps-resources). Você tem que especificar as dimensões da imagem manualmente.

Para drawables estáticos que vivem junto com seu código JS, use a sintaxe `require` ou `import` (ambos funcionam da mesma forma):

```tsx
<Image
  source={require('./img/my_icon.xml')}
  style={{width: 40, height: 40}}
/>
```

Para drawables incluídos na pasta drawable do Android (ou seja, `res/drawable`), use o nome do recurso sem a extensão:

```tsx
<Image
  source={{uri: 'my_icon'}}
  style={{width: 40, height: 40}}
/>
```

A única diferença chave entre recursos drawable e outros tipos de imagem é que o asset deve ser referenciado em tempo de compilação da aplicação Android, pois o Android precisa executar o [Android Asset Packaging Tool (AAPT)](https://developer.android.com/tools/aapt2) para empacotar o asset. XML binário, o formato de arquivo que AAPT cria, não pode ser carregado pela rede pelo Metro. Se você alterar o diretório ou nome de um asset, você precisará recompilar a aplicação Android cada vez.

#### Criando recursos drawable XML

Android fornece documentação abrangente sobre cada um dos tipos de recurso drawable suportados em seu guia [Recursos Drawable](https://developer.android.com/guide/topics/resources/drawable-resource), junto com exemplos de arquivos XML brutos. Você pode utilizar ferramentas do Android Studio como o [Vector Asset Studio](https://developer.android.com/studio/write/vector-asset-studio) para criar vector drawables a partir de arquivos Scalable Vector Graphic (SVG) e Adobe Photoshop Document (PSD).

:::info
Você deve tentar evitar referenciar outros recursos no arquivo XML que você cria se quiser tratar seu arquivo XML como um recurso de imagem estática (ou seja, com uma declaração `import` ou `require`). Se você deseja utilizar referências a outros drawables ou atributos, como [listas de estado de cor](https://developer.android.com/guide/topics/resources/color-list-resource) ou [recursos de dimensão](https://developer.android.com/guide/topics/resources/more-resources#Dimension), você deve incluir seu drawable como um [recurso híbrido](#images-from-hybrid-apps-resources) e importá-lo por nome.
:::

### Melhor Imagem do Camera Roll

iOS salva múltiplos tamanhos para a mesma imagem no seu Camera Roll, é muito importante escolher a que está o mais próxima possível por razões de performance. Você não gostaria de usar a imagem de qualidade total 3264x2448 como source ao exibir uma miniatura 200x200. Se houver uma correspondência exata, React Native a escolherá, caso contrário, usará a primeira que for pelo menos 50% maior para evitar desfoque ao redimensionar de um tamanho próximo. Tudo isso é feito por padrão, então você não precisa se preocupar em escrever o código tedioso (e propenso a erros) para fazê-lo você mesmo.

## Por Que Não Dimensionar Tudo Automaticamente?

_No navegador_ se você não der um tamanho a uma imagem, o navegador vai renderizar um elemento 0x0, baixar a imagem e então renderizar a imagem com o tamanho correto. O grande problema com esse comportamento é que sua UI vai pular por todo lado à medida que as imagens carregam, isso faz uma experiência de usuário muito ruim. Isso é chamado de [Cumulative Layout Shift](https://web.dev/cls/).

_No React Native_ esse comportamento é intencionalmente não implementado. É mais trabalho para o desenvolvedor conhecer as dimensões (ou aspect ratio) da imagem remota com antecedência, mas acreditamos que isso leva a uma melhor experiência de usuário. Imagens estáticas carregadas do bundle do app via a sintaxe `require('./my-icon.png')` _podem ser dimensionadas automaticamente_ porque suas dimensões estão disponíveis imediatamente no momento da montagem.

Por exemplo, o resultado de `require('./my-icon.png')` pode ser:

```tsx
{"__packager_asset":true,"uri":"my-icon.png","width":591,"height":573}
```

## Source como um objeto

No React Native, uma decisão interessante é que o atributo `src` é nomeado `source` e não recebe uma string mas um objeto com um atributo `uri`.

```tsx
<Image source={{uri: 'something.jpg'}} />
```

Do lado da infraestrutura, a razão é que isso nos permite anexar metadados a este objeto. Por exemplo, se você está usando `require('./my-icon.png')`, então adicionamos informações sobre sua localização e tamanho reais (não confie neste fato, pode mudar no futuro!). Isso também é prova de futuro, por exemplo, podemos querer suportar sprites em algum momento, em vez de retornar `{uri: ...}`, podemos retornar `{uri: ..., crop: {left: 10, top: 50, width: 20, height: 40}}` e suportar sprites transparentemente em todos os sites de chamada existentes.

Do lado do usuário, isso permite que você anote o objeto com atributos úteis como a dimensão da imagem para calcular o tamanho em que ela vai ser exibida. Sinta-se livre para usá-lo como sua estrutura de dados para armazenar mais informações sobre sua imagem.

## Imagem de Fundo via Aninhamento

<<<<<<< pt
Uma solicitação de funcionalidade comum de desenvolvedores familiarizados com a web é `background-image`. Para lidar com este caso de uso, você pode usar o componente `<ImageBackground>`, que tem as mesmas props que `<Image>`, e adicionar quaisquer filhos que você gostaria de sobrepor em cima dele.

Você pode não querer usar `<ImageBackground>` em alguns casos, já que a implementação é básica. Consulte a [documentação](imagebackground.md) de `<ImageBackground>` para mais informações e crie seu próprio componente customizado quando necessário.
||||||| base_en
A common feature request from developers familiar with the web is `background-image`. To handle this use case, you can use the `<ImageBackground>` component, which has the same props as `<Image>`, and add whatever children to it you would like to layer on top of it.

You might not want to use `<ImageBackground>` in some cases, since the implementation is basic. Refer to `<ImageBackground>`'s [documentation](imagebackground.md) for more insight, and create your own custom component when needed.
=======
To layer content over an image, render an absolutely positioned [`Image`](image.md) inside a [`View`](view.md), followed by the content that should appear on top.
>>>>>>> new_en

```tsx
return (
  <View style={{width: '100%', height: '100%'}}>
    <Image source={...} style={StyleSheet.absoluteFill} />
    <Text>Inside</Text>
  </View>
);
```

<<<<<<< pt
Note que você deve especificar alguns atributos de estilo width e height.
||||||| base_en
Note that you must specify some width and height style attributes.
=======
Note that you must specify some width and height style attributes on the containing `View`.
>>>>>>> new_en

## Estilos de Border Radius do iOS

Por favor, note que as seguintes propriedades de estilo de border radius específicas de canto podem ser ignoradas pelo componente de imagem do iOS:

- `borderTopLeftRadius`
- `borderTopRightRadius`
- `borderBottomLeftRadius`
- `borderBottomRightRadius`

## Decodificação Off-thread

A decodificação de imagem pode levar mais do que o tempo de um frame. Esta é uma das principais fontes de quedas de frame na web porque a decodificação é feita na thread principal. No React Native, a decodificação de imagem é feita em uma thread diferente. Na prática, você já precisa lidar com o caso quando a imagem não foi baixada ainda, então exibir o placeholder por alguns frames a mais enquanto ela está sendo decodificada não requer nenhuma mudança de código.

## Configurando Limites de Cache de Imagem do iOS

<<<<<<< pt
No iOS, expomos uma API para sobrescrever os limites de cache de imagem padrão do React Native. Isso deve ser chamado de dentro do seu código nativo AppDelegate (por exemplo, dentro de `didFinishLaunchingWithOptions`).
||||||| base_en
On iOS, we expose an API to override React Native's default image cache limits. This should be called from within your native AppDelegate code (e.g. within `didFinishLaunchingWithOptions`).
=======
On iOS, we expose an API to override React Native's default image cache limits. Call this early during app startup from your `SceneDelegate` (in `scene:willConnectToSession:options:`) or from `AppDelegate` if you are not using the UIScene lifecycle (for example, within `application:didFinishLaunchingWithOptions:`).
>>>>>>> new_en

```objectivec
RCTSetImageCacheLimits(4*1024*1024, 200*1024*1024);
```

**Parâmetros:**

| Nome           | Tipo   | Requerido | Descrição                         |
| -------------- | ------ | --------- | --------------------------------- |
| imageSizeLimit | number | Sim       | Limite de tamanho de cache de imagem. |
| totalCostLimit | number | Sim       | Limite de custo total de cache.      |

No exemplo de código acima, o limite de tamanho de imagem é definido para 4 MB e o limite de custo total é definido para 200 MB.
