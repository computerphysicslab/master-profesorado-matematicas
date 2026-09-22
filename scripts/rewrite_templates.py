#!/usr/bin/env python3
"""
rewrite_templates.py
Reescribe los README principales y de cada asignatura con plantillas
limpias (sin UNIZAR ni códigos numéricos).

Uso:
  python3 scripts/rewrite_templates.py
  python3 scripts/rewrite_templates.py --dry-run
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Datos canónicos (sin códigos)
# ---------------------------------------------------------------------------

OBLIGATORIAS = [
    # (slug, título, tipo, periodo, grupo, ects)
    ("psicologia-del-desarrollo-y-de-la-educacion", "Psicología del desarrollo y de la educación", "Obligatoria", "S1", "7", "4"),
    ("procesos-y-contextos-educativos", "Procesos y contextos educativos", "Obligatoria", "S1", "7", "6"),
    ("sociedad-familia-y-procesos-grupales", "Sociedad, familia y procesos grupales", "Obligatoria", "S1", "7", "4"),
    ("practicum-i", "Practicum I", "Obligatoria", "S1", "1", "3"),
    ("contenidos-disciplinares-de-matematicas", "Contenidos disciplinares de Matemáticas", "Obligatoria", "S2", "1", "6"),
    ("diseno-curricular-e-instruccional-de-matematicas", "Diseño curricular e instruccional de Matemáticas", "Obligatoria", "S1", "1", "6"),
    ("diseno-de-actividades-para-el-aprendizaje-de-matematicas", "Diseño de actividades para el aprendizaje de Matemáticas", "Obligatoria", "S2", "1", "8"),
    ("innovacion-e-investigacion-educativa-en-matematicas", "Innovación e investigación educativa en Matemáticas", "Obligatoria", "S2", "1", "4"),
    ("practicum-ii", "Practicum II", "Obligatoria", "Anual", "1", "7"),
    ("trabajo-fin-de-master", "Trabajo fin de Máster", "Obligatoria", "Anual", "99", "6"),
]

OPTATIVAS_S1 = [
    ("atencion-al-alumnado-con-necesidades-educativas-especificas", "Atención al alumnado con necesidades educativas específicas", "grupo 2 · tarde", "3"),
    ("educacion-emocional-en-el-profesorado", "Educación emocional en el profesorado", "grupo 2-3 · tarde", "3"),
    ("prevencion-y-resolucion-de-conflictos", "Prevención y resolución de conflictos", "grupo 2-3 · tarde", "3"),
]

OPTATIVAS_S2 = [
    ("diseno-de-materiales-para-la-educacion-a-distancia", "Diseño de materiales para la educación a distancia", "grupo 1 · tarde", "3"),
    ("ensenanza-del-espanol-para-alumnado-inmigrante", "Enseñanza del español para alumnado inmigrante", "grupo 1 · tarde", "3"),
    ("habilidades-comunicativas-para-docentes", "Habilidades comunicativas para docentes", "grupo 2 · tarde", "3"),
    ("tecnologias-de-la-informacion-y-la-comunicacion-para-el-aprendizaje", "Tecnologías de la información y la comunicación para el aprendizaje", "grupo 2 · tarde", "3"),
]

# ---------------------------------------------------------------------------
# Plantillas
# ---------------------------------------------------------------------------

README_ROOT = """# Máster Universitario en Profesorado — Matemáticas · 2026–2027

Repositorio personal de trabajo del **Máster Universitario en Profesorado de Educación Secundaria Obligatoria, Bachillerato, Formación Profesional y Enseñanzas de Idiomas, Artísticas y Deportivas**, especialidad **Matemáticas**, curso 2026–2027.

El repositorio reúne apuntes, materiales, actividades, trabajos, bibliografía, proyectos, recursos digitales y evidencias de aprendizaje generados durante el máster.

## Estructura

- `00-administracion/` — matrícula, calendario, trámites, organización y documentación administrativa.
- `01-asignaturas/` — asignaturas del curso 2026–2027, con grupos, ECTS y espacios de trabajo.
- `02-apuntes/` — índice general y apuntes transversales.
- `03-materiales/` — materiales docentes y recursos reutilizables.
- `04-pbl-abp/` — aprendizaje basado en proyectos/problemas.
- `05-python-jupyter/` — Python, Jupyter y recursos computacionales para educación matemática.
- `06-inteligencia-artificial/` — IA aplicada a educación, docencia y aprendizaje.
- `07-evaluacion/` — evaluación, instrumentos, rúbricas y evidencias.
- `08-podcasts/` — podcasts relacionados con aprendizaje, enseñanza y Matemáticas.
- `09-bibliografia/` — bibliografía y referencias.
- `10-proyectos/` — proyectos integradores y propuestas didácticas.
- `99-archivo/` — materiales históricos o no activos.

## Asignaturas obligatorias

| Periodo | Grupo | Asignatura | ECTS |
|---|---:|---|---:|
{obligatorias_table}

## Optativas

