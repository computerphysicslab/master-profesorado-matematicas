# Fibonacci y el problema de los conejos

| Campo | Contenido |
|-------|-----------|
| **Nivel** | ESO (1.º–3.º; ampliación en 4.º con razón áurea) |
| **Conceptos** | Sucesiones, recurrencia, patrones; opcional: número áureo |
| **Sentidos** | Numérico, algebraico |
| **Tiempo de aula** | 1 sesión (problema → tabla → regla → generalización) |

---

## 1. Pregunta generatriz

> Un hombre pone **una pareja de conejos** en un lugar cerrado. Cada mes, toda pareja **adulta** produce una pareja nueva; las crías tardan **un mes** en ser adultas. ¿Cuántas **parejas** habrá tras 12 meses?

No des la sucesión al inicio: que construyan mes a mes.

---

## 2. Historia (relato para el aula)

**Leonardo de Pisa** (c. 1170 – c. 1240), conocido después como **Fibonacci** («hijo de Bonaccio»), fue matemático y mercader en el mundo mediterráneo medieval. Pasó parte de su juventud en el norte de África (Bugía, hoy Béjaïa), donde conoció el sistema de **numeración indoarábiga** y técnicas de cálculo que circulaban en el islam medieval.

En 1202 publica el ***Liber abaci*** (*Libro del cálculo*), obra decisiva para difundir en Europa:

- las cifras 0–9 y el valor posicional;
- algoritmos de cálculo útiles al comercio (cambios de moneda, precios, repartos…);
- una gran colección de problemas.

Entre ellos figura el **problema de los conejos**, cuya solución genera la sucesión que hoy llamamos de Fibonacci:

$$1,\ 1,\ 2,\ 3,\ 5,\ 8,\ 13,\ 21,\ 34,\ 55,\ \ldots$$

(cada término es la suma de los dos anteriores). En el *Liber abaci* la presentación puede omitir el primer 1; lo esencial es la **regla de recurrencia**.

**Matices honestos:**

- Fibonacci **no inventó** la sucesión en el sentido de que patrones similares aparecen antes en otras tradiciones; su mérito es incluir el problema en un libro que marcó el cálculo europeo y popularizar esa recurrencia.
- El nombre «Fibonacci» se consolidó siglos después; la sucesión fue bautizada así en el s. XIX (Lucas y otros).
- El modelo de los conejos es una **idealización** (no es biología realista): sirve para pensar en recurrencias, no para gestionar una granja.

Lo más importante históricamente del *Liber abaci* no es solo el conejo: es el **cambio de herramienta numérica** (de sistemas engorrosos al cálculo posicional) que transforma el comercio y la enseñanza del número.

---

## 3. Intentos y debate

Construye con la clase una tabla:

| Mes | Parejas adultas | Parejas jóvenes | Total |
|-----|-----------------|-----------------|-------|
| 1 | … | … | … |
| 2 | … | … | … |
| … | | | |

Preguntas:

- ¿Cómo se obtiene el total del mes $n$ a partir de meses anteriores?
- ¿Hace falta listar hasta el mes 12 o hay atajo?

Error productivo: sumar mal adultos/jóvenes; creer que cada mes se duplica el total.

---

## 4. Idea matemática

Sucesión definida por **recurrencia**:

$$
F_1 = 1,\quad F_2 = 1,\quad F_n = F_{n-1} + F_{n-2}\quad (n \geq 3).
$$

(Alternativa: $F_0 = 0$, $F_1 = 1$, misma regla.)

El patrón no es «sumar siempre lo mismo» (no es PA): cada término **depende de los dos previos**.

---

## 5. Formalización (nivel ESO)

1. Tabla hasta $n = 12$ y comprobación del enunciado medieval.  
2. Regla $F_n = F_{n-1} + F_{n-2}$.  
3. Comparar con progresión aritmética y geométrica (¿qué se parece y qué no?).  
4. **Ampliación 3.º–4.º:** cocientes $F_{n+1}/F_n$ → se acercan al **número áureo** $\varphi = \dfrac{1+\sqrt{5}}{2} \approx 1{,}618$.  
5. (Opcional) Apariciones del patrón: espirales aproximadas, mosaicos, pero sin forzar «todo en la naturaleza es Fibonacci».

---

## 6. Problema para el alumnado

**Base**

> Completa los doce primeros términos y responde al problema de los conejos. Explica la regla en una frase.

**Transferencia**

> Define una sucesión con otra regla (p. ej. cada término es la suma de los *tres* anteriores, con tres semillas). Calcula 8 términos.

**Ampliación**

> Calcula $F_{n+1}/F_n$ para $n = 5, 8, 10, 12$. ¿Qué observas? ¿Cómo lo relacionarías con $\varphi$?

**Historia**

> ¿Por qué fue tan importante el *Liber abaci* además del problema de los conejos? (Numeración posicional y cálculo mercantil.)

---

## 7. Criterios LOMLOE (orientación)

Reconocer y generalizar patrones; modelizar una situación simplificada; comunicar la regla de formación; usar la sucesión en problemas.

---

## 8. Precauciones docentes

- No presentar la sucesión como “descubrimiento único de un genio aislado”: contextualizar el **Mediterráneo** y el préstamo cultural de la numeración.  
- El modelo de conejos es didáctico, no empírico.  
- Evitar misticismo del número áureo; si se introduce $\varphi$, con cocientes numéricos y honestidad.

---

## 9. Material relacionado

- [Gauss — patrones y sumas](gauss-suma-1-a-100.md)  
- [Generatrices de patrones / álgebra](../../../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/banco-problemas/generatrices.md)  
- [Catálogo](../indices/catalogo.md)
