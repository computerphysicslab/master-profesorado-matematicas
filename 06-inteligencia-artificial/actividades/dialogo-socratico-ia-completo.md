# Actividad completa: Diálogo socrático con la IA

**Nivel orientativo:** 3.º–4.º ESO y Bachillerato (adaptable a 1.º–2.º ESO con problemas más guiados).  
**Duración:** 50–55 minutos en clase + cierre/reflexión (o 2 sesiones si el problema es largo).  
**Tema:** cualquiera del momento que admita **bloqueo productivo** (no un ejercicio mecánico de una sola operación).  
**Rol de la IA:** *tutor socrático* (pistas y preguntas), **nunca** resolutor del producto final.

Enlaces: [catálogo de prompts](../prompts/catalogo-prompts-matematicas.md) · [plantilla de proceso](../evaluacion/plantilla-proceso-ia.md) · [rúbricas de uso](../evaluacion/rubricas-uso-ia.md) · [propuestas-aula](propuestas-aula.md)

---

## 1. Objetivos

| Tipo | Objetivo |
|------|----------|
| **Matemático** | Resolver un problema desafiante argumentando pasos y decisiones |
| **Metacognitivo** | Pedir ayuda de forma estratégica; distinguir pista útil de solución regalo |
| **Sobre IA** | Usar un chatbot con normas; detectar si rompe el rol socrático; documentar el proceso |

**Criterios de evaluación (orientativos LOMLOE):** los del bloque de la unidad (resolución de problemas, razonamiento, comunicación). El uso de IA se valora con la [rúbrica de uso](../evaluacion/rubricas-uso-ia.md), no sustituye el criterio matemático.

---

## 2. Materiales

- Un **problema desafiante** del tema actual (ver §4): requiere modelización, varios pasos o una decisión no trivial.
- Acceso a un chatbot autorizado por el centro (o sesión preparada por el docente).
- Prompt de **tutor socrático** listo para copiar (§5).
- [Plantilla de proceso con IA](../evaluacion/plantilla-proceso-ia.md) (versión breve en papel si no hay digital).
- Norma de aula visible: *prohibido pedir la solución completa; si la IA la da, se señala y no se usa*.

---

## 3. Secuencia paso a paso

| Tiempo | Fase | Qué hace el docente | Qué hace el alumnado |
|--------|------|---------------------|----------------------|
| 5 min | **Marco y norma** | Explica el objetivo: «La IA pregunta y da pistas; tú razonas y entregas la solución.» Lee la norma en voz alta. | Escucha; aclara dudas sobre qué está permitido |
| 5 min | **Problema** | Entrega el enunciado. Prohíbe abrir el chat todavía. | Lee; anota qué entiende y qué no; 2–3 min de intento en silencio o pareja |
| 25–30 min | **Diálogo socrático** | Circula. Si alguien pide «resuélveme», redirige al prompt. Si la IA se rompe y da la solución, recuerda la norma. | Pega el prompt socrático + el problema. Dialoga. Toma notas de pistas útiles/inútiles. Escribe su resolución en el cuaderno |
| 8 min | **Producto y proceso** | Recuerda qué entregar. | Completa resolución final + plantilla de proceso (o reflexión 5–8 líneas) |
| 5 min | **Cierre** | 2–3 voces: «¿Qué pista te desbloqueó? ¿Cuál no sirvió?» | Comparte una estrategia de pregunta a la IA |

**Variante en dos sesiones:** sesión 1 = marco + diálogo + borrador; sesión 2 = verificación, resolución en limpio y defensa oral breve (1–2 min a una muestra).

---

## 4. Cómo elegir el problema

| Sirve bien | Evitar |
|------------|--------|
| Varios caminos o representaciones | Una sola operación aritmética |
| Requiere interpretar el enunciado | Copia literal de fórmula del libro |
| Posible bloqueo a mitad (buena para pistas) | Problema que el grupo ya automatizó |
| Datos reales o decisión a justificar | Enunciado ambiguo sin interés matemático |

