---
layout: default
title: "SA: Hamlet y los dígitos de π"
parent: Situaciones de aprendizaje
nav_order: 31
---

# SA — ¿Está «ser o no ser» escondido en π?

## 0. Metadatos

| Campo | Contenido |
|-------|-----------|
| **Título de la SA** | Hamlet y los dígitos de π |
| **Nivel / curso** | 4.º ESO / 1.º Bachillerato (Matemáticas) |
| **Duración** | 5 sesiones × 50–55 min |
| **Autor/a de la ficha** | Material del repositorio |
| **Fecha / versión** | 2026-10 · v1.0 |
| **Contexto de uso** | Diseño curricular · Practicum · pensamiento computacional · germen de TFM |

**Palabras clave:** π, codificación, probabilidad, órdenes de magnitud, números irracionales, pensamiento computacional, normalidad de π

---

## 1. Pregunta guía / reto

> *¿Está la frase «ser o no ser» escondida en los dígitos de π? ¿Dónde la buscaríamos… y cuántos dígitos harían falta?*

**Producto final esperado:** informe de equipo con (1) propuesta de codificación texto→dígitos, (2) longitud de la cadena y probabilidad $10^{-L}$, (3) comparación de $10^{L}$ con el récord de dígitos conocidos, (4) conclusión argumentada sobre si «ya podría estar» en los dígitos calculados y (5) reflexión sobre qué cambia si cambia la codificación.

---

## 2. Justificación y sentido educativo

- Une **literatura, codificación y probabilidad** en un enigma memorable.
- Trabaja órdenes de magnitud y potencias de 10 de forma significativa (no como ejercicio rutinario).
- Distingue «probabilidad 1 en una secuencia infinita» de «aparición en el prefijo que conocemos».
- Introduce de forma honesta la conjetura de normalidad de π (sin presentarla como teorema).

**Germen narrativo:** [Hamlet y los dígitos de π](../../03-materiales/historias-matematicas/fichas/hamlet-pi.md).

---

## 3. Objetivos de aprendizaje

1. Diseñar y comparar codificaciones de texto en dígitos decimales.
2. Calcular la longitud $L$ de una cadena y la probabilidad $10^{-L}$ por posición.
3. Estimar la posición esperada de la primera aparición ($\sim 10^{L}$).
4. Comparar $10^{L}$ con el número de dígitos de π calculados y argumentar la conclusión.
5. Explicar por qué cambiar la codificación cambia «el lugar» de la frase en π.
6. (Ampliación) Distinguir conjetura de normalidad, probabilidad 1 en la expansión infinita y aparición en el prefijo conocido.

---

## 4. Competencias específicas y criterios de evaluación

| CE (síntesis) | Criterios prioritarios | Evidencia en esta SA |
|---------------|------------------------|----------------------|
| **CE1–CE2** Resolver / modelizar | Modelizar búsqueda en secuencia; validar escalas | Cadena + $10^{L}$ vs récord |
| **CE3** Razonar | Argumentar con potencias de 10 | Conclusión del informe |
| **CE5–CE6** Conexiones | Codificación ↔ probabilidad ↔ números | Apartado de conexiones |
| **CE7–CE8** Representar / comunicar | Tablas de códigos; claridad | Informe o póster |
| **CE9–CE10** Socioafectivas | Gestión de la incertidumbre; debate respetuoso | Observación + autoevaluación |

**Competencias clave:** STEM, CCL, CD, CPSAA.

---

## 5. Saberes básicos y sentidos matemáticos

| Sentido | Saberes / contenidos | Prioridad |
|---------|----------------------|----------|
| Numérico | Potencias de 10; órdenes de magnitud; notación científica | Alta |
| Estocástico | Probabilidad en modelo simple (i.i.d. uniforme) | Alta |
| Algebraico | Codificación; longitud de cadena; representación | Alta |
| Socioafectivo | Argumentar bajo incertidumbre; distinguir conjetura y hecho | Media |
| De la medida / espacial | N/A | Baja |

**Conexiones interdisciplinares:** Lengua (Hamlet), Tecnología (codificación, ASCII), Filosofía de la ciencia (conjetura vs teorema).

---

## 6. Secuencia de aprendizaje

| Sesión | Fase | Actividad del alumnado | Rol docente | Agrupamiento |
|--------|------|------------------------|-------------|--------------|
| 1 | Activación | Pregunta «¿está en π?»; lluvia de ideas; qué significa «estar dentro de π» | Recoger hipótesis en pizarra; no cerrar | Individual → clase |
| 2 | Codificación | Diseñar códigos propios (A=1…; ASCII; …); normalizar la frase; contar caracteres | Contrastar diseños; introducir alfabeto de 37 símbolos (00–36) | Equipos |
| 3 | Probabilidad y escala | Calcular $L$, $10^{-L}$, posición esperada $\sim 10^{L}$; buscar el récord de dígitos de π | Guiar notación científica; evitar «infinito = ya está» | Equipos |
| 4 | Comparación y producto | Comparar $10^{62}$ con $\sim 3{,}14\times 10^{14}$; redactar conclusión; (opcional) buscar cadenas *cortas* en un buscador de π | Supervisar honestidad científica (conjetura ≠ teorema) | Equipos |
| 5 | Comunicación | Puesta en común: ¿podría estar ya? ¿qué cambia con otra codificación?; cierre docente | Moderar; subrayar contraste de escalas | Grupo-clase |

