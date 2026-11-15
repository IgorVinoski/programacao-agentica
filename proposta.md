# Proposta — Trabalho final de Programação Agêntica

**Grupo:** Igor Vinoski, _[integrante 2]_, _[integrante 3]_
**Data da proposta:** 2026-11-13 _(atualizar se o texto mudar antes do primeiro commit)_

> ⚠️ RASCUNHO. A hipótese precisa ser **de vocês**. Leiam, reescrevam com as próprias palavras e só então façam o commit. O commit deve vir antes de qualquer código.

## Curiosidade

Em 2026, os laboratórios passaram a usar agentes para atacar problemas matemáticos em aberto. Em maio, um modelo interno da OpenAI refutou a conjectura de Erdős sobre distâncias unitárias. Em agosto, o Astra publicou 10 resultados, cada um com certificado em Lean 4. O fluxo que se repete é: **o modelo propõe → o Lean verifica → um humano decide se confia**. Queremos montar esse fluxo em escala de aluno e descobrir o que acontece com **quem opera** esse fluxo sem ser matemático pesquisador.

## Pergunta e hipótese (Igor)

**Pergunta:** quando um agente me entrega uma "prova" de um problema em aberto, ou de difícil solução, e o Lean diz que compila, o que eu realmente consigo afirmar, e o que me falta para confiar nisso?

**Hipótese:** espero que o agente produza argumentos em linguagem natural que me pareçam convincentes em quase todas as tentativas, mas que pouquíssimas, talvez nenhuma, virem Lean sem `sorry`. Espero também que o gargalo seja **formalizar o enunciado com fidelidade**, e não a prova em si. Por fim, espero que eu aceite como "provado" algo que compila e só depois descubra que o enunciado em Lean não era o problema original. O motivo é que não tenho base para ler o enunciado em Lean, então "compilou" vira um selo que substitui a minha leitura.

_[Hipóteses dos outros integrantes, se forem diferentes]_

## Cenário

**Pessoa:** uma pesquisadora de combinatória de uma universidade, sem tempo e cética.
**Pedido, nas palavras dela:** _"Tem uns problemas do Erdős da minha área que estão abertos, mas que ninguém olhou direito. Queria saber se essas IAs conseguem pelo menos atacar algum. Só que não vou ler dez páginas de prova de chatbot: quero algo que me diga o que está realmente verificado e o que é só conversa."_

**O que vamos construir:** um *harness* pequeno, uma espécie de "mini-Astra", que recebe um problema do [erdosproblems.com](https://www.erdosproblems.com) e executa quatro etapas:
1. verifica a literatura, para saber se o problema já foi resolvido;
2. tenta encontrar uma prova ou um contraexemplo, com busca computacional quando couber;
3. formaliza o resultado em Lean 4 com mathlib;
4. gera um relatório honesto: compilou? sobrou `sorry`? quais axiomas foram usados (`#print axioms`)? o enunciado formal é fiel ao original?

**Escopo:** começar calibrando com 1 ou 2 problemas **já resolvidos por IA** (como o #728, que tem formalização em Lean), sem olhar a solução antes. Depois, tentar de 3 a 5 problemas abertos e pouco estudados. Resolver nenhum é um resultado válido: Tao estima que só 1% a 2% dos problemas abertos estão ao alcance da IA atual.

## Como vamos observar

- **Diário** (`registro/`), com commit a cada sessão: antes de cada etapa, previsão de tempo, do que vai ser delegado e de onde vai travar; depois, o que de fato aconteceu.
- **Tabela por problema:** o agente alegou prova? compilou? quantos `sorry`? o enunciado é fiel (julgado por mim antes e depois de estudar)? o resultado já existia na literatura?
- **Histórico das sessões com os agentes**, harness e versões dos modelos, horas trabalhadas e gasto. **Teto de gasto:** R$ _[definir]_ por pessoa.
- **O que eu aceitei, o que refiz e o que precisei aprender** de Lean e de matemática para julgar o resultado.
