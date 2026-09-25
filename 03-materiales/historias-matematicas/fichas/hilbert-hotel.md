# Hilbert y el hotel infinito

| Campo | Contenido |
|-------|-----------|
| **Nivel** | 4.º ESO (versión narrativa + conteos) · Bachillerato (cardinales, biyecciones) |
| **Conceptos** | Infinito numerable; correspondencia biyectiva; $\aleph_0$; «parte = todo» en infinitos |
| **Sentidos** | Numérico; razonamiento |
| **Tiempo** | 1–2 sesiones (relato → casos → formalización → debate) |

---

## 1. Pregunta generatriz

> Un hotel tiene habitaciones numeradas $1, 2, 3, 4, \ldots$ (una por cada natural). **Todas están ocupadas**. Llega un viajero más. ¿Puede el recepcionista alojarlo **sin desalojar** a nadie y **sin construir** habitaciones nuevas?

Variantes que conviene plantear en el mismo bloque:

- ¿Y si llegan **1000** viajeros a la vez?  
- ¿Y si llega un **autobús con infinitos** pasajeros?  
- ¿Y si llegan **infinitos autobuses**, cada uno con infinitos pasajeros?

---

## 2. Historia y sentido de la parábola

**David Hilbert** (1862–1943) —problemas de Hilbert (1900), formalismo, Gotinga— usó el **hotel infinito** como **recurso didáctico** para hacer tangible lo que Cantor había demostrado: el infinito de los naturales se comporta de modo radicalmente distinto al de los conjuntos finitos.

No es un artículo técnico ni una paradoja en el sentido de contradicción lógica. Es una **historia que fuerza una definición**: dos conjuntos tienen el mismo tamaño (cardinal) cuando existe una **biyección** entre ellos. Bajo esa regla, un conjunto infinito puede ponerse en correspondencia con una **parte propia** de sí mismo.

En un hotel finito de 100 habitaciones llenas, un huésped más implica echar a alguien o decir que no hay sitio. En el hotel de Hilbert, **sí hay sitio**… si se acepta reasignar a **infinitos** huéspedes de golpe según una regla clara.

---

## 3. Caso 1 — Un solo huésped nuevo

**Regla:** el ocupante de la habitación $n$ pasa a la $n+1$.

| Antes | Después |
|-------|---------|
| Hab. 1 → huésped A | Hab. 1 → **nuevo** |
| Hab. 2 → huésped B | Hab. 2 → A |
| Hab. 3 → huésped C | Hab. 3 → B |
| … | … |
| Hab. $n$ → … | Hab. $n$ → quien estaba en $n-1$ |

- Nadie se queda sin habitación: quien estaba en $n$ tiene la $n+1$.  
- La habitación 1 queda libre.  
- En términos de conjuntos: $\mathbb{N}$ y $\mathbb{N}\setminus\{1\}$ tienen el **mismo cardinal** (biyección $n \mapsto n+1$).

**Para el aula:** representar en la pizarra solo las primeras 8–10 habitaciones y escribir la regla general. Que el alumnado complete «¿adónde va el de la 7?».

---

## 4. Caso 2 — $k$ huéspedes nuevos ($k$ finito)

**Regla:** el de la habitación $n$ pasa a la $n+k$. Quedan libres $1, 2, \ldots, k$.

Misma lógica: desplazar $k$ posiciones. Funciona para 2, 1000 o un millón de llegadas simultáneas.

---

## 5. Caso 3 — Un autobús con infinitos pasajeros

El hotel sigue lleno. Llega un autobús con asientos $1, 2, 3, \ldots$

**Regla clásica:** el huésped de la habitación $n$ pasa a la **$2n$** (solo pares).

| Habitación | Quién queda |
|------------|-------------|
| 1, 3, 5, 7, … (impares) | **libres** para el autobús |
| 2, 4, 6, 8, … (pares) | antiguos huéspedes (el de $n$ en $2n$) |

Asignación del autobús: el pasajero $j$ → habitación $2j-1$ (la $j$-ésima impar).

**Idea clave:** hay «tantos» números pares como naturales; y «tantos» impares como naturales. Por eso un hotel numerable lleno aún puede absorber **otro** tanto numerable de personas.

$$\lvert \mathbb{N} \rvert = \lvert 2\mathbb{N} \rvert = \lvert \mathbb{N}_{\mathrm{impar}} \rvert = \aleph_0$$

---

## 6. Caso 4 — Infinitos autobuses infinitos

Llegan autobuses $B_1, B_2, B_3, \ldots$; en el autobús $B_i$ viajan pasajeros $1, 2, 3, \ldots$

Hay que alojar un conjunto del tamaño de $\mathbb{N}\times\mathbb{N}$ (pares $(i,j)$).

**Una solución elegante:** usar que $\mathbb{N}\times\mathbb{N}$ es numerable. Por ejemplo, numerar por diagonales (como en la demostración de que $\mathbb{Q}^+$ es numerable):

$$(1,1),\ (1,2),(2,1),\ (1,3),(2,2),(3,1),\ \ldots$$

