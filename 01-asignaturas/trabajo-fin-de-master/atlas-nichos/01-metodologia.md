# Metodología del Atlas de Nichos TFM

## Objetivo

Pasar de una clasificación **intuitiva** de temas a un mapa basado en **TFM y literatura reales**, con intersecciones candidatas a TFM del Máster de Profesorado (Matemáticas).

## Versión 0 (actual)

1. Corpus semilla: ejemplos en `ejemplos-tfm/` + TFM abiertos localizados en repositorios españoles.
2. Clasificación manual por ejes (contenido, metodología, tecnología, cognición, socioafectivo…).
3. Identificación cualitativa de zonas densas vs. intersecciones poco pobladas.
4. Formulación de preguntas investigables en [02-nichos-candidatos.md](02-nichos-candidatos.md).

Plantilla de datos: [corpus/plantilla-corpus.csv](corpus/plantilla-corpus.csv).

## Hacia la versión 1.0

### Ampliación del corpus (meta orientativa: 100–200 TFM)

Repositorios prioritarios (lista no exhaustiva):

- Zaguán / repositorios de másteres de profesorado de matemáticas
- UNED, Oviedo, Navarra, Alcalá
- Universidades catalanas y valencianas
- Otros repositorios institucionales españoles con TFM en abierto

### Campos a extraer por trabajo

```text
TFM
 ├── id
 ├── año
 ├── universidad
 ├── título
 ├── url_pdf
 ├── nivel_educativo          (ESO / Bach. / mixto)
 ├── contenido_matematico     (álgebra, funciones, geometría, estadística…)
 ├── metodologia              (ABP, flipped, cooperativo, secuencia didáctica…)
 ├── tecnologia               (GeoGebra, Desmos, IA, videojuego, RA, 3D…)
 ├── competencia_matematica   (RP, modelización, representación…)
 ├── variable_cognitiva       (espacial, memoria de trabajo, metacognición…)
 ├── variable_socioafectiva   (ansiedad, motivación, mindset…)
 ├── evaluacion               (rúbricas, pre-post, observación…)
 ├── poblacion                (curso, N si consta)
 └── palabras_clave
```

### Análisis

1. Frecuencias por eje.
2. **Matriz de coocurrencias** (contenido × tecnología, tecnología × cognición, etc.).
3. Posicionamiento en el plano **centralidad × densidad** (ver [03-mapa-saturacion.md](03-mapa-saturacion.md)).
4. Ranking de **15–30 intersecciones** con ficha:

| Campo | Pregunta |
|-------|----------|
| Qué se ha investigado | Resumen breve del corpus + literatura |
| Qué está saturado | Evitar repetición estéril |
| Qué falta | Hueco concreto |
| Pregunta investigable | Formulación operativa |
| Metodología viable en un TFM | Diseño realista (Practicum, N, instrumentos) |

### Criterios de calidad

- Solo TFM con **acceso abierto** verificable (o metadatos suficientes + enlace estable).
- No plagiar: el Atlas orienta la **elección de tema**, no aporta texto reutilizable de memorias ajenas.
- Separar **evidencia de TFM** (producción del máster) de **evidencia científica** (artículos/revisiones).

### Versionado

| Versión | Criterio de cierre |
|---------|-------------------|
| **v0** | Corpus semilla + hallazgos cualitativos + nichos candidatos |
| **v1.0** | ≥100 TFM codificados + coocurrencias + ranking de intersecciones |
| **v1.x** | Actualización anual de corpus y literatura frontera |
