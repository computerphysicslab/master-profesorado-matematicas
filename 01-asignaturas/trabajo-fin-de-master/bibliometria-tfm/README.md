# Bibliometría de TFM — Educación Matemática

Estudio exploratorio de **Trabajos Fin de Máster** de la especialidad de Matemáticas que muestran señales de **trascendencia académica** más allá del propio máster (publicaciones derivadas, investigación empírica de aula, reutilización potencial, continuidad investigadora).

> **No es un ranking oficial de calidad ni de citas.** Los repositorios españoles no ofrecen contadores homogéneos de citas y Google Scholar / OpenAlex no indexan todos los TFM de forma comparable. Esta carpeta reúne evidencias documentadas y criterios explícitos para ir afinando el mapa.

## Relación con el resto del TFM

| Carpeta | Pregunta |
|---------|----------|
| [ejemplos-tfm/](../ejemplos-tfm/) | ¿Cómo son los TFM que existen? |
| [atlas-nichos/](../atlas-nichos/) | ¿Qué temas están saturados y dónde están los huecos? |
| **bibliometria-tfm/** | ¿Qué TFM han conseguido trascender y por qué? |
| [ideas-interesantes/](../ideas-interesantes/) | ¿Qué ideas concretas podría desarrollar yo? |

Cadena de uso recomendada:

```text
CORPUS DE TFM
      ↓
ATLAS DE NICHOS          (saturación temática)
      ↓
BIBLIOMETRÍA / IMPACTO   (trascendencia)
      ↓
CARACTERÍSTICAS DE LOS TFM QUE TRASCIENDEN
      ↓
NICHOS POCO SATURADOS + ALTO POTENCIAL DE PUBLICACIÓN
      ↓
IDEAS PARA EL TFM
```

## Estructura

| Ruta | Contenido |
|------|-----------|
| [metodologia.md](metodologia.md) | Criterios, señales de influencia, limitaciones |
| [corpus/corpus-tfm.csv](corpus/corpus-tfm.csv) | Metadatos normalizados (preselección inicial) |
| [rankings/tfm-potencialmente-influyentes.md](rankings/tfm-potencialmente-influyentes.md) | Preselección de 20 TFM con señales de impacto |
| [rankings/tfm-con-publicaciones-derivadas.md](rankings/tfm-con-publicaciones-derivadas.md) | Casos con artículo o congreso derivado |
| [analisis/caracteristicas-tfm-trascendentes.md](analisis/caracteristicas-tfm-trascendentes.md) | Patrones metodológicos |
| [analisis/tfm-to-paper.md](analisis/tfm-to-paper.md) | Del TFM a la publicación |
| [analisis/oportunidades-investigacion.md](analisis/oportunidades-investigacion.md) | Implicaciones para elegir tema |
| `fichas/` | Reservado: fichas individuales cuando el corpus esté contrastado |

## Hipótesis de trabajo

Los TFM con más potencial de trascender no son necesariamente los que presentan la unidad didáctica más elaborada, sino los que siguen una lógica cercana a la investigación:

```text
problema educativo → marco teórico → pregunta/hipótesis
    → intervención / datos → análisis → resultados → preguntas abiertas
```

## Estado

- **v0.1 (2026-10-01):** preselección exploratoria de 20 TFM; metodología y análisis inicial.
- Próximo paso: ampliar corpus (50–100), contrastar citas en Scholar / OpenAlex / Dialnet y completar fichas solo con evidencia verificada.

## Licencia y uso

Uso educativo y de investigación. Los trabajos originales pertenecen a sus autores y repositorios.
