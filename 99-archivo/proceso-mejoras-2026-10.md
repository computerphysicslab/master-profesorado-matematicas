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

### Fase 1 — Evaluación (prioridad máxima)

- [x] Completar `07-evaluacion/README.md` e `INDICE.md`
- [ ] Instrumentos de bajo coste (6–8) en `instrumentos/`
- [ ] Completar / alinear rúbricas de proceso (ya hay 4 CE; socioafectivo cubierto en CE9–10)
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

**Hecho:** inventario; `ESTADO.md`; esta memoria; trabajo en `main`.

### 2026-10-13 — Paso 1.1 (README + INDICE de evaluación)

**Objetivo:** convertir la puerta de entrada de `07-evaluacion/` en documentación operativa (sin crear aún los instrumentos).

**Archivos afectados:**

- `07-evaluacion/README.md` — reescrito: principios, mapa de carpetas, 4 rúbricas enlazadas, enlaces al resto del repo, próximos pasos.
- `07-evaluacion/INDICE.md` — reescrito: tablas por subcarpeta, estado pendiente/operativo, enlaces cruzados.
- `99-archivo/proceso-mejoras-2026-10.md` — checklist y diario.

**Verificación:**

- Enlaces relativos a `02-apuntes/evaluacion/`, rúbricas existentes, materiales de Diseño curricular, síntesis y bibliografía: coherentes desde `07-evaluacion/`.
- No se ha borrado ni reescrito ninguna rúbrica CE.
- Tono académico alineado con el apunte de evaluación formativa global.
- Sin datos personales.

**Siguiente paso:** Fase 1.2 — primer lote de instrumentos de bajo coste en `instrumentos/` (p. ej. ticket entrada/salida + portfolio de errores + lista de cotejo de argumentación), 1–3 archivos por commit.

**Riesgos / dudas:** ninguna. Las rúbricas CE9–10 ya cubren socioafectivo/colaboración; no es obligatorio crear una quinta rúbrica solo de CE.M.9.

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
