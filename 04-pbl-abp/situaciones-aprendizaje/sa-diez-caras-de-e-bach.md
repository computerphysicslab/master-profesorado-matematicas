---
layout: default
title: "SA: Las diez caras de e"
parent: Situaciones de aprendizaje
nav_order: 32
---

# SA — Las diez caras de *e* (del modelo abstracto a las aplicaciones)

## 0. Metadatos

| Campo | Contenido |
|-------|-----------|
| **Título de la SA** | Las diez caras de *e* |
| **Nivel / curso** | 1.º Bachillerato (Matemáticas I o CCSS I); ampliación 2.º Bach. Matemáticas II |
| **Duración** | 6 sesiones × 50–55 min (+ 1–2 opcionales en 2.º Bach.) |
| **Autor/a de la ficha** | Material del repositorio |
| **Fecha / versión** | 2026-10 · v1.0 |
| **Contexto de uso** | Diseño curricular · Practicum · germen de TFM (orden abstracto→concreto) |

**Palabras clave:** número *e*, límite, serie, función exponencial, logaritmo natural, interés compuesto continuo, decaimiento, transferencia, Elkonin-Davydov

![The 10 Faces of e — infografía de las representaciones de la constante e](media/10-faces-of-e.svg)

---

## 1. Pregunta guía / reto

> *Si **e** aparece en finanzas, en radiactividad y en la identidad \(e^{i\pi}+1=0\), ¿qué tienen en común esas situaciones más allá del símbolo?*

**Producto final esperado:** mapa conceptual o póster de equipo con (1) definición de *e* (límite y/o serie), (2) propiedad \(\frac{d}{dx}e^x=e^x\) y vínculo con \(\ln\), (3) dos aplicaciones resueltas (interés continuo y decaimiento), (4) transferencia a un contexto nuevo y (5) texto breve sobre qué se mantiene invariante entre «caras».

---

## 2. Justificación y sentido educativo

La constante *e* concentra varias representaciones (límite, serie, función igual a su derivada, inversa del logaritmo, ley de crecimiento/decaimiento) y contextos muy distintos. Una secuencia **concreto-primero** (empezar por el banco o por la radiactividad) puede dejar el modelo abstracto diluido.

Esta SA **invierte el orden** (ascenso de lo abstracto a lo concreto, tradición Elkonin-Davydov):

1. Modelo abstracto (límite / serie / propiedad diferencial).
2. Especialización en dos aplicaciones.
3. Síntesis: la misma estructura bajo distintas caras.

Así la contextualización es **medio** de comprensión y transferencia, no criterio único de selección de contenidos. Coherente con la [ficha TFM 21](../../01-asignaturas/trabajo-fin-de-master/ideas-interesantes/21-elkonin-davydov-abstracto-concreto.md).

**SA hermana:** [La campana que esconde un círculo](sa-campana-gaussiana-bach.md) (cara 9 / integral gaussiana).

---

## 3. Objetivos de aprendizaje

1. Definir *e* como \(\displaystyle e=\lim_{n\to\infty}\bigl(1+\frac{1}{n}\bigr)^n\) y/o como serie \(\displaystyle e=\sum_{n=0}^{\infty}\frac{1}{n!}\), y aproximar su valor.
2. Reconocer que \(f(x)=e^x\) es (salvo factor constante) la única función que coincide con su derivada; relacionarla con \(\ln\) como inversa.
3. Modelizar crecimiento o decaimiento continuo con \(A=Pe^{rt}\) o \(N(t)=N_0e^{-\lambda t}\), interpretando parámetros.
4. Transferir el modelo a un contexto nuevo no trabajado en clase.
5. Explicar qué se mantiene invariante al pasar de una cara de *e* a otra.

---

## 4. Competencias específicas y criterios de evaluación

| CE (síntesis Bachillerato) | Criterios prioritarios | Evidencia en esta SA |
|----------------------------|------------------------|----------------------|
| **CE1–CE2** Modelizar / resolver | Plantear modelos continuos; validar | Informes de interés y decaimiento + transferencia |
| **CE3** Razonar y argumentar | Justificar el paso del modelo a la aplicación | Texto de invariancia entre caras |
| **CE5–CE6** Conexiones | Análisis ↔ finanzas / física | Apartado de conexiones del producto |
| **CE7–CE8** Representar / comunicar | Gráficas, notación, claridad | Póster o mapa conceptual |
| **CE9–CE10** Socioafectivas | Perseverancia ante el modelo abstracto; cooperación | Rúbrica de proceso |

**Competencias clave:** STEM, CCL, CD, CPSAA.

---

## 5. Saberes básicos y sentidos matemáticos