**Ejemplos de tipo (adaptar al nivel y a la unidad):**

- ESO: sistema o ecuación contextualizada con dato superfluo; área/optimización sencilla; probabilidad con condición.
- Bachillerato: optimización, demostración guiada por preguntas, modelización con dos variables, coherencia función–gráfica–tabla.

El docente debe haber **resuelto antes** el problema y anticipado 2–3 puntos de bloqueo típicos.

---

## 5. Prompts listos para el aula

### 5.1. Prompt principal — Tutor socrático (alumno)

Copiar al inicio del chat (sustituir nivel y problema):

```
Eres un tutor de Matemáticas paciente y socrático para alumnado de [nivel].
El alumno está trabajando este problema:
[pegar problema]

Reglas estrictas:
- Nunca des la solución final ni el resultado numérico.
- Nunca escribas la resolución completa paso a paso.
- Haz solo UNA pregunta o da UNA pista cada vez.
- Adapta el nivel de ayuda según lo que el alumno diga que ya ha intentado.
- Si el alumno se bloquea, ofrece una pista más concreta, pero sigue sin resolver.
- Si el alumno pide la solución, recuérdale que tu rol es guiar y hazle una pregunta.

Empieza preguntando qué ha intentado ya.
```

### 5.2. Si el modelo «se rompe» y da la solución

El alumno debe:

1. Señalarlo en la plantilla («la IA dio la solución en el mensaje X»).
2. **No copiar** ese mensaje como producto.
3. Reiniciar el chat con el mismo prompt o pedir: *«No quiero la solución. Solo una pregunta sobre el siguiente paso.»*

### 5.3. Prompt de refuerzo (opcional, si solo da pistas demasiado vagas)

```
Sigue siendo tutor socrático. No des la solución.
Mi bloqueo concreto es: [describir en una frase].
Dame UNA pista más concreta sobre la estrategia, sin números del resultado final.
```

### 5.4. Para el docente — generar un problema adecuado

```
Diseña un problema de [tema] para [nivel] (LOMLOE) que:
- Requiera al menos tres pasos de razonamiento o una decisión de modelización
- Admita bloqueo productivo a mitad (no sea mecánico)
- Incluya un contexto realista
No des la solución. Indica en una línea qué criterio de evaluación orientativo trabaja.
```

---

## 6. Evidencias a recoger

1. **Resolución final** del alumno (cuaderno o digital), escrita por él/ella.
2. **Proceso con IA:** [plantilla-proceso-ia.md](../evaluacion/plantilla-proceso-ia.md) **o**, como mínimo:
   - captura/resumen del hilo (prompts clave, no hace falta todo),
   - reflexión de 5–8 líneas: *qué pistas ayudaron, cuáles no, por qué; si la IA dio la solución y qué hizo entonces*.
3. **Opcional:** defensa oral de 1–2 minutos sobre un paso clave (muestra de alumnos).

**No evaluar** la longitud del chat ni la «calidad literaria» de la IA. Evaluar comprensión matemática + uso estratégico y honesto de la herramienta.

---

## 7. Rúbrica rápida

### 7.1. Uso de la IA (alineada con [rubricas-uso-ia.md](../evaluacion/rubricas-uso-ia.md))

| Criterio | Excelente | Adecuado | En desarrollo | Insuficiente |
|----------|-----------|----------|---------------|--------------|
| **Norma socrática** | No pide la solución; si la IA la da, la marca y no la usa | Cumple la norma con algún desliz menor | Pide «casi la solución» o usa un regalo parcial sin señalarlo | Copia la resolución de la IA como propia |
| **Estrategia de diálogo** | Pregunta con foco («estoy en…; he intentado…») | Diálogo útil aunque genérico | Solo «no sé» / «resuelve» | No hay diálogo real |
| **Declaración y reflexión** | Plantilla o reflexión clara y honesta | Completa lo esencial | Muy incompleta | Ausente o falsa |

