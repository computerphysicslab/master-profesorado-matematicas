---
layout: default
title: "SA: Monty Hall y la probabilidad condicionada"
parent: Situaciones de aprendizaje
nav_order: 32
---

# SA — ¿Te conviene cambiar de puerta? (Monty Hall)

## 0. Metadatos

| Campo | Contenido |
|-------|-----------|
| **Título de la SA** | ¿Te conviene cambiar de puerta? |
| **Nivel / curso** | 4.º ESO / 1.º Bachillerato (Matemáticas) |
| **Duración** | 5 sesiones × 50–55 min |
| **Autor/a de la ficha** | Material del repositorio |
| **Fecha / versión** | 2026-10 · v1.0 |
| **Contexto de uso** | Diseño curricular · Practicum · sentido estocástico · germen de TFM |

**Palabras clave:** Monty Hall, probabilidad condicionada, intuición vs cálculo, simulación, Bayes, sentido estocástico

---

## 1. Pregunta guía / reto

> *Tres puertas: un coche y dos cabras. Eliges una. El presentador, que sabe qué hay detrás de cada puerta, abre otra y muestra una cabra. ¿Te conviene cambiar a la puerta que queda cerrada?*

**Producto final esperado:** informe o póster de equipo con (1) predicción inicial sellada, (2) resultados de simulación (cambiar vs no cambiar), (3) argumento de por qué cambiar gana con probabilidad $2/3$, (4) condiciones del presentador que hacen válido el modelo y (5) puente breve hacia la actualización de creencias (Bayes) con un ejemplo sencillo.

---

## 2. Justificación y sentido educativo

- Laboratorio escolar clásico de **conflicto intuición–razón** en probabilidad condicionada.
- La simulación (cartas, aula o Python) convence antes que la fórmula sola.
- Permite explicitar **hipótesis del modelo** (el presentador siempre abre una cabra y nunca la puerta del concursante).
- Puente natural hacia Bayes y tablas de frecuencias (test médico, falsos positivos).

**Germen narrativo:** [El problema de Monty Hall](../../03-materiales/historias-matematicas/fichas/monty-hall.md).  
**Profundización:** [Bayes y la probabilidad condicionada](../../03-materiales/historias-matematicas/fichas/bayes.md).

---

## 3. Objetivos de aprendizaje

1. Formular una predicción intuitiva y contrastarla con datos.
2. Diseñar y ejecutar una simulación del juego (cambiar siempre / no cambiar nunca).
3. Explicar con un argumento de casos por qué $P(\text{ganar si cambias}) = 2/3$.
4. Identificar las reglas del presentador sin las cuales el problema cambia.
5. Comunicar el resultado a un público escéptico (intuición vs modelo).
6. (Ampliación) Conectar con probabilidad condicionada y un ejemplo bayesiano simple (tabla de frecuencias).

---

## 4. Competencias específicas y criterios de evaluación

| CE (síntesis) | Criterios prioritarios | Evidencia en esta SA |
|---------------|------------------------|----------------------|
| **CE1–CE2** Modelizar / resolver | Modelizar el juego; validar con simulación | Tabla de ensayos + conclusión |
| **CE3** Razonar y conjeturar | Argumentar $2/3$ con casos o árbol | Apartado de razonamiento del producto |
| **CE4** Pensamiento computacional | Algoritmo de simulación (opcional) | Protocolo o código breve |
| **CE7–CE8** Representar / comunicar | Diagramas, frecuencias, claridad | Póster o informe |
| **CE9–CE10** Socioafectivas | Aceptar revisión de la intuición; debate respetuoso | Observación + autoevaluación |

**Competencias clave:** STEM, CCL, CD, CPSAA.

---

## 5. Saberes básicos y sentidos matemáticos

| Sentido | Saberes / contenidos | Prioridad |
|---------|----------------------|----------|
| Estocástico | Probabilidad; sucesos; probabilidad condicionada (idea); simulación | Alta |
| Numérico | Frecuencias relativas; fracciones; porcentajes | Alta |
| Algebraico | Casos; árbol de probabilidad (opcional) | Media |
| Socioafectivo | Humildad epistémica; argumentar bajo desacuerdo | Alta |

**Conexiones interdisciplinares:** Psicología (sesgos), Medios (concursos), Filosofía (actualización de creencias).

---

## 6. Secuencia de aprendizaje

| Sesión | Fase | Actividad del alumnado | Rol docente | Agrupamiento |
|--------|------|------------------------|-------------|--------------|
| 1 | Apuesta | Enunciado del juego; predicción individual en sobre («cambio / no cambio / da igual»); debate breve sin resolver | Recoger sobres; no revelar la respuesta | Individual → clase |
| 2 | Simulación manual | Juego con 3 cartas (as = coche); mitad de la clase «siempre cambia», mitad «nunca»; registrar éxitos | Asegurar reglas del presentador; arbitrar | Parejas / equipos |
| 3 | Agregación y modelo | Poner en común frecuencias; construir argumento de casos ($1/3$ vs $2/3$); diagrama de árbol opcional | Guiar sin adelantar la cifra mágica antes de los datos | Equipos + clase |
| 4 | Condiciones y Bayes | ¿Qué pasa si el presentador elige al azar? Puente a tabla de frecuencias (test médico ficticio) o relectura bayesiana de Monty Hall | Introducir hipótesis del modelo; números de ficción en salud | Equipos |
| 5 | Producto y cierre | Abrir sobres; redactar/presentar producto; reflexión «¿por qué falló la intuición?» | Moderar; normalizar el error intuitivo | Equipos + clase |

