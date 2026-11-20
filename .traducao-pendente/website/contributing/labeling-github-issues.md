---
title: Rotulando Issues do GitHub
ia-translated: true
---

<<<<<<< pt
A maioria das [nossas labels](https://github.com/facebook/react-native/issues/labels) tem um prefixo que fornece uma dica sobre seu propósito.
||||||| base_en
Most of [our labels](https://github.com/facebook/react-native/issues/labels) have a prefix that provides a hint of their purpose.
=======
Most of [our labels](https://github.com/react/react-native/issues/labels) have a prefix that provides a hint of their purpose.
>>>>>>> new_en

<<<<<<< pt
Você notará imediatamente que há dois prefixos de label que dominam a lista, [API:](https://github.com/facebook/react-native/labels?utf8=%E2%9C%93&q=API%3A) e [Component:](https://github.com/facebook/react-native/labels?utf8=%E2%9C%93&q=Component%3A).
||||||| base_en
You'll notice right away there's two label prefixes that dominate the list, [API:](https://github.com/facebook/react-native/labels?utf8=%E2%9C%93&q=API%3A), and [Component:](https://github.com/facebook/react-native/labels?utf8=%E2%9C%93&q=Component%3A).
=======
You'll notice right away there's two label prefixes that dominate the list, [API:](https://github.com/react/react-native/labels?utf8=%E2%9C%93&q=API%3A), and [Component:](https://github.com/react/react-native/labels?utf8=%E2%9C%93&q=Component%3A).
>>>>>>> new_en

Estes geralmente indicam issues e pull requests relacionados a uma API ou Component na biblioteca principal do React Native. Isso nos ajuda a entender, de relance, quais componentes estão em necessidade urgente de documentação ou suporte.

Essas labels são adicionadas automaticamente por um dos nossos [bots](/contributing/bots-reference), mas sinta-se à vontade para ajustá-las se o bot atribuir incorretamente uma issue.

<<<<<<< pt
- A classe de labels `p:` indica uma empresa com a qual mantemos algum tipo de [relacionamento](https://github.com/facebook/react-native/blob/main/ECOSYSTEM.md). Isso inclui Microsoft e Expo, por exemplo. Essas também são adicionadas automaticamente por nossas ferramentas, com base no autor da issue.
- A classe de labels `DX:` indica áreas que lidam com a experiência do desenvolvedor. Use essas para issues que impactam negativamente pessoas que usam o React Native.
- A classe de labels `Tool:` indica ferramentas. CocoaPods, Buck...
- As labels `Resolution:` nos ajudam a comunicar o status de uma issue. Ela precisa de mais informações? O que precisa ser feito antes que ela possa avançar?
- As labels `Type:` são adicionadas por um bot, com base no campo changelog em um pull request. Elas também podem se referir a tipos de issues que não são relatórios de bugs.
- As labels `Platform:` nos ajudam a identificar qual plataforma de desenvolvimento ou SO de destino é afetado pela issue.
||||||| base_en
- The `p:` class of labels denote a company with whom with maintain some sort of [relationship](https://github.com/facebook/react-native/blob/main/ECOSYSTEM.md). These include Microsoft and Expo, for example. These are also added automatically by our tooling, based on the issue author.
- The `DX:` class of labels denote areas that deal with the developer experience. Use these for issues that negatively impact people who use React Native.
- The `Tool:` class of labels denote tooling. CocoaPods, Buck...
- The `Resolution:` labels help us communicate the status of an issue. Does it need more information? What needs to be done before it can move forward?
- The `Type:` labels are added by a bot, based on the changelog field in a pull request. They may also refer to types of issues that are not bug reports.
- The `Platform:` labels help us identify which development platform or target OS is affected by the issue.
=======
- The `p:` class of labels denote a company with whom with maintain some sort of [relationship](https://github.com/react/react-native/blob/main/ECOSYSTEM.md). These include Microsoft and Expo, for example. These are also added automatically by our tooling, based on the issue author.
- The `DX:` class of labels denote areas that deal with the developer experience. Use these for issues that negatively impact people who use React Native.
- The `Tool:` class of labels denote tooling. CocoaPods, Buck...
- The `Resolution:` labels help us communicate the status of an issue. Does it need more information? What needs to be done before it can move forward?
- The `Type:` labels are added by a bot, based on the changelog field in a pull request. They may also refer to types of issues that are not bug reports.
- The `Platform:` labels help us identify which development platform or target OS is affected by the issue.
>>>>>>> new_en

<<<<<<< pt
Quando não tiver certeza sobre o significado de uma label específica, vá para https://github.com/facebook/react-native/labels e olhe o campo de descrição. Faremos o nosso melhor para documentar adequadamente essas labels.
||||||| base_en
When unsure of the meaning of a particular label, go to https://github.com/facebook/react-native/labels and look at the description field. We'll do our best to properly document these.
=======
When unsure of the meaning of a particular label, go to https://github.com/react/react-native/labels and look at the description field. We'll do our best to properly document these.
>>>>>>> new_en

### Ações de Labels

Aplicar uma das seguintes labels pode resultar em uma interação do bot. O objetivo dessas é ajudar na triagem de issues fornecendo uma resposta pré-definida quando considerada necessária.

- Labels que instruem o bot a deixar um comentário com os próximos passos:
  - `Needs: Issue Template`
  - `Needs: Environment Info`
  - `Needs: Verify on Latest Version`
  - `Needs: Repro`

- Labels que instruem o bot a fechar a issue após deixar um comentário explicativo:
  - `Resolution: For Stack Overflow`
  - `Type: Question`
  - `Type: Docs`

- Labels que simplesmente fecham uma issue sem comentário:
  - `Type: Invalid`
