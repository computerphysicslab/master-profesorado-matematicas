# Fractales Mandelbrot (y Julia) en Bachillerato

**Asignatura:** Contenidos disciplinares de Matemáticas  
**Nivel:** 1.º Bachillerato (Matemáticas I) — taller de ampliación tras el bloque de complejos  
**Prerrequisito curricular:** forma binómica, módulo, operaciones básicas en $\mathbb{C}$; conviene haber visto el plano de Argand.

> **No es contenido obligatorio** del currículo LOMLOE. Es una **aplicación visual** de los números complejos: motiva el plano complejo, el módulo y la iteración, sin sustituir la operatoria oficial.

---

## 1. Idea central (nivel Bachillerato)

Se elige un número complejo $c$ y se construye la sucesión

$$
z_0 = 0, \qquad z_{n+1} = z_n^2 + c.
$$

- Si la órbita $\{z_n\}$ **permanece acotada** (no «escapa» a infinito), se dice que $c$ pertenece al **conjunto de Mandelbrot** $M$.
- Si $|z_n|$ crece sin límite, $c \notin M$.

En la práctica se usa un criterio de escape: si en algún momento $|z_n| > 2$, la órbita se va a infinito. El color de cada punto del plano suele codificar **cuántas iteraciones** se necesitan para superar ese umbral (o un color fijo si no escapa en $N$ pasos).

**Mensaje didáctico:** un objeto «bonito» nace de una regla algebraica mínima en $\mathbb{C}$: sumar y elevar al cuadrado.

---

## 2. Qué se trabaja del temario (y qué no)

| Sí se refuerza | No se exige en Bachillerato |
|----------------|-----------------------------|
| Plano complejo (punto = $c = a+bi$) | Teoría de la dimensión fractal |
| Módulo $|z| = \sqrt{a^2+b^2}$ | Dinámica compleja formal |
| Producto y potencia $z^2$ | Demostración de que el umbral 2 es óptimo |
| Idea de sucesión / iteración | Programación avanzada |
| Lectura de un gráfico (pertenece / no pertenece / «tarda en escapar») | Análisis de la frontera de $M$ |

---

## 3. Conjuntos de Julia (versión breve)

Fijado $c$, se itera $z_{n+1} = z_n^2 + c$ pero ahora el **punto variable es el $z_0$ inicial** (no el parámetro $c$). El conjunto de Julia $J_c$ describe el comportamiento de esas órbitas. En clase basta con:

- Mandelbrot = mapa de parámetros $c$;
- Julia = «retrato» para un $c$ concreto.

Una observación motivadora (sin demostración): si $c$ está en $M$, el Julia asociado suele verse «conectado»; si no, más «disperso». Útil para explorar con un applet, no para examinar teoría.

---

## 4. Cálculo a mano (pocos pasos)

Ejemplo orientativo con $c = i$ (fuera de $M$ o en la frontera según precisión; sirve para practicar):

$$
z_0 = 0, \quad z_1 = c = i, \quad z_2 = i^2 + i = -1 + i, \quad z_3 = (-1+i)^2 + i = -2i + i = -i, \ldots
$$

Mejor en aula: elegir $c$ con partes reales/imaginarias sencillas ($0$, $-1$, $-0{,}5$, $0{,}25$, $-0{,}75+0{,}1i$) y calcular **3–5 términos** y el módulo de cada uno. Comparar quién «se dispara» antes.

**Actividad corta (15–20 min):** tabla $n \mid z_n \mid |z_n|$ para dos valores de $c$; conjetura de pertenencia a $M$.

---

## 5. Propuesta de taller (1–2 sesiones de 50 min)

### Sesión A — Del álgebra a la imagen

1. **Recordatorio (10 min):** punto del plano = complejo; $|z|$; $z^2$ en binómica.
2. **Regla de Mandelbrot (10 min):** escribir la recurrencia; criterio $|z|>2$.
3. **Cálculo manual (15 min):** 2–3 valores de $c$; tabla de módulos.
4. **Visualización (15 min):** applet o GeoGebra/Python; localizar los $c$ calculados en la imagen.

### Sesión B — Exploración y producto

