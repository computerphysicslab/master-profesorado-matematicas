---
layout: default
title: "¿Cuántas personas para compartir cumpleaños?"
parent: Situaciones de aprendizaje
nav_order: 21
---

# SA — ¿Cuántas personas hacen falta para que dos compartan cumpleaños?

## 0. Metadatos

| Campo | Contenido |
|-------|-----------|
| **Título de la SA** | La paradoja del cumpleaños |
| **Nivel / curso** | 3.º–4.º ESO (Matemáticas) |
| **Duración** | 5 sesiones × 50–55 min |
| **Autor/a de la ficha** | Material del repositorio |
| **Fecha / versión** | 2026-10 / v1.0 |
| **Contexto de uso** | Diseño curricular · Practicum |

**Palabras clave:** probabilidad, combinatoria, paradoja, simulación, sentido estocástico, intuición vs cálculo

---

## 1. Pregunta guía / reto

> *En un grupo de 23 personas, ¿crees que es raro que dos cumplan años el mismo día? ¿Y si apuestas?*

**Producto final esperado:** (1) estimación intuitiva inicial sellada en un sobre, (2) experimento con la clase o simulación, (3) cálculo aproximado de la probabilidad y (4) póster «intuición vs matemática» con un ejemplo de aplicación (hashing, coincidencias en redes).

---

## 2. Justificación y sentido educativo

- **Efecto wow garantizado:** casi nadie intuye que con 23 personas la probabilidad supera el 50 %.
- Entrena el **conflicto cognitivo** entre intuición y modelo matemático (idea clave del sentido estocástico).
- Puente natural hacia **complementario** $P(\text{al menos un par}) = 1 - P(\text{todos distintos})$.
- Aplicaciones reales sorprendentes: colisiones en criptografía, coincidencias en bases de datos.

---

## 3. Objetivos de aprendizaje

1. Distinguir probabilidad intuitiva y probabilidad modelizada.
2. Usar el razonamiento del complementario en un contexto combinatorio.
3. Estimar $P$ mediante producto de fracciones o simulación.
4. Interpretar el resultado y comunicarlo a un público no experto.
5. Identificar un contexto real donde la misma lógica aparece.

---

## 4. Competencias específicas y criterios de evaluación

| CE | Criterios prioritarios | Evidencia |
|----|------------------------|----------|
| **CE1–CE2** | Modelizar e interpretar | Cálculo / simulación de $P$ |
| **CE3** | Conjeturar | Sobre de predicción inicial |
| **CE4** | Pensamiento computacional | Algoritmo de simulación (opcional) |
| **CE7–CE8** | Representar y comunicar | Póster o hilo explicativo |
| **CE9–CE10** | Socioafectivas | Aceptar que «me equivoqué de intuición» |

---

## 5. Saberes básicos y sentidos matemáticos

| Sentido | Saberes | Prioridad |
|---------|---------|----------|
| Estocástico | Probabilidad; sucesos; complementario; independencia aproximada | Alta |
| Numérico | Fracciones; productos largos; porcentajes | Alta |
| Algebraico | Fórmula general $P(n)$; patrones | Media |
| Socioafectivo | Humildad epistémica; debate respetuoso | Alta |

**Conexiones:** Informática (hash collisions), Psicología (sesgos), Ética (privacidad).

---

## 6. Secuencia de aprendizaje

| Sesión | Fase | Actividad del alumnado | Rol docente | Agrupamiento |
|--------|------|------------------------|-------------|--------------|
| 1 | Apuesta | Cada alumno escribe en secreto: «con N personas, ¿P > 50 %?» | Recoger sobres; no revelar | Individual |
| 2 | Experimento | Cumpleaños de la clase (o lista anonimizada); o simulación | Facilitar datos sin juzgar | Grupo-clase |
| 3 | Modelo | Construir $P(\text{todos distintos}) = \frac{365}{365}\cdot\frac{364}{365}\cdots$ | Guiar el complementario | Parejas |
| 4 | Cálculo / simulación | Completar tabla $n = 10, 20, 23, 30, 50, 70$ | Apoyo con hoja de cálculo | Equipos |
| 5 | Producto | Abrir sobres; comparar intuición vs resultado; póster de aplicación | Cerrar con sesgos cognitivos | Equipos + clase |

---

## 7. Metodología y organización

- **Enfoque:** conflicto cognitivo + modelización probabilística.
- **Materiales:** sobres, lista de cumpleaños (RGPD: solo día/mes), calculadora, opcional Sheets/Python.
- **Cuidado ético:** nadie está obligado a decir su cumpleaños; usar dataset público o simulación.

---

## 8. Evaluación

### 8.1. Formativa
- Pregunta en caliente: «¿Por qué falló la intuición?»
- Lista de cotejo del producto complementario.

### 8.2. Sumativa
| Criterio | Indicadores |
|----------|-------------|
| Modelo | Explican el complementario con sus palabras |
| Cálculo | Obtienen $P(23) \approx 0{,}5$ (tolerancia razonable) |
| Transferencia | Citan al menos una aplicación real plausible |
| Metacognición | Comparan su predicción inicial con el resultado |

### 8.3. Autoevaluación
- Una frase: «Mi intuición falló / acertó porque…»

---

## 9. Atención a la diversidad y DUA

| Principio | Medida |
|-----------|--------|
| Implicación | Formato «apuesta»; gamificación ligera |
| Representación | Diagrama de árbol reducido; simulación visual; fórmula |
| Acción y expresión | Cálculo manual, hoja de cálculo o explicación oral |

**Refuerzo:** solo $n = 10$ y $n = 23$ paso a paso. **Ampliación:** año bisiesto; mismo día de la semana.

---

## 10. Dimensión socioafectiva

- Normalizar el **error intuitivo**: no es «ser malo en mates», es un sesgo humano documentado.
- Debate: ¿preferimos intuición rápida o modelo lento?
- CE9–CE10: respeto a predicciones ajenas; no ridiculizar al que dijo «hace falta un grupo de 180».

---

## 11. Orientaciones

- No revelar el 23 hasta después del experimento.
- Variante corta (2 sesiones): solo apuesta + simulación + cifra final.
- Evitar datos personales sensibles (RGPD).

---

## 12. Referencias

### Normativa
- RD 217/2022 (sentido estocástico, probabilidad)

### Didáctica
1. Problema clásico de probabilidad; ver también «hash collisions».
2. Material del repo: evaluación formativa global (feedback sin humillar).

---

## 13. Anexo — Valores orientativos (docente)

| $n$ | $P$ (aprox.) |
|------|----------------|
| 10 | 12 % |
| 20 | 41 % |
| 23 | **50,7 %** |
| 30 | 70 % |
| 50 | 97 % |
| 70 | 99,9 % |

Fórmula: $P(n) = 1 - \dfrac{365 P_n}{365^n}$ donde $365 P_n = 365!/(365-n)!$.