Se elige **una optativa de S1 y una optativa de S2**. Además, se puede matricular **un segundo Contenido Disciplinar de otra especialidad en lugar de elegir dos optativas**.

### Optativas S1

| Grupo/turno | Asignatura | ECTS |
|---|---|---:|
{opt_s1_table}

### Optativas S2

| Grupo/turno | Asignatura | ECTS |
|---|---|---:|
{opt_s2_table}

## Practicum y TFM

- El turno de las clases presenciales **no determina el turno del Practicum**.
- El Practicum se realizará **por las mañanas**, salvo que una resolución específica establezca otro turno.
- Parte del trabajo del **TFM se desarrollará conjuntamente con el Practicum**.

## Criterio de organización

Cada asignatura dispone de un `README.md`, un índice de apuntes, espacios para materiales y trabajos, y una referencia bibliográfica inicial. Los contenidos concretos se incorporarán durante el curso y se distinguirán de la documentación oficial.

## Objetivo

Convertir este repositorio en un cuaderno digital de trabajo completo para el máster y, posteriormente, en una base de conocimiento reutilizable para la enseñanza de Matemáticas y Ciencias en Secundaria y Bachillerato.
"""

MANIFEST = """# Manifest

Estructura generada para el Máster de Profesorado de Matemáticas — 2026–2027.

- Asignaturas obligatorias: **10**
- Optativas S1: **3**
- Optativas S2: **4**

La lista de asignaturas y optativas se ha construido a partir de la estructura del curso 2026–2027.
"""

README_ASIGNATURAS = """# 📚 Asignaturas — Máster de Profesorado · Matemáticas

Repositorio de trabajo correspondiente a las asignaturas del **Máster Universitario en Profesorado de Educación Secundaria Obligatoria, Bachillerato, Formación Profesional y Enseñanzas de Idiomas, Artísticas y Deportivas**, especialidad en **Matemáticas**.

**Curso académico:** 2026–2027  
**Especialidad:** Matemáticas para E.S.O. y Bachillerato

---

## 🗺️ Estructura

Cada asignatura tiene su propia carpeta dentro de `01-asignaturas/`.

```text
01-asignaturas/
│
├── README.md
│
{tree}
└── optativas/
{opt_tree}
```

---

# 📋 Asignaturas del Máster

## 1. Formación general

| Asignatura | Tipo | Semestre | ECTS |
| --- | --- | --- | ---: |
{formacion_table}

Estas materias constituyen parte de la formación psicopedagógica y contextual común del Máster.

---

# ➗ 2. Especialidad de Matemáticas

| Asignatura | Tipo | Semestre | ECTS |
| --- | --- | --- | ---: |
{especialidad_table}

Estas asignaturas constituyen el núcleo específico de la especialidad de Matemáticas.

---

# 🎓 3. Trabajo Fin de Máster y Practicum II

| Asignatura | Tipo | ECTS |
| --- | --- | ---: |
{tfm_table}

El TFM integrará los conocimientos adquiridos durante el Máster y podrá relacionarse con la didáctica de las Matemáticas, la innovación educativa, las metodologías activas, la tecnología educativa, Python, la Inteligencia Artificial u otras líneas de investigación educativa.

---

# 🧩 Relación entre asignaturas

Una de las finalidades de este repositorio es evitar que las asignaturas se estudien como compartimentos aislados.

La formación puede contemplarse como una cadena de aprendizaje que conecta psicología del desarrollo, contextos educativos, diseño curricular, diseño de actividades, innovación e investigación, practicum y TFM.
"""

SUBJECT_README = """# {title}

**Tipo:** {tipo}

## Descripción

Espacio de trabajo para la asignatura **{title}** del Máster de Profesorado de Educación Secundaria, especialidad Matemáticas, curso 2026–2027.

## Contenidos

Los contenidos, apuntes y materiales se incorporarán progresivamente durante el curso a partir de la documentación docente y del trabajo personal.

## Carpetas

- `apuntes/` — apuntes y resúmenes.
- `materiales/` — recursos docentes y documentación.
- `trabajos/` — tareas, actividades y entregas.
- `bibliografia.md` — referencias bibliográficas.
"""

OPTATIVAS_README = """# Optativas

Las optativas están organizadas por semestre.

La planificación contempla **una optativa de S1 y una optativa de S2**. Como alternativa, se puede matricular **un segundo Contenido Disciplinar de otra especialidad en lugar de elegir dos optativas**.
"""

OPT_S1_README = """# Optativas S1

Optativas disponibles en S1.

{list}
"""

OPT_S2_README = """# Optativas S2

Optativas disponibles en S2.

{list}
"""

ADMIN_README = """# Administración del máster

Seguimiento de matrícula, documentación, calendario, Practicum, TFM, comunicaciones y trámites administrativos.

No sustituye la información oficial ni las resoluciones correspondientes.
"""

SECTION_README = """# {title}

Sección del repositorio del Máster de Profesorado de Matemáticas 2026–2027.

Esta carpeta se utilizará para organizar documentación, apuntes, recursos y evidencias relacionadas con **{title}**.

