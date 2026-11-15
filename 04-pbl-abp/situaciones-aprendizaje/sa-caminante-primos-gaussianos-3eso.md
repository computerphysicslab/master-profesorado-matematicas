---
layout: default
title: "SA: El caminante de los primos gaussianos"
nav_order: 43
parent: Situaciones de aprendizaje
---

# SA — El caminante de los primos gaussianos: cuando la aritmética dibuja

> Situación de aprendizaje de indagación matemática en la que una regla aritmética clasifica puntos de una cuadrícula y gobierna los giros de un caminante. Integra divisibilidad, coordenadas, Pitágoras, simetría, algoritmos y pensamiento crítico ante resultados virales.

## 0. Metadatos

| Campo | Contenido |
|-------|-----------|
| **Título de la SA** | El caminante de los primos gaussianos: cuando la aritmética dibuja |
| **Nivel / curso** | 3.º ESO (Matemáticas) · adaptable a 4.º ESO |
| **Duración** | 7 sesiones × 55 min (ampliable a 8 con programación y exposición) |
| **Autor/a de la ficha** | Material del repositorio |
| **Fecha / versión** | 2026-11-15 · v1.0 |
| **Contexto de uso** | Diseño curricular / Practicum / indagación matemática / pensamiento computacional |
| **Áreas** | Matemáticas · Tecnología / Computación (conexión opcional) |

**Palabras clave:** números primos, enteros gaussianos, suma de cuadrados, coordenadas, Pitágoras, simetría, autómata, algoritmo, Python, conjetura

---

## 1. Pregunta guía / reto

> ¿Puede una regla basada únicamente en la divisibilidad de los números hacer que un caminante recorra una cuadrícula y dibuje una trayectoria inesperada? ¿Podemos explicar, comprobar y modificar matemáticamente ese comportamiento?

**Producto final esperado:**

Cada equipo construirá y documentará un **caminante aritmético**. Entregará:

1. Una definición comprensible de la regla que gobierna el movimiento.
2. Una cuadrícula con los puntos clasificados y la trayectoria del caminante.
3. Un registro de los primeros movimientos y una representación de una ejecución más larga (manual, hoja de cálculo o Python).
4. Dos conjeturas sobre el comportamiento observado, acompañadas de pruebas, contraejemplos o límites explícitos.
5. Una explicación pública breve (póster, infografía o exposición de 3–5 minutos) que distinga lo que se ha observado de lo que se ha demostrado.

**Condición de rigor:** el dibujo no es el objetivo matemático principal. La evidencia central será que el equipo pueda justificar la clasificación de los puntos y explicar cómo esa clasificación determina cada giro.

---

## 2. Justificación y sentido educativo

La propuesta parte de un fenómeno visual atractivo: un caminante se desplaza por una cuadrícula de puntos enteros y gira cuando alcanza una posición que satisface una condición de primalidad. La regla local es sencilla; la trayectoria global puede resultar difícil de anticipar. Esta diferencia entre regla y resultado permite convertir una imagen llamativa en una investigación matemática.

El fundamento es la aritmética de los **enteros gaussianos**. Un punto de coordenadas enteras \((a,b)\) se puede asociar al número \(a+bi\), y su norma es:

\[
N(a+bi)=a^2+b^2.
\]

La norma conecta la divisibilidad con el teorema de Pitágoras: es el cuadrado de la distancia del punto al origen. Para puntos fuera de los ejes, la primalidad gaussiana se puede reconocer comprobando si \(a^2+b^2\) es un primo ordinario. En los ejes hay una excepción que debe explicitarse: los elementos \(p\), \(pi\) y sus asociados son primos gaussianos cuando \(p\) es un primo ordinario congruente con 3 módulo 4. Esta distinción evita que el algoritmo escolar aplique una regla incompleta.

La situación es adecuada para 3.º ESO si se presenta la norma como suma de cuadrados y se trabaja con coordenadas, divisibilidad y algoritmos; **no es necesario introducir formalmente los números complejos ni construir el anillo \(\mathbb Z[i]\)**. En 4.º ESO puede añadirse una ampliación sobre el plano complejo y la factorización. El docente debe decidir si el objetivo es una primera exploración geométrico-aritmética o una introducción formal a los primos gaussianos.

