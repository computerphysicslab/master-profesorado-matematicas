# Análisis PISA 2018: Aragón, España y B-S-J-Z (China)

**Análisis de microdatos** · Matemáticas · Control por índice socioeconómico y cultural (ESCS)

**Ciclo:** PISA 2018 (CY07)  
**Fichero de estudiantes:** `CY07_MSU_STU_QQQ.sav`  
**Código de B-S-J-Z (China):** QCI  
**Fecha del análisis:** octubre 2026  
**Herramientas:** Python (pyreadstat, pandas, scikit-learn)

---

## 1. Objetivo y preguntas de investigación

1. ¿Cuál es el rendimiento medio en matemáticas de Aragón, del conjunto de España y de las cuatro provincias chinas B-S-J-Z (Beijing–Shanghai–Jiangsu–Zhejiang) en PISA 2018?
2. ¿Qué parte de las diferencias se explica por el índice socioeconómico y cultural de los estudiantes (ESCS)?
3. ¿Se mantiene la ventaja de Aragón sobre España a igualdad de ESCS?
4. ¿Qué patrón muestra B-S-J-Z una vez controlado el ESCS?

---

## 2. Datos y método

### 2.1. Muestra analítica

| Grupo              | Código CNT | n (muestra) | n ponderado (aprox.) |
|--------------------|------------|-------------|----------------------|
| España             | ESP        | 35 943      | 416 703              |
| Aragón             | ESP (región) | 1 614     | 9 688                |
| B-S-J-Z (China)    | QCI        | 12 058      | 992 302              |

**Identificación de Aragón** a partir de la variable `STRATUM`:
- `ESP0203` → público (n = 1 026)
- `ESP0204` → privado/concertado (n = 588)

### 2.2. Variables utilizadas

- **Rendimiento:** 10 valores plausibles de matemáticas (`PV1MATH` … `PV10MATH`).
- **Peso:** peso final del estudiante (`W_FSTUWT`).
- **ESCS:** índice socioeconómico y cultural de PISA (media OCDE ≈ 0, DT ≈ 1).
- **Tipo de centro:** derivado del código de estrato (público vs privado/concertado).

### 2.3. Procedimientos de estimación

- **Media de matemáticas:** promedio de las 10 medias ponderadas de cada valor plausible.
- **Control por ESCS:**
  - Medias por quintiles de ESCS (cortes calculados sobre la muestra española).
  - Regresión lineal ponderada:  
    `MATH ≈ β₀ + β₁·ESCS + β₂·Aragón + β₃·QCI (+ β₄·privado)`

No se reportan errores estándar con replicate weights en esta versión (punto de mejora futuro).

---

## 3. Resultados descriptivos

### 3.1. Medias globales

| Grupo              | MATH  | ESCS   | Diferencia vs España |
|--------------------|-------|--------|----------------------|
| **España**         | 481.4 | –0.124 | —                    |
| **Aragón**         | 497.4 | –0.037 | **+16.0**            |
| **QCI (B-S-J-Z)**  | 591.4 | –0.665 | **+110.0**           |

- La media de España (481.4) y la de B-S-J-Z (591.4) coinciden con los valores oficiales publicados por la OCDE para PISA 2018.
- Aragón se sitúa **16 puntos** por encima de la media nacional (equivalente a aproximadamente medio curso escolar según la convención de la OCDE de ~30 puntos ≈ 1 curso).

### 3.2. Desglose por tipo de centro

| Grupo     | Tipo de centro       | n     | MATH  | ESCS   |
|-----------|----------------------|-------|-------|--------|
| Aragón    | Privado/concertado   | 588   | 510.0 | +0.238 |
| Aragón    | Público              | 1 026 | 490.3 | –0.192 |
| España    | Privado/concertado   | 14 251| 483.0 | –0.018 |
| España    | Público              | 21 692| 480.3 | –0.200 |

**Observaciones:**
- En el conjunto de España la diferencia público–privado en matemáticas es mínima (~2.7 puntos).
- En Aragón el gap es mayor (~19.7 puntos) y está alineado con la diferencia de ESCS entre familias.
- Los centros privados/concertados de Aragón (510) superan claramente la media nacional.

