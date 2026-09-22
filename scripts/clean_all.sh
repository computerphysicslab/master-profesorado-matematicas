#!/usr/bin/env bash
# clean_all.sh
# Orquestador: renombra carpetas + limpia textos + reescribe plantillas canónicas.
#
# Uso:
#   ./scripts/clean_all.sh              # aplica todo
#   ./scripts/clean_all.sh --dry-run    # simula sin escribir
#   ./scripts/clean_all.sh --skip-rename
#   ./scripts/clean_all.sh --skip-templates
#
# Orden recomendado sobre un clon fresco del repo original:
#   1. rename_asignaturas.sh
#   2. clean_references.py   (limpia residuales en ficheros no reescritos)
#   3. rewrite_templates.py  (garantiza README principales limpios)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

DRY_RUN=0
SKIP_RENAME=0
SKIP_TEMPLATES=0
SKIP_CLEAN=0

for arg in "$@"; do
  case "$arg" in
    --dry-run)        DRY_RUN=1 ;;
    --skip-rename)    SKIP_RENAME=1 ;;
    --skip-templates) SKIP_TEMPLATES=1 ;;
    --skip-clean)     SKIP_CLEAN=1 ;;
    -h|--help)
      sed -n '2,20p' "$0"
      exit 0
      ;;
    *)
      echo "Opción desconocida: $arg" >&2
      exit 1
      ;;
  esac
done

DRY_FLAG=()
[[ $DRY_RUN -eq 1 ]] && DRY_FLAG=(--dry-run)

echo "========================================"
echo " Limpieza del repo master-profesorado-matematicas"
echo " Root: $ROOT"
echo "========================================"

if [[ $SKIP_RENAME -eq 0 ]]; then
  echo ""
  echo ">>> Paso 1/3: Renombrar carpetas de asignaturas"
  bash "$ROOT/scripts/rename_asignaturas.sh" "${DRY_FLAG[@]}"
else
  echo ""
  echo ">>> Paso 1/3: Renombrado OMITIDO (--skip-rename)"
fi

if [[ $SKIP_CLEAN -eq 0 ]]; then
  echo ""
  echo ">>> Paso 2/3: Limpiar referencias en Markdown"
  python3 "$ROOT/scripts/clean_references.py" "${DRY_FLAG[@]}"
else
  echo ""
  echo ">>> Paso 2/3: Limpieza de textos OMITIDA (--skip-clean)"
fi

if [[ $SKIP_TEMPLATES -eq 0 ]]; then
  echo ""
  echo ">>> Paso 3/3: Reescribir plantillas canónicas"
  python3 "$ROOT/scripts/rewrite_templates.py" "${DRY_FLAG[@]}"
else
  echo ""
  echo ">>> Paso 3/3: Plantillas OMITIDAS (--skip-templates)"
fi

echo ""
echo "========================================"
echo " Verificación final"
echo "========================================"
if [[ $DRY_RUN -eq 1 ]]; then
  echo "[DRY-RUN] Verificación omitida (no se modificó nada)."
else
  echo -n "Referencias UNIZAR/Zaragoza restantes: "
  if grep -riE 'unizar|universidad de zaragoza' --include='*.md' . 2>/dev/null | grep -v scripts | head -1; then
    echo "(aún hay coincidencias — revisar)"
  else
    echo "0"
  fi
  echo -n "Códigos 63xxx restantes en .md: "
  if grep -rE '\b63[0-9]{3}\b' --include='*.md' . 2>/dev/null | grep -v scripts | head -1; then
    echo "(aún hay coincidencias — revisar)"
  else
    echo "0"
  fi
  echo -n "Carpetas con prefijo numérico de asignatura: "
  left=$(find 01-asignaturas -maxdepth 2 -type d -name '63*' 2>/dev/null | wc -l)
  echo "$left"
fi

echo ""
echo "Listo."
