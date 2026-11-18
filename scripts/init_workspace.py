#!/usr/bin/env python3
"""Cria uma Career Knowledge Base vazia, sem sobrescrever arquivos existentes.

Uso: python scripts/init_workspace.py /caminho/para/minha-career-base
Somente biblioteca padrão; sem acesso à rede.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dest", type=Path, help="Pasta de destino, vazia ou inexistente")
    args = parser.parse_args()
    dest = args.dest.expanduser().resolve()
    src = Path(__file__).resolve().parent.parent / "assets" / "templates"

    if dest.exists() and (not dest.is_dir() or any(dest.iterdir())):
        print(f"Destino já possui arquivos; nenhuma alteração realizada: {dest}", file=sys.stderr)
        return 2
    if not src.is_dir():
        print("Templates da skill não encontrados", file=sys.stderr)
        return 3

    dest.mkdir(parents=True, exist_ok=True)
    for folder in ("profile", "experiences", "achievements", "skills", "sources", "governance", "_templates"):
        (dest / folder).mkdir(exist_ok=True)
    for template in src.glob("*.md"):
        shutil.copy2(template, dest / "_templates" / template.name)

    (dest / "INDEX.md").write_text(
        "# Career Knowledge Base\n\n"
        "**Estado:** vazia; preencher a partir de entrevistas e fontes autorizadas.\n\n"
        "## Experiências\n\n## Realizações\n\n## Competências\n\n"
        "## Fontes e revisão\n\n"
        "Modelos em _templates/. Nunca colocar dados reais nos modelos originais.\n",
        encoding="utf-8",
    )
    (dest / "profile" / "summary.md").write_text(
        "# Perfil profissional\n\n## Fatos\n\n## Hipóteses de posicionamento\n\n"
        "## Privacidade e pendências\n",
        encoding="utf-8",
    )
    (dest / "sources" / "source-log.md").write_text(
        (src / "registro-fontes.md").read_text(encoding="utf-8"), encoding="utf-8"
    )
    (dest / "governance" / "open-questions.md").write_text(
        "# Questões em aberto\n\n- [ ] Validar períodos e cargos com a pessoa\n",
        encoding="utf-8",
    )
    (dest / "governance" / "revisions.md").write_text(
        (src / "historico-revisoes.md").read_text(encoding="utf-8"), encoding="utf-8"
    )
    print(f"Base vazia criada: {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