El valor didáctico no reside en prometer que toda trayectoria se cierre o que aparezca una figura determinada. Reside en investigar qué depende de la regla, qué depende de las condiciones iniciales y qué afirmaciones requieren una demostración o una comprobación computacional reproducible.

**Conexión con otras SA del repositorio:** [Eratóstenes](sa-eratostenes-3eso.md) (primalidad y método); [Falacia \(\pi=4\)](sa-falacia-pi-4-4eso.md) (argumentación ante imágenes persuasivas); [Constantes matemáticas](sa-constantes-matematicas-4eso.md) (ampliación de conceptos numéricos).

---

## 3. Objetivos de aprendizaje

1. Clasificar números naturales como primos o compuestos y justificar la decisión mediante divisibilidad.
2. Interpretar parejas de coordenadas enteras y calcular \(a^2+b^2\), relacionando el resultado con la distancia al origen.
3. Reconocer simetrías de la condición \(a^2+b^2\) al cambiar signos o intercambiar coordenadas.
4. Describir un procedimiento determinista mediante estados, instrucciones, condicionales y repeticiones.
5. Construir, ejecutar y depurar una simulación sencilla del caminante, manualmente o con una herramienta digital.
6. Formular conjeturas sobre la trayectoria y distinguir entre observación finita, evidencia computacional y demostración matemática.
7. Comunicar el procedimiento y sus resultados con representaciones, vocabulario y argumentos comprensibles.

---

## 4. Competencias específicas y criterios de evaluación

> La tabla emplea la síntesis de competencias utilizada en otras fichas del repositorio. Antes de utilizarla como programación oficial, se deben seleccionar y transcribir los criterios concretos del curso en el anexo de Matemáticas de Aragón (Orden ECD/1172/2022 y modificación ECD/867/2024).

| CE (síntesis) | Criterios prioritarios | Evidencia principal en esta SA |
|---------------|------------------------|-------------------------------|
| **CE1–CE2** Resolución de problemas | Interpretar el reto, seleccionar estrategias, ejecutar y revisar procedimientos; comprobar resultados | Registro de movimientos, cálculos de normas y depuración de la simulación |
| **CE3** Razonamiento y prueba | Formular conjeturas, buscar regularidades, justificar la clasificación y examinar contraejemplos | Cuaderno de investigación y explicación de las conjeturas |
| **CE4** Pensamiento computacional | Descomponer el proceso, diseñar instrucciones ordenadas, detectar errores y evaluar el algoritmo | Diagrama de flujo, pseudocódigo o programa comentado |
| **CE5–CE6** Conexiones y modelización | Relacionar divisibilidad, suma de cuadrados, distancia y movimiento; interpretar el modelo | Explicación de la norma y de su función en el autómata |
| **CE7–CE8** Representación y comunicación | Usar coordenadas, tablas, esquemas y lenguaje matemático para comunicar el proceso | Mapa de puntos, trayectoria y exposición |
| **CE9–CE10** Socioafectivas | Perseverar, gestionar el error, cooperar y revisar las propias ideas | Observación del trabajo, coevaluación y reflexión individual |

**Competencia protagonista:** CE3 (razonamiento y prueba), con CE4 (pensamiento computacional) como competencia de apoyo relevante.

**Competencias clave:** STEM, CD, CCL, CPSAA y CCEC.

---

## 5. Saberes básicos y sentidos matemáticos

| Sentido | Saberes / contenidos | Prioridad |
|---------|----------------------|----------|
| Numérico | Números naturales; primos y compuestos; divisibilidad; múltiplos; resto de una división; primalidad | Alta |
| Espacial | Plano cartesiano; coordenadas enteras; desplazamientos; simetrías respecto de ejes y diagonales | Alta |
| De la medida | Cuadrados de longitudes; distancia al origen; interpretación geométrica de \(a^2+b^2\) | Media–Alta |
| Algebraico | Expresiones \(a^2+b^2\); reglas condicionales; sucesión de estados; invariantes sencillos | Media |
| Socioafectivo | Perseverancia; gestión del error; tolerancia a la incertidumbre; cooperación y revisión de conjeturas | Alta |
| Estocástico | N/A: el sistema es determinista, no aleatorio. Puede introducirse una comparación con procesos aleatorios como extensión | Baja |

