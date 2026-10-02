---
layout: default
title: "SA: La campana que esconde un círculo"
parent: Situaciones de aprendizaje
nav_order: 30
---

# SA — La campana que esconde un círculo (integral gaussiana)

## 0. Metadatos

| Campo | Contenido |
|-------|-----------|
| **Título de la SA** | La campana que esconde un círculo |
| **Nivel / curso** | 2.º Bachillerato (Matemáticas); adaptable a 1.º Bach. sin demostración completa |
| **Duración** | 6 sesiones × 50–55 min |
| **Autor/a de la ficha** | Material del repositorio |
| **Fecha / versión** | 2026-10 · v1.0 |
| **Contexto de uso** | Diseño curricular · Practicum · ampliación de análisis · germen de TFM |

**Palabras clave:** integral gaussiana, $e^{-x^2}$, coordenadas polares, cambio de representación, modelización, GeoGebra, Python, π

---

## 1. Pregunta guía / reto

> *¿Cómo puede una curva en forma de campana, que parece no tener nada que ver con un círculo, acabar dando como área exacta $\sqrt{\pi}$?*

**Producto final esperado:** informe o póster de equipo con (1) gráfica y propiedades de $e^{-x^2}$, (2) explicación de por qué no basta la primitiva elemental, (3) esquema de la estrategia «cuadrar → plano → polares», (4) comparación numérica con $\sqrt{\pi}$ y (5) reflexión sobre el cambio de representación.

---

## 2. Justificación y sentido educativo

- Convierte un resultado «universitario» en una **historia de estrategia matemática** accesible en Bachillerato.
- Trabaja la idea transversal: cuando una representación no funciona, otra puede hacer visible la estructura oculta.
- Conecta análisis (área, integral), geometría (polares, círculo) y pensamiento computacional (aproximación numérica).
- Puente natural hacia la distribución normal y aplicaciones en física/estadística.

**Germen narrativo:** [La campana que esconde un círculo](../../03-materiales/historias-matematicas/fichas/la-campana-que-esconde-un-circulo.md).

---

## 3. Objetivos de aprendizaje

1. Interpretar gráficamente $y=e^{-x^2}$ (simetría, máximo, comportamiento en el infinito).
2. Explicar por qué la ausencia de primitiva elemental no impide calcular el área exacta.
3. Describir la estrategia de elevar la integral al cuadrado e interpretar el producto sobre el plano.
4. Justificar el paso a coordenadas polares y el factor $r$ en el elemento de área.
5. Comparar una aproximación numérica con $\sqrt{\pi}$ y valorar la razonabilidad del resultado.
6. (Ampliación) Completar el cálculo formal hasta $I=\sqrt{\pi}$ y conectar con la campana de Gauss.

---

## 4. Competencias específicas y criterios de evaluación

| CE (síntesis Bachillerato) | Criterios prioritarios | Evidencia en esta SA |
|----------------------------|------------------------|----------------------|
| **CE1–CE2** Modelizar / resolver | Cambiar de representación; validar | Esquema cuadrar→polares + comparación numérica |
| **CE3** Razonar y argumentar | Justificar pasos del método | Informe: por qué polares |
| **CE5–CE6** Conexiones | Análisis ↔ geometría; mates ↔ estadística/física | Apartado de conexiones del producto |
| **CE7–CE8** Representar / comunicar | Gráficas, notación, claridad | Póster o informe |
| **CE9–CE10** Socioafectivas | Perseverancia ante el «imposible»; gestión del error numérico | Rúbrica de proceso |

**Competencias clave:** STEM, CCL, CD, CPSAA.

---

## 5. Saberes básicos y sentidos matemáticos

| Sentido | Saberes / contenidos | Prioridad |
|---------|----------------------|----------|
| Algebraico | Función exponencial; cambio de variable; notación integral | Alta |
| De la medida | Área bajo la curva; integral definida e impropia (idea) | Alta |
| Espacial | Coordenadas polares; distancia al origen; elemento de área | Alta |
| Numérico | Aproximación; órdenes de magnitud; $\sqrt{\pi}$ | Media |
| Estocástico | Distribución normal (ampliación) | Baja–media |
| Socioafectivo | Tolerancia a la incertidumbre; valoración de estrategias | Media |

**Conexiones interdisciplinares:** Física (difusión, óptica), Estadística (campana de Gauss), Computación (integración numérica).

---

## 6. Secuencia de aprendizaje

| Sesión | Fase | Actividad del alumnado | Rol docente | Agrupamiento |
|--------|------|------------------------|-------------|--------------|
| 1 | Activación | Representar $e^{-x^2}$; propiedades; pregunta del área total; hipótesis | Provocar sin dar la solución | Individual → equipos |
| 2 | Bloqueo productivo | Intentar primitiva; discutir por qué «no sale»; proponer alternativas (numérico, cambio de problema) | Legitimar el bloqueo; listar estrategias | Equipos + clase |
| 3 | Cambio de representación | Idea $I^2$; interpretación sobre el plano; aparición de $r^2$ | Guiar con preguntas; visual GeoGebra 3D o curvas de nivel | Equipos |
| 4 | Polares y cálculo | Introducir polares; factor $r$; (nivel alto) cambio $u=r^2$ hasta $I=\sqrt{\pi}$ | Andamiaje diferenciado: idea vs demostración completa | Equipos |
| 5 | Numérico y producto | Aproximar $\int_{-a}^{a}e^{-x^2}\,dx$ (GeoGebra/Python); comparar con $\sqrt{\pi}$; redactar producto | Tutoría de escritura y código | Equipos |
| 6 | Comunicación | Mini-congreso: estrategia, resultado, limitaciones; debate «¿qué aprendimos del cambio de representación?» | Moderar; cerrar con conexiones (normal, física) | Grupo-clase |