Los materiales se incorporarán progresivamente durante el curso académico.
"""

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def write(path: Path, content: str, dry_run: bool) -> None:
    if dry_run:
        print(f"  would-write {path.relative_to(ROOT)}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {path.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.dry_run:
        print("[DRY-RUN] No se escribirán cambios.")

    # --- Root README ---
    obl_rows = "\n".join(
        f"| {periodo} | {grupo} | {titulo} | {ects} |"
        for _, titulo, _, periodo, grupo, ects in OBLIGATORIAS
    )
    s1_rows = "\n".join(
        f"| {turno} | {titulo} | {ects} |"
        for _, titulo, turno, ects in OPTATIVAS_S1
    )
    s2_rows = "\n".join(
        f"| {turno} | {titulo} | {ects} |"
        for _, titulo, turno, ects in OPTATIVAS_S2
    )
    write(
        ROOT / "README.md",
        README_ROOT.format(
            obligatorias_table=obl_rows,
            opt_s1_table=s1_rows,
            opt_s2_table=s2_rows,
        ),
        args.dry_run,
    )

    # --- MANIFEST ---
    write(ROOT / "MANIFEST.md", MANIFEST, args.dry_run)

    # --- 01-asignaturas/README.md ---
    tree_lines = "\n".join(f"├── {slug}/\n│   └── README.md" for slug, *_ in OBLIGATORIAS)
    opt_tree = "\n".join(f"    ├── {slug}/" for slug, *_ in OPTATIVAS_S1 + OPTATIVAS_S2)
    # last opt with └──
    if OPTATIVAS_S1 or OPTATIVAS_S2:
        last = (OPTATIVAS_S1 + OPTATIVAS_S2)[-1][0]
        opt_tree = opt_tree.replace(f"    ├── {last}/", f"    └── {last}/")

    formacion = OBLIGATORIAS[:4]  # primeras 4
    especialidad = OBLIGATORIAS[4:8]
    tfm = OBLIGATORIAS[8:]

    formacion_table = "\n".join(
        f"| [{t}]({s}/) | {tipo} | {per} | {e} |"
        for s, t, tipo, per, _, e in formacion
    )
    especialidad_table = "\n".join(
        f"| [{t}]({s}/) | {tipo} | {per} | {e} |"
        for s, t, tipo, per, _, e in especialidad
    )
    tfm_table = "\n".join(
        f"| [{t}]({s}/) | {tipo} | {e} |"
        for s, t, tipo, _, _, e in tfm
    )

    write(
        ROOT / "01-asignaturas" / "README.md",
        README_ASIGNATURAS.format(
            tree=tree_lines,
            opt_tree=opt_tree,
            formacion_table=formacion_table,
            especialidad_table=especialidad_table,
            tfm_table=tfm_table,
        ),
        args.dry_run,
    )

    # --- Subject READMEs (obligatorias) ---
    for slug, titulo, tipo, *_ in OBLIGATORIAS:
        path = ROOT / "01-asignaturas" / slug / "README.md"
        write(path, SUBJECT_README.format(title=titulo, tipo=tipo), args.dry_run)

    # --- Optativas ---
    write(ROOT / "01-asignaturas" / "optativas" / "README.md", OPTATIVAS_README, args.dry_run)
    write(
        ROOT / "01-asignaturas" / "optativas" / "S1-README.md",
        OPT_S1_README.format(list="\n".join(f"- {t}" for _, t, _, _ in OPTATIVAS_S1)),
        args.dry_run,
    )
    write(
        ROOT / "01-asignaturas" / "optativas" / "S2-README.md",
        OPT_S2_README.format(list="\n".join(f"- {t}" for _, t, _, _ in OPTATIVAS_S2)),
        args.dry_run,
    )
    for slug, titulo, *_ in OPTATIVAS_S1 + OPTATIVAS_S2:
        path = ROOT / "01-asignaturas" / "optativas" / slug / "README.md"
        write(path, SUBJECT_README.format(title=titulo, tipo="Optativa"), args.dry_run)

    # --- Admin ---
    write(ROOT / "00-administracion" / "README.md", ADMIN_README, args.dry_run)

    # --- Secciones genéricas (solo si el README actual menciona UNIZAR o está muy sucio) ---
    sections = {
        "02-apuntes": "Apuntes",
        "03-materiales": "Materiales",
        "04-pbl-abp": "PBL / ABP",
        "05-python-jupyter": "Python y Jupyter",
        "06-inteligencia-artificial": "Inteligencia Artificial",
        "07-evaluacion": "Evaluación",
        "08-podcasts": "Podcasts",
        "09-bibliografia": "Bibliografía",
        "10-proyectos": "Proyectos",
        "99-archivo": "Archivo",
    }
    for folder, title in sections.items():
        path = ROOT / folder / "README.md"
        if path.exists():
            current = path.read_text(encoding="utf-8")
            if "UNIZAR" in current or "Universidad de Zaragoza" in current or "63" in current:
                write(path, SECTION_README.format(title=title), args.dry_run)

    print("==> Plantillas reescritas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
