# Pierre de Fermat: números, margen y método

| Campo | Contenido |
|-------|-----------|
| **Nivel** | ESO (potencias, Pitágoras, idea de conjetura) · Bachillerato (último teorema, descenso, probabilidad) |
| **Conceptos** | Potencias, ecuaciones diofánticas, demostración / conjetura; opcional: probabilidad (con Pascal) |
| **Sentidos** | Numérico, algebraico; razonamiento |
| **Tiempo de aula** | 1 sesión (retrato de la obra + problema) o 2 si se enlaza con Sophie Germain / Pascal |

---

## 1. Pregunta generatriz

> Sabemos que hay infinitos triples con $x^2+y^2=z^2$ (Pitágoras). ¿Habrá enteros positivos con $x^3+y^3=z^3$? ¿Y con exponente $n>2$?

O:

> Un matemático anota en el margen de un libro: «tengo una demostración maravillosa, pero el margen es demasiado estrecho». ¿Qué valor tiene una afirmación así *sin* la prueba escrita?

---

## 2. Historia y obra (relato para el aula)

**Pierre de Fermat** (1601/1607–1665), jurista en el Parlamento de Toulouse, dedicó su tiempo libre a las matemáticas. Publicó poco; avanzó sobre todo por **cartas** y notas. Con Descartes, es una de las figuras centrales de la primera mitad del s. XVII.

### Campos principales

| Campo | Aporte (síntesis) |
|-------|-------------------|
| **Teoría de números** | Núcleo de su legado: primos, sumas de cuadrados, ecuaciones diofánticas |
| **Último teorema** | $x^n+y^n=z^n$ sin soluciones enteras positivas si $n>2$ (demostrado por Wiles, 1994–95) |
| **Pequeño teorema** | Si $p$ es primo y $a$ entero, $p$ divide a $a^p-a$ (base de mucha aritmética modular) |
| **Descenso infinito** | Método de imposibilidad: de una solución se construye otra *menor* → contradicción |
| **Geometría analítica** | Independientemente de Descartes, métodos de coordenadas, tangentes, máximos y mínimos |
| **Probabilidad** | Correspondencia con **Pascal** (1654): problema de los puntos / partidas interrumpidas |
| **Óptica** | Principio de Fermat: la luz sigue caminos de tiempo extremal |

### El margen de Diofanto

En su ejemplar de la *Arithmetica* de Diofanto, Fermat escribió que no existen soluciones enteras positivas de $x^n+y^n=z^n$ para $n>2$, y que tenía una «demostración admirable» que no cabía en el margen. **No se ha encontrado** esa prueba general. Sí demostró el caso $n=4$ (vía descenso infinito, ligado a resultados sobre triángulos rectángulos de área cuadrada). Para el caso general hicieron falta herramientas del s. XX.

**Lectura honesta en clase:** la nota del margen es el origen de tres siglos de trabajo; no prueba que Fermat dispusiera de una demostración correcta del caso general.

### Enlace con Sophie Germain

Germain y otros obtuvieron resultados **parciales** hacia el último teorema. La ficha [Sophie Germain](sophie-germain.md) complementa esta.

---

## 3. Intentos y debate

- Buscad triples pitagóricos; intentad $n=3$ con números pequeños.  
- ¿Qué diferencia hay entre «no lo he encontrado» y «he demostrado que no existe»?  
- ¿Por qué el caso $n=4$ es más accesible históricamente que el general?

---

## 4. Ideas matemáticas nucleares

**Último teorema (enunciado):** no hay enteros $x,y,z \neq 0$ y $n>2$ con $x^n+y^n=z^n$.

**Pequeño teorema (formulación escolar):** si $p$ es primo, entonces $a^p \equiv a \pmod p$ para todo entero $a$ (o, si $p\nmid a$, $a^{p-1}\equiv 1 \pmod p$).

**Descenso infinito (idea):** suponer una solución positiva mínima y fabricar otra estrictamente menor en enteros positivos → imposible.

---

## 5. Formalización según nivel

**ESO**

1. Potencias y comparación $n=2$ vs $n>2$.  
2. Exploración numérica (no es demostración).  
3. Idea de conjetura vs teorema demostrado.

**Bachillerato**

1. Enunciado preciso del último teorema y del caso $n=4$.  
2. Esquema del descenso (sin la prueba completa).  
3. (Opcional) Enunciado del pequeño teorema y un ejemplo numérico.  
4. (Opcional) Problema de los puntos con Pascal — otra ficha prevista.

---

## 6. Problema para el alumnado

**Base**

> Encuentra tres triples pitagóricos distintos. ¿Encuentras enteros positivos con $x^3+y^3=z^3$? ¿Qué puedes *afirmar* con rigor tras buscar?

**Pequeño teorema**

> Comprueba que $7$ divide a $2^7-2$. ¿Y a $3^7-3$?

**Historia**

> Redacta un párrafo: «Fermat no demostró en público el caso general del último teorema, pero…» (debe incluir al menos un aporte suyo *sí* documentado).

**Ampliación**

> Investiga qué significa «demostrado por Wiles» a nivel divulgativo (curva elíptica / modularidad): una frase, sin tecnicismos falsos.

---

## 7. Criterios LOMLOE (orientación)

Conjeturar y comprobar; distinguir prueba de ejemplo; sentido numérico; comunicar la historia de un problema abierto resuelto siglos después.

---

## 8. Precauciones docentes

- No afirmar que «Fermat tenía la prueba y se perdió».  
- No reducir a Fermat al último teorema: teoría de números, probabilidad y geometría.  
- El pequeño teorema no es el último teorema (confusión de nombres frecuente).

---

## 9. Material relacionado

- [Sophie Germain](sophie-germain.md)  
- [Descartes](descartes-coordenadas.md) (geometría analítica en paralelo)  
- [Laplace](laplace-demonio.md) (probabilidad, linaje posterior)  
- [Catálogo](../indices/catalogo.md)