### 7.2. Matemáticas (criterios de la unidad)

Usar la rúbrica o los criterios de la programación de aula. La IA no altera el listón de corrección y justificación.

---

## 8. Posibles problemas y gestión

| Problema | Qué hacer |
|----------|-----------|
| La IA da la solución al primer mensaje | Recordar norma; reiniciar chat; valorar positivamente a quien lo declare |
| El alumno no intenta nada antes del chat | Exigir 3–5 min de intento previo (anotado) antes de abrir la IA |
| Chat muy largo y sin avance | Intervenir: «Escribe en una frase dónde estás bloqueado» y usar el prompt de refuerzo |
| Sin dispositivos / sin red | El docente proyecta un diálogo socrático *preparado* y el alumnado responde en papel a las preguntas del tutor; o trabajo por estaciones con pocos dispositivos |
| Copia entre compañeros del hilo | Resolución individual; el hilo puede ser parecido, el producto y la reflexión deben ser propios |
| Ansiedad («sin la IA no sé») | Cierre: el objetivo es necesitar *menos* pistas la próxima vez; anotar qué estrategia interna se aprendió |

---

## 9. Variantes

| Variante | Descripción |
|----------|-------------|
| **Parejas** | Un alumno dialoga con la IA; el otro observa y anota si se respeta el rol socrático; luego intercambian |
| **Sin pantalla (docente-tutor)** | El docente actúa como tutor socrático en vivo (mismas reglas); después se compara con un hilo de IA |
| **Pistas en papel** | El docente prepara 4 pistas graduadas en sobres; el alumno solo puede abrir la siguiente tras justificar por qué la necesita |
| **Bachillerato** | Problema de demostración o modelización; defensa oral obligatoria del paso clave |
| **1.º–2.º ESO** | Problema más corto; máximo 3–4 intercambios con la IA; más modelado conjunto al inicio |

---

## 10. Diferenciación (DUA)

| Necesidad | Ajuste |
|-----------|--------|
| Dificultades de lectura / comprensión del enunciado | Reformular el problema antes (prompt de reformulación del catálogo); permitir audio |
| TDAH / bloqueo frecuente | Permitir más turnos de pista; exigir igual la resolución propia y la verificación |
| Alta capacidad | Problema de extensión o con dato contradictorio a detectar; menos pistas o autoimposición de máximo N mensajes |
| Poco acceso a dispositivos | Estación compartida o versión en papel con pistas del docente |

Enlazar con el dilema ético de andamiaje vs. sustitución: [dilemas-eticos.md](../etica/dilemas-eticos.md) (viñeta 1).

---

## 11. Relación con otras piezas del repo

| Pieza | Uso en esta actividad |
|-------|----------------------|
| [Tutor socrático en el catálogo](../prompts/catalogo-prompts-matematicas.md) | Base del prompt §5.1 |
| [Plantilla de proceso](../evaluacion/plantilla-proceso-ia.md) | Evidencia de uso declarado |
| [Cazador de alucinaciones](cazador-alucinaciones-completo.md) | Conviene **antes**: el alumnado ya sabe que la IA puede fallar |
| [Apunte transversal](../../02-apuntes/tecnologia-educativa/ia-en-el-aula-matematicas.md) | Marco de usos legítimos y normas |

---

## 12. Después de la sesión

- Guardar 1–2 problemas que hayan funcionado bien (reutilizables).
- Si muchos chats «rompieron» el rol socrático, practicar 10 min solo de *formulación de preguntas a la IA* en la sesión siguiente.
- Conectar con tareas para casa: mismo prompt + plantilla de proceso solo si la norma de aula lo permite.

---

*Actividad de apoyo para el Máster de Profesorado · Matemáticas. Adaptar al grupo, a los dispositivos disponibles y a la programación de aula.*