**Hito intermedio (sesión 3):** tabla del equipo con $L$ y $10^{L}$ documentada.

---

## 7. Metodología y organización

- **Enfoque:** enigma progresivo + modelización probabilística simple.
- **Agrupamientos:** equipos de 3–4.
- **Espacios:** aula; opcional aula de informática (sesión 4).
- **Materiales:** tabla de codificación 00–36; calculadora; (opcional) buscador online de dígitos de π solo para cadenas cortas.

**Codificación de referencia (docente):** 37 símbolos (0–9, a–z, espacio) → 2 dígitos/símbolo; frase normalizada de 31 caracteres → **62 dígitos**; $P=10^{-62}$; posición esperada $\sim 10^{62}$; récord $\approx 3{,}14\times 10^{14}$ dígitos.

---

## 8. Evaluación

### 8.1. Formativa
Preguntas en sesiones 2–3; revisión de la longitud $L$ antes de comparar escalas.

### 8.2. Sumativa
| Criterio | Indicadores (peso orientativo) |
|----------|--------------------------------|
| Codificación | Propuesta coherente + longitud correcta (25 %) |
| Modelo probabilístico | $10^{-L}$ y posición esperada (25 %) |
| Comparación de escalas | Conclusión alineada con $10^{L}$ vs récord (25 %) |
| Comunicación y matices | Distinguen conjetura/prefijo conocido; claridad (15 %) |
| Proceso | Cooperación, revisión entre iguales (10 %) |

### 8.3. Autoevaluación y coevaluación
Escala breve: «entendí por qué la codificación importa / usé potencias de 10 con sentido». Coevaluación del apartado de conclusión de otro equipo.

---

## 9. Atención a la diversidad y DUA

| Principio DUA | Medida concreta |
|---------------|-----------------|
| Implicación | Gancho literario (Hamlet); reto con sorpresa de escalas |
| Representación | Tabla de códigos, potencias de 10, analogías de «búsqueda en una lista enorme» |
| Acción y expresión | Informe escrito, póster o presentación oral |

**Refuerzo:** frase más corta (p. ej. solo «ser o no ser») para $L$ menor. **Ampliación:** ASCII; debate sobre normalidad de π; búsqueda de cadenas de 6–10 dígitos.

---

## 10. Dimensión socioafectiva

- **Gestión de la incertidumbre:** aceptar «no lo sabemos con los dígitos actuales» como respuesta científica válida.
- **Pensamiento crítico:** resistir el eslogan «π contiene todo».
- **Cooperación:** contrastar codificaciones entre equipos sin ridiculizar diseños iniciales.

---

## 11. Orientaciones para la implementación

- **No afirmar** que π contiene todas las obras de Shakespeare como hecho demostrado.
- El punto didáctico es el **contraste de escalas**, no encontrar la frase.
- Si se usa buscador online, **solo cadenas cortas** y comentar límites de las bases públicas.
- Variante corta (3 sesiones): codificación fija del docente + cálculo de escalas + debate.
- Variante Bachillerato: normalidad de π, esperanza de la primera aparición, otras bases de codificación.

---

## 12. Referencias

### Normativa
- [RD 217/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-4975) · [RD 243/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-5521)

### Didáctica y recursos
1. Guinness World Records / StorageReview–Micron: récord de dígitos de π (314 billones, nov 2025).
2. Conjetura de normalidad de π (comportamiento estadístico; no demostrada).
3. Historia matemática: [Hamlet y los dígitos de π](../../03-materiales/historias-matematicas/fichas/hamlet-pi.md).
4. SA relacionadas: [Paradoja del cumpleaños](sa-paradoja-cumpleanos-3eso.md) (probabilidad), [Independencia y Drake](sa-independencia-drake-4eso.md) (modelos probabilísticos).

---

## 13. Anexo — Guía rápida (docente)

Alfabeto 37 símbolos → 2 dígitos/símbolo.  
Frase: `ser o no ser he ahi la cuestion` (31 caracteres) → **62 dígitos**.  
$P=10^{-62}$ por posición; posición esperada $\sim 10^{62}$.  
Récord $\approx 3{,}14\times 10^{14}$ dígitos → factor $\sim 3\times 10^{47}$ a favor del espacio de búsqueda esperado.
