# Euler y los siete puentes de Königsberg

| Campo | Contenido |
|-------|-----------|
| **Nivel** | ESO (2.º–4.º) · Bachillerato (profundización en grafos) |
| **Conceptos** | Grafos, grado de un vértice, camino / circuito euleriano, razonamiento de imposibilidad |
| **Sentidos** | Espacial (relaciones, no medidas), algebraico discreto, razonamiento lógico |
| **Tiempo de aula** | 1 sesión completa (exploración + formalización); ideal con dibujo en la pizarra |

---

## 1. Pregunta generatriz

> En una ciudad hay **siete puentes** que unen orillas e islas. ¿Es posible dar un paseo cruzando **cada puente exactamente una vez**? ¿Y volver al punto de partida?

Antes de contar a Euler: proyecta un esquema de los siete puentes y deja **intentar** rutas (5–10 minutos). La experiencia del bloqueo prepara la idea matemática.

---

## 2. Historia (relato para el aula)

En el s. XVIII, la ciudad prusiana de **Königsberg** (hoy Kaliningrado) estaba atravesada por el río Pregel, con islas y orillas unidas por **siete puentes**. Los habitantes se preguntaban si existía un recorrido que cruzara cada puente una sola vez.

El problema llegó a **Leonhard Euler** (1707–1783), matemático suizo de producción inmensa (análisis, teoría de números, mecánica, notación moderna…). Al principio el enigma le pareció poco «geométrico» en el sentido clásico: no se trataba de medir longitudes ni ángulos, sino de **conexiones**.

Euler comprendió que lo esencial no era el mapa a escala, sino un esquema abstracto:

- cada **zona de tierra** → un punto (vértice);
- cada **puente** → una línea que une dos puntos (arista).

Así nació, en la práctica, el primer resultado de lo que hoy llamamos **teoría de grafos** (y un embrión de la topología: lo que importa es la *conexión*, no la forma exacta).

Su conclusión: **tal paseo es imposible** con la configuración de Königsberg. El argumento no es «lo hemos intentado muchas veces», sino una **demostración** basada en el número de puentes que llegan a cada zona.

El trabajo se presenta en la Academia de San Petersburgo (hacia 1735) y se publica después (*Solutio problematis ad geometriam situs pertinentis*).

**Matiz:** Euler establece con claridad condiciones de *imposibilidad* y la idea central del grado; la formulación moderna completa de existencia de caminos eulerianos se precisó después. En clase basta el criterio que usamos hoy.

---

## 3. Intentos y debate

1. Dibuja el grafo de Königsberg (4 vértices; grados típicos: uno de grado 5 y tres de grado 3, o el esquema estándar con cuatro vértices de grado impar).  
2. Pregunta: al atravesar un puente, ¿cuántas veces «usas» una conexión de una zona?

Idea clave informal:

> Cada vez que **entras** en una zona por un puente, debes **salir** por otro (salvo el inicio y el final del paseo).

Por tanto, en las zonas intermedias el número de puentes debe ser **par**. Como máximo puede haber **dos** zonas con número **impar** de puentes (inicio y final). Si hay **más de dos** vértices de grado impar, el paseo que usa cada arista una vez **no existe**.

En Königsberg hay **cuatro** vértices de grado impar → imposible.

---

## 4. Idea matemática

| Término | Significado escolar |
|---------|---------------------|
| **Grafo** | Puntos unidos por líneas (aquí: tierras y puentes) |
| **Grado** | Número de aristas que tocan un vértice |
| **Camino euleriano** | Recorrido que usa cada arista **exactamente una vez** |
| **Circuito euleriano** | Camino euleriano que **empieza y termina** en el mismo vértice |

**Criterio (versión aula):**

- Circuito euleriano (cerrar el paseo): grafo conexo y **todos** los grados **pares**.  
- Camino euleriano (sin exigir volver): grafo conexo y **exactamente 0 o 2** vértices de grado impar.

---

## 5. Formalización (nivel ESO / Bachillerato)

1. Modelizar un mapa como grafo.  
2. Calcular grados.  
3. Aplicar el criterio.  
4. (Bachillerato) Discutir conexidad; variantes con un puente de más o de menos.

No hace falta la notación avanzada de grafos; sí la **demostración por paridad**.

---

## 6. Problema para el alumnado

**Base**

> Dado el esquema de Königsberg, calcula el grado de cada vértice y concluye si existe camino euleriano. Explica en dos frases el porqué.

**Diseño**

> Añade **un** puente nuevo (eligiendo qué zonas une) de modo que el paseo **sí** sea posible. ¿Y para que sea posible **volver al inicio**?

**Transferencia**

> Un museo tiene salas y pasillos. ¿Se puede recorrer cada pasillo una sola vez? (Proporciona un plano simple.)

**Ampliación**

> Inventa un grafo con circuito euleriano y otro que no lo admita; intercambiadlos con un compañero y clasificadlos.

---

## 7. Criterios LOMLOE (orientación)

Modelizar; conjeturar y **demostrar imposibilidad**; representar; comunicar el argumento; pensamiento «computacional» / discreto (descomponer la situación en vértices y aristas).

---

## 8. Precauciones docentes

- Que el alumnado **intente** rutas antes de oír «es imposible»: si no, el teorema llega vacío.  
- No convertir la sesión en vocabulario de grafos sin el argumento de la paridad.  
- Königsberg histórica ≠ mapa turístico actual: usamos el **problema clásico de siete puentes**.  
- Euler no es solo «el de los puentes»: si hay tiempo, mencionar la amplitud de su obra sin desviar el foco.

---

## 9. Material relacionado en el repo

- [Generatrices y problemas de razonamiento](../../../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/banco-problemas/)  
- [Bloque 8 — Resolución de problemas](../../../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/apuntes/08-resolucion-de-problemas.md)  
- [Catálogo de historias](../indices/catalogo.md)
