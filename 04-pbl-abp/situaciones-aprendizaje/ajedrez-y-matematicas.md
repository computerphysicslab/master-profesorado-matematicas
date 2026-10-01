---
layout: default
title: Matemáticas sobre 64 casillas (ajedrez y grafos)
parent: Situaciones de aprendizaje
nav_order: 10
---

# Matemáticas sobre 64 casillas: optimización y grafos

**Nivel:** 4.º ESO (opción académica) / 1.º Bachillerato (Matemáticas I)  
**Duración orientativa:** 7 sesiones  
**Sentidos:** espacial, algorítmico, algebraico, socioafectivo  
**Palabras clave:** ajedrez, grafos, recorrido del caballo, vectores, combinatoria, backtracking, CE9–CE10, gamificación ligera

## Pregunta guía / reto

¿Cómo programaría un ordenador (o cómo razonaría un equipo) para encontrar una **ruta mínima del caballo** entre dos casillas cualesquiera del tablero?

## Competencias específicas (síntesis RD 217/2022)

| Competencia | Enfoque en esta SA | Evidencia |
|-------------|--------------------|----------|
| **CE1–CE2** Resolución de problemas | Descomponer el reto, planificar, comprobar | Diario de intentos; camino mínimo documentado |
| **CE3** Razonamiento y argumentación | Justificar movimientos legales / óptimos | Explicaciones orales y escritas |
| **CE4** Pensamiento computacional | Grafo del caballo, búsqueda, restricciones | Algoritmo o pseudocódigo |
| **CE5–CE6** Conexiones y modelización | Tablero → vectores → grafo → algoritmo | Modelo vectorial + diagrama |
| **CE7–CE8** Representar y comunicar | Notación algebraica, diagramas, portfolio | Producto final |
| **CE9–CE10** Socioafectivas | Perseverancia, cooperación, gestión del error | Rúbrica de proceso + autoevaluación |

## Saberes y métricas en el tablero

| Sentido | Contenidos | Intensidad |
|---------|------------|------------|
| Espacial | Coordenadas $a1$–$h8$ en $\mathbb{Z}^2$; vectores del caballo $(\pm 1,\pm 2)$ y $(\pm 2,\pm 1)$; **distancia de Chebyshev** $d_\infty$ (rey) | Alta |
| Algebraico | Combinatoria; crecimiento exponencial (trigo en el tablero) | Media |
| Algorítmico | Grafos, grado, *backtracking*, recorrido del caballo | Alta |
| Socioafectivo | Error productivo, trabajo en equipo | Media |

**Métricas (no confundir):** Manhattan $d_1$; Chebyshev $d_\infty$ (rey); caballo = distancia en el grafo de movimientos legales.

## Secuencia orientativa (7 sesiones)

| # | Foco | Actividad | Evaluación formativa |
|---|------|-----------|----------------------|
| 1 | Coordenadas y vectores | Casillas ↔ $\mathbb{Z}^2$; vectores del caballo | Mini-check de notación |
| 2 | Rey vs caballo | Comparar $d_\infty$ y distancia del caballo | Debate guiado |
| 3 | Grafo del tablero | Subgrafo; grados de vértices | Diagrama en portfolio |
| 4 | Búsqueda | Camino mínimo (BFS informal) | Diario de intentos |
| 5 | Clásicos | 8 reinas o recorrido del caballo (versión reducida) | Criterios de éxito |
| 6 | Producto | Portfolio completo | Rúbrica visible |
| 7 | Puesta en común | Presentaciones; transferencia a otro grafo | Coevaluación |

## DUA y socioafectivo

Varias vías de representación; productos alternativos; error como dato sin penalizar la exploración.

## Producto final

Portfolio: (1) modelo vectorial, (2) grafo, (3) camino mínimo documentado, (4) reflexión CE9–CE10.

## Referencias

- [RD 217/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-4975) · [RD 243/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-5521)
- [plantilla-situacion-aprendizaje.md](plantilla-situacion-aprendizaje.md)
