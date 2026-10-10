# Geometría proyectiva: plano ampliado, dualidad y cónicas

**Asignatura:** Contenidos disciplinares de Matemáticas  
**Bloque de referencia:** Parte 2 (segunda mitad) — Desarrollo de la geometría proyectiva: el plano ampliado, dualidad y cónicas.

> Continúa el hilo de [02-geometria-sintetica-euclides.md](02-geometria-sintetica-euclides.md). La geometría proyectiva nace, en buena medida, del problema de la **perspectiva** y de la necesidad de tratar de forma uniforme las “direcciones” y los puntos del infinito.

---

## 1. El problema que originó la geometría proyectiva

### 1.1. Perspectiva y representación del espacio
En el Renacimiento (Brunelleschi, Alberti, Piero della Francesca, Durero…) se desarrolla la **perspectiva lineal**: representar el espacio tridimensional sobre un plano de modo que las proyecciones de las rectas paralelas se corten en un **punto de fuga**.

Matemáticamente aparece una pregunta natural:

> ¿Cómo tratar de forma unificada las rectas que se cortan “en el infinito” y las que se cortan en un punto propio?

La geometría euclidiana ordinaria no dispone de un lenguaje cómodo para esto: las paralelas “no se cortan”.

### 1.2. De la perspectiva a la geometría
En el siglo XVII, **Girard Desargues** (y más tarde **Blaise Pascal**) desarrollan ideas que hoy reconocemos como proyectivas: teoremas que involucran haces de rectas, puntos de intersección y propiedades que se conservan por proyección.

En el siglo XIX la geometría proyectiva se consolida como disciplina autónoma (Poncelet, Chasles, von Staudt, Möbius, Plücker, Steiner, Cayley…).

---

## 2. El plano proyectivo: idea del plano ampliado

### 2.1. Añadir puntos del infinito
Se amplía el plano euclidiano (afín) añadiendo:

- Un **punto del infinito** por cada dirección de rectas paralelas.
- Una **recta del infinito** que contiene todos esos puntos.

Resultado: **cualquier par de rectas distintas se cortan en exactamente un punto** (si eran paralelas, se cortan en el punto del infinito correspondiente a su dirección).

De forma dual: **cualquier par de puntos distintos determina exactamente una recta**.

### 2.2. Modelo intuitivo
Puede pensarse en el plano proyectivo como el conjunto de **rectas que pasan por el origen** en el espacio tridimensional $\mathbb{R}^3$ (modelo de coordenadas homogéneas). Cada recta por el origen representa un “punto” del plano proyectivo.

Las coordenadas homogéneas $[x:y:z]$ (no todas nulas, y definidas salvo múltiplo escalar no nulo) permiten tratar de forma algebraica tanto los puntos propios como los del infinito ($z=0$).

### 2.3. Por qué importa didácticamente
Aunque el plano proyectivo no suele aparecer de forma explícita en Secundaria, la idea de **punto de fuga** y de “paralelas que se cortan en el infinito” es culturalmente accesible y conecta con:

- Dibujo técnico y perspectiva.
- Geometría analítica (comportamiento asintótico de rectas y cónicas).
- La unificación de casos “especiales” (paralelas vs. secantes).

---

## 3. Principio de dualidad

Uno de los rasgos más característicos de la geometría proyectiva plana:

> Si en un teorema válido se intercambian sistemáticamente las palabras **punto** y **recta** (y las relaciones “pertenece a” / “pasa por”), se obtiene otro teorema válido (el **dual**).

Ejemplos clásicos:

| Afirmación | Dual |
|------------|------|
| Dos puntos distintos determinan una única recta | Dos rectas distintas determinan un único punto |
| Tres puntos no colineales determinan un triángulo | Tres rectas no concurrentes determinan un trilátero |

El principio de dualidad no es un truco de lenguaje: refleja la simetría profunda de la estructura proyectiva. En el plano euclidiano ordinario esta simetría se rompe (las paralelas no se cortan).

**Valor formativo:** muestra que una misma estructura matemática puede leerse de dos maneras equivalentes y que el “objeto primitivo” (punto o recta) no está fijado de antemano.

---

## 4. Cónicas desde el punto de vista proyectivo

### 4.1. Definición proyectiva
Una **cónica** puede definirse de varias maneras equivalentes en el plano proyectivo:

- Lugar de puntos que satisfacen una ecuación homogénea de segundo grado.
- Imagen proyectiva de una circunferencia.
- Generada por haces proyectivos (definición de Steiner), etc.

### 4.2. Clasificación afín vs. proyectiva
En el plano afín (euclidiano) las cónicas no degeneradas se clasifican en:

- Elipse (incluida la circunferencia)
- Parábola
- Hipérbola

En el plano proyectivo **todas las cónicas no degeneradas son proyectivamente equivalentes**: cualquiera puede transformarse en cualquiera otra mediante una proyectividad. La distinción elipse/parábola/hipérbola depende de cómo la cónica corta a la recta del infinito:

| Tipo afín | Intersección con la recta del infinito |
|-----------|----------------------------------------|
| Elipse | No corta (o corta en puntos imaginarios) |
| Parábola | Es tangente a la recta del infinito |
| Hipérbola | Corta en dos puntos reales distintos |

Esta es una de las unificaciones más elegantes de la geometría clásica.

### 4.3. Teoremas emblemáticos
- **Teorema de Pascal** (hexágono inscrito en una cónica): los pares de lados opuestos se cortan en puntos colineales.
- **Teorema de Brianchon** (dual de Pascal): hexágono circunscrito a una cónica; las diagonales que unen vértices opuestos son concurrentes.

Estos teoremas ilustran tanto la potencia de los métodos proyectivos como el principio de dualidad.

---

## 5. Conexión con el currículo de Secundaria y Bachillerato

| Contenido curricular | Puente proyectivo posible |
|----------------------|---------------------------|
| Perspectiva y dibujo técnico | Puntos de fuga = puntos del infinito |
| Cónicas en Bachillerato (Matemáticas II / CCSS) | Clasificación afín; mención de la unificación proyectiva como ampliación |
| Geometría analítica (ecuaciones de cónicas) | Coordenadas homogéneas como ampliación opcional |
| Transformaciones | Homologías, proyectividades (nivel avanzado / optativo) |

**Recomendación didáctica:** no se trata de “enseñar geometría proyectiva” como bloque formal en Secundaria. Sí de:

1. Usar el lenguaje de los puntos de fuga con rigor conceptual.
2. Señalar, cuando se estudien las cónicas, que la distinción elipse/parábola/hipérbola es relativa al “infinito” del plano.
3. Ofrecer (en ampliaciones o trabajos) una visión unificada que muestre la potencia de cambiar de marco geométrico.

---

## 6. Relación con la geometría sintética euclidiana

La geometría proyectiva **no sustituye** a la euclidiana; la amplía y, en cierto sentido, la simplifica:

- Elimina casos especiales (paralelas).
- Introduce una dualidad que la geometría euclidiana no posee.
- Permite demostrar teoremas sobre cónicas de forma más económica.

Al mismo tiempo, la geometría euclidiana recupera la métrica (distancias, ángulos, perpendicularidad) que la proyectiva, en su versión pura, no considera. El programa de Erlangen de Klein (1872) clarificó después que cada geometría se caracteriza por el grupo de transformaciones que la dejan invariante.

---

## 7. Orientaciones para el aula y el TFM

Posibles hilos de trabajo (ampliación, optativa o TFM):

- Construcción de perspectivas y análisis de puntos de fuga en obras de arte o arquitectura.
- Clasificación de cónicas según su corte con la recta del infinito (con GeoGebra).
- Demostración (o exploración) del teorema de Pascal en un caso sencillo.
- Comparación de demostraciones sintéticas vs. analíticas de propiedades de cónicas.

Recursos del repositorio ya existentes que pueden enlazarse:
- Materiales de cónicas y geometría en Diseño curricular.
- Fichas de historias matemáticas relacionadas con perspectiva o cónicas (cuando existan).
- Notebooks o actividades GeoGebra de la carpeta de materiales.

---

## 8. Mapa conceptual breve

```text
Perspectiva renacentista
        ↓
Puntos de fuga / direcciones
        ↓
Plano ampliado (puntos + recta del infinito)
        ↓
Cualquier par de rectas se corta
        ↓
Principio de dualidad (punto ↔ recta)
        ↓
Cónicas unificadas proyectivamente
        ↓
Clasificación afín = posición respecto a la recta del infinito
```

---

## 9. Referencias orientativas

- Coxeter, H. S. M. *Projective Geometry* (clásico accesible).
- Hartshorne, R. *Foundations of Projective Geometry*.
- Stillwell, J. *The Four Pillars of Geometry* (incluye un tratamiento elemental de proyectiva).
- Historias generales ya citadas (Boyer, Katz) para el contexto de Desargues, Poncelet, etc.
- Para el aula: cualquier manual de dibujo técnico que trate la perspectiva cónica con rigor, y actividades GeoGebra sobre cónicas y recta del infinito.

---

## 10. Relación con el resto de la asignatura

- **T-CD-01** (visión histórica): sitúa el origen en la perspectiva y el siglo XVII–XIX.
- **T-CD-02** (Euclides): la geometría proyectiva supera algunas limitaciones del marco euclidiano (paralelismo).
- **T-CD-04** (reflexión curricular): permitirá decidir qué aspectos de este material merecen presencia (aunque sea breve) en la programación de Bachillerato.
- **T-CD-05** (laboratorio de software): GeoGebra es especialmente adecuado para explorar puntos del infinito y cónicas.

---

**Estado del apunte:** primera versión (T-CD-03).  
**Siguiente tarea natural:** T-CD-04 (reflexión y análisis de conceptos del currículo de Secundaria/Bachillerato).
