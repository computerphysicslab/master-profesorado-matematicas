---
layout: default
title: "SA: Matemáticas sobre 64 casillas (ajedrez, grafos y optimización)"
nav_order: 10
parent: Situaciones de aprendizaje
---

# SA — Matemáticas sobre 64 casillas: optimización, grafos y ajedrez

> Situación de aprendizaje completa. El banco de problemas clásicos del ajedrez se resume en el anexo; el núcleo es el diseño implementable en aula.

## 0. Metadatos

| Campo | Contenido |
|-------|-----------|
| **Título de la SA** | Matemáticas sobre 64 casillas: optimización y grafos |
| **Nivel / curso** | 4.º ESO (opción académica) / 1.º Bachillerato (Matemáticas I) |
| **Duración** | 7 sesiones × 50–55 min |
| **Autor/a de la ficha** | Equipo del repositorio (adaptación del recurso de ajedrez) |
| **Fecha / versión** | 2026-09-30 · v1.0 |
| **Contexto de uso** | Diseño curricular / Practicum / germen de TFM (grafos, DGBL) |

**Palabras clave:** ajedrez, grafos, recorrido del caballo, vectores, combinatoria, backtracking, CE8, gamificación ligera

---

## 1. Pregunta guía / reto

> ¿Cómo describiría un ordenador la ruta más corta de un caballo entre dos casillas cualesquiera del tablero, y qué matemáticas hacen falta para entenderlo?

**Producto final esperado:**  
Informe-portfolio de equipo (4–5 páginas o equivalente digital) que incluya: (1) modelo vectorial del movimiento del caballo; (2) grafo de casillas alcanzables desde una posición dada; (3) algoritmo o pseudocódigo de búsqueda de camino mínimo; (4) reflexión socioafectiva sobre ensayo-error y cooperación.

---

## 2. Justificación y sentido educativo

El tablero de ajedrez es un **sistema formal finito** con reglas explícitas: permite trabajar representación espacial, grafos, combinatoria y pensamiento algorítmico sin salir de un entorno conocido y motivador.

La práctica guiada del ajedrez se asocia en la literatura a funciones ejecutivas (planificación, inhibición, memoria de trabajo) y a la transferencia hacia la descomposición de problemas. En LOMLOE, conecta de forma natural con resolución de problemas, modelización y sentido socioafectivo (gestión del error, tolerancia a la frustración).

---

## 3. Objetivos de aprendizaje

1. Representar el movimiento de piezas (en especial el caballo) mediante **vectores** en $\mathbb{Z}^2$.
2. Modelizar el tablero como un **grafo** y calcular grados / vecindarios de un vértice.
3. Aplicar una estrategia de **búsqueda** (BFS o exploración sistemática) para caminos mínimos del caballo entre dos casillas.
4. Analizar un problema clásico de combinatoria o restricción (8 reinas o trigo en el tablero) con lenguaje matemático preciso.
5. Argumentar decisiones y **gestionar el error** en equipo (variantes, contrajuego, revisión de hipótesis).

---

## 4. Competencias específicas y criterios de evaluación

| CE (RD 217/2022 / 243/2022) | Criterios (enfoque) | Evidencia en esta SA |
|-----------------------------|---------------------|----------------------|
| **CE1–CE2** Resolución de problemas | Descomponer el reto, planificar, comprobar | Diario de intentos; camino mínimo documentado |
| **CE3** Razonamiento y argumentación | Justificar por qué un movimiento es legal / óptimo | Explicaciones orales y escritas en el portfolio |
| **CE5–CE6** Conexiones y modelización | Tablero → vectores → grafo → algoritmo | Modelo vectorial + diagrama de grafo |
| **CE8** Socioafectivas | Perseverancia, cooperación, gestión del error | Rúbrica de proceso + autoevaluación |

**Competencias clave:** STEM, CD (si se usa software), CPSAA, CCL.

---

## 5. Saberes básicos y sentidos matemáticos

| Sentido | Saberes / contenidos | Prioridad |
|---------|----------------------|-----------|
| Espacial | Coordenadas $a1$–$h8$; vectores $(\pm 1,\pm 2)$; distancia de Chebyshev $d_\infty$ | Alta |
| Algebraico | Sucesiones geométricas (trigo); notación y generalización | Media |
| Estocástico / algorítmico | Árboles de decisión; grafos; búsqueda de caminos | Alta |
| Numérico | Órdenes de magnitud (Shannon $\sim 10^{120}$) | Baja |
| Socioafectivo | Error como información; trabajo en equipo; autoconcepto | Alta |

**Conexiones:** Tecnología (pseudocódigo / GeoGebra / Python opcional), Historia (origen del problema del trigo).

---

## 6. Secuencia de aprendizaje

