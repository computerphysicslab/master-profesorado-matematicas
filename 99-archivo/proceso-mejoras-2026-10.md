# Memoria del proceso supervisado — Mejoras oct 2026

**Repo:** [master-profesorado-matematicas](https://github.com/computerphysicslab/master-profesorado-matematicas)  
**Rama:** `main`  
**Inicio:** 2026-10-13  
**Estado global:** [ESTADO.md](../ESTADO.md)

Este archivo es la **memoria persistente** del proceso. Cada paso actualiza el diario y la checklist.

---

## Principios (recordatorio)

- Pasos atómicos (1–3 archivos por commit preferible).
- Informe al usuario en cada update.
- Verificar enlaces, MANIFEST, tono académico, anonimato.
- No inventar teoría: basarse en material ya presente en el repo.
- No borrar sin confirmación; no cambios de estructura de primer nivel sin OK.

---

## Checklist de fases

### Fase 0 — Preparación y diagnóstico

- [x] Crear `ESTADO.md` en la raíz
- [x] Inventario rápido de madurez y carpetas con solo README / `.gitkeep`
- [x] Confirmar trabajo en `main` (protegida: sin force push ni borrado)
- [x] Crear esta memoria en `99-archivo/`

**Hallazgos clave (diagnóstico):**

| Zona | Situación |
|------|-----------|
| `07-evaluacion/` | README + INDICE mínimos; **4 rúbricas CE** ya existen; `instrumentos/`, `ejemplos/`, `normativa/` solo `.gitkeep`; formativa/sumativa/auto/coeval = README carcasa |
| `04-pbl-abp/` | Plantilla SA + varias SA (`ajedrez`, `gaussiana`, `eratostenes`, etc.); `retos/` vacío; unificar y completar |
| `06-inteligencia-artificial/` | Estructura rica (prompts, ética, evaluación); ampliable |
| `10-proyectos/` | Investigación Elkonin-Davydov; resto reserva |
| Enlaces | Pendiente revisión sistemática (Fase 3) |

### Fase 1 — Evaluación (prioridad máxima)

- [ ] Completar `07-evaluacion/README.md` e `INDICE.md`
- [ ] Instrumentos de bajo coste (6–8) en `instrumentos/`
- [ ] Completar / alinear rúbricas de proceso (ya hay 4 CE; añadir socioafectivo si falta)
- [ ] Ejemplo completo de alineación criterio → tarea → evidencia → calificación
- [ ] Enlazar desde `02-apuntes/evaluacion/` y Diseño curricular / Diseño de actividades

### Fase 2 — Situaciones de Aprendizaje

- [ ] Revisar plantilla SA
- [ ] 4–5 SA completas listas para adaptar
- [ ] Actualizar `04-pbl-abp/INDICE.md` y README

### Fase 3 — Enlaces

- [ ] `sintesis-conocimientos-fundamentales.md`
- [ ] `02-apuntes/INDICE.md`
- [ ] READMEs de asignaturas y Diseño curricular
- [ ] `09-bibliografia/autores-pensadores/`

### Fase 4 — Practicum II / TFM / IA / Python

- [ ] Carcasas practicum-ii / TFM
- [ ] Ejemplo flujo observación → diario → memoria (sintético)
- [ ] Material mínimo adicional IA / Python si hay margen

### Fase 5 — Cierre

- [ ] Actualizar MANIFEST + ESTADO
- [ ] Coherencia de la síntesis
- [ ] Resumen final al usuario

---

## Diario de ejecución

### 2026-10-13 — Paso 0.1 (diagnóstico)

**Hecho:**

- Inventario del árbol del repo (~1128 rutas).
- Creado [`ESTADO.md`](../ESTADO.md) con madurez por carpeta.
- Creada esta memoria.
- Confirmado: trabajo en `main`.

**Archivos:** `ESTADO.md`, `99-archivo/proceso-mejoras-2026-10.md`.

**Verificación:** no se han tocado apuntes ni materiales existentes; solo documentación de estado. MANIFEST no modificado aún (se actualizará en Fase 5 o cuando cambie la estructura).

**Siguiente paso:** Fase 1.1 — Completar `07-evaluacion/README.md` e `INDICE.md` (sin crear aún todos los instrumentos).

**Riesgos / dudas:** ninguna bloqueante. Las 4 rúbricas CE ya existentes se reutilizarán y se enlazarán; no se reescriben de cero.

---

## Formato de informe (plantilla para cada update)

```
### Paso X.Y — título
- Objetivo:
- Archivos afectados:
- Verificación:
- Pendientes actualizados:
- Riesgos / confirmación usuario:
```