---

## 4. Control por ESCS: quintiles

Las medias de matemáticas se calcularon dentro de cada quintil de ESCS, utilizando los mismos puntos de corte derivados de la distribución española (para permitir comparación directa).

| Quintil ESCS     | España | Aragón | QCI     | Aragón – España | QCI – España |
|------------------|--------|--------|---------|-----------------|--------------|
| **Q1 (más bajo)**| 443.4  | 455.0  | **570.4** | +11.6         | **+127.0**   |
| **Q2**           | 463.0  | 480.5  | 586.8   | +17.5           | +123.8       |
| **Q3**           | 482.3  | 498.4  | 600.3   | **+16.1**       | **+118.0**   |
| **Q4**           | 504.4  | 521.9  | 628.0   | +17.5           | +123.6       |
| **Q5 (más alto)**| 529.4  | 534.5  | **643.3** | +5.1          | **+113.9**   |

### Lectura de los quintiles

1. **Aragón mantiene una ventaja estable de 11–17 puntos** sobre España en casi todos los niveles de ESCS. Solo se reduce en el quintil más alto (+5.1). La ventaja de Aragón **no se explica** por un ESCS medio ligeramente más favorable.

2. **B-S-J-Z mantiene una ventaja superior a 110 puntos en todos los quintiles.**  
   El alumnado de QCI del **quintil socioeconómico más bajo** (ESCS ≈ –1.67) obtiene **570 puntos**, por encima del alumnado español del **quintil más alto** (529 puntos).

3. El gradiente socioeconómico existe en los tres grupos (aproximadamente 73–86 puntos de Q1 a Q5), pero en QCI parte de una base mucho más elevada.

---

## 5. Regresión lineal ponderada

### Modelo 1: MATH ~ ESCS + Aragón + QCI

| Coeficiente                  | Valor   |
|-----------------------------|---------||
| Intercepto (España, ESCS=0) | 485.0   |
| Pendiente ESCS              | +25.2   |
| Efecto Aragón (vs España)   | **+14.1** |
| Efecto QCI (vs España)      | **+123.3** |

### Modelo 2: MATH ~ ESCS + Aragón + QCI + privado/concertado

| Coeficiente                  | Valor   |
|-----------------------------|---------||
| Intercepto                  | 485.7   |
| Pendiente ESCS              | +25.2   |
| Efecto Aragón               | **+14.1** |
| Efecto QCI                  | **+122.6** |
| Efecto privado/concertado   | –1.5    |

**Interpretación:**
- Cada unidad adicional de ESCS se asocia, de media, con **+25 puntos** en matemáticas.
- La ventaja neta de Aragón, una vez controlado el ESCS, es de **+14.1 puntos**.
- La ventaja neta de B-S-J-Z es de **+122–123 puntos** (incluso superior a la diferencia bruta, porque el ESCS medio de QCI es más bajo).
- El coeficiente del tipo de centro privado es **ligeramente negativo** (–1.5) una vez controlado el ESCS: la ventaja bruta de los centros privados se explica casi por completo por la composición socioeconómica de su alumnado.

---

## 6. Conclusiones

### 6.1. Sobre Aragón

- Aragón obtiene consistentemente mejores resultados en matemáticas que el conjunto de España (**+14 a +16 puntos**), y esta ventaja **se mantiene a igualdad de nivel socioeconómico**.
- La diferencia es relevante desde el punto de vista educativo (aproximadamente medio curso escolar) y no puede atribuirse a un perfil socioeconómico más favorable de la muestra aragonesa.
- Existe un gap público–privado más marcado en Aragón que en el conjunto de España, pero está fuertemente asociado al ESCS de las familias.

### 6.2. Sobre B-S-J-Z (China)

