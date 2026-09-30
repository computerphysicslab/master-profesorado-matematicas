# Diseño de prompts educativos para Matemáticas

Un **prompt** es la instrucción que damos a la IA. La calidad de la salida depende mucho de cómo se formula.

---

## 1. Principios básicos (RTF + contexto didáctico)

| Elemento | Qué incluir |
|----------|-------------|
| **Rol** | Quién es la IA (profesor de Matemáticas de 3.º ESO, diseñador de materiales, tutor socrático…) |
| **Tarea** | Qué debe hacer exactamente (generar, reformular, dar pistas, detectar errores…) |
| **Formato** | Cómo debe responder (pasos numerados, tabla, lista de pistas sin solución, rúbrica…) |
| **Restricciones** | Nivel curricular, no dar la solución final, usar lenguaje accesible, evitar términos no introducidos… |
| **Contexto** | Criterio de evaluación, saberes básicos, características del grupo (si es relevante y no sensible) |

---

## 2. Técnicas útiles

### Cadena de pensamiento (para el modelo)

«Razona paso a paso antes de dar la respuesta final.»  
Útil cuando se quiere una resolución detallada (siempre verificada después).

### Few-shot (ejemplos)

Dar 1-2 ejemplos del tipo de salida deseada mejora mucho la calidad, especialmente en generación de problemas o pistas.

### Separación de roles

«Actúa solo como generador de pistas. No des nunca la solución completa ni el resultado numérico final.»

### Iteración

Primera versión → «Ahora hazlo más corto / más motivador / con contexto de deporte / para alumnado con dificultad en fracciones.»

---

## 3. Errores frecuentes al promptar

- Pedir «un problema de ecuaciones» sin especificar nivel, tipo de solución ni contexto.
- No prohibir la solución final cuando se quieren solo pistas.
- Aceptar la primera salida sin pedir variantes o mejoras.
- Incluir datos personales del alumnado.

---

## 4. Plantilla mínima reutilizable

```
Eres un profesor de Matemáticas de [nivel] en España (currículo LOMLOE).
Tu tarea es: [tarea concreta].
Restricciones:
- [lista]
Formato de salida:
- [lista]
Contexto adicional: [criterio, saberes, etc.]
```

---

## 5. Siguiente paso

Usa el [catálogo de prompts](catalogo-prompts-matematicas.md) como punto de partida y adáptalo.
