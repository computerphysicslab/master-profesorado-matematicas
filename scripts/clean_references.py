#!/usr/bin/env python3
"""
clean_references.py
Elimina referencias a UNIZAR / Universidad de Zaragoza y códigos numéricos
de asignaturas (63xxx) en todos los ficheros Markdown del repositorio.

Uso:
  python3 scripts/clean_references.py          # aplica cambios
  python3 scripts/clean_references.py --dry-run  # solo informa
  python3 scripts/clean_references.py --verbose
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Patrones a eliminar / sustituir
PATTERNS: list[tuple[re.Pattern[str], str]] = [
    # Curso / créditos / grupos / turnos
    (re.compile(r"curso\s+2026[–-]2027", re.IGNORECASE), ""),
    (re.compile(r"2026[–-]2027"), ""),
    (re.compile(r"\b2026\b"), ""),
    (re.compile(r"\b2027\b"), ""),
    (re.compile(r"\bECTS\b"), ""),
    (re.compile(r"\*\*Curso académico:\*\*.*\n"), ""),
    (re.compile(r"\*\*Periodo:\*\*.*\n"), ""),
    (re.compile(r"\*\*Grupo:\*\*.*\n"), ""),
    (re.compile(r"\*\*ECTS:\*\*.*\n"), ""),
    (re.compile(r"grupo\s+\d+(-\d+)?\s*[·•]\s*tarde", re.IGNORECASE), ""),
    (re.compile(r"Grupo/turno"), ""),

    # Universidad
    (re.compile(r"Universidad de Zaragoza\s*\(UNIZAR\)", re.IGNORECASE), ""),
    (re.compile(r"Universidad de Zaragoza", re.IGNORECASE), ""),
    (re.compile(r"\bUNIZAR\b"), ""),
    # Códigos de asignatura sueltos (63200, 63328, etc.)
    (re.compile(r"\b63[0-9]{3}\b"), ""),
    # Líneas de metadatos con código
    (re.compile(r"\*\*Código:\*\*\s*\d+\s*", re.IGNORECASE), ""),
    (re.compile(r"Código:\s*\d+\s*", re.IGNORECASE), ""),
    # "código 12 según Resolución Practicum DGA"
    (re.compile(
        r"[—\-–]?\s*código\s+\d+\s+según\s+Resolución\s+Practicum\s+DGA",
        re.IGNORECASE,
    ), ""),
    # Enlaces a educacion.unizar.es (opcional: dejar o vaciar)
    # Se dejan los URLs por si el usuario quiere conservar enlaces oficiales.
]

# Limpieza de espacios / puntuación residual tras las sustituciones
POST_CLEAN: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"[ \t]{2,}"), " "),           # espacios múltiples
    (re.compile(r" +([,.;:])"), r"\1"),        # espacio antes de puntuación
    (re.compile(r"\( +\)"), ""),               # paréntesis vacíos
    (re.compile(r" · +"), " · "),
    (re.compile(r"— +"), "— "),
    (re.compile(r" +—"), " —"),
    (re.compile(r"\n{3,}"), "\n\n"),           # demasiadas líneas en blanco
    (re.compile(r"[ \t]+\n"), "\n"),            # trailing spaces
]


def clean_text(text: str) -> str:
    for pat, repl in PATTERNS:
        text = pat.sub(repl, text)
    for pat, repl in POST_CLEAN:
        text = pat.sub(repl, text)
    return text


def process_file(path: Path, dry_run: bool, verbose: bool) -> bool:
    try:
        original = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as e:
        print(f"  SKIP {path}: {e}", file=sys.stderr)
        return False

    cleaned = clean_text(original)
    if cleaned == original:
        if verbose:
            print(f"  ok   {path.relative_to(ROOT)}")
        return False

    if dry_run:
        print(f"  would-clean {path.relative_to(ROOT)}")
        return True

    path.write_text(cleaned, encoding="utf-8")
    print(f"  cleaned {path.relative_to(ROOT)}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Limpia referencias UNIZAR y códigos de asignatura")
    parser.add_argument("--dry-run", action="store_true", help="Solo mostrar qué se cambiaría")
    parser.add_argument("--verbose", "-v", action="store_true", help="Mostrar también ficheros sin cambios")
    args = parser.parse_args()

    md_files = sorted(ROOT.rglob("*.md"))
    md_files = [p for p in md_files if ".git" not in p.parts and "scripts" not in p.parts]

    print(f"==> Procesando {len(md_files)} ficheros Markdown en {ROOT}")
    if args.dry_run:
        print("[DRY-RUN] No se escribirán cambios.")

    changed = 0
    for path in md_files:
        if process_file(path, args.dry_run, args.verbose):
            changed += 1

    print(f"==> Ficheros afectados: {changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
