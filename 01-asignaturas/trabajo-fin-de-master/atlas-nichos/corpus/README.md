# Corpus del Atlas de Nichos TFM

## Archivos

| Archivo | Contenido |
|---------|-----------|
| `plantilla-corpus.csv` | Corpus base v0.9 (~69 TFM) |
| `plantilla-corpus-v010-addon.csv` | **+20 entradas v0.10** (UPNA, UCM, UJI, UDIMA, UPV, UAH, UNIR + internacionales) |

**Total efectivo v0.10:** ~89 TFM (concatenar base + addon).

## Esquema

```text
id, anio, universidad, titulo, url_pdf, nivel_educativo, contenido_matematico,
metodologia, tecnologia, competencia_matematica, variable_cognitiva,
variable_socioafectiva, evaluacion, poblacion, palabras_clave, fuente_repo
```

## Nuevas fuentes v0.10

- **UPNA:** flipped+funciones, GeoGebra visual→álgebra, derivadas, socioafectivo PMAR
- **UCM:** movimientos en el plano (TAD)
- **UDIMA:** gamificación funciones + revisión videojuegos
- **UJI:** programaciones y progresiones
- **UPV:** SA geometría volúmenes
- **UAH:** DUA matemáticas
- **UNIR / otras:** GeoGebra funciones Bach; YouTube divulgación
- **Internacional:** DGBL scoping, GenAI algebra game, AR+GeoGebra microgames, Nepal circles

Ver ranking en [`../04-coocurrencias-y-ranking-v09.md`](../04-coocurrencias-y-ranking-v09.md) y hallazgos en [`../00-hallazgos-v0.md`](../00-hallazgos-v0.md).

## Enlace con bibliometría

Para señales de trascendencia (publicaciones derivadas, datos de aula) ver [**bibliometria-tfm/**](../../bibliometria-tfm/).
