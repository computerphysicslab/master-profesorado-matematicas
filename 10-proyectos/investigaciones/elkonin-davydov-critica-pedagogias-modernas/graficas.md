# Gráficas de la investigación (visual)

**Actualizado 2026-10-10**

Los 5 gráficos generados con matplotlib se mostraron directamente en la conversación de investigación (imágenes renderizadas).  
Aquí se documentan y se enlazan las versiones oficiales publicadas que sí funcionan de forma permanente.

---

## 1. Tendencia PISA OCDE (Lectura, Matemáticas, Ciencias) 2015–2025

**Gráfico oficial (Statista — funciona):**  
https://www.statista.com/chart/36590/long-term-trend-in-pisa-scores/

**Resumen de los datos usados en el gráfico propio:**  
- Lectura: descenso ~28 puntos  
- Matemáticas: descenso ~22 puntos  
- Ciencias: descenso más moderado (~7 puntos)  
- ~20 puntos ≈ 1 año de aprendizaje

---

## 2. Tamaño de efecto: guía vs descubrimiento mínimo

Gráfico de barras generado (valores representativos de meta-análisis):  
- Descubrimiento mínimamente guiado: ~ −0.3  
- Indagación guiada (+guía): ~ +0.5  
- IBL guiada (meta recientes): ~ +0.9

Fuentes: Alfieri et al., Lazonder & Harmsen (2016), meta-análisis 2022–2025.

---

## 3. Efecto expertise-reversal (esquema conceptual)

Curvas cruzadas:  
- Instrucción altamente guiada → alta eficacia en novatos, desciende con expertise.  
- Indagación abierta → baja en novatos, asciende con expertise.  
Punto de cruce = momento óptimo para reducir la guía externa.

---

## 4. Dos caminos pedagógicos contrastados

- **Rojo (empirista / muchas pedagogías modernas simplificadas):** Concreto particular → generalización inductiva → abstracción (riesgo de pensamiento empírico).  
- **Verde (Elkonin-Davydov):** Abstracto germinal (relación esencial) → modelado + mediación → concreción múltiple (pensamiento teórico).

---

## 5. Resumen cualitativo de hallazgos Elkonin-Davydov

| Dimensión                  | Fuerza relativa |
|---------------------------|-----------------|
| Pensamiento teórico       | Alta (~85 %)    |
| Problemas no estándar     | Alta (~75 %)    |
| Independencia de readiness| Alta (~80 %)    |
| Logros currículo estándar | Media (~45 %)   |

---

## Enlaces oficiales permanentes

| Recurso | Enlace |
|---------|--------|
| Statista – Tendencia PISA a largo plazo | https://www.statista.com/chart/36590/long-term-trend-in-pisa-scores/ |
| OCDE PISA 2025 Results (Volume I) | https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report.html |
| Visualizaciones interactivas por país | https://www.leonpalafox.com/pisa_results/ |
| OCDE Education Today | https://oecdedutoday.com/the-state-of-global-education-according-to-pisa/ |

Los gráficos propios se generaron con Python/matplotlib y se visualizaron en la conversación de investigación.  
Para uso offline se pueden regenerar a partir de los datos de `bibliografia.md` y `estado.md`.
