#!/usr/bin/env bash
# rename_asignaturas.sh
# Renombra carpetas de asignaturas eliminando prefijos numéricos (63200-, 63305-, etc.)
# Uso:
#   ./scripts/rename_asignaturas.sh          # aplica cambios
#   ./scripts/rename_asignaturas.sh --dry-run  # solo muestra qué haría
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ASIG="$ROOT/01-asignaturas"
OPT="$ASIG/optativas"
DRY_RUN=0

if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=1
  echo "[DRY-RUN] No se aplicarán cambios."
fi

run() {
  if [[ $DRY_RUN -eq 1 ]]; then
    echo "  would: $*"
  else
    echo "  $*"
    "$@"
  fi
}

# Mapa: nombre_con_codigo -> nombre_limpio
declare -A OBLIGATORIAS=(
  ["63200-psicologia-del-desarrollo-y-de-la-educacion"]="psicologia-del-desarrollo-y-de-la-educacion"
  ["63201-procesos-y-contextos-educativos"]="procesos-y-contextos-educativos"
  ["63202-sociedad-familia-y-procesos-grupales"]="sociedad-familia-y-procesos-grupales"
  ["63209-practicum-i"]="practicum-i"
  ["63222-contenidos-disciplinares-de-matematicas"]="contenidos-disciplinares-de-matematicas"
  ["63223-diseno-curricular-e-instruccional-de-matematicas"]="diseno-curricular-e-instruccional-de-matematicas"
  ["63224-diseno-de-actividades-para-el-aprendizaje-de-matematicas"]="diseno-de-actividades-para-el-aprendizaje-de-matematicas"
  ["63225-innovacion-e-investigacion-educativa-en-matematicas"]="innovacion-e-investigacion-educativa-en-matematicas"
  ["63226-practicum-ii"]="practicum-ii"
  ["63227-trabajo-fin-de-master"]="trabajo-fin-de-master"
)

declare -A OPTATIVAS=(
  ["63305-educacion-emocional-en-el-profesorado"]="educacion-emocional-en-el-profesorado"
  ["63308-prevencion-y-resolucion-de-conflictos"]="prevencion-y-resolucion-de-conflictos"
  ["63309-diseno-de-materiales-para-la-educacion-a-distancia"]="diseno-de-materiales-para-la-educacion-a-distancia"
  ["63311-ensenanza-del-espanol-para-alumnado-inmigrante"]="ensenanza-del-espanol-para-alumnado-inmigrante"
  ["63312-habilidades-comunicativas-para-docentes"]="habilidades-comunicativas-para-docentes"
  ["63315-tecnologias-de-la-informacion-y-la-comunicacion-para-el-aprendizaje"]="tecnologias-de-la-informacion-y-la-comunicacion-para-el-aprendizaje"
  ["63328-atencion-al-alumnado-con-necesidades-educativas-especificas"]="atencion-al-alumnado-con-necesidades-educativas-especificas"
)

# Carpetas vacías/legacy que colisionan con los nombres limpios (solo .gitkeep)
LEGACY_DIRS=(
  "aprendizaje-y-desarrollo-de-la-personalidad"
  "didactica-de-las-matematicas"
  "diseno-curricular"
  "innovacion-e-investigacion-educativa"
  "procesos-y-contextos-educativos"
  "psicologia-social"
  "sociedad-familia-y-procesos-grupales"
)

echo "==> Eliminando carpetas legacy vacías que colisionan..."
for d in "${LEGACY_DIRS[@]}"; do
  path="$ASIG/$d"
  if [[ -d "$path" ]]; then
    # Solo borrar si parece placeholder (solo .gitkeep o vacío)
    file_count=$(find "$path" -type f ! -name '.gitkeep' 2>/dev/null | wc -l)
    if [[ "$file_count" -eq 0 ]]; then
      run rm -rf "$path"
    else
      echo "  AVISO: $path tiene contenido real; no se elimina automáticamente."
    fi
  fi
done

echo "==> Renombrando asignaturas obligatorias..."
for old in "${!OBLIGATORIAS[@]}"; do
  new="${OBLIGATORIAS[$old]}"
  src="$ASIG/$old"
  dst="$ASIG/$new"
  if [[ -d "$src" ]]; then
    if [[ -d "$dst" ]]; then
      echo "  AVISO: destino $dst ya existe; se omite $old"
    else
      run mv "$src" "$dst"
    fi
  fi
done

echo "==> Renombrando optativas..."
for old in "${!OPTATIVAS[@]}"; do
  new="${OPTATIVAS[$old]}"
  src="$OPT/$old"
  dst="$OPT/$new"
  if [[ -d "$src" ]]; then
    if [[ -d "$dst" ]]; then
      echo "  AVISO: destino $dst ya existe; se omite $old"
    else
      run mv "$src" "$dst"
    fi
  fi
done

echo "==> Renombrado terminado."
