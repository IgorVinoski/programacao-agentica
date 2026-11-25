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

---

# Atualização (pesquisado em 2026-11-25)

## Novos marcos

| Data | O quê | Como foi verificado | Fonte |
|---|---|---|---|
| jan/2026 | **Numina-Lean-Agent**: Claude Code + um pacote MCP para Lean (inclui o `lean-lsp-mcp`). Com Claude Opus 4.5 resolve 12/12 do Putnam 2025. Código aberto | Lean | [arXiv 2601.14027](https://arxiv.org/html/2601.14027v1) |
| 03/08/2026 | Quanta: por que os problemas de Erdős estão caindo para a IA | — | [Quanta](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/) |
| 04/09/2026 | **Anthropic formaliza o Último Teorema de Fermat** em Lean: cerca de 11 dias de agentes Claude em grande parte autônomos, cerca de 13 milhões de linhas, só os 3 axiomas padrão; um *comparator* confirma que o enunciado bate com o do mathlib. As primeiras tentativas falharam porque os agentes "perdiam o estado do projeto"; a correção foi um **DAG compartilhado de enunciados** que cada agente consulta para escolher o próximo lema. Plataforma: Prove2Me (DAPLab/Columbia), com "missões" paralelas | Lean + comparator | [Anthropic](https://www.anthropic.com/news/formalizing-fermats-last-theorem), [DAPLab](https://daplab.cs.columbia.edu/general/2026/09/09/fermats-last-theorem-agents.html), [TechRadar](https://techradar.com/pro/anthropic-formalizes-fermats-last-theorem-like-never-before-using-claude-but-it-still-took-11-days-to-write-out) |
| 2026 | ICML AI4Math: **seis subagentes + uma máquina de estados determinística em shell** fazendo a coordenação; 30/34 desafios, sem humano no loop | Lean local | [ICML 2026](https://icml.cc/virtual/2026/82590) |
| 2026 | **LeanMarathon**: o próprio arquivo Lean é o esqueleto da prova *e* a memória compartilhada; 4 agentes com contrato (construir, auditar, provar, reparar) e um *gate* de CI determinístico | Lean | [ResearchGate](https://www.researchgate.net/publication/406040187_LeanMarathon_Toward_Reliable_AI_Co-Mathematicians_through_Long-Horizon_Lean_Autoformalization) |
| nov/2026 | "Autonomous AI Agents Systematically Diverge From Human Preferences in Proof Formalization": a formalização que compila nem sempre é a que um humano escreveria | — | [arXiv 2611.06995](https://arxiv.org/pdf/2611.06995) |
| nov/2026 | Proposta de infraestrutura para grupos de pesquisa com agentes: o grupo **não consegue ler tudo** o que os agentes produzem, e não está claro o que precisa de revisão humana | — | [arXiv 2611.11645](https://arxiv.org/html/2611.11645v1) |

Sistemas de referência mais antigos: **Aristotle** (Harmonic; busca em árvore sobre estados de prova Lean + raciocínio informal; [arXiv 2510.01346](https://arxiv.org/pdf/2510.01346v1)) e **AlphaEvolve** (DeepMind; LLM propõe mutações de código, um avaliador automático pontua, um laço evolutivo seleciona; [arXiv 2511.02864](https://arxiv.org/abs/2511.02864)). Acompanhamento dos casos de Erdős: [wiki de Tao](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems) e [opiniões de Tao sobre IA](https://teorth.github.io/tao-web/ai-views.html).

## Como esses sistemas são orquestrados (nível de código)

Os sistemas acima repetem quatro padrões. É isso que queremos ver por dentro, construindo uma versão pequena.

1. **Verificador como fonte da verdade.** O LLM nunca decide se está certo. Quem decide é um programa determinístico: o kernel do Lean (`lake build`, `#print axioms`) ou um avaliador numérico (AlphaEvolve). O agente recebe o erro do compilador como *feedback* e tenta de novo.
2. **Papéis separados com contrato.** Os papéis são propositor (prova informal), formalizador (Lean), crítico adversarial ("um defeito fatal basta", como no Stellar Colosseum) e juiz de fidelidade do enunciado (Theo). Cada papel tem um prompt, ferramentas e um formato de saída próprios.
3. **Estado fora do contexto do modelo.** Os agentes "esquecem" (lição do FLT). O estado fica num artefato: um DAG de lemas, o arquivo `.lean` com `sorry` marcando o que falta (LeanMarathon) ou um JSON de tarefas.
4. **Coordenação em código, não em prompt.** A decisão de quem roda, quando, e quando parar fica num laço determinístico (shell ou Python), e o LLM faz só o trabalho cognitivo (ICML AI4Math).

Esqueleto conceitual (pseudocódigo para estudo, não é o produto):

```python
# estado vive fora do modelo: um DAG de lemas, cada um com status
dag = carregar_dag("problema.json")          # {lema: {enunciado, deps, status}}

while (lema := dag.proximo_pronto()) and orcamento.ok():
    informal = agente("propositor", lema.enunciado, contexto=dag.provados())
    if agente("critico", informal).tem_defeito_fatal:
        dag.marcar(lema, "rejeitado"); continue
    for tentativa in range(N):
        codigo = agente("formalizador", informal, erros_anteriores)
        r = lean_build(codigo)                # verificador determinístico
        if r.ok and "sorryAx" not in r.axiomas:
            dag.marcar(lema, "provado"); break
        erros_anteriores = r.erros            # o erro do compilador vira feedback
    else:
        dag.dividir_ou_desistir(lema)        # decompor em sublemas ou parar

relatorio(dag, juiz_fidelidade=agente("juiz", enunciado_original, enunciado_lean))
```

Ferramentas concretas para isso: Claude Code (subagentes, *hooks*, *skills*) como orquestrador ou um laço próprio com o Claude Agent SDK; [`lean-lsp-mcp`](https://github.com/project-numina/lean-lsp-mcp) para dar ao agente diagnósticos, estado de metas e busca de teoremas (`claude mcp add lean-lsp uvx lean-lsp-mcp`).
