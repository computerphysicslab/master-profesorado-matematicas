# Metodología — Bibliometría de TFM

## 1. Objetivo

Identificar **señales de trascendencia académica** en TFM de Educación Matemática (Máster de Profesorado, especialidad Matemáticas) y describir qué características metodológicas aparecen en los trabajos que más allá del máster generan publicaciones, datos de aula o continuidad investigadora.

No se pretende:

- un ranking oficial de «mejores TFM»;
- una métrica única de citas (imposible con la indexación actual);
- sustituir al [Atlas de nichos](../atlas-nichos/) (que mide saturación temática).

## 2. Señales de influencia (indicadores)

| Indicador | Qué mide | Fiabilidad relativa |
|-----------|----------|---------------------|
| Publicación derivada (artículo) | El TFM se convirtió en paper | Alta si hay enlace explícito repositorio ↔ artículo |
| Comunicación en congreso | Difusión académica posterior | Media–alta |
| Citas (Scholar, OpenAlex, Dialnet, Semantic Scholar) | Impacto bibliométrico | Baja–media (cobertura desigual de TFM) |
| Citado en tesis o TFM posteriores | Reutilización académica | Media cuando se verifica |
| Intervención real de aula + datos | Potencial empírico | Alta como *proxy* de investigabilidad |
| Pretest–postest / diseño cuasiexperimental | Rigor de la evidencia | Alta como señal de diseño |
| Acceso abierto | Visibilidad | Media |
| Continuidad investigadora del autor | Carrera posterior en el tema | Media (requiere seguimiento) |
| Antigüedad | Tiempo para acumular citas | Contexto, no calidad |
| Descargas del repositorio | Interés de lectura | Baja–media (sesgos de portal) |

## 3. Criterios de inclusión en la preselección v0.1

Un TFM entra en la lista de «potencialmente influyentes» si cumple **al menos una** de:

1. Evidencia de **publicación o comunicación científica** derivada.
2. **Diseño de investigación de aula** (cuestionario, intervención, análisis de datos, preguntas abiertas), no solo propuesta didáctica.
3. **Tema pionero o muy reutilizable** en el contexto español del momento (p. ej. primeras oleadas de gamificación, flipped, GeoGebra con datos de centro).
4. Acceso abierto y documentación suficiente para contrastar metodología.

## 4. Limitaciones (leer antes de citar esta carpeta)

- No hay un registro bibliométrico nacional de TFM comparable al de artículos.
- Muchos TFM excelentes no están en abierto o no generan paper; **ausencia en esta lista no implica baja calidad**.
- Las «estrellas» de la preselección son **orientativas**, no puntuaciones objetivas.
- Los nombres de universidad se usan como **metadato factual** del trabajo, no como ranking de centros.
- La preselección v0.1 es **exploratoria** y debe actualizarse con verificación de URLs y citas.

## 5. Campos del corpus (`corpus-tfm.csv`)

```text
id, autor, titulo, universidad, anio, repositorio, url_tfm,
tema, etapa, metodologia, intervencion_aula, datos_empiricos,
publicacion_derivada, url_publicacion,
citas_google_scholar, citas_openalex, citas_dialnet, citas_semantic_scholar,
citado_por_tesis, citado_por_tfm, descargas,
continuidad_investigadora, senales_influencia, nivel_evidencia,
fecha_verificacion, observaciones
```

- `nivel_evidencia`: alta | media | exploratoria  
- `senales_influencia`: lista breve separada por `;`

## 6. Fase 2 (ampliación prevista)

1. Ampliar a 50–100 TFM (mismas fuentes que el atlas + repositorios de UCM, UAM, UNED, UJA, Sevilla, Granada, Málaga, etc.).
2. Contrastar citas en Google Scholar, OpenAlex, Crossref, Dialnet, Semantic Scholar.
3. Crear fichas individuales **solo** cuando haya evidencia verificada.
4. Cruzar con el atlas: temas de **baja saturación** y **alta tasa de publicación derivada**.

## 7. Preguntas de análisis

- ¿Qué proporción de TFM con publicación derivada tuvieron intervención experimental?
- ¿Qué temas producen más artículos (GeoGebra, flipped, gamificación, estadística…)?
- ¿Qué metodologías aparecen en los TFM que luego generan paper?
- ¿Qué intersecciones tienen a la vez baja saturación (atlas) y alto potencial de publicación (bibliometría)?
