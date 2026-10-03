# Bibliometría de TFM — Educación Matemática

Estudio exploratorio de Trabajos Fin de Máster relacionados con Educación Matemática y especialidad de Matemáticas, centrado en **trascendencia, investigabilidad y reutilización posterior**.

> No es un ranking oficial de calidad ni de citas. El corpus distingue entre trabajos **verificados en repositorios institucionales** y candidatos exploratorios.

## Relación con el resto del TFM

| Carpeta | Pregunta |
|---------|----------|
| [ejemplos-tfm/](../ejemplos-tfm/) | ¿Cómo son los TFM existentes? |
| [atlas-nichos/](../atlas-nichos/) | ¿Saturación y huecos temáticos? |
| **bibliometria-tfm/** | ¿Señales de trascendencia e investigabilidad? |
| [ideas-interesantes/](../ideas-interesantes/) | ¿Qué idea concreta desarrollo? |

```text
CORPUS → ATLAS DE NICHOS → BIBLIOMETRÍA/IMPACTO
      → CARACTERÍSTICAS DE LOS TFM QUE TRASCIENDEN
      → NICHOS POCO SATURADOS + POTENCIAL DE PUBLICACIÓN
      → IDEAS PARA EL TFM
```

## Corpus v0.5

- **v0.1:** 20 registros exploratorios.
- **v0.2:** 30 registros (+10 verificados UVa / UAH / otros).
- **v0.3:** 38 registros (+8 de nicho: IA generativa, aprendizaje-servicio, contextualización cultural, investigación de aula UPNA sobre funciones/derivadas).
- **v0.4:** 40 registros (+2 de nicho: sostenibilidad + SA + DUA; videojuego educativo + DUA).
- **v0.5:** **43 registros** (+3 de **pensamiento crítico** / estadística crítica: correlación mates–PC; calidad del aire + ABP + R; LibreOffice + estadística).

Documentación de fuentes nuevas:
- [corpus/fuentes-verificadas-v03.md](corpus/fuentes-verificadas-v03.md)
- [corpus/fuentes-verificadas-v04.md](corpus/fuentes-verificadas-v04.md)
- [corpus/fuentes-verificadas-v05.md](corpus/fuentes-verificadas-v05.md) — pensamiento crítico
- [corpus/corpus-addon-v05.csv](corpus/corpus-addon-v05.csv) — filas nuevas aisladas

**Importante:** verificado ≠ influyente. La lista de potencialmente influyentes se mantiene en [rankings/](rankings/).

### Línea pensamiento crítico (v0.5)

| ID | Enfoque |
|----|--------|
| tfm-028 | IA + estudiante auditor + sesgo de automatización |
| tfm-031 | Bootcamp IA generativa + pensamiento crítico |
| **tfm-041** | Investigación cuantitativa: ¿las mates predicen el pensamiento crítico? |
| **tfm-042** | Estadística con datos reales de calidad del aire + juicio crítico |
| **tfm-043** | Estadística con LibreOffice + pensamiento crítico |

Encaje directo con [idea 05 — esfuerzo cognitivo y pensamiento crítico](../ideas-interesantes/05-esfuerzo-cognitivo-y-pensamiento-critico.md).

## Estructura

- [metodologia.md](metodologia.md)
- [corpus/corpus-tfm.csv](corpus/corpus-tfm.csv)
- [corpus/fuentes-verificadas-v02.md](corpus/fuentes-verificadas-v02.md) … [v05](corpus/fuentes-verificadas-v05.md)
- [rankings/tfm-potencialmente-influyentes.md](rankings/tfm-potencialmente-influyentes.md)
- [rankings/tfm-con-publicaciones-derivadas.md](rankings/tfm-con-publicaciones-derivadas.md)
- [analisis/caracteristicas-tfm-trascendentes.md](analisis/caracteristicas-tfm-trascendentes.md)
- [analisis/tfm-to-paper.md](analisis/tfm-to-paper.md)
- [analisis/oportunidades-investigacion.md](analisis/oportunidades-investigacion.md)
- [fichas/](fichas/) — fichas individuales solo con evidencia contrastada

## Estado y siguiente fase

- Ampliar hacia 50–100 TFM.
- Contrastar citas (Scholar, OpenAlex, Dialnet) y publicaciones derivadas.
- Cruzar sistemáticamente con intersecciones del atlas y con idea 05 (demanda cognitiva × pensamiento crítico).