**Conexiones interdisciplinares:** Tecnología (algoritmos y programación); Física (posición, dirección y desplazamiento); Educación plástica (composición visual y patrones); Lengua (comunicación argumentada y exposición).

### Precisión matemática para el docente: ¿qué significa «primo gaussiano»?

Los enteros gaussianos son los números \(a+bi\), con \(a,b\in\mathbb Z\) e \(i^2=-1\). En este dominio, las unidades son \(1,-1,i,-i\). Un primo gaussiano es un elemento no nulo, no unidad, que no admite una factorización en dos no unidades.

Para clasificar los puntos de la cuadrícula se puede utilizar este criterio:

- **Si \(a\ne0\) y \(b\ne0\):** \(a+bi\) es primo gaussiano si y solo si \(a^2+b^2\) es primo ordinario.
- **Si el punto está en un eje:** \(a+0i\) o \(0+bi\) es primo gaussiano cuando el valor absoluto de su coordenada no nula es un primo ordinario congruente con \(3\pmod 4\).
- **El origen y las unidades** no son primos gaussianos.

Ejemplos:

| Punto \((a,b)\) | Norma \(a^2+b^2\) | Clasificación |
|-----------------|-------------------:|---------------|
| \((1,1)\) | 2 | Primo gaussiano |
| \((1,2)\) | 5 | Primo gaussiano |
| \((2,3)\) | 13 | Primo gaussiano |
| \((2,2)\) | 8 | No es primo gaussiano |
| \((3,4)\) | 25 | No es primo gaussiano |
| \((3,0)\) | 9 | Primo gaussiano por la regla especial de los ejes |
| \((5,0)\) | 25 | No es primo gaussiano |
| \((0,7)\) | 49 | Primo gaussiano por la regla especial de los ejes |

La norma es invariante al cambiar signos o intercambiar coordenadas. Por eso el conjunto de primos gaussianos presenta simetrías respecto de los ejes y las diagonales. **La trayectoria del caminante no tiene por qué heredar todas esas simetrías**, porque la regla de girar a la izquierda distingue un sentido de giro.

---

## 6. Secuencia de aprendizaje

| Sesión | Fase | Actividad del alumnado | Rol docente | Agrupamiento |
|--------|------|------------------------|-------------|--------------|
| **1** | Activación / reto | Observan una trayectoria o una animación sin conocer la regla. Describen qué ven, proponen explicaciones y registran una predicción individual: «¿qué información necesita la máquina para decidir el siguiente movimiento?» | Presentar el fenómeno sin revelar la regla; recoger ideas y separar observación de explicación | Individual → grupo-clase |
| **2** | Exploración aritmética | Repasan primos y compuestos. En una cuadrícula, toman puntos \((a,b)\), calculan \(a^2+b^2\) y comprueban si el resultado es primo. Comparan, por ejemplo, \((1,2)\), \((2,3)\) y \((3,4)\) | Modelar un ejemplo y ayudar a identificar errores de cálculo o de primalidad | Parejas |
| **3** | Construcción geométrica | Representan puntos que cumplen la condición. Cambian signos e intercambian coordenadas; buscan simetrías. Relacionan la norma con el cuadrado de la distancia al origen mediante Pitágoras | Guiar la conexión entre cálculo, distancia y simetría; introducir la excepción de los ejes en una ficha graduada | Equipos de 3–4 |
| **4** | Formalización de la regla | Definen el estado del caminante: posición \((x,y)\) y dirección. Simulan manualmente 15–20 pasos. Tras avanzar una casilla, comprueban si el punto de llegada es primo gaussiano; si lo es, giran 90° a la izquierda | Asegurar que todos usan la misma convención temporal y registrar el estado completo, no solo la posición | Parejas → equipos |
| **5** | Algoritmo y simulación | Elaboran pseudocódigo o diagrama de flujo. Quienes tengan recursos digitales ejecutan una simulación en hoja de cálculo o Python. Comparan los primeros pasos manuales con los del programa | Facilitar una plantilla de código y ayudar a depurar; pedir que se compruebe la clasificación en puntos de los ejes | Equipos |
| **6** | Investigación y contraste | Cambian una sola condición cada vez: giro a la derecha, dirección inicial, punto inicial o regla de clasificación. Formulan dos conjeturas y buscan evidencia, contraejemplos o límites | Exigir que cada afirmación indique las condiciones iniciales y el número de pasos explorados | Equipos |
| **7** | Comunicación y metacognición | Presentan el autómata, sus reglas, una trayectoria y una conjetura. Explican qué han demostrado, qué solo han observado y qué no han podido concluir. Autoevalúan el proceso | Moderar la exposición, valorar la argumentación y cerrar con una síntesis de aritmética, geometría y algoritmo | Grupo-clase |