| Sesión | Fase | Actividad del alumnado | Rol docente | Agrupamiento |
|--------|------|------------------------|-------------|--------------|
| 1 | Activación | Explorar notación algebraica y movimientos del caballo en tablero físico o app; formular conjeturas sobre «¿cuántos saltos mínimos de e4 a a8?» | Presentar el reto; recoger conjeturas | Parejas |
| 2 | Exploración espacial | Traducir movimientos a vectores; calcular $d_\infty$ del rey vs caballo; mapa de casillas alcanzables en 1, 2, 3 saltos | Guiar formalización vectorial | Parejas → cuarteto |
| 3 | Modelo de grafo | Construir grafo (vértices = casillas de interés; aristas = salto legal); grado de vértices centrales vs bordes | Introducir vocabulario de grafos | Equipos de 3–4 |
| 4 | Algoritmo | Diseñar búsqueda sistemática de camino mínimo (cola BFS en papel o simulación); contrastar con fuerza bruta | Andamiaje de pseudocódigo; sin exigir lenguaje formal de programación | Equipos |
| 5 | Problema clásico | Elegir: (A) 8 reinas a escala reducida $n=4$ o $n=5$; o (B) suma del trigo $\sum_{k=0}^{63} 2^k$ y órdenes de magnitud | Diferenciar por nivel; aportar pistas | Individual + puesta en común |
| 6 | Producto | Redactar portfolio: modelo, grafo, camino, reflexión CE8 | Rúbrica visible; tutorías de equipo | Equipos |
| 7 | Comunicación | Exposición breve (5 min) + coevaluación + cierre metacognitivo | Moderación; síntesis de aprendizajes | Grupo clase |

**Hito intermedio (sesión 4):** diagrama de grafo + un camino mínimo correcto entre dos casillas fijadas por el docente.

---

## 7. Metodología y organización

- **Enfoque:** indagación + modelización + ligera gamificación (retos cronometrados opcionales).
- **Agrupamientos:** parejas (sesiones 1–2), equipos de 3–4 heterogéneos (3–6), individual en el problema clásico.
- **Espacios:** aula con tableros o apps (Lichess board editor, Chess.com tools); opcional aula de informática.
- **Materiales:** tableros/piezas o plantillas impresas 8×8; papel milimetrado; GeoGebra (rejilla) o Python opcional; rúbrica impresa.

---

## 8. Evaluación

### 8.1. Formativa
Lista de cotejo por sesión (modelo vectorial, grafo, camino); preguntas clave («¿por qué no basta la distancia euclídea?»); feedback oral en hito intermedio.

### 8.2. Sumativa del producto
Portfolio de equipo evaluado con rúbrica (modelo 30 %, algoritmo/camino 30 %, comunicación 20 %, socioafectivo/proceso 20 %).

### 8.3. Autoevaluación y coevaluación
Ficha individual de 5 ítems (contribución, gestión del error, claridad del modelo) + coevaluación entre equipos en la exposición.

---

## 9. Atención a la diversidad y DUA

| Principio DUA | Medida concreta |
|---------------|-----------------|
| Implicación | Retos de dificultad escalonada (casillas cercanas → lejanas; $n=4$ reinas antes que $n=8$) |
| Representación | Tablero físico, diagrama en papel, GeoGebra; glosario visual de vectores |
| Acción y expresión | Portfolio escrito, oral o vídeo corto; pseudocódigo o descripción en lenguaje natural |

**Refuerzo:** plantillas de grafo parcialmente rellenadas. **Ampliación:** ciclo cerrado del caballo (Knight’s tour) o implementación en Python.

---

## 10. Dimensión socioafectiva

- **Perseverancia y gestión del error:** los caminos incorrectos se registran como datos, no como fracaso.
- **Cooperación:** roles rotativos (modelizador, verificador, portavoz).
- **Autoconcepto:** cierre con «una estrategia que me funcionó / una que cambiaría».
- Registro: ítems en rúbrica de proceso + autoevaluación sesión 7.

---

## 11. Orientaciones para la implementación

- **Dificultades:** confundir distancia euclídea con saltos de caballo; grafos demasiado densos → limitar a un subconjunto de 9–16 casillas al inicio.
- **Variante corta (4 sesiones):** solo vectores + caminos mínimos, sin 8 reinas ni trigo.
- **Variante Bachillerato:** formalizar BFS; conectar con matrices de adyacencia.
- **Extensión TFM:** comparar resolución con/sin app; medir ansiedad o motivación pre-post.

---

## 12. Referencias

### Normativa
- [RD 217/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-4975), [RD 243/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-5521)

### Didáctica y recursos
1. Problemas clásicos: [Eight queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle), [Knight’s tour](https://en.wikipedia.org/wiki/Knight%27s_tour), [Shannon number](https://en.wikipedia.org/wiki/Shannon_number)
2. Literatura sobre ajedrez y cognición (Sala, Gobet y revisiones recientes) para marco teórico de TFM
3. Materiales del repo: [plantilla SA](plantilla-situacion-aprendizaje.md), rúbricas en `../rubricas/`

---

## 13. Anexo — Banco breve de problemas clásicos

**Vectores del caballo:** $(\pm 1,\pm 2)$, $(\pm 2,\pm 1)$.

**Distancia de Chebyshev (rey):**  
$d_{\infty}(A,B)=\max(|x_2-x_1|,|y_2-y_1|)$

**Trigo en el tablero:**  
$\sum_{k=0}^{63} 2^k = 2^{64}-1 = 18\,446\,744\,073\,709\,551\,615$

**8 reinas:** 92 soluciones en $8\times 8$ (12 fundamentales por simetría); empezar por $n=4$.
