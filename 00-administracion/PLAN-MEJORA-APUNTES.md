# Plan de mejora incremental de apuntes — Máster de Profesorado (Matemáticas)

**Ubicación canónica:** `00-administracion/PLAN-MEJORA-APUNTES.md`  
**Última actualización:** 2026-10-10  
**Estado de la auditoría inicial:** completada (Fase I–III)

---

## 1. Objetivo y criterios generales

Realizar una mejora **iterativa, tema a tema**, de los apuntes del repositorio, priorizando:

1. Asignaturas sin apuntes o con materiales mínimos.
2. Asignaturas con apuntes muy incompletos.
3. Ampliaciones sustanciales.
4. Correcciones y mejoras puntuales de materiales ya desarrollados.

**Principios inquebrantables**

- Los apuntes reales de clase son la fuente prioritaria: no se eliminan, sustituyen ni reescriben arbitrariamente.
- Los programas oficiales se usan solo como **referencia** para detectar lagunas; el orden real de las clases prevalece.
- El resultado final debe ser **genérico y reutilizable** (sin referencias a universidades concretas ni dominios institucionales).
- Se conservan referencias bibliográficas académicas (autores, obras).
- Cada tarea es pequeña, verificable e independiente.
- No se marca una tarea como completada hasta comprobar sus criterios de finalización.

---

## 2. Resumen del estado de la auditoría (2026-10-10)

### Estructura del repositorio
Organizado según `MANIFEST.md`. Núcleo en `01-asignaturas/`. Transversales reales en `02-apuntes/`. Materiales reutilizables en `03-materiales/` (incluye `historias-matematicas/` con ~32 fichas).

### Inventario resumido de cobertura

| Asignatura | Estado de apuntes | Prioridad |
|------------|-------------------|-----------|
| Psicología del desarrollo y de la educación | Cubierto (5 temas) | Baja |
| Procesos y contextos educativos | Cubierto (6 temas) | Baja |
| Sociedad, familia y procesos grupales | Cubierto (4 temas) | Baja |
| Diseño curricular e instruccional de Matemáticas | Cubierto / Parcial (9 bloques + materiales ricos) | Media-baja |
| **Contenidos disciplinares de Matemáticas** | **Completo** (T-CD-01 a T-CD-05) | Media (pasar a Diseño de actividades) |
| **Diseño de actividades para el aprendizaje de Matemáticas** | **Sin apuntes** | **Alta** |
| **Innovación e investigación educativa en Matemáticas** | **Sin apuntes** | **Alta** |
| Practicum I / II | Parcial (trabajo anonimizado + carcasas) | Media |
| Trabajo Fin de Máster | Parcial (herramientas y ejemplos) | Media |
| Educación emocional (optativa) | Cubierto (11+ temas) | Baja |
| Otras optativas | Sin apuntes o mínimos | Baja |

---

## 3. Matriz de cobertura (resumen)

Clasificación: Sin apuntes · Pendiente · Parcial · Cubierto · Por verificar.

---

## 4. Lista ordenada de tareas

### Bloque A — Contenidos disciplinares de Matemáticas (prioridad 1)

| ID | Tema | Archivo | Estado | Notas |
|----|------|---------|--------|-------|
| **T-CD-01** | Visión histórica del desarrollo de las Matemáticas | `…/01-vision-historica.md` | **completada** | 2026-10-10 |
| **T-CD-02** | Geometría sintética, escuela griega, axiomatización euclidiana | `…/02-geometria-sintetica-euclides.md` | **completada** | 2026-10-10 |
| **T-CD-03** | Plano ampliado, dualidad, cónicas y génesis de la geometría proyectiva | `…/03-geometria-proyectiva.md` | **completada** | 2026-10-10 |
| **T-CD-04** | Reflexión sobre conceptos del currículo de Secundaria/Bachillerato | `…/04-reflexion-curricular.md` | **completada** | 2026-10-10 |
| **T-CD-05** | Laboratorio de software / aplicaciones | `…/05-laboratorio-software.md` | **completada** | 2026-10-10 |

### Bloque B — Diseño de actividades (prioridad 2)

| ID | Tema | Estado |
|----|------|--------|
| T-DA-01 | Principios de diseño de tareas matemáticas | pendiente |
| T-DA-02 | Secuenciación y análisis de actividades | pendiente |
| T-DA-03 | Modelización y situaciones de aprendizaje | pendiente |
| T-DA-04 | Evaluación de actividades y feedback | pendiente |

### Bloque C — Innovación e investigación (prioridad 3)

| ID | Tema | Estado |
|----|------|--------|
| T-II-01 | Conceptos de innovación docente en matemáticas | pendiente |
| T-II-02 | Metodologías de investigación educativa en didáctica de las matemáticas | pendiente |
| T-II-03 | Análisis de innovaciones y evaluación de impacto | pendiente |
| T-II-04 | Líneas de investigación y conexión con TFM | pendiente |

### Bloque D — Seguimiento y coherencia

| ID | Tema | Estado |
|----|------|--------|
| T-PLAN-01 | Mantener este documento de seguimiento | en curso |
| T-REV-01 | Coherencia terminológica Diseño curricular ↔ nuevos apuntes S2 | pendiente |

---

## 5. Registro breve de cambios

| Fecha | Tarea | Cambio realizado |
|-------|-------|------------------|
| 2026-10-10 | Auditoría inicial | Diagnóstico, matriz, plan y documento de seguimiento creados |
| 2026-10-10 | T-CD-01 | Creado `01-vision-historica.md` |
| 2026-10-10 | T-CD-02 | Creado `02-geometria-sintetica-euclides.md` |
| 2026-10-10 | T-CD-03 | Creado `03-geometria-proyectiva.md` |
| 2026-10-10 | T-CD-04 | Creado `04-reflexion-curricular.md` |
| 2026-10-10 | T-CD-05 | Creado `05-laboratorio-software.md` (laboratorio GeoGebra/Python) |

---

## 6. Próxima tarea recomendada

**T-DA-01** — Principios de diseño de tareas matemáticas  
(Asignatura: Diseño de actividades para el aprendizaje de Matemáticas).

---

## 7. Decisiones pendientes y limitaciones

- Commits remotos realizados vía conector GitHub.
- Bloque A (Contenidos disciplinares) cerrado.

---

*Este documento se actualiza al final de cada ciclo de trabajo.*
