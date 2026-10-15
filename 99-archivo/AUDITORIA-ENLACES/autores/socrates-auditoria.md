# Auditoría - Sócrates

- **Ficha:** `09-bibliografia/autores-pensadores/01-filosofia-educacion/socrates.md` (**EXISTE**)
- **Menciones totales (estimación):** 15+ en el repo (código de búsqueda + índices)
- **Enlaces actuales a `socrates.md`:** **4** — todos **dentro** de `09-bibliografia/autores-pensadores/`

## Enlaces actuales (archivo)

| Archivo | Tipo |
|---------|------|
| `09-bibliografia/autores-pensadores/INDICE.md` | Índice con enlace |
| `09-bibliografia/autores-pensadores/INDICE-POR-RELEVANCIA.md` | Tabla |
| `09-bibliografia/autores-pensadores/MAPA-AUTOR-AMBITO.md` | Lista por ámbito |
| `09-bibliografia/autores-pensadores/historia-del-pensamiento-educativo.md` | Entrada histórica con enlace |

**Ningún enlace** a la ficha desde `01-asignaturas/`, `04-pbl-abp/` ni `06-inteligencia-artificial/`.

## Menciones sustantivas sin enlace (huecos críticos)

### 06-inteligencia-artificial/ (prioridad ALTA)

| Archivo | Contexto |
|---------|----------|
| `actividades/dialogo-socratico-ia-completo.md` | Título y cuerpo: «diálogo socrático», «tutor socrático»; secuencia completa sin citar ficha |
| `actividades/propuestas-aula.md` | Sección «Diálogo socrático con la IA» |
| `actividades/README.md` | Enlace a la actividad socrática |
| `INDICE.md` | Entrada «tutor socrático» |
| `prompts/catalogo-prompts-matematicas.md` | Prompt «Tutor socrático (sin dar la solución)» |
| `prompts/diseno-prompts.md` | Rol «tutor socrático» |
| `educacion/ia-educacion-matematicas.md` | «Simulación de diálogo socrático» |
| `herramientas/matriz-herramientas.md` | «pistas socráticas» |

### 01-asignaturas/ (prioridad ALTA)

| Archivo | Contexto |
|---------|----------|
| `procesos-y-contextos-educativos/materiales/origenes-pedagogia-practica-y-reflexion.md` | Sección «Sócrates y después»: mayéutica, filosofía de la educación; **sin enlace** a la ficha (Platón y Aristóteles tampoco) |

### Otras posibles (prioridad MEDIA — re-verificar en iteración de cierre)

- Habilidades comunicativas / diálogo / pregunta (optativas), si mencionan método socrático.
- Diseño de actividades / IRF / feedback, si aluden a pregunta socrática.

## Propuesta de enlaces

| Archivo origen | Texto actual (idea) | Propuesta |
|----------------|---------------------|-----------|
| `06-inteligencia-artificial/actividades/dialogo-socratico-ia-completo.md` | Diálogo socrático / tutor socrático | Añadir en metadatos o «Marco»: fundamento en [Sócrates — mayéutica](../../09-bibliografia/autores-pensadores/01-filosofia-educacion/socrates.md) |
| `06-inteligencia-artificial/actividades/propuestas-aula.md` | ## 2. Diálogo socrático… | Enlace a la ficha en el título o primera mención sustantiva |
| `06-inteligencia-artificial/prompts/catalogo-prompts-matematicas.md` | ### Tutor socrático | Nota: basado en el método socrático → [socrates.md](../../09-bibliografia/autores-pensadores/01-filosofia-educacion/socrates.md) |
| `06-inteligencia-artificial/educacion/ia-educacion-matematicas.md` | diálogo socrático | Enlace en la primera mención |
| `01-asignaturas/procesos-y-contextos-educativos/materiales/origenes-pedagogia-practica-y-reflexion.md` | Con **Sócrates**, **Platón**… (mayéutica) | `[Sócrates](../../../../09-bibliografia/autores-pensadores/01-filosofia-educacion/socrates.md)` (y análogo Platón / Aristóteles) |

## Prioridad global

**ALTA** — Patrón tipo «caso Sócrates»: mucha pedagogía aplicada (IA socrática) y cero enlaces fuera del directorio de autores.

## Notas metodológicas

- La búsqueda en la API de código de GitHub **no indexa el 100 %** del texto; los conteos son **mínimos verificados**. Un `git grep` local en un clon completo puede subir el número de menciones.
- No se proponen cambios fuera de `99-archivo/` en esta fase (solo auditoría).