**Hito intermedio (sesión 3–4):** esquema visual «campana → plano → círculo» documentado por equipo.

---

## 7. Metodología y organización

- **Enfoque:** indagación + modelización + cambio de representación.
- **Agrupamientos:** equipos de 3–4 (roles: gráfica, estrategia, cálculo/numérico, portavoz).
- **Espacios:** aula; aula de informática recomendable en sesiones 5–6.
- **Materiales:** GeoGebra (2D/3D), Python o calculadora, plantilla de informe, (opcional) vídeo breve desencadenante pausado.

---

## 8. Evaluación

### 8.1. Formativa
Preguntas clave en sesiones 2–4; revisión del esquema antes del cálculo formal; feedback entre equipos.

### 8.2. Sumativa
| Criterio | Indicadores (peso orientativo) |
|----------|--------------------------------|
| Comprensión gráfica y del problema | Propiedades de la campana; por qué no basta la primitiva (20 %) |
| Estrategia | Explican cuadrar → plano → polares con claridad (30 %) |
| Cálculo o idea formal | Completan pasos acordes al nivel (20 %) |
| Numérico | Comparan aproximación con $\sqrt{\pi}$ (15 %) |
| Comunicación y proceso | Informe/póster + cooperación (15 %) |

### 8.3. Autoevaluación y coevaluación
Checklist: «entendí el bloqueo / aporté una estrategia / distinguí aproximación de exacto». Coevaluación de un esquema ajeno (una fortaleza + una mejora).

---

## 9. Atención a la diversidad y DUA

| Principio DUA | Medida concreta |
|---------------|-----------------|
| Implicación | Reto «imposible»; roles; meta realista (entender la estrategia, no memorizar la demostración) |
| Representación | Gráfica 2D, superficie 3D, esquema de flujo, notación simbólica |
| Acción y expresión | Informe, póster, notebook Python o exposición oral |

**Refuerzo (1.º Bach. / apoyo):** centrarse en idea + numérico, sin integral doble formal. **Ampliación:** $e^{-x^2/2}$, normal estándar, fracción de área en $[-1,1]$, $[-2,2]$.

---

## 10. Dimensión socioafectiva

- **Perseverancia:** el bloqueo de la primitiva es intencional; se valora cambiar de vía.
- **Flexibilidad cognitiva:** aceptar que «otra representación» es matemáticas de verdad.
- **Autoconcepto:** descubrir $\sqrt{\pi}$ como resultado de una estrategia, no de una fórmula mágica.
- Registro: rúbrica CE9–CE10 (esfuerzo ante el problema abierto; respeto a conjeturas).

---

## 11. Orientaciones para la implementación

- **No exigir** la demostración completa a todo el grupo en 1.º de Bachillerato.
- Distinguir siempre **aproximación numérica** vs **resultado exacto**.  
- Dificultad típica: creer que «sin primitiva no hay área»; confundir $I^2$ con un truco arbitrario.
- Variante corta (3–4 sesiones): historia + idea polares + numérico, sin detalle del cambio $u=r^2$.
- Variante larga: notebook Python + conexión formal con la densidad normal.

---

## 12. Referencias

### Normativa
- [RD 243/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-5521) (Bachillerato)

### Didáctica y recursos
1. Resultado clásico: $\int_{-\infty}^{+\infty}e^{-x^2}\,dx=\sqrt{\pi}$.
2. GeoGebra / Python para integración numérica.
3. Historia matemática: [La campana que esconde un círculo](../../03-materiales/historias-matematicas/fichas/la-campana-que-esconde-un-circulo.md).
4. SA hermanas: [Kepler](sa-kepler-ley-planetas-4eso.md) (modelización), [Eratóstenes](sa-eratostenes-3eso.md) (cambio de perspectiva geométrica).

---

## 13. Anexo — Guía rápida (docente)

$$I=\int_{-\infty}^{+\infty}e^{-x^2}\,dx,\quad I^2=\iint_{\mathbb{R}^2}e^{-(x^2+y^2)}\,dx\,dy=\int_0^{2\pi}\int_0^{\infty}e^{-r^2}r\,dr\,d\theta$$

$$\int_0^{\infty}re^{-r^2}\,dr=\tfrac12\ (u=r^2),\quad \int_0^{2\pi}d\theta=2\pi \implies I^2=\pi \implies I=\sqrt{\pi}$$

$\sqrt{\pi}\approx 1{,}77245385$. Comparar con $\int_{-a}^{a}e^{-x^2}\,dx$ para $a=1,2,3,\ldots$
