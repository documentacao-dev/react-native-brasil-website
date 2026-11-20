---
ia-translated: true
id: handling-text-input
title: Manipulação de Entrada de Texto
---

<<<<<<< pt
[`TextInput`](textinput#content) é um [Core Component](intro-react-native-components) que permite ao usuário inserir texto. Ele tem uma prop `onChangeText` que recebe uma função a ser chamada toda vez que o texto muda, e uma prop `onSubmitEditing` que recebe uma função a ser chamada quando o texto é enviado.
||||||| base_en
[`TextInput`](textinput#content) is a [Core Component](intro-react-native-components) that allows the user to enter text. It has an `onChangeText` prop that takes a function to be called every time the text changed, and an `onSubmitEditing` prop that takes a function to be called when the text is submitted.
=======
[`TextInput`](textinput) is a [Core Component](intro-react-native-components) that allows the user to enter text. It has an `onChangeText` prop that takes a function to be called every time the text changed, and an `onSubmitEditing` prop that takes a function to be called when the text is submitted.
>>>>>>> new_en

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

<<<<<<< pt
A entrada de texto é uma das maneiras pelas quais o usuário interage com o aplicativo. A seguir, vamos ver outro tipo de entrada e [aprender a manipular toques](handling-touches.md).
||||||| base_en
Text input is one of the ways the user interacts with the app. Next, let's look at another type of input and [learn how to handle touches](handling-touches.md).
=======
A `TextInput` is one of many ways for the user to interact with your app. For examples of other ways to handle input, see the documentation on [how to handle touches](handling-touches.md).

Now, let's take a look at [ScrollView](using-a-scrollview), another Core Component.
>>>>>>> new_en
