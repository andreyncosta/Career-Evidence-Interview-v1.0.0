#!/usr/bin/env python3
"""Valida a estrutura da skill Career Evidence Interview (sem dependências externas)."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


EXPECTED_FILES = [
    "SKILL.md", "README.md", "LICENSE",
    "references/roteiro-entrevista.md", "references/entrevista-tecnica.md",
    "references/rubrica-evidencia.md", "references/modelo-de-dados.md",
    "references/testes-de-aceitacao.md",
    "assets/templates/experiencia.md", "assets/templates/realizacao.md",
    "assets/templates/competencia.md", "assets/templates/matriz-consolidada.md",
    "assets/templates/registro-fontes.md", "assets/templates/historico-revisoes.md",
    "examples/sessao-ficticia.md", "scripts/init_workspace.py",
    "scripts/validate_skill.py",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", default=".")
    root = Path(parser.parse_args().directory).expanduser().resolve()
    failures = []
    for rel in EXPECTED_FILES:
        p = root / rel
        if not p.is_file() or p.stat().st_size == 0:
            failures.append(f"Arquivo ausente ou vazio: {rel}")

    p = root / "SKILL.md"
    if p.exists():
        content = p.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---\n", content, flags=re.DOTALL)
        if not frontmatter:
            failures.append("SKILL.md sem frontmatter YAML válido")
        else:
            header = frontmatter.group(1)
            match = re.search(r"^name:\s*(\S+)\s*$", header, flags=re.MULTILINE)
            description = re.search(r"^description:\s*(.+)$", header, flags=re.MULTILINE)
            if not match or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", match.group(1)):
                failures.append("name ausente ou fora do formato kebab-case")
            else:
                skill_name = match.group(1)
                folder_name = root.name.lower()
                if folder_name != skill_name and not folder_name.startswith(skill_name + "-v"):
                    failures.append("name incompatível com o nome da pasta")
            if not description or not description.group(1).strip():
                failures.append("description ausente ou vazia")
            elif len(description.group(1)) > 1024:
                failures.append("description excede 1024 caracteres")
            if len(content.split()) > 5000:
                failures.append("SKILL.md excede o limite recomendado de 5.000 palavras")

    if failures:
        for failure in failures:
            print("ERRO:", failure, file=sys.stderr)
        return 1
    print(f"OK: estrutura válida em {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
