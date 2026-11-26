"""Verificador determinístico do mini-Astra (etapa 4 da proposta).

Não usa LLM. Recebe um arquivo .lean e os nomes dos teoremas principais e responde:
  - compilou?  (o Lean aceitou o arquivo sem erros)
  - quantos `sorry`?
  - quais axiomas cada teorema usa (`#print axioms`), separando os 3 padrões
    (propext, Classical.choice, Quot.sound) dos extras (sorryAx, axiomas declarados,
    Lean.ofReduceBool de native_decide etc.)

O que ele NÃO responde: se o enunciado em Lean é fiel ao problema original.
Isso continua sendo julgamento humano (ver a hipótese em proposta.md).

Uso (a partir da raiz do repositório):
    python produto/harness/verificar.py produto/MiniAstra/MiniAstra/Exemplo.lean exemplo_soma
    python produto/harness/verificar.py ARQUIVO.lean TEOREMA [TEOREMA ...] --json
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

PROJETO_LEAN = Path(__file__).resolve().parents[1] / "MiniAstra"
AXIOMAS_PADRAO = {"propext", "Classical.choice", "Quot.sound"}


def rodar_lean(arquivo: Path) -> tuple[int, str]:
    """Roda `lake env lean` no arquivo, dentro do projeto (para achar o mathlib)."""
    lake = shutil.which("lake")
    if lake is None:
        sys.exit("lake não encontrado no PATH (instale o elan e reabra o terminal).")
    proc = subprocess.run(
        [lake, "env", "lean", str(arquivo)],
        cwd=PROJETO_LEAN,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return proc.returncode, proc.stdout + proc.stderr


def axiomas_de(saida: str, teorema: str) -> list[str] | None:
    """Extrai a lista de axiomas impressa por `#print axioms teorema`."""
    if re.search(rf"'{re.escape(teorema)}' does not depend on any axioms", saida):
        return []
    m = re.search(
        rf"'{re.escape(teorema)}' depends on axioms: \[(.*?)\]", saida, re.DOTALL
    )
    if not m:
        return None  # teorema não encontrado (nome errado ou arquivo não compilou)
    return [a.strip() for a in m.group(1).replace("\n", " ").split(",") if a.strip()]


def verificar(arquivo: Path, teoremas: list[str]) -> dict:
    fonte = arquivo.read_text(encoding="utf-8")
    t0 = time.monotonic()

    # 1) uma única execução do Lean, numa cópia temporária com `#print axioms` no fim
    #    (o original não é alterado; carregar o mathlib custa ~50 s, então roda uma vez só)
    with tempfile.NamedTemporaryFile(
        "w", suffix=".lean", dir=PROJETO_LEAN, delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(fonte + "\n\n" + "\n".join(f"#print axioms {t}" for t in teoremas) + "\n")
        caminho_tmp = Path(tmp.name)
    try:
        codigo, saida_ax = rodar_lean(caminho_tmp)
    finally:
        caminho_tmp.unlink(missing_ok=True)
    saida_ax = saida_ax.replace(str(caminho_tmp), str(arquivo))

    erros = [l for l in saida_ax.splitlines() if ": error" in l or "error:" in l]
    # Lean 4.37 escreve "declaration uses `sorry`"; versões antigas usavam 'sorry'
    sorrys = len(re.findall(r"declaration uses [`']sorry[`']", saida_ax))

    por_teorema = {}
    for t in teoremas:
        ax = axiomas_de(saida_ax, t)
        por_teorema[t] = {
            "encontrado": ax is not None,
            "axiomas": ax,
            "extras": sorted(set(ax) - AXIOMAS_PADRAO) if ax is not None else None,
        }

    # 3) sinais textuais que merecem olho humano mesmo quando compila
    alertas = []
    if re.search(r"^\s*axiom\s", fonte, re.MULTILINE):
        alertas.append("o arquivo declara `axiom` próprio")
    if "native_decide" in fonte:
        alertas.append("usa native_decide (confia no compilador, não só no kernel)")
    if re.search(r"\badmit\b", fonte):
        alertas.append("usa admit")

    limpo = (
        codigo == 0
        and not erros
        and sorrys == 0
        and all(v["encontrado"] and not v["extras"] for v in por_teorema.values())
    )
    return {
        "arquivo": str(arquivo),
        "compilou": codigo == 0 and not erros,
        "erros": erros[:20],
        "sorry": sorrys,
        "teoremas": por_teorema,
        "alertas": alertas,
        "verificado_sem_ressalvas": limpo,
        "segundos": round(time.monotonic() - t0, 1),
        "fidelidade_do_enunciado": "NÃO VERIFICADA (julgamento humano)",
    }


def relatorio_md(r: dict) -> str:
    sim = lambda b: "sim" if b else "**não**"
    linhas = [
        f"### Verificação de `{r['arquivo']}`",
        f"- Compilou: {sim(r['compilou'])}",
        f"- `sorry`: {r['sorry']}",
    ]
    for t, v in r["teoremas"].items():
        if not v["encontrado"]:
            linhas.append(f"- `{t}`: **não encontrado** (nome errado ou não compilou)")
        else:
            extras = ", ".join(v["extras"]) or "nenhum"
            linhas.append(f"- `{t}`: axiomas extras: {extras}")
    for a in r["alertas"]:
        linhas.append(f"- ⚠️ {a}")
    for e in r["erros"]:
        linhas.append(f"- erro: `{e}`")
    linhas.append(f"- Verificado sem ressalvas: {sim(r['verificado_sem_ressalvas'])}")
    linhas.append(f"- Fidelidade do enunciado: {r['fidelidade_do_enunciado']}")
    linhas.append(f"- Tempo: {r['segundos']} s")
    return "\n".join(linhas)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("arquivo", type=Path)
    p.add_argument("teoremas", nargs="+")
    p.add_argument("--json", action="store_true", help="saída em JSON")
    a = p.parse_args()
    r = verificar(a.arquivo.resolve(), a.teoremas)
    print(json.dumps(r, ensure_ascii=False, indent=2) if a.json else relatorio_md(r))
    sys.exit(0 if r["verificado_sem_ressalvas"] else 1)


if __name__ == "__main__":
    main()