**Hito intermedio (sesión 4):** tabla de al menos 15 estados consecutivos con posición, dirección, condición de primalidad y acción. La tabla debe permitir que otro equipo reproduzca exactamente el recorrido.

---

## 7. Metodología y organización

- **Enfoque:** indagación matemática guiada + resolución de problemas + pensamiento computacional. El producto visual sirve como medio de investigación, no como sustituto del razonamiento.
- **Agrupamientos:** equipos heterogéneos de 3–4. Roles rotatorios: responsable de cálculos, cartógrafo/a, verificador/a del algoritmo y portavoz.
- **Espacios:** aula ordinaria; aula de informática si se programa; exposición final en el aula o pasillo.
- **Materiales:** papel cuadriculado, lápices de colores, regla, calculadora, tarjetas con coordenadas, ficha de registro; ordenador opcional con Python, GeoGebra o una hoja de cálculo.
- **Organización del trabajo:** cada equipo conserva un registro de las reglas y de las condiciones iniciales. Si modifica varias cosas simultáneamente, no podrá atribuir con claridad el cambio de trayectoria a una sola causa.

### Convención del autómata que se utilizará en clase

Para evitar ambigüedades, la versión común de la SA se define así:

1. La cuadrícula contiene todos los puntos \((x,y)\) con coordenadas enteras.
2. El estado es \((x,y,d_x,d_y)\), donde \((d_x,d_y)\) es uno de los cuatro vectores cardinales: \((1,0)\), \((0,1)\), \((-1,0)\) o \((0,-1)\).
3. En cada iteración, el caminante avanza una unidad: \((x,y)\leftarrow(x+d_x,y+d_y)\).
4. Se clasifica el **punto de llegada**. Si es primo gaussiano, gira 90° a la izquierda: \((d_x,d_y)\leftarrow(-d_y,d_x)\). Si no lo es, conserva la dirección.
5. Se dibuja el segmento recorrido y se registra el nuevo estado.

La posición inicial y la dirección inicial deben anotarse siempre. Para la exploración común se puede elegir \((0,0)\) y dirección Este \((1,0)\), pero esa elección es una convención didáctica, no una propiedad intrínseca del sistema.

### Pseudocódigo de referencia

```text
posición ← (0, 0)
dirección ← (1, 0)          # Este

REPETIR N veces:
    posición ← posición + dirección

    SI es_primo_gaussiano(posición):
        dirección ← giro_izquierda_90(dirección)

    dibujar_segmento
    registrar_estado
```

**Nota:** la función `es_primo_gaussiano` debe aplicar los dos casos del criterio de la sección 5. No basta con comprobar que \(a^2+b^2\) es primo cuando el punto está en un eje.

---

## 8. Evaluación

> [Instrumentos](../../07-evaluacion/instrumentos/) · [Rúbricas](../../07-evaluacion/rubricas/) · [Alineación criterio–tarea–evidencia](../../07-evaluacion/ejemplos/alineacion-criterio-tarea-evidencia.md).

### 8.1. Evaluación formativa

- [x] Ticket de entrada: predicción individual sobre la regla.
- [x] Observación del proceso y de la participación en el equipo.
- [x] Lista de cotejo de cálculos de norma y clasificación de puntos.
- [x] Revisión de la tabla de estados antes de programar.
- [x] Comparación entre simulación manual y digital.
- [x] Autoevaluación de cierre y coevaluación del producto.
- [ ] Audio 60–90 s (opcional): explicación individual de una decisión del algoritmo.

