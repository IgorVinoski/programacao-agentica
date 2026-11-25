# Diário

Regra: **a previsão é escrita e commitada ANTES da etapa**, e o resultado é escrito depois. Cada pessoa usa a própria seção ou o próprio arquivo (`diario-igor.md` etc.).

## Modelo de entrada

### AAAA-MM-DD — [etapa] — [quem]
**Previsão (antes):** tempo esperado / o que vou delegar / onde acho que vai travar
**Ferramentas:** harness, modelo e versão
**O que aconteceu:**
**Aceitei / refiz / nem deleguei:**
**Travei em / precisei aprender:**
**Horas:** · **Gasto:**

---

## Tabela de problemas

| Problema | Status no site | Agente alegou? | Compilou? | `sorry` | Axiomas extras | Enunciado fiel? (meu julgamento) | Já existia? |
|---|---|---|---|---|---|---|---|

---

### 2026-11-25 — Pesquisa complementar e montagem do ambiente — Igor (executado pelo agente)
**Previsão (antes):** não registrada antes da etapa. Pedi ao agente para "começar o que precisa ser feito" sem escrever a previsão primeiro. Fica anotado como falha de processo; a partir da calibração (#728), a previsão vem antes.
**Ferramentas:** Claude Code 2.1.270 (desktop, Windows 11), modelo Claude Opus 5.5; elan 4.4.0; uv 0.13.10; lean-lsp-mcp (via uvx); Lean/mathlib pelo template `math` do lake (versão exata registrada quando o build terminar).
**O que aconteceu:**
- Pedi ao agente para pesquisar como a IA está sendo usada para resolver problemas de matemática e para repensar o tema com foco na orquestração dos agentes no código. Ele ampliou o `docs/estado-da-arte.md` (FLT em Lean pela Anthropic, LeanMarathon, ICML AI4Math, Numina-Lean-Agent, e os quatro padrões de orquestração).
- Ele também propôs uma hipótese nova (foco em orquestração). **Rejeitei e mantive a hipótese original** da proposta de 15/11. A pesquisa ficou só como contexto.
- Instalação (aprovei os downloads): elan, uv, projeto `produto/MiniAstra` (Lean + mathlib, cache de cerca de 5 GB).
- O agente escreveu `produto/harness/verificar.py` (etapa 4, sem LLM: compilou? `sorry`? axiomas extras?) e três arquivos de controle em `produto/harness/testes/` (limpo, com `sorry`, com `axiom`).
- Configurou o `.mcp.json` com o `lean-lsp-mcp`, para o agente enxergar o Lean.
**Aceitei / refiz / nem deleguei:** aceitei a pesquisa (falta conferir as fontes primárias antes de citar) e a infraestrutura. Rejeitei a troca de hipótese. Ainda **não li** o `verificar.py` com atenção, então não sei explicá-lo linha a linha (pendência para o critério de domínio).
**Travei em / precisei aprender:** nada ainda; tudo foi delegado.
**Horas:** ~1 h (contando a espera do download) · **Gasto:** assinatura (sem custo extra de API)
