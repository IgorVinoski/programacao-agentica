<!-- Cópia do enunciado oficial, obtida em 2026-11-14 de:
https://elderbernardiifsul.github.io/programacao-agentica/trabalho-final/enunciado.md
PDF oficial: https://elderbernardiifsul.github.io/programacao-agentica/trabalho-final/enunciado.pdf -->

# Trabalho final

**Disciplina:** Programação Agêntica · **Professor:** Élder F. F. Bernardi ·
IFSul, Campus Passo Fundo

## Prelúdio

Há aproximadamente um ano, o desenvolvimento de software foi invadido por um tsunami de agentes. A IA que antes atuava como um "copiloto" passou a ser capaz de, de fato, pilotar: agentes capazes de coordenar trabalhos longos e complexos, escrevendo código com menos erros do que seus antecessores. Este cenário fez com que o mercado de desenvolvimento abraçasse a tecnologia sem titubear, mas também sem ter nenhuma certeza do impacto dessa invasão a longo prazo. Além dos problemas diversos que podem acontecer com o controle do processo de desenvolvimento, passou-se por cima das questões da resposta humana ao novo jeito de trabalhar e até mesmo abriu-se um precedente perigoso ao lançar produtos com verniz de inovação, mas qualidade descartável: o famoso *AI Slop*.

É muito pouco tempo para trazer qualquer conclusão à mesa, mas algumas evidências curiosas aparecem: são exceções os times que comprovadamente melhoraram seu "desempenho" após este um ano; é consenso que a IA impulsiona a produtividade, mas ela é constantemente medida apenas pelo código produzido, menos pelo valor de produto que produz e menos ainda pela saúde da estrutura produtiva de uma companhia, especialmente se for medida a longo prazo. Tampouco a IA tem feito as pessoas trabalharem menos, pelo contrário. Há muito ainda o que acontecer e a acomodação da realidade ainda não aconteceu. Tem espaço para bastante pesquisa e experimentações no sentido de entender primeiro o que realmente tem valor naquilo que se propõe a ser uma solução "com IA" e quão seguro é; há incertezas sobre como aplicar engenharia de software onde os agentes são os escritores de código, mas também os especificadores e planejadores de seu próprio trabalho: qual problema ou necessidade está sendo atacada? Quem vai usar e por quanto tempo vai usar? Dá certo um produto que é concebido e desenvolvido numa semana? Será que dá *mesmo* pra desenvolver em *uma semana*? Como ficam os programadores de verdade no meio disso tudo?

A abordagem da disciplina procurou equilibrar este caos, trazer conhecimento para ler o mapa e não se perder *tanto*, principalmente no sentido do objetivo próprio dela, que é a formação de pessoas. Há todas essas oportunidades, avanços, riscos, problemas e questões que enfurecem, apaixonam e dividem, mas uma coisa é inegável: a ciência e a tecnologia que nos trouxeram até aqui são fascinantes. E o meu posicionamento é de que ciência nunca deve ser ignorada. Por isso a proposta deste trabalho final é trazer a programação agêntica para o foco da observação. Encontrar um problema e uma oportunidade reais que hipoteticamente dão *match* e testar essa hipótese! Testar desde se pode funcionar, se é viável fazer, se o resultado vale a pena etc. Mas, mais que tudo, trazer a coisa para a primeira pessoa: testar como a gente (e não os agentes :D) encara tudo isso: o que precisa aprender, que tipo de visão necessita para identificar o que vale a pena ser feito, como pode ser feito, o que se pode e não pode delegar à IA, que tipo de tecnologia serve ou não para um cenário.

Pra finalizar este prelúdio, invoco a mãe da inovação, da ciência e da maioria das coisas legais que aconteceram até aqui: a **curiosidade**. No enunciado seguem alguns cenários em que pensei, outros que o modelo sugeriu, mas quero que cada um se pergunte: "onde eu tô hoje, com o que sei, o que tenho *curiosidade* de descobrir?" A resposta a esta pergunta deve nortear a escolha do que experimentar! O que estudar, metodologia, a gente vai construindo. Tem bastante trabalho bom para se inspirar, conhecimento amplo e disponível e, agora com os agentes, força potencial de trabalho para executar.

Se tudo isso vai dar bom ou não, ninguém sabe. Mas é fato que não volta atrás (salvo grandes transformações). E se for pra voltar atrás ou para avançar neste mundo, que sejamos os primeiros a desenhar o mapa.

Boa expedição!

## Enunciado

Em grupos de duas ou três pessoas, durante quatro semanas, vocês escolhem
algo que têm curiosidade de descobrir sobre desenvolver software com agentes.
Depois montam um cenário em que essa curiosidade apareça, constroem algo
nesse cenário e observam o que acontece. O grupo apresenta o que descobriu em
cinco minutos. Cada pessoa escreve o próprio artigo, de até seis páginas.