O con una fórmula explícita (una de varias posibles):

$$(i,j) \mapsto 2^{i}(2j-1)$$

(cada natural se escribe de forma única como potencia de 2 por un impar). Así cada pasajero del autobús $i$ asiento $j$ recibe una habitación distinta y **todas** las habitaciones se pueden usar (o se reubica primero a los antiguos con una regla similar).

**Mensaje:** $\aleph_0 \cdot \aleph_0 = \aleph_0$. El «infinito de los naturales» no crece al multiplicarlo por sí mismo de esta forma.

---

## 7. Formalización (Bachillerato)

1. **Conjuntos finitos:** si $A$ es finito y $a \notin A$, entonces $\lvert A \cup \{a\} \rvert = \lvert A \rvert + 1$. No hay biyección entre $A$ y $A \cup \{a\}$.  
2. **Numerables:** $A$ es numerable (infinito) si existe biyección $A \leftrightarrow \mathbb{N}$.  
3. **Caracterización útil:** un conjunto infinito es numerable ssi es infinito y sus elementos se pueden **listar** sin repetición en una secuencia $a_1, a_2, a_3, \ldots$  
4. **Hilbert resume:** para $A$ numerable, $A \sim A \cup \{x\} \sim A \cup B$ si $B$ es finito o numerable.

El hotel **no** funciona con un «número de habitaciones» igual al de **reales** $(0,1)$: ese cardinal es estrictamente mayor ($\mathfrak{c} = 2^{\aleph_0} > \aleph_0$). Ahí enlaza [Cantor y la diagonal](cantor-infinitos.md).

---

## 8. Intentos, debates y errores productivos

| Intuición frecuente | Matización |
|---------------------|------------|
| «Si está lleno, no cabe nadie» | Cierto en finito; en numerable, «lleno» no impide una reordenación biyectiva |
| «Mover a todos es trampa» | Es exactamente el contenido matemático: una función $f: \mathbb{N}\to\mathbb{N}$ inyectiva no sobreyectiva (caso +1) o biyectiva entre partes |
| «Entonces el infinito es un número enorme» | Mejor: es un **tipo de cardinal**; $\aleph_0$ no se comporta como un natural muy grande |
| «Se pueden alojar los reales igual» | **No** con habitaciones numerables; el argumento diagonal lo prohíbe |

**Debate filosófico breve (opcional):** ¿el hotel «existe»? No. ¿La matemática del conteo infinito es coherente? Sí, dentro de la teoría de conjuntos habitual (ZF, etc.), con más de un siglo de trabajo.

---

## 9. Actividades de aula

**A. Teatro matemático (4.º ESO)**  
10 alumnos = 10 habitaciones «llenas». Llega un 11.º. Con filas finitas **no** hay regla que funcione sin dejar a alguien fuera. Contrastar con el esquema infinito en la pizarra.

**B. Tabla del autobús**  
Columnas: habitación antigua → nueva ($2n$). Filas impares libres → pasajeros del bus.

**C. Reto**  
Inventar una regla para: hotel lleno + 1 autobús infinito + 1 huésped suelto que llegó después.

**D. Escritura**  
«Explica a un compañero de 3.º por qué el hotel puede aceptar un huésped más sin usar la palabra *biyección*.»

---

## 10. Problemas

1. Hotel lleno. Llegan 7 personas. Escribe la regla $n \mapsto \ldots$ y di qué habitaciones quedan libres.  
2. Hotel lleno. Un bus infinito. ¿A qué habitación va el pasajero 15 del bus con la regla de las impares?  
3. Demuestra (nivel Bach.) que la aplicación $n \mapsto 2n$ es una biyección $\mathbb{N} \to 2\mathbb{N}$.  
4. ¿Por qué la estrategia del hotel **falla** si las habitaciones fueran $\{x \in \mathbb{R} : 0 < x < 1\}$? (Una frase enlazando con Cantor.)  
5. (Ampliación) Busca una biyección explícita entre $\mathbb{N}$ y $\mathbb{Z}$.

---

## 11. Criterios LOMLOE (orientación)

Argumentar con ejemplos y contraejemplos; generalizar patrones numéricos; distinguir finito/infinito; comunicar una definición de «mismo número de elementos» más precisa que la intuición cotidiana.

---

## 12. Precauciones docentes

- No presentar el hotel como «paradoja que rompe las matemáticas», sino como **choque de intuición finita con una definición**.  
- Separar claramente: metáfora (hotel) vs teorema (numerabilidad de $\mathbb{N}\times\mathbb{N}$).  
- Evitar decir «infinito + 1 = infinito» como aritmética de instantes sin definir cardinales o cardinales extendidos.  
- Coordinar con [Cantor](cantor-infinitos.md): Hilbert ilustra $\aleph_0$; Cantor muestra que hay infinitos **mayores**.

---

## 13. Material relacionado

- [Cantor y los infinitos](cantor-infinitos.md)  
- [Galois](galois.md) (otro tipo de «límites» del método)  
- [Catálogo](../indices/catalogo.md)
