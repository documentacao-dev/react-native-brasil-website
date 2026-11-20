---
ia-translated: true
title: Lançando 0.56
author: Lorenzo Sciandra
authorTitle: Core Maintainer & React Native Developer at Drivetribe
authorURL: 'https://github.com/kelset'
authorImageURL: 'https://avatars2.githubusercontent.com/u/16104054?s=460&v=4'
authorTwitter: kelset
tags: [announcement, release]
---

A tão aguardada versão 0.56 do React Native está agora disponível 🎉. Este blog post destaca algumas das [mudanças](https://github.com/react-native-community/react-native-releases/blob/master/CHANGELOG.md#highlights) introduzidas neste novo lançamento. Também queremos aproveitar a oportunidade para explicar o que nos manteve ocupados desde março.

### O dilema das mudanças breaking, ou, "quando lançar?" {#the-breaking-changes-dilemma-or-when-to-release}

O [Guia do Contribuidor](https://github.com/facebook/react-native/blob/master/CONTRIBUTING.md) explica o processo de integração pelo qual todas as mudanças no React Native passam. O projeto é composto por [muitas ferramentas diferentes](https://github.com/facebook/react-native-website/issues/370), requerendo coordenação e suporte constante para manter tudo funcionando adequadamente. Adicione a isso a vibrante comunidade open source que contribui de volta para o projeto, e você terá uma noção da escala alucinante de tudo isso.

Com a impressionante adoção do React Native, mudanças breaking devem ser feitas com muito cuidado, e o processo não é tão suave quanto gostaríamos. Uma decisão foi tomada para pular os lançamentos de abril e maio para permitir que a equipe principal integre e teste um novo conjunto de mudanças breaking. [Canais de comunicação dedicados da comunidade](https://github.com/react-native-community/react-native-releases/issues/14) foram usados ao longo do caminho para garantir que o lançamento de junho de 2018 (`0.56.0`) seja o mais livre de problemas possível para adotar por aqueles que pacientemente aguardaram pelo lançamento estável.

O `0.56.0` é perfeito? Não, como todo software por aí: mas chegamos a um ponto onde o tradeoff entre "esperar por mais estabilidade" versus "os testes levaram a resultados bem-sucedidos, então podemos avançar" que sentimos prontos para lançá-lo. Além disso, estamos cientes [de](https://github.com/facebook/react-native/issues/19955) [alguns](https://github.com/facebook/react-native/issues/19827) [problemas](https://github.com/facebook/react-native/issues/19763) [que](https://github.com/facebook/react-native/issues/19859) não estão resolvidos no lançamento final `0.56.0`. A maioria dos desenvolvedores não deve ter problemas atualizando para `0.56.0`. Para aqueles que estão bloqueados pelos problemas mencionados, esperamos vê-los por aí em nossas discussões e estamos ansiosos para trabalhar com vocês em uma solução para esses problemas.

Você pode considerar `0.56.0` como um bloco de construção fundamental em direção a um framework mais estável: provavelmente levará uma semana ou duas de adoção generalizada antes que todos os casos extremos sejam polidos, mas isso levará a um lançamento ainda melhor de julho de 2018 (`0.57.0`).

Gostaríamos de concluir esta seção agradecendo [todos os 67 contribuidores que trabalharam em um total de 818 commits](https://github.com/facebook/react-native/compare/v0.55.4...v0.56.0-rc.4) (!) que ajudarão a tornar seus apps ainda melhores 👏.

E agora, sem mais delongas...

## As Grandes Mudanças {#the-big-changes}

### Babel 7

Como você pode saber, a ferramenta transpiladora que permite que todos nós usemos os recursos mais recentes e melhores do JavaScript, Babel, está mudando para [v7 em breve](https://babeljs.io/blog/2017/12/27/nearing-the-7.0-release). Como esta nova versão traz algumas mudanças importantes, sentimos que agora seria um bom momento para atualizar, permitindo que o [Metro](https://github.com/facebook/metro) [aproveite suas melhorias](https://github.com/facebook/metro/issues/92).

Se você se encontrar com problemas ao atualizar, consulte a [seção de documentação relacionada a isso](https://new.babeljs.io/docs/en/next/v7-migration.html).

### Modernizando o suporte Android {#modernizing-android-support}

No Android, muito do ferramental ao redor mudou. Atualizamos para [Gradle 3.5](https://github.com/facebook/react-native/commit/699e5eebe807d1ced660d2d2f39b5679d26925da), [Android SDK 26](https://github.com/facebook/react-native/commit/065c5b6590de18281a8c592a04240751c655c03c), [Fresco para 1.9.0, e OkHttp para 3.10.0](https://github.com/facebook/react-native/commit/6b07602915157f54c39adbf0f9746ac056ad2d13) e até o [alvo da API NDK para API 16](https://github.com/facebook/react-native/commit/5ae97990418db613cd67b1fb9070ece976d17dc7). Essas mudanças devem ocorrer sem problemas e resultar em builds mais rápidos. Mais importante, isso ajudará os desenvolvedores a cumprir com os [novos requisitos da Play Store](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html) que entrarão em vigor no próximo mês.

Relacionado a isso, gostaríamos de agradecer particularmente [Dulmandakh](https://github.com/dulmandakh) pelos muitos PRs enviados para tornar isso possível 👏.

Existem mais alguns passos que precisam ser dados nesta direção, e você pode acompanhar o planejamento futuro e discussão sobre atualizar o suporte Android na [issue dedicada](https://github.com/facebook/react-native/issues/19297) (e uma lateral para o [JSC](https://github.com/facebook/react-native/issues/19737)).

### Novos Node, Xcode, React e Flow – nossa! {#new-node-xcode-react-and-flow--oh-my}

Node 8 é agora o padrão para React Native. Na verdade já estava sendo testado, mas colocamos os dois pés para frente já que o Node 6 entrou em modo de manutenção. React também foi atualizado para 16.4, que traz uma tonelada de correções com ele.

Estamos descontinuando o suporte para iOS 8, [tornando iOS 9 a versão mais antiga do iOS que pode ser alvo](https://github.com/facebook/react-native/commit/f50df4f5eca4b4324ff18a49dcf8be3694482b51). Não prevemos que isso seja um problema, já que qualquer dispositivo que pode executar iOS 8, pode ser atualizado para iOS 9. Esta mudança nos permitiu remover código raramente usado que implementava soluções alternativas para dispositivos mais antigos executando iOS 8.

A toolchain de integração contínua foi atualizada [para usar Xcode 9.4](https://github.com/facebook/react-native/commit/c55bcd6ea729cdf57fc14a5478b7c2e3f6b2a94d), garantindo que todos os testes iOS sejam executados nas ferramentas de desenvolvedor mais recentes fornecidas pela Apple.

Atualizamos para [Flow 0.75](https://github.com/facebook/react-native/commit/6264b6932a08e1cefd83c4536ff7839d91938730) para usar o novo formato de erro [que muitos desenvolvedores apreciam](https://twitter.com/dan_abramov/status/998610821096857602). Também criamos tipos para muitos mais componentes. Se você ainda não está aplicando tipagem estática em seu projeto, considere usar Flow para identificar problemas conforme você codifica em vez de em runtime.

### E muitas outras coisas... {#and-a-lot-of-other-things}

Por exemplo, YellowBox foi [substituído](https://github.com/facebook/react-native/commit/d0219a0301e59e8b0ef75dbd786318d4b4619f4c) com uma nova implementação que torna o debugging muito melhor.

Para as notas de lançamento completas, consulte o [changelog completo aqui](https://github.com/react-native-community/react-native-releases/blob/master/CHANGELOG.md). E lembre-se de ficar de olho no [guia de atualização](/docs/upgrading) para evitar problemas ao mudar para esta nova versão.

---

Uma nota final: a partir desta semana, a equipe principal do React Native retomará as reuniões mensais. Vamos nos certificar de manter todos atualizados sobre o que é coberto, e garantir manter seu feedback à mão para reuniões futuras.

Feliz codificação a todos!

[Lorenzo](https://twitter.com/Kelset), [Ryan](https://github.com/turnrye), e toda a [equipe principal do React Native](https://twitter.com/reactnative)

**PS:** como sempre, gostaríamos de lembrar a todos que React Native ainda está em versionamento 0.x devido às muitas mudanças ainda em andamento - então lembre-se ao atualizar que sim, provavelmente, algo pode ainda crashar ou estar quebrado. Seja prestativo uns com os outros nas issues e ao enviar PRs - e lembre-se de seguir o [CoC](https://code.fb.com/codeofconduct/) aplicado: sempre há um humano do outro lado da tela.