Vocês estudam quem desenvolve e como desenvolve: como você julgou se o
problema e a solução davam *match*, se era viável e se valia a pena; o que
precisou aprender; o que delegou e o que teve de refazer; que método ou
tecnologia serviu e qual não serviu. O produto faz parte do cenário e prende o
trabalho à realidade. Ele pode ficar incompleto, e a qualidade dele não entra
na nota.

Quatro palavras organizam o trabalho:

- **Curiosidade:** o que você quer descobrir sobre desenvolver com agentes.
- **Hipótese:** o que você espera encontrar, escrito antes de começar.
- **Cenário:** a pessoa, o problema e o produto que dão chão ao trabalho.
- **Mapa:** o artigo, escrito para quem fizer esse caminho depois.

### 1. Curiosidade e hipótese

Comece pela pergunta do prelúdio: "onde eu tô hoje, com o que sei, o que
tenho curiosidade de descobrir?" A curiosidade pode ser sobre:

- **Você:** consigo explicar e manter um código que o agente escreveu? O que
  eu delego e depois tenho de refazer? As minhas previsões de prazo melhoram
  ao longo do trabalho?
- **Um método:** desenvolver com especificação antes do código (SDD,
  *spec-driven development*) funciona para este tipo de produto? Escrever os
  testes antes muda o que eu aceito do agente?
- **Um harness:** consigo montar um modo de trabalho meu, a partir das skills e
  metodologias que já existem? Como ele se sai? O que aprendi montando?
- **Uma tecnologia:** o que eu preciso aprender para um modelo local dar conta
  deste cenário? Como eu decido se o problema precisa de IA dentro do
  produto?

A curiosidade vira hipótese quando você escreve, **antes de começar a
construir**, duas coisas:

> **Pergunta:** o que você quer descobrir.
>
> **Hipótese:** o que você espera encontrar, e por quê.

Um exemplo:

> **Pergunta:** como é desenvolver com especificação antes do código um
> sistema pequeno cujo pedido muda no meio do caminho?
>
> **Hipótese:** espero que a especificação me ajude no começo, quando ainda
> não conheço o problema, e vire um peso quando o pedido mudar, porque
> atualizar o documento parece mais lento do que pedir a mudança direto ao
> agente.

A hipótese não precisa comparar duas formas de trabalhar nem ser um teste de
certo ou errado. Ela registra o que você esperava, para que o artigo possa
contar o que se confirmou, o que mudou e o que surpreendeu. Por isso ela vem
antes. Se a hipótese mudar no caminho, escreva a nova embaixo da antiga, com
a data e o motivo. Hipótese que não se confirma é resultado e não perde nota.

### 2. Cenário

O cenário tem uma pessoa, um problema e o que vocês vão construir para ela.
O prelúdio fala em problema real. Aqui, real quer dizer plausível: a pessoa
não precisa existir, mas alguém poderia ter esse problema e usar essa
solução. Serve um comércio, um setor do campus, um produtor rural, um
laboratório ou a própria turma. Escrevam o pedido como essa pessoa
escreveria: com as palavras dela e sem os detalhes que ela esqueceria de
dizer.

Escolham um cenário em que a curiosidade de vocês apareça durante o
trabalho. Se a pergunta é sobre manter um código que o agente escreveu, o
cenário precisa de manutenção. Se é sobre segurança, precisa de algo que
valha a pena atacar.

O cenário é obrigatório mesmo quando a curiosidade é sobre um método ou um
harness: sem algo para construir, vocês não têm como ver o método ou o
harness funcionando.

O produto pode ter IA dentro ou não. Se tiver, discutam no artigo se ela era
necessária.

O produto precisa caber nas semanas 2 e 3, com folga até a quinta-feira da
semana 4. Ele pode ficar incompleto, desde que o registro mostre o que foi
cortado e por quê.

