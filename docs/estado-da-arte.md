# Estado da arte: IA provando matemática (pesquisado em 2026-11-13)

Contexto para a proposta e para o artigo. Antes de citar qualquer item no artigo, conferir na fonte original.

## Marcos

| Data | O quê | Como foi verificado | Fonte |
|---|---|---|---|
| nov/2025–abr/2026 | GPT-5.x Pro, Aristotle (Harmonic), Gemini Deep Think e AxiomProver resolvem ou contribuem para vários problemas de Erdős. A autonomia vai de "totalmente autônoma" a "humano conduziu e reescreveu" | Alguns casos em Lean (#728, #729, #1148), outros só por revisão humana | [The Neuron](https://www.theneuron.ai/explainer-articles/from-erdos-to-axiom-the-open-problems-ai-has-actually-solved/) |
| jan/2026 | Erdős #728: o GPT-5.2 Pro gera a prova, o Aristotle traduz para Lean e corrige erros, e a comunidade reescreve o texto em linguagem natural | Lean + revisão | [The Decoder (Tao)](https://the-decoder.com/terence-tao-says-gpt-5-2-pro-cracked-an-erdos-problem-but-warns-the-win-says-more-about-speed-than-difficulty/) |
| 20/05/2026 | Um modelo interno de raciocínio geral da OpenAI refuta a conjectura de distâncias unitárias de Erdős (1946). Foi testado num lote de problemas de Erdős, sem direcionamento para este | Matemáticos externos; o post não menciona Lean | [OpenAI](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) |
| 02/06/2026 | Declaração de Leiden (endossada pela IMU; assinada por Tao, Scholze, Buzzard e outros): crédito e responsabilidade cabem a humanos; divulgar o uso de IA; rigor proporcional ao risco; prova formal quando possível; anúncio não substitui revisão por pares | — | [leidendeclaration.ai](https://www.leidendeclaration.ai/) |
| 01/08/2026 | Astra (OpenAI, não lançado): 10 resultados (empacotamento de esferas, grupos não sóficos, Erdős #146, #180 e #183...). O modelo gera os argumentos, humanos preparam os manuscritos com o mesmo modelo, e o modelo formaliza em Lean 4.32 + mathlib. Repositório `openai/ten-proofs` (Apache 2.0) | Certificados Lean + Comparator (kernel externo) | [SiliconANGLE](https://siliconangle.com/2026/08/02/openais-astra-solves-10-long-open-math-problems-publishes-proofs/), [Developers Digest](https://www.developersdigest.tech/blog/openai-ten-advances-mathematics-lean-2026), [Implicator](https://www.implicator.ai/openai-astra-10-math-problems-lean-proofs/) |
| 2026 | **Theo**: orquestrador em Claude Code que autoformaliza artigos de pesquisa em Lean. Inclui um "juiz de fidelidade" do enunciado, uma árvore de lemas e um crítico. Formalizou 7 artigos (2 manuscritos da OpenAI) e achou uma falha numa prova publicada. Custou cerca de US$ 1.200 em assinatura | Lean | [arXiv 2606.31134](https://arxiv.org/pdf/2606.31134) |
| set/2026 | **Stellar Colosseum** (Google Research): harness multiagente com exploração, *readiness gate*, decomposição, solução paralela e verificação adversarial ("um defeito fatal concreto basta para rejeitar") | Críticos adversariais, sem Lean | [arXiv 2609.15983](https://arxiv.org/pdf/2609.15983) |

## Ressalvas recorrentes (úteis para a hipótese e para os limites)

- **Literatura:** vários "problemas abertos resolvidos" já tinham solução publicada (#1026; o conjunto sem três pontos colineares).
- **Seleção:** segundo Tao, os problemas de Erdős variam em dificuldade "por várias ordens de magnitude", e só cerca de 1% a 2% dos abertos estão ao alcance da IA atual com pouca ajuda. Falhas não são divulgadas, então não se conhece a taxa real de sucesso.
- **Lean ≠ verdade do problema:** o Lean valida o *enunciado formalizado*. A fidelidade do enunciado e os axiomas extras (uma formalização da prova de Erdős precisou assumir resultados de teoria dos corpos de classes) continuam exigindo julgamento humano. Ver [Automation Without Understanding, arXiv 2607.06377](https://arxiv.org/pdf/2607.06377): "A proof is a product. Understanding is a capacity."

## Ferramentas para o nosso harness

- Lean 4 + mathlib (instalar com `elan`); `lake build`; `#print axioms`; proibir `sorry`.
- Agentes: Claude Code / Codex como orquestrador (no estilo do Theo).
- Calibração: o repositório `openai/ten-proofs` e as formalizações já publicadas do #728.