1. Zoom en la frontera (copos, filamentos): «la misma estructura a otra escala» (idea cualitativa de autosimilitud).
2. Probar un Julia para un $c$ interior y uno exterior a $M$.
3. **Producto:** captura de pantalla + 8–10 líneas: qué es $M$, qué papel juega el módulo, un $c$ que probaron a mano.

---

## 6. Herramientas accesibles

| Herramienta | Uso en aula |
|-------------|-------------|
| **GeoGebra** | Posible con hojas o applets compartidos; bueno si ya se usa en el centro |
| **Python** (matplotlib / numba opcional) | Buen puente con la optativa de programación del máster; 15–20 líneas bastan para una malla gruesa |
| **Applets online** (Mandelbrot/Julia) | Máxima velocidad para explorar; conviene que el alumno *antes* haya hecho 1–2 órbitas a mano |
| **Desmos** | Limitado para mallas densas; útil para órbitas de un solo $c$ |

### Esqueleto mínimo en Python (orientativo)

```python
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_escape(c, max_iter=50, radius=2.0):
    z = 0j
    for n in range(max_iter):
        if abs(z) > radius:
            return n
        z = z * z + c
    return max_iter

# Malla gruesa (aula / portátil)
x = np.linspace(-2.0, 1.0, 400)
y = np.linspace(-1.2, 1.2, 320)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y
img = np.vectorize(mandelbrot_escape)(C)

plt.imshow(img, extent=[-2, 1, -1.2, 1.2], origin="lower", cmap="hot")
plt.title("Mandelbrot (escape time)")
plt.xlabel("Re(c)"); plt.ylabel("Im(c)")
plt.show()
```

En clase no hace falta optimizar: una malla de pocos cientos de puntos ya muestra la forma de «cardioide + bulbos».

---

## 7. Precauciones didácticas

| Riesgo | Qué hacer |
|--------|-----------|
| Convertir el bloque de complejos en «solo fractales» | Taller *después* de binómica/módulo; 1–2 sesiones |
| Solo mirar imágenes sin álgebra | Obligar 1–2 órbitas a mano y el criterio de escape |
| Vocabulario inflado («dimensión no entera», «caos») | Usar: órbita, acotada, escape, parámetro $c$ |
| Frustración con el código | Ofrecer applet + hoja de cálculo de módulos como plan B |
| Confundir Mandelbrot y Julia | Tabla clara: qué se fija y qué se mueve |

---

## 8. Evaluación orientativa (ampliación)

1. Escribe la recurrencia del conjunto de Mandelbrot y explica el papel de $|z_n|$.
2. Para $c = -1$, calcula $z_1, z_2, z_3$ y sus módulos. ¿Sugiere escape rápido o no?
3. En una imagen de $M$, señala aproximadamente la región donde $\operatorname{Re}(c) > 0$ y comenta si esperas muchos puntos de $M$ ahí (observación empírica tras explorar).
4. (Opcional) Diferencia en una frase Mandelbrot y Julia.

**Rúbrica breve:** correcto uso de $z_n^2+c$ y del módulo; al menos un cálculo coherente; interpretación ligada a la imagen o a la tabla.

---

## 9. Competencias y sentido LOMLOE (encaje)

- **Modelización / herramientas digitales:** representar un proceso iterativo en el plano.
- **Sentido algebraico y geométrico:** operaciones en $\mathbb{C}$ con lectura en Argand.
- **STEM:** puente natural hacia programación y visualización científica.

No sustituye criterios de evaluación oficiales de complejos; **ilustra** su utilidad.

---

## 10. Para seguir

- Marco de aplicaciones de complejos: [aplicaciones-numeros-complejos-bachillerato.md](aplicaciones-numeros-complejos-bachillerato.md)
- Cuaterniones / 3D (otra ampliación): [hipercomplejos-cuaterniones-videojuegos.md](hipercomplejos-cuaterniones-videojuegos.md)
- Temario Mat. I Aragón: [06_matematicas_i_1_bachillerato.md](../../diseno-curricular-e-instruccional-de-matematicas/materiales/temarios-matematicas-aragon/06_matematicas_i_1_bachillerato.md)
- Historias / cultura matemática: [`03-materiales/historias-matematicas/`](../../../03-materiales/historias-matematicas/) (posible ficha futura sobre Mandelbrot o Fatou/Julia)