Em [cenarios.md](https://elderbernardiifsul.github.io/programacao-agentica/trabalho-final/cenarios.md) há sugestões para inspirar. Usem uma delas,
misturem ou montem a de vocês.

### 3. Grupo

O grupo existe para trocar ideias, dividir conhecimento e construir junto.
Ele compartilha uma curiosidade e um cenário. A hipótese pode ser a mesma
para todos ou uma para cada pessoa, desde que todas estejam escritas na
proposta. Cada pessoa registra a própria experiência. Se duas pessoas viveram
a mesma tarefa de jeitos diferentes, essa diferença é um dado e merece ir
para o artigo.

Quem colaborou com o grupo pode usar no próprio artigo o trabalho dos
colegas, declarando o que foi feito em grupo e o que foi feito pela pessoa.

### 4. Registro

O que você afirmar no seu artigo precisa aparecer no registro feito durante o
trabalho. O registro vive no repositório git do grupo, em formato livre:
diário, notas, histórico das sessões com o agente. Façam commits ao longo do
trabalho: a data do commit é a prova de que a anotação veio antes do
resultado. Não reconstruam o registro de memória no fim, e anotem cada
previsão antes da etapa a que ela se refere.

Vale a pena anotar, conforme a pergunta de vocês:

- antes de uma etapa, o que você espera: tempo, o que vai delegar, onde acha
  que vai dar problema; depois, o que aconteceu;
- horas e gasto com modelos;
- o que o agente fez e você aceitou, o que você refez, o que nem delegou;
- onde travou, o que precisou aprender, o que surpreendeu;
- harness, modelo e versões usados.

Vocês combinam com o professor, na conversa da proposta, como vão observar. O
combinado pode ser ajustado nos checkpoints.

Cuidados, porque o repositório será compartilhado:

- não coloquem senha, token ou credencial no repositório;
- não enviem dado pessoal real para o modelo;
- rodem skills, distribuições e código de terceiros em ambiente descartável
  antes de usar;
- definam um teto de gasto antes de começar e registrem o que gastaram.

### 5. Calendário

| Quando | O que acontece |
|---|---|
| Semana 1 | Curiosidade, cenário e hipótese. Cada grupo cria o repositório git, dá acesso ao professor, escreve uma proposta de meia página e conversa com o professor em aula. |
| Semanas 2 e 3 | Desenvolvimento. Ao fim de cada semana, em aula, há um checkpoint: cada grupo conta em dois minutos o que viu até ali, e o professor pode perguntar a qualquer integrante sobre o que foi construído. |
| Semana 4, até quinta | Fechamento da construção e preparo da apresentação. |
| Semana 4, sexta | Apresentação do grupo, em aula. |
| Segunda-feira seguinte, pela manhã | Último commit do repositório, com o artigo de cada pessoa. |

Tudo é entregue pelo repositório git do grupo: a proposta, o registro, o que
vocês construírem e o artigo de cada pessoa, em PDF, na pasta `artigos/`. O professor acompanha o repositório
desde a semana 1, e o que conta é o histórico de commits, não uma cópia
enviada no fim. A proposta tem a pergunta e a hipótese (de cada pessoa, se forem
diferentes), o cenário com o pedido da pessoa, o que
vocês pretendem construir e como pensam em observar. Ela entra no repositório
em um commit anterior a qualquer código. A versão combinada na conversa com o
professor vale como a hipótese original.

### 6. Apresentação

São cinco minutos por grupo, em aula, com o foco nos aprendizados. Mostrar o
produto funcionando é desejável, mas não é obrigatório. Uma ordem possível:

1. a curiosidade e a hipótese;
2. o cenário e o que vocês construíram;
3. o que aconteceu, e se a hipótese se sustentou;
4. o que vocês aprenderam que não esperavam;
5. o que diriam a quem fosse começar o mesmo caminho.

Cada integrante pode comentar o que foi particular na própria experiência. As
perguntas da turma depois da apresentação podem entrar no artigo.

### 7. Artigo: o mapa

Cada pessoa escreve o próprio artigo, de até seis páginas, no modelo de
artigos da SBC. Escreva para um colega que vai começar algo parecido no
próximo semestre: ele precisa saber por onde você foi, onde se perdeu e até
onde o seu mapa vale.

O artigo precisa mostrar:

- a pergunta e a hipótese como foram escritas na proposta, com a data;
- o relato em primeira pessoa do que aconteceu, apoiado no registro;
- o que foi feito em grupo e o que foi feito por você;
- os limites: o que a sua evidência não sustenta;
- como você usou IA para escrever o artigo.

Uma estrutura possível: curiosidade e hipótese; cenário e como você
observou; o que aconteceu; o que você aprendeu (o que delegaria, o que não
delegaria e onde se perdeu); limites e recado; referências. Deixe a seção
sobre o que você aprendeu ser a mais longa.

### 8. Avaliação

A nota de cada pessoa vem de quatro critérios, de 25% cada. Coerência,
evidência e primeira pessoa são lidas no artigo. O domínio é observado nas
respostas da pessoa nos checkpoints e na apresentação.

| Critério | O que o professor observa |
|---|---|
| Coerência | O cenário e o que você construiu permitem responder à sua pergunta. |
| Evidência | O que o artigo afirma aparece no registro feito durante o trabalho. |
| Primeira pessoa | O artigo traz descobertas sobre você e sobre desenvolver com agentes, e não só uma descrição do produto. |
| Domínio | Você explica a parte que fez e as escolhas que declarou no artigo. |

Não perdem nota, quando registrados e explicados: hipótese que não se
confirmou, previsão errada, produto menor do que o planejado.

O trabalho fica insuficiente se a hipótese foi escrita depois do resultado, se
o artigo afirma o que o registro não mostra, ou se você não consegue explicar
a parte que declarou como sua.