| Sentido | Saberes / contenidos | Prioridad |
|---------|----------------------|----------|
| Algebraico | Límites de sucesiones; *e*; exponencial y logaritmo; \(y'=ky\) | Alta |
| De la medida | Crecimiento continuo; semivida; interpretación de tasas | Alta |
| Numérico | Aproximación de *e*; órdenes de magnitud | Media |
| Socioafectivo | Valoración de la estructura abstracta; tolerancia a la dificultad inicial | Media |

**Conexiones interdisciplinares:** Economía (interés), Física/Química (decaimiento, enfriamiento), Estadística (ampliación gaussiana).

---

## 6. Secuencia de aprendizaje

| Sesión | Fase | Actividad del alumnado | Rol docente | Agrupamiento |
|--------|------|------------------------|-------------|--------------|
| 1 | **Modelo** | Infografía; definición límite; tabla \((1+1/n)^n\) | Presentar estructura sin applications aún | Individual → equipos |
| 2 | **Modelo** | Serie \(\sum 1/n!\); propiedad \(d/dx\,e^x=e^x\) | Andamiaje serie/derivada | Equipos |
| 3 | **Estructura** | \(\ln\) como inversa; \(\int e^x\); ecuación \(y'=ky\) | Consolidar el modelo diferencial | Equipos + clase |
| 4 | **Especialización A** | Interés compuesto continuo \(A=Pe^{rt}\) | Guiar interpretación de parámetros | Equipos |
| 5 | **Especialización B** | Decaimiento \(N=N_0e^{-\lambda t}\) (o enfriamiento) | Contraste crecimiento/decaimiento | Equipos |
| 6 | **Transferencia + síntesis** | Contexto nuevo; póster; «qué se mantiene» | Tutoría de producto; cierre | Equipos → clase |
| 7–8 (opc.) | Ampliación 2.º Bach. | Serie de Taylor; Euler \(e^{ix}\); puente gaussiana | Diferenciar por nivel | Equipos |

**Hito intermedio (sesión 3):** el alumnado escribe en una frase la estructura \(y'=ky\) antes de las aplicaciones.

---

## 7. Metodología y organización

- **Enfoque:** modelo abstracto primero → especialización → transferencia (Davydov).
- **Agrupamientos:** equipos de 3–4 (roles: modelo, aplicación A, aplicación B, síntesis).
- **Materiales:** [infografía SVG](media/10-faces-of-e.svg), GeoGebra (deslizador *n*, gráficas \(e^x\), \(\ln x\)), calculadora/hoja de cálculo para sumas parciales.

---

## 8. Evaluación

### 8.1. Formativa
Feedback en sesiones 1–3 sobre límite/serie y notación; en 4–5 sobre interpretación de parámetros (no solo el número final).

### 8.2. Sumativa

| Criterio | Indicadores (peso orientativo) |
|----------|--------------------------------|
| Definición y aproximación de *e* | Límite y/o serie con sentido (15 %) |
| Propiedad diferencial y \(\ln\) | Aplica \(d/dx\,e^{kx}\); relaciona inversa (20 %) |
| Modelos de interés / decaimiento | Plantea, resuelve e interpreta (25 %) |
| Transferencia lejana | Reconoce la estructura en contexto nuevo (20 %) |
| Síntesis y comunicación | Invariancia entre caras; póster claro (20 %) |

### 8.3. Autoevaluación / coevaluación
Checklist: «puedo definir *e* sin mirar / señalo qué es común entre el banco y el decaimiento / resolví un contexto no ensayado».

---

## 9. Atención a la diversidad y DUA

| Principio DUA | Medida concreta |
|---------------|-----------------|
| Implicación | Infografía como mapa; roles; meta realista (modelo + una aplicación bien hecha) |
| Representación | Tabla de límite, serie, gráfica GeoGebra, fórmula, contexto verbal |
| Acción y expresión | Póster, informe, vídeo corto o defensa oral |

**Refuerzo:** plantilla de modelización (identificar \(P\)/\(N_0\), \(r\)/\(\lambda\), \(t\)). **Ampliación:** identidad de Euler; integral gaussiana (enlace a [SA campana](sa-campana-gaussiana-bach.md)).

---

## 10. Dimensión socioafectiva

- **Perseverancia:** el modelo abstracto (límite/serie) puede resultar seco al inicio; se valora llegar a ver las caras concretas *desde* él.
- **Sentido de competencia:** descubrir que el mismo \(y'=ky\) sirve para el banco y para la radiactividad.
- Registro: rúbrica CE9–CE10 (esfuerzo ante el modelo; cooperación en la síntesis).

---

## 11. Orientaciones para la implementación

- **No empezar** por el interés compuesto «y de paso sale *e*»; el orden es parte del diseño.
- La infografía se muestra en la sesión 1 como *mapa*, no como lista de aplicaciones a memorizar.
- Dificultad típica: confundir capitalización discreta y continua; olvidar el signo en el decaimiento.
- Variante corta (4 sesiones): límite + derivada + una sola aplicación + transferencia.
- Variante larga (2.º Bach.): añadir Euler y puente a la gaussiana.

---

## 12. Referencias

### Normativa
- [RD 243/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-5521) (Bachillerato)

### Didáctica y marco
1. Davydov / tradición Elkonin-Davydov — ascenso de lo abstracto a lo concreto.
2. [Idea TFM 21 — orden abstracto→concreto](../../01-asignaturas/trabajo-fin-de-master/ideas-interesantes/21-elkonin-davydov-abstracto-concreto.md).
3. Infografía: [media/10-faces-of-e.svg](media/10-faces-of-e.svg).
4. SA hermana: [Campana gaussiana](sa-campana-gaussiana-bach.md).

---

## 13. Principios didácticos (ficha TFM 21)

| Principio | Cómo se concreta aquí |
|-----------|----------------------|
| No confundir accesibilidad con concreción | Límite y serie se presentan con andamiaje (tablas, sumas parciales) |
| Contextualizar para abstraer | Finanzas y decaimiento *después* del modelo |
| Diseñar para la transferencia lejana | Sesión 6: contexto no ensayado |
| Fomentar el habla interna | Explicación de «qué se mantiene» entre caras |
| Abstracción como competencia vital | Anticipar (crecimiento futuro, semivida) desde la estructura |
