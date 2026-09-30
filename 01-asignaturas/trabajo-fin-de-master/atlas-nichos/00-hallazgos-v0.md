# Atlas v0 — Hallazgos del corpus inicial

## 1. Qué hemos encontrado

El corpus inicial reúne **TFM reales** de repositorios universitarios españoles (acceso abierto), más los ejemplos ya fichados en este repo. Hay concentración clara en:

| Eje | Presencia relativa (v0) |
|-----|-------------------------|
| **Secuencias didácticas / objetos matemáticos** (funciones, álgebra, probabilidad, estadística, trigonometría, proporcionalidad, logaritmos…) | Alta |
| **Tecnología digital**, sobre todo **GeoGebra** | Alta |
| **Metodologías activas** | Media (menor que las secuencias didácticas) |
| **Evaluación** | Media |
| **Modelización** | Baja–media |

**Ejemplos de patrón frecuente**

- TFM de **funciones** que combinan el objeto matemático con GeoGebra y múltiples representaciones; algunos explicitan **modelización**.
- En **estadística**, evolución desde propuestas didácticas tradicionales hacia proyectos, contextos reales, evaluación cooperativa y ciclos tipo **PPDAC**.

## 2. Primera conclusión importante

Empieza a dibujarse una diferencia entre:

### Zona muy poblada

```text
objeto matemático + secuencia didáctica
(+ a menudo GeoGebra o una metodología activa genérica)
```

### Zonas de intersección menos pobladas

```text
objeto matemático + tecnología + cognición
objeto matemático + socioafectivo
matemáticas + IA
matemáticas + videojuegos
matemáticas + razonamiento espacial
matemáticas + metacognición
```

Eso es precisamente lo que busca el Atlas: **no** listar temas, sino **intersecciones**.

La literatura científica reciente refuerza que algunas de esas intersecciones crecen rápido (p. ej. IA generativa en matemáticas desde ~2022–2023) y, a la vez, dejan **huecos** por nivel educativo y por función (enseñar / evaluar / metacognición / diseño instruccional).

## 3. Nicho especialmente interesante: videojuegos → espacial → geometría

La intuición

```text
videojuegos → cognición espacial → matemáticas
```

gana fuerza como **pregunta de investigación**, no como eslogan.

Revisiones recientes sobre intervenciones para el **razonamiento espacial** señalan efectos positivos, pero una **transferencia limitada y dependiente del dominio** hacia el rendimiento matemático general. Eso es más interesante que «hacer un TFM sobre videojuegos».

| Formulación débil | Formulación fuerte |
|-------------------|--------------------|
| TFM sobre videojuegos en mates | Videojuegos y razonamiento espacial como recurso para el aprendizaje de la **geometría** en ESO |
| Actividad lúdica con un juego | ¿Puede una intervención basada en videojuegos mejorar el **razonamiento espacial** y la **transferencia a problemas geométricos** en 2.º/3.º ESO? |

## 4. Gamificación: ya no es nicho virgen

La gamificación en secundaria está **bastante explorada**. Revisiones recientes en matemáticas de secundaria indican, no obstante, que **medida, probabilidad y estadística** siguen relativamente poco exploradas *dentro* de la gamificación, y que muchas experiencias se concentran en práctica individual en el aula.

```text
                 GAMIFICACIÓN
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
     Álgebra       Geometría     Estadística
        │             │             │
     bastante       bastante      menos
     trabajado      trabajado     explorado
                                      │
                                      ↓
                             posible nicho
```

Por tanto, **gamificación + estadística + ESO** suele ser más interesante como intersección que «gamificación + matemáticas» a secas.

## 5. Tercera familia prometedora: IA + metacognición + matemáticas

Líneas de la literatura reciente sobre ChatGPT/IA generativa en educación matemática incluyen: apoyo al aprendizaje, *problem posing*, diseño instruccional y **andamiaje metacognitivo**. En paralelo, meta-análisis de instrucción metacognitiva en matemáticas reúnen decenas de estudios y miles de participantes.

Pregunta alineada con una IA como **herramienta**, no como sustituto del pensamiento:

> ¿Puede utilizarse una IA generativa **no** para resolver el problema, sino para que el alumno **supervise y explique** su propio proceso de resolución?

## 6. Límites de la v0

- N pequeño; sesgo hacia repositorios fácilmente indexables.
- Clasificación temática aún manual y provisional.
- Sin matriz de coocurrencias ni ranking ponderado.

La hoja de ruta está en [01-metodologia.md](01-metodologia.md).