**Hito intermedio (sesión 2–3):** hoja de registro con ≥20 ensayos por estrategia (cambiar / no cambiar).

---

## 7. Metodología y organización

- **Enfoque:** conflicto cognitivo + simulación + formalización.
- **Agrupamientos:** parejas en la simulación; equipos de 3–4 para el producto.
- **Espacios:** aula; opcional aula de informática (simulación Python/Sheets).
- **Materiales:** tres cartas por pareja (o vasos/fichas); hojas de registro; (opcional) hoja de cálculo.

**Reglas que hay que fijar (docente):**
1. El coche se coloca al azar.
2. El concursante elige una puerta.
3. El presentador **siempre** abre una puerta con cabra distinta de la elegida.
4. Si hay dos cabras posibles, elige al azar entre ellas.

---

## 8. Evaluación

### 8.1. Formativa
Preguntas en caliente tras la simulación; revisión del argumento de casos antes del producto final.

### 8.2. Sumativa
| Criterio | Indicadores (peso orientativo) |
|----------|--------------------------------|
| Simulación | Registro claro; comparación cambiar vs no cambiar (25 %) |
| Razonamiento | Explican $2/3$ con casos o árbol (30 %) |
| Condiciones del modelo | Identifican reglas del presentador (15 %) |
| Comunicación | Producto legible; distinguen intuición y modelo (20 %) |
| Proceso / metacognición | Comparan predicción inicial y resultado (10 %) |

### 8.3. Autoevaluación y coevaluación
Una frase: «Mi intuición acertó/falló porque…». Coevaluación del argumento de otro equipo (claridad + una mejora).

---

## 9. Atención a la diversidad y DUA

| Principio DUA | Medida concreta |
|---------------|-----------------|
| Implicación | Formato «apuesta»; juego tangible con cartas |
| Representación | Simulación física, tabla de frecuencias, árbol, argumentación verbal |
| Acción y expresión | Informe, póster, vídeo de 90 s o exposición |

**Refuerzo:** solo simulación + conclusión empírica («cambiar gana más a menudo»). **Ampliación:** demostración formal; variante con $n$ puertas; conexión explícita con la fórmula de Bayes.

---

## 10. Dimensión socioafectiva

- **Humildad epistémica:** mucha gente (incluso expertas) se resiste al $2/3$; el desacuerdo es histórico (vos Savant, 1990).
- **Debate respetuoso:** no ridiculizar a quien «no cambia».
- **Autoconcepto:** valorar el cambio de opinión cuando los datos y el argumento lo exigen.
- Registro: CE9–CE10 (apertura a revisar intuiciones; cooperación en la simulación).

---

## 11. Orientaciones para la implementación

- **No revelar** el $2/3$ en la sesión 1; la simulación debe preceder a la certeza.
- Insistir en las **reglas del presentador**; sin ellas el problema es otro.
- Variante corta (3 sesiones): apuesta + simulación + argumento de casos.
- Variante Bachillerato: árbol formal + ejemplo bayesiano completo (prevalencia y falsos positivos con números de ficción).
- Evitar ejemplos médicos reales que generen ansiedad; usar datos inventados y explícitamente ficticios.

---

## 12. Referencias

### Normativa
- [RD 217/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-4975) · [RD 243/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-5521)

### Didáctica y recursos
1. Problema de Monty Hall; controversia Marilyn vos Savant (1990).
2. Historias matemáticas: [Monty Hall](../../03-materiales/historias-matematicas/fichas/monty-hall.md) · [Bayes](../../03-materiales/historias-matematicas/fichas/bayes.md).
3. SA hermanas: [Paradoja del cumpleaños](sa-paradoja-cumpleanos-3eso.md) · [Independencia y Drake](sa-independencia-drake-4eso.md).

---

## 13. Anexo — Guía rápida (docente)

**Argumento de casos**

| Situación inicial (prob.) | Acción del presentador | Si cambias |
|---------------------------|------------------------|------------|
| Elegiste el coche ($1/3$) | Abre una de las dos cabras | Pierdes |
| Elegiste cabra A ($1/3$) | Debe abrir la otra cabra | Ganas |
| Elegiste cabra B ($1/3$) | Debe abrir la otra cabra | Ganas |

$$P(\text{ganar si cambias}) = 2/3,\qquad P(\text{ganar si no cambias}) = 1/3$$

**Simulación orientativa:** con ≥30 ensayos por estrategia, las frecuencias suelen acercarse a $2/3$ y $1/3$ (variabilidad muestral esperable).
