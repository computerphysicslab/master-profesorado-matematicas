# Limitaciones y alucinaciones en Matemáticas

Las «alucinaciones» son respuestas incorrectas o inventadas presentadas con confianza. En Matemáticas son especialmente peligrosas porque el formato (pasos numerados, lenguaje formal) genera falsa sensación de rigor.

---

## 1. Errores frecuentes de la IA en problemas matemáticos

| Tipo de error | Ejemplo típico | Cómo detectarlo |
|---------------|----------------|-----------------|
| **Aritmética incorrecta** | Operaciones básicas fallidas en medio de un desarrollo | Sustituir números pequeños o usar calculadora |
| **Pasos inventados** | Teorema o propiedad que no existe o se aplica mal | Pedir justificación o buscar la propiedad |
| **Olvido de condiciones** | Resolver sin tener en cuenta dominio, unidades o restricciones | Revisar el enunciado original punto por punto |
| **Inconsistencia entre representaciones** | Tabla, gráfica y fórmula que no cuadran | Exigir coherencia entre varias formas |
| **Generalización indebida** | Caso particular presentado como regla general | Probar con otro ejemplo o contraejemplo |
| **Lenguaje impreciso** | Uso incorrecto de «por tanto», «se demuestra que» | Exigir definiciones y equivalencias |

---

## 2. Casos concretos (reproducibles en clase)

Los ejemplos siguientes son **tipos** de fallo que se observan con frecuencia en modelos de lenguaje. No dependen de una versión concreta: el docente puede regenerarlos pidiendo la misma tarea a un chatbot y contrastando.

### Caso A — Aritmética en números grandes

**Pedido típico:** «Calcula 3847 × 296 y explica el método.»

**Qué suele fallar:** el producto intermedio o el resultado final, aunque los pasos se presenten ordenados.

**Detección en aula:**
- Calcular con calculadora o a mano con números más pequeños y el mismo método.
- Comprobar paridad / orden de magnitud (3847 ≈ 4000, 296 ≈ 300 → orden 1,2·10⁶).

**Uso didáctico:** mostrar que un texto «bonito» no garantiza aritmética correcta.

### Caso B — Confusión de teoremas (Rolle vs. Lagrange / valor medio)

**Pedido típico:** «Enuncia el teorema de Rolle y aplícalo a f(x) = x² − 1 en [−1, 1].»

**Qué suele fallar:** mezclar hipótesis (Rolle exige f(a) = f(b); el teorema del valor medio no), o citar el nombre incorrecto con la conclusión correcta (o al revés).

**Detección en aula:**
- Pedir que escriban *solo* las hipótesis, sin la conclusión.
- Preguntar: «¿Qué cambia si f(−1) ≠ f(1)?»

**Uso didáctico:** el alumnado debe contrastar con el libro o apuntes, no con el tono seguro del chat.

### Caso C — Problema con datos contradictorios

**Pedido típico:** un enunciado con tres datos incompatibles (p. ej. triángulo con lados 3, 4 y 10; o sistema lineal sobredeterminado inconsistente presentado como si tuviera solución única).

**Qué suele fallar:** la IA «resuelve» inventando un valor o ignorando una restricción, en lugar de detectar la imposibilidad.

**Detección en aula:**
- Preguntar antes: «¿Es posible esta situación? Justifica.»
- Exigir que señalen la contradicción *antes* de calcular.

**Uso didáctico:** actividad de «error plantado» en el enunciado, no solo en la resolución.

### Caso D — Inconsistencia tabla–gráfica–fórmula

**Pedido típico:** «Da la fórmula, una tabla de 5 valores y describe la gráfica de una función cuadrática que pasa por (0, 3) y tiene vértice en (2, −1).»

**Qué suele fallar:** la fórmula no genera los puntos de la tabla, o la descripción del vértice no coincide con la expresión algebraica.

**Detección en aula:**
- Sustituir x = 0 y x = 2 en la fórmula y comparar con la tabla.
- Exigir que las tres representaciones se validen mutuamente (papel o GeoGebra).

**Uso didáctico:** convierte la verificación en el centro de la tarea.

### Caso E — «Demostración» con paso inventado

**Pedido típico:** «Demuestra que √2 es irracional» o una identidad trigonométrica sencilla.

**Qué suele fallar:** un paso que parece formal («por tanto, como n² es par, n es par») pero con una laguna, una hipótesis no justificada o un salto lógico.

**Detección en aula:**
- El alumnado marca cada línea como *justificado / no justificado*.
- Defensa oral del paso clave en 1 minuto.

**Uso didáctico:** ideal en Bachillerato; enlaza con la rúbrica de análisis de resolución de IA.

### Caso F — Regla de signos o dominio olvidado

**Pedido típico:** resolver √(x − 3) = x − 5 o una inecuación con valor absoluto.

**Qué suele fallar:** aceptar soluciones que no cumplen el dominio (radicando negativo, denominador nulo) o perder una de las ramas del valor absoluto.

**Detección en aula:** lista de comprobación fija: (1) dominio, (2) resolución, (3) verificación en la ecuación original.

---

## 3. Estrategias de verificación (para alumnado y docente)

1. **Caso particular numérico.** Sustituir valores sencillos y comprobar.
2. **Casos límite.** ¿Qué pasa si el parámetro es 0, 1, negativo, muy grande?
3. **Otra representación.** ¿Cuadra con una gráfica, tabla o interpretación geométrica?
4. **Explicación en voz alta.** Si no se puede explicar el paso clave sin mirar el chat, no se ha aprendido.
5. **Comparar dos modelos.** Pedir la misma tarea a dos IA distintas y contrastar.
6. **Pedir contraejemplos.** «Dame un caso en el que esta afirmación falle.»
7. **Checklist de dominio y restricciones** antes de aceptar cualquier solución.

---

## 4. Actividad de aula sugerida: «Cazador de alucinaciones»

Versión resumida (secuencia completa en [actividades/cazador-alucinaciones-completo.md](../actividades/cazador-alucinaciones-completo.md)):

1. El docente genera (o selecciona) una resolución de IA con 1-2 errores sutiles.
2. El alumnado, en parejas, debe:
   - Marcar los pasos dudosos.
   - Justificar por qué son incorrectos o incompletos.
   - Reescribir la resolución correcta.
3. Puesta en común: qué pistas usaron para detectar el error.

Esta actividad entrena **pensamiento crítico matemático** y convierte la IA en objeto de estudio, no solo en herramienta de resolución.

---

## 5. Implicación para el diseño de tareas

Si la tarea se puede resolver completamente pegando el enunciado en un chatbot y copiando la respuesta, es **vulnerable**. Hay que exigir:

- Proceso visible (intentos, bocetos).
- Defensa oral o cambio de datos en el momento.
- Coherencia entre representaciones.
- Datos locales o vivos difíciles de «buscar» en el entrenamiento.

Ver estrategias completas en el [apunte transversal](../../02-apuntes/tecnologia-educativa/ia-en-el-aula-matematicas.md).

---

## 6. Nota sobre caducidad

Los modelos mejoran; un error concreto puede desaparecer en una versión posterior. Lo que **no caduca** es el hábito de verificación. Los casos de esta ficha son plantillas: regenera el fallo con el modelo disponible en el aula y adapta el enunciado al tema de la unidad.
