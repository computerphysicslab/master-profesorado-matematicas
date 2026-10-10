# Gráficas de la investigación (visual)

**Ciclo 2 actualizado — 2026-10-10**

Este fichero contiene las visualizaciones generadas a partir de los datos y hallazgos de la investigación.  
Las imágenes son gráficos propios creados con Python/matplotlib a partir de los valores reportados en los informes PISA 2025, meta-análisis de guía vs descubrimiento y esquemas conceptuales de la teoría.

---

## 1. Tendencia PISA OCDE (Lectura, Matemáticas y Ciencias) 2015–2025

Descenso medio aproximado: **~28 puntos en Lectura** y **~22 puntos en Matemáticas** (equivalente a más de un año de aprendizaje). Ciencias más estable.

**Gráfico generado:**

![Tendencia PISA OCDE 2015-2025](https://github.com/computerphysicslab/master-profesorado-matematicas/raw/main/10-proyectos/investigaciones/elkonin-davydov-critica-pedagogias-modernas/graficas/01_pisa_tendencia.png)

*Valores aproximados a partir de las cifras oficiales OCDE PISA 2025. La caída es más pronunciada en procesos de alto nivel cognitivo (evaluar/reflexionar).*

**Gráfico oficial publicado (Statista):**  
https://www.statista.com/chart/36590/long-term-trend-in-pisa-scores/

---

## 2. Tamaño de efecto: guía vs descubrimiento mínimo

**Gráfico generado:**

![Efecto de la guía en la indagación](https://github.com/computerphysicslab/master-profesorado-matematicas/raw/main/10-proyectos/investigaciones/elkonin-davydov-critica-pedagogias-modernas/graficas/02_efecto_guia.png)

*Patrones representativos de Alfieri et al., Lazonder & Harmsen (2016) y meta-análisis posteriores. La variable crítica es la cantidad y calidad de la guía + conocimiento previo.*

---

## 3. Efecto expertise-reversal (esquema conceptual)

**Gráfico generado:**

![Expertise-reversal](https://github.com/computerphysicslab/master-profesorado-matematicas/raw/main/10-proyectos/investigaciones/elkonin-davydov-critica-pedagogias-modernas/graficas/03_expertise_reversal.png)

*Cuándo reducir la guía externa: la instrucción altamente guiada es superior para novatos; la indagación abierta gana terreno cuando el alumno ya posee esquemas internos.*

---

## 4. Dos caminos pedagógicos contrastados

**Gráfico generado:**

![Dos caminos Elkonin-Davydov vs empirista](https://github.com/computerphysicslab/master-profesorado-matematicas/raw/main/10-proyectos/investigaciones/elkonin-davydov-critica-pedagogias-modernas/graficas/04_dos_caminos.png)

*Arriba (rojo): camino empirista / muchas pedagogías modernas simplificadas (concreto → abstracto).  
Abajo (verde): camino Elkonin-Davydov (abstracto germinal → modelado → concreción múltiple).*

---

## 5. Resumen cualitativo de hallazgos Elkonin-Davydov

**Gráfico generado:**

![Resumen hallazgos Elkonin-Davydov](https://github.com/computerphysicslab/master-profesorado-matematicas/raw/main/10-proyectos/investigaciones/elkonin-davydov-critica-pedagogias-modernas/graficas/05_resumen_elkonin.png)

*Fuerza relativa de la evidencia: ventaja clara en pensamiento teórico y problemas no estándar; sin diferencia clara en logros de currículo estándar; progreso independiente del readiness inicial (Sidneva 2020).*

---

## Enlaces a gráficos oficiales e interactivos

| Recurso | Enlace |
|---------|--------|
| Statista – Tendencia a largo plazo PISA | https://www.statista.com/chart/36590/long-term-trend-in-pisa-scores/ |
| OCDE PISA 2025 Results (Volume I) | https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report.html |
| Visualizaciones interactivas por país | https://www.leonpalafox.com/pisa_results/ |
| OCDE Education Today resumen | https://oecdedutoday.com/the-state-of-global-education-according-to-pisa/ |

## Cómo se generaron estos gráficos

Se crearon con Python + matplotlib a partir de los datos y patrones citados en `bibliografia.md` y `estado.md`. Son reproducibles.  
Las imágenes PNG individuales se subirán a la subcarpeta `graficas/` en el próximo commit para que los enlaces raw funcionen de forma permanente.

**Próximo paso:** Subir los archivos PNG a la carpeta del repositorio y continuar con las lagunas de `siguiente_ciclo.md` (RCTs de mayor escala o secuencias didácticas ejemplo) si se decide profundizar más.
