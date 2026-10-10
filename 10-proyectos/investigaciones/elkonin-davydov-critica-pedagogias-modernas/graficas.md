# Gráficas y visualizaciones de la investigación
**Ciclo 2 — 2026-10-10**

Dado que esta investigación es textual y acumulativa, las visualizaciones se presentan como:
1. Descripciones precisas de gráficos conceptuales que resumen los hallazgos.
2. Enlaces a gráficos oficiales o de estudios publicados cuando existen.
3. Estructura de datos que permitiría generar gráficos propios.

## 1. Tendencia PISA OCDE (lectura y matemáticas, 2015–2025)
**Tipo:** Líneas de tendencia con puntos de ciclo.

- Lectura OCDE: descenso aproximado de **28 puntos** (2015 → 2025).
- Matemáticas OCDE: descenso aproximado de **22 puntos**.
- Ciencia: descenso más moderado (~7 puntos).
- Equivalencia orientativa: ~20 puntos ≈ 1 año de aprendizaje.

**Fuente oficial:**  
- https://oecdedutoday.com/the-state-of-global-education-according-to-pisa/  
- Informes PISA 2025 Volume I (OCDE).

**Interpretación visual clave:** La caída es más pronunciada en procesos de alto nivel cognitivo (evaluar/reflexionar) que en localizar información.

## 2. Efecto de la guía en la indagación (meta-análisis)
**Tipo:** Barras de tamaño de efecto (g de Hedges o d de Cohen).

- Descubrimiento **no asistido / minimal guidance**: efecto nulo o negativo respecto a instrucción explícita (Alfieri et al.; Kirschner-Sweller-Clark).
- Indagación **guiada**: efecto positivo medio-grande (Lazonder & Harmsen 2016: +~0,5 DE por añadir guía; meta-análisis posteriores g ≈ 0,7–1,2 según condiciones).

**Mensaje visual:** La variable crítica no es «indagación sí/no», sino **cantidad y calidad de la guía** + conocimiento previo del alumno.

## 3. Esquema del efecto expertise-reversal
**Tipo:** Dos curvas cruzadas (eje X = conocimiento previo; eje Y = eficacia de la instrucción).

- Curva A (instrucción altamente guiada / ejemplos resueltos): alta eficacia en novatos → desciende o se estabiliza con expertise.
- Curva B (indagación / problem-solving abierto): baja eficacia en novatos → asciende con expertise.

**Punto de cruce:** momento en que conviene reducir la guía externa porque el alumno ya posee esquemas internos.

## 4. Comparación conceptual Elkonin-Davydov vs empirismo clásico
**Tipo:** Dos flechas o diagramas de flujo.

- Empirismo / muchas pedagogías modernas simplificadas:  
  Concreto particular → generalización inductiva → abstracción (riesgo: pensamiento empírico + traductor perpetuo).

- Elkonin-Davydov:  
  Abstracción germinal (relación esencial) → modelado → concreción en múltiples manifestaciones (objetivo: pensamiento teórico).

**Nota:** El movimiento real de Davydov es dialéctico (ida y vuelta), no una flecha rígida única.

## 5. Hallazgos de implementaciones Elkonin-Davydov (resumen cualitativo)
**Tipo:** Tabla o radar conceptual.

| Dimensión                  | Resultado típico                          | Calidad de evidencia      |
|---------------------------|-------------------------------------------|---------------------------|
| Pensamiento teórico       | Ventaja clara                             | Media (estudios rusos + cualitativos EE.UU.) |
| Problemas no estándar     | Ventaja                                   | Media                     |
| Logros currículo estándar | Sin diferencia clara                      | Media                     |
| Independencia de readiness| Progreso no depende del nivel inicial     | Sidneva 2020 (N pequeña)  |
| Generalizabilidad         | Limitada fuera de Rusia                   | Baja-media                |

## Recomendación de uso
Estas visualizaciones pueden reproducirse fácilmente en herramientas como Excel, R, Python (matplotlib/seaborn) o Canva a partir de los datos numéricos citados en `bibliografia.md` y `estado.md`. Los enlaces a informes OCDE permiten acceder a las gráficas oficiales más actualizadas.
