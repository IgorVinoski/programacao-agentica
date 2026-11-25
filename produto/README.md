# Produto: mini-Astra

O harness da proposta, com quatro etapas: literatura → prova ou contraexemplo → Lean → relatório honesto.

| Pasta | O que é |
|---|---|
| `MiniAstra/` | Projeto Lean 4 + mathlib (criado com o template `math` do `lake`). As formalizações dos problemas ficam em `MiniAstra/MiniAstra/`. |
| `harness/verificar.py` | Etapa 4, **sem LLM**: compilou? quantos `sorry`? quais axiomas extras (`#print axioms`)? Não julga a fidelidade do enunciado, que continua sendo julgamento humano. |
| `harness/testes/` | Arquivos Lean de controle para checar se o verificador acusa o que deve. |

## Pré-requisitos

- `elan` (Lean) e `uv` no PATH. Depois da instalação, reabra o terminal.
- Na primeira vez, dentro de `produto/MiniAstra`: `lake exe cache get` (baixa o mathlib pré-compilado, cerca de 5 GB).

## Verificar um arquivo

```powershell
python produto/harness/verificar.py produto/MiniAstra/MiniAstra/Arquivo.lean nome_do_teorema
```

O código de saída é 0 só se compilou, sem `sorry` e sem axioma extra.

## Agente com acesso ao Lean

O `.mcp.json` na raiz do repositório registra o servidor [`lean-lsp-mcp`](https://github.com/project-numina/lean-lsp-mcp) para o Claude Code. Ele dá ao agente diagnósticos do Lean, o estado das metas e busca de teoremas no mathlib. Ao abrir o Claude Code no repositório, aprove o servidor `lean-lsp`.
