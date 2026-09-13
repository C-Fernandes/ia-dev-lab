#!/usr/bin/env python3
"""Hook PreToolUse: bloqueia `pip install <pacote>` para pacotes nao documentados.

Implementa a regra do CLAUDE.md: "Nao utilize bibliotecas externas sem que
estejam documentadas". A lista de pacotes aprovados fica em
docs/dependencias-aprovadas.md.

Recebe o payload do hook via stdin (JSON com tool_name/tool_input). Se o
comando Bash for uma instalacao pip de pacote fora da lista, imprime o motivo
em stderr e sai com codigo 2, o que bloqueia a execucao da ferramenta.
"""

import json
import re
import sys
from pathlib import Path

ALLOWLIST_PATH = Path(__file__).resolve().parents[2] / "docs" / "dependencias-aprovadas.md"

PIP_INSTALL_RE = re.compile(
    r"\bpip[3]?\s+install\b(?!.*(-r|--requirement)\b)(?P<args>[^;&|\n]*)"
)


def carregar_aprovados() -> set[str]:
    if not ALLOWLIST_PATH.exists():
        return set()
    aprovados = set()
    for linha in ALLOWLIST_PATH.read_text().splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        aprovados.add(linha.lower())
    return aprovados


def extrair_pacotes(args: str) -> list[str]:
    pacotes = []
    for token in args.split():
        if token.startswith("-"):
            continue
        nome = re.split(r"[=<>!~\[]", token)[0].strip()
        if nome:
            pacotes.append(nome.lower())
    return pacotes


def main() -> int:
    payload = json.load(sys.stdin)
    if payload.get("tool_name") != "Bash":
        return 0

    comando = payload.get("tool_input", {}).get("command", "")
    match = PIP_INSTALL_RE.search(comando)
    if not match:
        return 0

    pacotes = extrair_pacotes(match.group("args"))
    if not pacotes:
        return 0

    aprovados = carregar_aprovados()
    nao_documentados = [p for p in pacotes if p not in aprovados]

    if nao_documentados:
        print(
            "BLOQUEADO: pacote(s) externo(s) nao documentado(s): "
            + ", ".join(nao_documentados)
            + ". Adicione em docs/dependencias-aprovadas.md antes de instalar "
            + "(regra do CLAUDE.md: nao usar libs externas sem documentar).",
            file=sys.stderr,
        )
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
