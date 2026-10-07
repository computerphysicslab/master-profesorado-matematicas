# Limpieza estructural — 2026-10-07

Registro del commit de consolidación de solapamientos y reservas vacías.

## Problema

- Carpetas reservadas casi vacías en `02-apuntes/` (`psicologia/`, `matematicas/`, `sociologia-educacion/`) cuyo contenido real estaba en `01-asignaturas/`.
- Posible confusión entre `practicum-i/`, `practicum-ii/` y `practicum/`.
- MANIFEST e índices desfasados respecto al estado real del repo.

## Acciones

1. **Eliminado** el contenido versionado de las reservas vacías (`.gitkeep`) en:
   - `02-apuntes/psicologia/`
   - `02-apuntes/matematicas/`
   - `02-apuntes/sociologia-educacion/`
2. **Criterio fijado** en [MANIFEST.md](../MANIFEST.md):
   - Apuntes de asignatura → `01-asignaturas/<asignatura>/apuntes/`
   - Transversales → `02-apuntes/` **solo si hay archivo real**
   - No crear carpetas vacías “por si acaso”
3. **Practicum:**
   - `01-asignaturas/practicum/` = trabajo anonimizado versionable (diario, centro, aula…)
   - `practicum-i/` y `practicum-ii/` = carcasa de asignatura + enlace a `practicum/`
4. **Índices actualizados:** MANIFEST, README raíz, `01-asignaturas/README`, `02-apuntes/INDICE` y `README`, READMEs de practicum / I / II.

## Qué se mantiene en `02-apuntes/`

| Carpeta / archivo | Motivo |
|-------------------|--------|
| `glosario-central-master.md` | Transversal |
| `didactica/` | DUA |
| `evaluacion/` | Evaluación formativa global |
| `tecnologia-educativa/` | IA en el aula |
| `legislacion-educativa/` | Libertad de cátedra |
| `recursos-externos/` | Listados GitHub |

## Pendiente (no bloqueante)

- `10-proyectos/`: poco contenido; archivar o llenar a medio plazo.
- `06-inteligencia-artificial/`: estructura > contenido operativo.
- `.gitkeep` residuales en carpetas que **sí** tienen markdown (didactica, evaluacion, tecnologia) — inocuos; se pueden borrar en una pasada cosmética.

---

*Documento de archivo; la norma vigente está en MANIFEST.md.*
