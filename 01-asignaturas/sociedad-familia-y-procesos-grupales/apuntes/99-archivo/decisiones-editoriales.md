# Decisiones editoriales — reestructuración SFYPG apuntes

**Fecha inicio:** 2026-10-22

## Principios aplicados
1. No eliminar contenido académico útil.
2. Priorizar `git mv` (o mv equivalente) para preservar historial.
3. Clasificar por temática principal según programa oficial.
4. Para contenidos mixtos: ubicación principal + enlaces cruzados (sin duplicar).
5. Crear estructura de carpetas completa aunque algunos temas carezcan aún de documento principal.

## Decisiones registradas

### 2026-10-22 — Clasificación inicial de los 5 apuntes existentes
- Tema1_El_aula_como_grupo.md → 02-psicologia-social/05-el-aula-como-grupo/ (inequívoco)
- Tema2_Relaciones_de_poder_en_el_aula.md → 02-psicologia-social/06-relaciones-de-poder-en-el-aula/ (inequívoco)
- Tema3_Interaccion_y_comunicacion_en_el_aula.md → 02-psicologia-social/04-interaccion-y-comunicacion-en-el-aula/ (inequívoco)
- Tema4_Prejuicio_y_estereotipos_ante_la_diversidad.md → 02-psicologia-social/07-prejuicio-y-estereotipos-ante-la-diversidad/ (principal; secciones de género/cultura se enlazarán desde 03)
- Tema5_Familia_escuela_acompanamiento_aprendizaje.md → 01-sociologia/02-familia-y-educacion/ (inequívoco)

### 2026-10-22 — Contenidos mixtos (género / cultura)
- Tema4 (ahora en 07) incluye secciones relevantes de género en matemáticas, interculturalidad y diversidad cultural.
- Decisión: **no fragmentar** el documento. Ubicación principal = 07-prejuicio-y-estereotipos.
- En 03-familia-genero-y-cultura se crea un README que enlace explícitamente a las secciones correspondientes de Tema4.
- No se duplica texto.

### 2026-10-22 — Temas oficiales 1 y 3 sin documento principal
- 01-sociedad-y-educacion: carpeta + README con descripción y enlaces a bibliografía sociológica.
- 03-familia-genero-y-cultura: README + enlace cruzado a Tema4 (07).
- Se evita crear contenido inventado; solo estructura y punteros.

### Renombrado de archivos
- Se mantienen los nombres originales (TemaN_....md) dentro de las carpetas de tema.