**Feedback:**
- *Feed-up* (sesión 1): qué debe explicar el producto final.
- *Feed-back* (sesiones 2–5): corrección de cálculos, clasificación y transiciones.
- *Feed-forward* (sesión 6): cómo mejorar la conjetura y documentar las condiciones de la prueba.

### 8.2. Evaluación sumativa del producto

| Criterio | Indicadores orientativos | Peso |
|----------|--------------------------|------|
| Comprensión aritmética | Calcula correctamente \(a^2+b^2\), identifica primos y aplica la regla de los ejes cuando corresponde | 25 % |
| Comprensión geométrica | Sitúa puntos, interpreta desplazamientos y explica las simetrías de la clasificación | 15 % |
| Algoritmo y reproducibilidad | Describe estados, orden de operaciones y condiciones iniciales; el recorrido puede reproducirse | 20 % |
| Razonamiento y prueba | Formula conjeturas, aporta evidencia y distingue observación de demostración | 25 % |
| Comunicación y proceso cooperativo | Presenta con claridad y documenta aportaciones, revisión y gestión de errores | 15 % |

**Alineación:** no se premia la trayectoria más larga ni el dibujo más vistoso. La calificación debe reflejar la corrección matemática, la reproducibilidad y la calidad del razonamiento.

### 8.3. Autoevaluación y coevaluación

Cada estudiante responde individualmente:

- ¿Puedo explicar por qué un punto concreto se clasifica como primo gaussiano?
- ¿Puedo reconstruir el estado del caminante y justificar el siguiente movimiento?
- ¿Qué error detecté y cómo lo corregí?
- ¿Qué afirmación de nuestro equipo está demostrada y cuál solo hemos observado en una ejecución finita?
- ¿He escuchado y utilizado las comprobaciones de mis compañeros?

Coevaluación: otro equipo intenta reproducir los primeros 15 pasos con la ficha recibida. Si no puede hacerlo, debe señalar qué dato o regla falta.

---

## 9. Atención a la diversidad y DUA

| Principio DUA | Medida concreta en esta SA |
|---------------|----------------------------|
| Múltiples formas de **implicación** | Fenómeno visual como reto; elección entre roles; posibilidad de proponer una variante propia sin alterar la versión común |
| Múltiples formas de **representación** | Cuadrícula física, tabla de coordenadas, flechas de dirección, diagrama de flujo, pseudocódigo y simulación |
| Múltiples formas de **acción y expresión** | Registro escrito, construcción manual, programa, póster o exposición oral; plantilla de estados con parte de las columnas completadas |

**Refuerzo:**
- Limitar inicialmente la cuadrícula a coordenadas entre \(-4\) y \(4\).
- Proporcionar una tabla de números primos y una ficha para calcular cuadrados.
- Trabajar primero con puntos fuera de los ejes y presentar la regla especial de los ejes mediante ejemplos guiados.
- Dar una tabla de estados parcialmente completada y flechas recortables para representar giros.
- Permitir que el equipo siga una ejecución manual sin tener que programar.

**Ampliación:**
- Implementar una función de primalidad eficiente y comparar su coste con la división por todos los enteros menores.
- Estudiar la norma y la factorización en \(\mathbb Z[i]\) de forma introductoria.
- Comparar giros de 90° con otras reglas deterministas.
- Investigar si el sistema vuelve al mismo **estado completo** (posición y dirección), no solo si vuelve a pasar por el origen.

---

## 10. Dimensión socioafectiva

| Elemento | Manifestación observable en la SA |
|----------|-----------------------------------|
| Perseverancia | Revisar una trayectoria cuando un paso no coincide con el registro del equipo |
| Gestión del error | Localizar si el fallo está en el cálculo de la norma, en la clasificación del punto o en el orden de las instrucciones |
| Flexibilidad cognitiva | Modificar una hipótesis cuando aparece un contraejemplo o una nueva condición |
| Cooperación | Repartir cálculos, comprobar resultados ajenos y documentar acuerdos |
| Autoconcepto matemático | Reconocer que una explicación reproducible es un logro aunque el dibujo no sea espectacular |
| Humildad epistémica | No convertir una observación de 500 o 10 000 pasos en una afirmación universal |

