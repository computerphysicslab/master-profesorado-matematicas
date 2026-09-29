# Aplicaciones prácticas de los números complejos (Bachillerato)

**Asignatura:** Contenidos disciplinares de Matemáticas  
**Nivel:** 1.º Bachillerato (Matemáticas I) — ampliación y motivación  
**Currículo:** los complejos *sí* se estudian; el enfoque oficial suele ser algebraico/geométrico. Esta ficha prioriza el **para qué sirven**.

---

## 1. Situación en el currículo

| Etapa | ¿Complejos? | Notas |
|-------|-------------|-------|
| ESO | No como sistema numérico | Se menciona que $b^2-4ac < 0$ ⇒ sin solución *real* |
| **1.º Bachillerato (Mat. I)** | **Sí** | Binómica, polar, operaciones, Moivre, plano de Argand |
| 2.º Bachillerato | No central de forma obligatoria | Pueden reaparecer en contextos puntuales |

**Aragón (LOMLOE):** Matemáticas I incluye números complejos en binómica y polar entre los saberes de números y álgebra. Ver [temario Mat. I](../../diseno-curricular-e-instruccional-de-matematicas/materiales/temarios-matematicas-aragon/06_matematicas_i_1_bachillerato.md).

El currículo se centra en operatoria y representación. Las **aplicaciones** suelen quedar en segundo plano: conviene explicitarlas para que $i$ no se perciba solo como «número raro».

---

## 2. Por qué merece la pena una unidad / taller de aplicaciones

- Conecta con **Física** (corriente alterna, ondas, fasores).
- Tiene potencia **visual** (fractales, transformaciones en el plano).
- Aparece en **señales**, audio, imagen y control.
- Se puede trabajar con software accesible (GeoGebra, Python, Desmos).
- Refuerza la idea de que ampliar $\mathbb{R}$ no es un capricho formal: resuelve problemas y unifica lenguajes.

---

## 3. Bloques de aplicación motivadores

### 3.1. Rotaciones y transformaciones en el plano

Multiplicar por un complejo de módulo 1 es una **rotación**:

$$z \mapsto e^{i\theta} z = (\cos\theta + i\sin\theta)\, z.$$

- Actividad: rotar polígonos en GeoGebra o con listas en Python.
- Puente natural hacia cuaterniones y rotaciones 3D (ampliación): [hipercomplejos-cuaterniones-videojuegos.md](hipercomplejos-cuaterniones-videojuegos.md).

### 3.2. Fórmula de Euler y «la identidad más bella»

$$e^{i\pi} + 1 = 0$$

Une análisis, trigonometría y la unidad imaginaria. Útil como cierre cultural del bloque (no como demostración exhaustiva en 1.º).

### 3.3. Circuitos de corriente alterna (fasores)

En CA, tensiones e intensidades senoidales se representan como **complejos** (amplitud + fase). La impedancia de resistencias, bobinas y condensadores se escribe de forma compacta y las leyes de Kirchhoff se convierten en álgebra de complejos.

- Nivel: cualitativo + un ejemplo numérico sencillo si el grupo tiene Física.
- Mensaje didáctico: el mismo objeto $a+bi$ sirve para girar vectores y para desfasar señales.

### 3.4. Fractales (Mandelbrot / Julia)

La iteración $z_{n+1} = z_n^2 + c$ en el plano complejo genera el conjunto de Mandelbrot. No exige teoría profunda: basta con la idea de órbita y escape.

- Software: GeoGebra, Python (matplotlib), applets online.
- Interés alto; cuidado con no sustituir el bloque algebraico por solo «imágenes bonitas».

### 3.5. Señales y filtros (idea)

La representación compleja de senoides y la idea de respuesta en frecuencia motivan (a nivel divulgativo) el uso de complejos en audio e imagen. En Bachillerato: semilla, no curso de DSP.

---

## 4. Propuesta de secuencia corta (4–6 sesiones o un taller)

| Fase | Contenido | Producto |
|------|-----------|----------|
| 1 | Recordatorio binómica / polar / producto | Mapa «qué sé hacer con $z$» |
| 2 | Rotaciones en el plano | Construcción GeoGebra o script |
| 3 | Una aplicación física o fractal (elegir según grupo) | Informe breve o póster |
| 4 | Cierre: Euler + «qué queda fuera del currículo» (cuaterniones, 3D) | Debate o mini-demo |

**Criterio:** la operatoria oficial no se sustituye; se **ancla** a un uso.

---

## 5. Errores y precauciones didácticas

| Riesgo | Alternativa |
|--------|-------------|
| Presentar $i$ solo como «raíz de −1» sin geometría | Plano de Argand desde el primer día |
| Aplicaciones sin dominio algebraico mínimo | Primero producto y módulo; después la app |
| Fractales como único contenido | Un taller, no todo el bloque |
| Prometer cuaterniones como si fueran curriculares | Amplificación optativa, honesta con el nivel |

---

## 6. Evaluación orientativa (ampliación)

- Explicar con un dibujo por qué multiplicar por $i$ rota 90°.
- Resolver un producto en polar y traducir el resultado a «escalado + giro».
- Comentar en 8–10 líneas una aplicación (CA, fractal o rotación) con al menos un concepto del temario (módulo, argumento, conjugado…).

---

## 7. Para seguir

- Cuaterniones y videojuegos 3D: [hipercomplejos-cuaterniones-videojuegos.md](hipercomplejos-cuaterniones-videojuegos.md)
- Temario Mat. I Aragón: [06_matematicas_i_1_bachillerato.md](../../diseno-curricular-e-instruccional-de-matematicas/materiales/temarios-matematicas-aragon/06_matematicas_i_1_bachillerato.md)
- Historias matemáticas (ampliación cultural): [`03-materiales/historias-matematicas/`](../../../03-materiales/historias-matematicas/)