- Las cuatro provincias chinas (Beijing, Shanghai, Jiangsu, Zhejiang) muestran un rendimiento extraordinariamente alto (**591 puntos**).
- La ventaja respecto a España (**~110–123 puntos**) **no se reduce** al controlar por ESCS; al contrario, se mantiene o incluso aumenta ligeramente.
- El hallazgo más robusto es que el alumnado de QCI del quintil socioeconómico **más bajo** supera al alumnado español del quintil **más alto**. Esto apunta a factores sistémicos (currículo, cultura del esfuerzo, formación del profesorado, tiempo de aprendizaje, expectativas, etc.) que operan de forma transversal a los estratos sociales.

### 6.3. Implicaciones para la reflexión educativa

1. **El ESCS importa, pero no lo explica todo.** En España y Aragón el gradiente es claro (~25 puntos por unidad de ESCS). En B-S-J-Z también existe, pero la “línea base” es mucho más alta.
2. **Las diferencias entre sistemas educativos pueden ser mayores que las diferencias dentro de un mismo sistema.** El gap QCI–España supera ampliamente el gap entre el alumnado más y menos favorecido dentro de España.
3. **Aragón** ofrece un caso interesante de rendimiento superior al promedio nacional que no se reduce a composición socioeconómica. Merece análisis adicionales (organización escolar, prácticas docentes, políticas autonómicas, etc.).
4. Cualquier comparación internacional de rendimiento debe acompañarse de un control por ESCS (o variables equivalentes) para no confundir efectos de sistema con efectos de composición social.

---

## 7. Limitaciones y próximos pasos

**Limitaciones de esta versión:**
- No se han calculado errores estándar con los 80 pesos de replicación (`W_FSTURWT1`–`80`). Las diferencias son de gran magnitud y muy probablemente significativas, pero la inferencia formal queda pendiente.
- El mapeo de algunas comunidades autónomas a partir de `STRATUM` (especialmente códigos `90xx`) es aproximado; Aragón está identificado de forma inequívoca.
- Solo se ha analizado matemáticas. Lectura y ciencias quedan fuera del alcance actual.
- No se han incluido variables de proceso (clima de aula, tiempo de estudio, motivación, etc.).

**Posibles ampliaciones:**
- Errores estándar correctos (replicate weights).
- Inclusión de Singapur, Macao, Hong Kong, Japón, Corea, País Vasco y Castilla y León.
- Análisis por sexo y por repetición de curso.
- Exploración de variables de proceso y de contexto escolar.
- Comparación con PISA 2022 / 2025 cuando los microdatos de B-S-J-Z vuelvan a estar disponibles.

---

## 8. Scripts y reproducibilidad

Los scripts utilizados se encuentran en la subcarpeta `scripts/`:

| Script                         | Función                                      |
|--------------------------------|----------------------------------------------|
| `extract_pisa_analytic.py`     | Extracción inicial de columnas y filtrado    |
| `pisa_fix_regions_v2.py`      | Mapeo de STRATUM → región y tipo de centro   |
| `pisa_means_math.py`           | Medias ponderadas globales                   |
| `pisa_means_by_type.py`        | Desglose por tipo de centro                  |
| `pisa_escs_quintiles.py`       | Medias por quintiles de ESCS                 |
| `pisa_regression_escs.py`      | Regresiones lineales ponderadas              |

**Dependencias:** `pyreadstat`, `pandas`, `pyarrow`, `numpy`, `scikit-learn`.

**Nota sobre los datos:** los microdatos de PISA son de acceso público a través de la OCDE. Este análisis no redistribuye los ficheros `.sav` originales.

---

## Referencias

- OECD (2019). *PISA 2018 Results (Volume I): What Students Know and Can Do*. OECD Publishing.
- OECD (2019). *PISA 2018 Results (Volume II): Where All Students Can Succeed*. OECD Publishing.
- OECD (2020). *PISA 2018 Technical Report*.
- INEE (2019). *PISA 2018. Informe español*. Ministerio de Educación y Formación Profesional.

---

*Documento generado a partir del análisis de microdatos realizado en octubre 2026. Compatible con el repositorio del Máster en Profesorado de Educación Secundaria (especialidad Matemáticas).*