Registro: observación docente, coevaluación de reproducibilidad y reflexión individual final.

---

## 11. Orientaciones para la implementación

### Dificultades previsibles

- **Confundir primo ordinario y primo gaussiano.** La primalidad de \(a^2+b^2\) es un criterio directo para puntos fuera de los ejes; los ejes requieren la condición \(p\equiv3\pmod4\).
- **Olvidar las unidades.** \(1,-1,i,-i\) no son primos gaussianos. En la cuadrícula, el origen tampoco se clasifica como primo.
- **Confundir punto con estado.** Para saber si el caminante ha regresado al inicio hay que recuperar posición y dirección, no solo pasar por la misma coordenada.
- **Cambiar varias reglas a la vez.** Impide saber qué modificación ha producido el efecto observado.
- **Confundir simetría del conjunto con simetría del recorrido.** La clasificación de puntos es simétrica; una regla de giro a la izquierda introduce orientación.
- **Afirmar periodicidad sin prueba.** Una simulación finita solo demuestra lo ocurrido durante los pasos ejecutados.

### La afirmación viral de los «39 212 pasos»

Si el material de partida afirma que el caminante regresa al punto inicial tras 39 212 pasos, esa cifra debe tratarse como una **afirmación por verificar**, no como un hecho matemático ya establecido. Para comprobarla hacen falta, como mínimo:

- posición inicial;
- dirección inicial;
- definición exacta de primo gaussiano;
- si se comprueba el punto al llegar o antes de salir;
- sentido y ángulo del giro;
- si «regresar» significa recuperar solo la posición o el estado completo (posición y dirección).

En una prueba exploratoria con una convención concreta —origen, dirección Este, avance unitario, comprobación del punto de llegada y giro a la izquierda— se obtuvo un ciclo de 64 pasos en la ejecución de referencia. Este dato **no valida ni refuta por sí solo** los 39 212 pasos: las condiciones del vídeo pueden ser diferentes. La actividad debe reproducir primero las reglas exactas antes de comparar cifras.

### Variantes

- **Versión corta (4 sesiones):** sin programación; cuadrícula pequeña, clasificación de puntos, simulación manual y exposición.
- **Versión estándar (7 sesiones):** secuencia completa de esta ficha, con programación opcional.
- **Versión ampliada (8–9 sesiones):** implementación Python, comparación de condiciones iniciales y análisis del ciclo de estados.
- **Variante 4.º ESO:** introducir notación compleja \(a+bi\), norma y una primera discusión de factorización en los enteros gaussianos.

### Precisión didáctica

No presentar la actividad como un ejemplo de «caos»: el algoritmo descrito es determinista. Tampoco afirmar que el resultado es aleatorio o que toda trayectoria debe cerrarse. Es preferible hablar de **comportamiento emergente de una regla determinista** y estudiar las condiciones bajo las que se observan ciclos.

---

## 12. Referencias

### Normativa

