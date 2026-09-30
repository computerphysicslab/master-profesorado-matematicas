# Fundamentos de los modelos de lenguaje grandes (LLM)

**Nivel:** orientativo para profesorado no especialista en IA  
**Propósito:** entender *por qué* la IA generativa se comporta como se comporta al resolver o explicar matemáticas.

---

## 1. Qué es (y qué no es) un LLM

Un **modelo de lenguaje grande** (GPT, Claude, Gemini, Llama, etc.) es un sistema estadístico entrenado para predecir la siguiente palabra (o token) más probable dado un contexto.

- **No** es una base de datos de hechos verificados.
- **No** es un motor de cálculo simbólico (aunque algunos se conectan a herramientas externas).
- **Sí** es un generador de texto muy fluido que ha visto enormes cantidades de texto, código y problemas resueltos.

Por eso puede:

- Escribir explicaciones con tono seguro y estructura clara.
- Reproducir patrones de resolución de problemas frecuentes.
- Inventar pasos, teoremas o números cuando el patrón «suena bien».

---

## 2. Implicaciones directas para Matemáticas

| Característica del LLM | Consecuencia en el aula de Matemáticas |
|------------------------|----------------------------------------|
| Predicción estadística | Puede dar la respuesta correcta «de memoria» sin razonamiento generalizable |
| Entrenamiento con textos | Favorece enunciados y soluciones estereotipados |
| Falta de verificación interna | Errores aritméticos o lógicos con apariencia impecable |
| Contexto limitado | Olvida restricciones del enunciado en conversaciones largas |
| Sesgo de entrenamiento | Representaciones y contextos poco diversos o sesgados |

---

## 3. Generación vs. cálculo

Muchos modelos actuales pueden:

- Llamar a herramientas externas (código Python, calculadoras, búsqueda).
- Usar «cadena de pensamiento» (mostrar pasos intermedios).

Aun así, el resultado final sigue siendo texto generado. La verificación externa (GeoGebra, calculadora, papel, caso particular) sigue siendo responsabilidad del usuario.

---

## 4. Qué debe saber el alumnado (versión mínima)

1. La IA puede equivocarse con tono convincente.
2. «Suena bien» ≠ «es correcto».
3. Hay que comprobar: sustituir valores, casos límite, otra representación.
4. El aprendizaje ocurre cuando *tú* puedes explicar y defender el razonamiento.

---

## 5. Lectura recomendada interna

- [Limitaciones y alucinaciones](limitaciones-alucinaciones.md)
- [Catálogo de prompts](../prompts/catalogo-prompts-matematicas.md) (incluye prompts de verificación)
