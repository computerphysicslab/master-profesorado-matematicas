# La campana que esconde un círculo

| Campo | Contenido |
|-------|-----------|
| **Nivel** | 2.º Bachillerato (ampliación); adaptable a 1.º Bach. y, como historia sin cálculo formal, a ESO |
| **Conceptos** | Función exponencial, área bajo la curva, simetría, coordenadas polares, cambio de variable, π |
| **Sentidos** | Espacial, de la medida, algebraico, numérico |
| **Tiempo de aula** | 1–2 sesiones (historia + idea clave); ampliación con GeoGebra/Python |

---

## 1. Pregunta generatriz

> ¿Cómo puede una curva que parece no tener nada que ver con un círculo acabar dando como resultado $\sqrt{\pi}$?

Deja que el alumnado proponga ideas antes de formalizar: «hay que integrar», «es imposible», «aparece π porque hay círculo escondido», «se aproxima numéricamente»…

---

## 2. Historia / enigma (relato para el aula)

Partimos de la función

$$f(x)=e^{-x^2}.$$

Su gráfica tiene forma de **campana**. La pregunta aparentemente sencilla es: ¿cuál es el área exacta bajo esta curva entre $-\infty$ y $+\infty$?

$$I=\int_{-\infty}^{+\infty}e^{-x^2}\,dx.$$

La integral **no tiene primitiva elemental**. Insistir en buscar antiderivada no resuelve el problema. La clave es **cambiar de representación**: elevar la integral al cuadrado e interpretar el producto como una integral sobre el plano.

$$I^2=\iint_{\mathbb{R}^2}e^{-(x^2+y^2)}\,dx\,dy.$$

Como $x^2+y^2=r^2$, el problema unidimensional se transforma en un problema **circular**. En coordenadas polares ($dx\,dy=r\,dr\,d\theta$) la integral se separa y aparece $\pi$. Como $I>0$, se obtiene

$$\boxed{I=\sqrt{\pi}}.$$

**Matices honestos para el aula:**

- No hace falta que el alumnado domine integrales dobles para captar la idea: «cuadrar → plano → círculo → polares».
- El resultado clásico es universitario; aquí se presenta como **historia de estrategia matemática**, no como técnica rutinaria de cálculo.
- La enseñanza transversal: cuando una representación no funciona, otra puede hacer visible la estructura oculta.

---

## 3. Intentos y debate

Antes de la demostración, pide al alumnado:

- ¿Qué forma tiene $y=e^{-x^2}$? ¿Simetría? ¿Máximo?
- ¿Qué ocurre cuando $x\to\pm\infty$?
- ¿Se puede hallar una primitiva «a mano»?
- Si no hay primitiva elemental, ¿qué otras estrategias existen (aproximación numérica, cambio de problema…)?

Errores productivos frecuentes: creer que «si no hay primitiva no se puede calcular el área»; confundir convergencia de la integral impropia con existencia de antiderivada elemental; no ver por qué elevar al cuadrado ayuda.

---

## 4. Idea matemática

### 4.1. De la campana al plano

$$I^2=\left(\int_{-\infty}^{+\infty}e^{-x^2}\,dx\right)\left(\int_{-\infty}^{+\infty}e^{-y^2}\,dy\right)=\iint_{\mathbb{R}^2}e^{-(x^2+y^2)}\,dx\,dy.$$

### 4.2. Coordenadas polares

$$x=r\cos\theta,\quad y=r\sin\theta,\quad dx\,dy=r\,dr\,d\theta.$$

$$I^2=\int_0^{2\pi}\int_0^{\infty}e^{-r^2}r\,dr\,d\theta=\left(\int_0^{2\pi}d\theta\right)\left(\int_0^{\infty}re^{-r^2}\,dr\right).$$

### 4.3. Cambio de variable y cierre

Con $u=r^2$, $du=2r\,dr$:

$$\int_0^{\infty}re^{-r^2}\,dr=\frac12.\qquad\int_0^{2\pi}d\theta=2\pi.$$

$$I^2=2\pi\cdot\frac12=\pi\quad\Rightarrow\quad I=\sqrt{\pi}\quad(I>0).$$

---

## 5. Formalización (nivel Bachillerato)

1. Interpretar $I$ como área bajo $e^{-x^2}$.
2. Justificar que elevar al cuadrado convierte el problema en una integral sobre el plano.
3. Reconocer $x^2+y^2=r^2$ y la conveniencia de coordenadas polares.
4. Explicar el factor $r$ en el elemento de área.
5. Realizar el cambio $u=r^2$ en la integral radial.
6. Argumentar $I>0$ para tomar la raíz positiva.
7. (Ampliación) Conectar con la distribución normal y $\int e^{-x^2/2}$.

---

## 6. Problema para el alumnado (por etapas)

**Enigma: «La campana que esconde un círculo»**

1. Representa $y=e^{-x^2}$. ¿Dónde está el máximo? ¿Es simétrica?
2. ¿Por qué no basta con «buscar la primitiva» de $e^{-x^2}$?
3. Explica con tus palabras qué significa elevar $I$ al cuadrado e interpretar el producto sobre el plano.
4. ¿Por qué aparece de forma natural la distancia al origen $r$?
5. ¿Qué sistema de coordenadas resulta natural cuando la expresión depende solo de $r$?
6. (Bachillerato) Completa el cálculo en polares hasta obtener $I=\sqrt{\pi}$.
7. Compara una aproximación numérica (p. ej. con GeoGebra o Python entre $-a$ y $a$) con $\sqrt{\pi}\approx 1{,}77245$.

**Ampliación**

- ¿Qué fracción del área total queda entre $-1$ y $1$? ¿Entre $-2$ y $2$?
- ¿Qué cambiaría si la función fuera $e^{-x^2/2}$?
- Conexión con la campana de Gauss en estadística.

**Variante ESO (sin integral formal)**

- Aproxima el área bajo la campana con cuadrículas o rectángulos.
- Descubre que el valor se acerca a $1{,}772\ldots$
- Pregunta-misterio: ¿por qué aparece un número ligado a $\pi$?

---

## 7. Criterios LOMLOE (orientación)

Modelizar; establecer conexiones entre análisis y geometría; cambiar de representación; usar cambio de variable; comunicar estrategias; valorar la razonabilidad del resultado; (ampliación) pensamiento computacional con aproximación numérica.

---

## 8. Precauciones docentes

- No presentar la demostración completa como obligatoria en 1.º de Bachillerato: la idea de «cambiar de representación» puede bastar.
- Evitar transmitir que «si no hay primitiva elemental el área no se puede calcular».
- Distinguir claramente aproximación numérica y resultado exacto $\sqrt{\pi}$.
- Si se usa un vídeo desencadenante, conviene pausarlo y recuperar las preguntas del alumnado antes de cerrar la demostración.

---

## 9. Material relacionado en el repo

- [Newton y Leibniz](newton-leibniz.md) (cálculo, áreas)
- [Descartes](descartes-coordenadas.md) (cambio de representación, coordenadas)
- [Kepler](kepler-orbitas.md) (geometría y modelización)
- [Gauss — suma 1 a 100](gauss-suma-1-a-100.md) (estrategia frente a fuerza bruta)
- Temarios LOMLOE Aragón: funciones, cálculo integral, geometría (Diseño curricular)

---

## 10. Referencias rápidas

- Resultado clásico: $\displaystyle\int_{-\infty}^{+\infty}e^{-x^2}\,dx=\sqrt{\pi}$ (integral gaussiana).
- Conexión: distribución normal, física estadística, difusión, óptica.
- Desencadenante audiovisual: demostración visual de la integral gaussiana (p. ej. publicaciones de divulgación matemática en X / MathFiles).