- [Real Decreto 217/2022, de 29 de marzo](https://www.boe.es/buscar/act.php?id=BOE-A-2022-4975), por el que se establece la ordenación y las enseñanzas mínimas de la ESO.
- Aragón: [Orden ECD/1172/2022](https://educa.aragon.es/) y modificación [Orden ECD/867/2024](https://educa.aragon.es/). Comprobar en el texto consolidado los criterios del curso y la redacción vigente antes de incorporar esta ficha a una programación oficial.

### Matemáticas: enteros gaussianos y primos

1. Weisstein, E. W. [“Gaussian Integer”](https://mathworld.wolfram.com/GaussianInteger.html), *Wolfram MathWorld*.
2. Weisstein, E. W. [“Gaussian Prime”](https://mathworld.wolfram.com/GaussianPrime.html), *Wolfram MathWorld*. Clasificación de primos gaussianos y casos de los ejes.
3. Cox, D. A. (2012). *Primes of the Form \(x^2+ny^2\)* (2.ª ed.). Wiley. Referencia avanzada para profundizar en representación de primos mediante formas cuadráticas.
4. Hardy, G. H. y Wright, E. M. (2008). *An Introduction to the Theory of Numbers* (6.ª ed.). Oxford University Press. Contexto general de teoría de números.

### Pensamiento computacional y didáctica

5. Wing, J. M. (2006). “Computational Thinking”. *Communications of the ACM*, 49(3), 33–35. https://doi.org/10.1145/1118178.1118215
6. Papert, S. (1980). *Mindstorms: Children, Computers, and Powerful Ideas*. Basic Books.

### Materiales del repositorio

- [Plantilla de situaciones de aprendizaje](plantilla-situacion-aprendizaje.md).
- [SA — Eratóstenes](sa-eratostenes-3eso.md): primalidad, investigación y modelización.
- [SA — ¿Es \(\pi\) igual a 4?](sa-falacia-pi-4-4eso.md): argumentación y contraste de afirmaciones visuales.
- [SA — Constantes matemáticas](sa-constantes-matematicas-4eso.md): ampliación de conceptos numéricos.
- [Instrumentos de evaluación](../../07-evaluacion/).
- [Temarios de Matemáticas de Aragón](../../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/temarios-matematicas-aragon/).

---

## 13. Anexo — Guía técnica para el docente

### A. Función de clasificación

La siguiente implementación de referencia ilustra el criterio matemático. Está escrita para que el docente pueda probar la regla; no es necesario que el alumnado la programe completa.

```python
from math import isqrt

def es_primo(n: int) -> bool:
    """Primalidad ordinaria para enteros positivos."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True

def es_primo_gaussiano(a: int, b: int) -> bool:
    """Clasifica a + bi en Z[i], salvo el caso cero y las unidades."""
    if a == 0 and b == 0:
        return False

    # Puntos fuera de los ejes: la norma debe ser primo ordinario.
    if a != 0 and b != 0:
        return es_primo(a*a + b*b)

    # Puntos en los ejes: |coordenada| debe ser primo 3 módulo 4.
    p = abs(a) if b == 0 else abs(b)
    return es_primo(p) and p % 4 == 3
```

Comprobaciones mínimas:
- `es_primo_gaussiano(1, 1)` → `True` (norma 2).
- `es_primo_gaussiano(2, 3)` → `True` (norma 13).
- `es_primo_gaussiano(3, 4)` → `False` (norma 25).
- `es_primo_gaussiano(3, 0)` → `True` (caso especial del eje).
- `es_primo_gaussiano(5, 0)` → `False` (5 no es 3 módulo 4).
- `es_primo_gaussiano(1, 0)` → `False` (unidad).

### B. Simulación reproducible

```python
def caminar(n_pasos=1000, inicio=(0, 0), direccion=(1, 0)):
    x, y = inicio
    dx, dy = direccion
    estados = [(x, y, dx, dy)]

    for _ in range(n_pasos):
        x += dx
        y += dy

        if es_primo_gaussiano(x, y):
            dx, dy = -dy, dx  # giro de 90 grados a la izquierda

        estados.append((x, y, dx, dy))

    return estados
```

El estado se almacena como `(x, y, dx, dy)`. Para detectar un ciclo, se debe buscar la repetición de un estado completo, no únicamente de una posición. Si se quiere afirmar que el caminante vuelve al estado inicial, hay que comprobar que reaparece exactamente `(x_inicial, y_inicial, dx_inicial, dy_inicial)`.

### C. Preguntas de investigación posibles

1. ¿Qué puntos de la cuadrícula son primos gaussianos y cuáles no? ¿Cómo se justifica cada clasificación?
2. ¿Por qué los puntos \((a,b)\), \((-a,b)\), \((a,-b)\) y \((b,a)\) tienen la misma norma?
3. ¿La trayectoria conserva las simetrías del conjunto de puntos? ¿Qué papel desempeña el sentido de giro?
4. ¿Qué diferencia hay entre volver al origen y volver al mismo estado?
5. ¿Qué evidencias permiten afirmar que una ejecución es periódica?
6. ¿Cómo cambia la trayectoria si se gira a la derecha en vez de a la izquierda?
7. ¿Qué parte del resultado depende de la aritmética y cuál de la convención elegida para el autómata?

**Idea de cierre:** una regla sencilla no elimina la necesidad de razonar. Al contrario: cuanto más sorprendente sea el resultado, más importante es especificar el modelo, reproducirlo y justificar las conclusiones.
