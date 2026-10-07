# Manifest del repositorio

Inventario de la estructura y **criterios de organización**. Actualizar al cambiar carpetas de primer nivel o reglas de ubicación.

**Última limpieza estructural:** 2026-10-07 — eliminación de reservas vacías en `02-apuntes/` (`psicologia/`, `matematicas/`, `sociologia-educacion/`); contenido de asignatura solo en `01-asignaturas/`.

---

## Criterio: ¿dónde va cada cosa?

| Tipo de contenido | Ubicación canónica |
|-------------------|--------------------|
| Apuntes **de una asignatura** (temas numerados) | `01-asignaturas/<asignatura>/apuntes/` |
| Materiales **de una asignatura** | `01-asignaturas/<asignatura>/materiales/` |
| Apuntes **transversales** (cruzan varias materias) | `02-apuntes/` (subcarpetas con contenido real) |
| Fichas reutilizables multi-asignatura | `03-materiales/` |
| Diario / centro / aula / reflexiones de prácticas (**anonimizado**) | `01-asignaturas/practicum/` |
| Carcasa académica Practicum I o II (bibliografía, trabajos locales) | `practicum-i/` · `practicum-ii/` |
| Histórico / scripts de un solo uso | `99-archivo/` |

**No crear** carpetas vacías “por si acaso” en `02-apuntes/` que dupliquen `01-asignaturas/`.

---

## Carpetas de primer nivel

| Carpeta | Contenido | Madurez orientativa |
|---------|-----------|---------------------|
| `00-administracion/` | Matrícula, calendario, trámites (anonimizado) | Operativo |
| `01-asignaturas/` | Una carpeta por asignatura + optativas + TFM + `practicum/` | Núcleo maduro (Psicología, Procesos, Sociedad, Diseño curricular…) |
| `02-apuntes/` | Índice general, glosario central, transversales con **contenido** | Operativo (sin reservas vacías) |
| `03-materiales/` | Materiales docentes reutilizables | Operativo |
| `04-pbl-abp/` | Situaciones de aprendizaje, ABP, Jigsaw | Parcial / en crecimiento |
| `05-python-jupyter/` | Marco didáctico + notebooks (tarifas, perímetro-área) | Operativo (base) |
| `06-inteligencia-artificial/` | IA en educación (estructura + recursos) | Parcial |
| `07-evaluacion/` | Instrumentos y rúbricas | Parcial |
| `08-podcasts/` | Guiones e índices | Operativo |
| `09-bibliografia/` | Autores-pensadores, índices | Operativo |
| `10-proyectos/` | Proyectos integradores | Reserva / poco contenido |
| `99-archivo/` | Histórico / scripts one-shot | Activo para archivo |

---

## `02-apuntes/` — solo lo que existe

| Ruta | Contenido |
|------|-----------|
| `glosario-central-master.md` | Lenguaje común |
| `didactica/` | DUA transversal |
| `evaluacion/` | Evaluación formativa global |
| `tecnologia-educativa/` | IA en el aula de Matemáticas |
| `legislacion-educativa/` | Libertad de cátedra |
| `recursos-externos/` | Listados GitHub |

*Eliminado (2026-10-07):* `psicologia/`, `matematicas/`, `sociologia-educacion/` (solo `.gitkeep`; el contenido vive en Psicología, Diseño curricular y Sociedad/Procesos).

---

## Practicum — tres carpetas, un criterio

| Carpeta | Rol |
|---------|-----|
| **`01-asignaturas/practicum/`** | **Espacio de trabajo integrado** versionable: observación, centro, aula, diario, memoria, reflexiones, actividades (**anonimizado**). |
| **`practicum-i/`** | Ficha de la asignatura Practicum I (README, bibliografía, `trabajos/` local no versionado). |
| **`practicum-ii/`** | Idem Practicum II. |

No duplicar diarios ni análisis de centro en I/II: eso va en `practicum/`.

Ver [TRABAJOS-LOCAL.md](01-asignaturas/TRABAJOS-LOCAL.md).

---

## Asignaturas (01-asignaturas/)

- **Obligatorias:** Psicología; Procesos y contextos; Sociedad-familia-grupos; Diseño curricular; Contenidos disciplinares; Diseño de actividades; Innovación e investigación; Practicum I; Practicum II; TFM.
- **Optativas:** ver `01-asignaturas/optativas/`.
- **Trabajo de prácticas anonimizado:** `01-asignaturas/practicum/`.

---

## Índices que deben mantenerse al día

| Índice | Ruta |
|--------|------|
| Manifest (este archivo) | `MANIFEST.md` |
| README raíz | `README.md` |
| Asignaturas | `01-asignaturas/README.md` |
| Apuntes generales | `02-apuntes/INDICE.md` |
| Autores | `09-bibliografia/autores-pensadores/INDICE.md` |

---

## Licencia

Contenido propio: **CC BY-SA 4.0** (`LICENSE`). Enlaces a terceros: licencia original.
