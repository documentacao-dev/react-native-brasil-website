---
ia-translated: true
id: handling-text-input
title: Manipulação de Entrada de Texto
---

[`TextInput`](textinput) é um [Core Component](intro-react-native-components) que permite ao usuário inserir texto. Ele tem uma prop `onChangeText` que recebe uma função a ser chamada toda vez que o texto muda, e uma prop `onSubmitEditing` que recebe uma função a ser chamada quando o texto é enviado.

Por exemplo, digamos que conforme o usuário digita, você está traduzindo suas palavras para uma língua diferente. Nesta nova língua, cada palavra é escrita da mesma maneira: 🍕. Então a frase "Hello there Bob" seria traduzida como "🍕 🍕 🍕".

```SnackPlayer name=Handling%20Text%20Input
import {useState} from 'react';
import {Text, TextInput, View} from 'react-native';

const PizzaTranslator = () => {
  const [text, setText] = useState('');
  return (
    <View style={{flex: 1, justifyContent: 'center'}}>
      <TextInput
        placeholder="Type here to translate!"
        onChangeText={newText => setText(newText)}
        defaultValue={text}
        style={{
          height: 40,
          padding: 5,
          marginHorizontal: 8,
          borderWidth: 1,
        }}
      />
      <Text style={{padding: 10, fontSize: 42}}>
        {text
          .split(' ')
          .map(word => word && '🍕')
          .join(' ')}
      </Text>
    </View>
  );
};

export default PizzaTranslator;
```

Neste exemplo, armazenamos `text` no state, porque ele muda ao longo do tempo.

Há muito mais coisas que você pode querer fazer com uma entrada de texto. Por exemplo, você pode validar o texto enquanto o usuário digita. Para exemplos mais detalhados, veja a [documentação do React sobre componentes controlados](https://react.dev/reference/react-dom/components/input#controlling-an-input-with-a-state-variable), ou a [documentação de referência para TextInput](textinput.md).

Um `TextInput` é uma das várias formas de o usuário interagir com seu app. Para exemplos de outras formas de lidar com entrada, veja a documentação sobre [como lidar com toques](handling-touches.md).

Agora, vamos dar uma olhada em [ScrollView](using-a-scrollview), outro Core Component.
