# Eratóstenes y el tamaño de la Tierra

| Campo | Contenido |
|-------|-----------|
| **Nivel** | ESO (especialmente 2.º–3.º; adaptable a 1.º con más andamiaje) |
| **Conceptos** | Geometría del círculo, proporcionalidad, ángulos, medida, trigonometría elemental (opcional) |
| **Sentidos** | Espacial, de la medida, numérico |
| **Tiempo de aula** | 1 sesión de apertura + formalización; o 2 sesiones con medición/experimento |

---

## 1. Pregunta generatriz

> ¿Podrías estimar el **tamaño de la Tierra** sin verla completa y sin dar la vuelta al mundo?

Deja que el alumnado proponga ideas (viajar, satélites, «es imposible»…) antes de contar la historia.

---

## 2. Historia (relato para el aula)

**Eratóstenes de Cirene** (s. III a. e. c.) trabajó en Alejandría, en un entorno donde se cultivaban la geometría y la astronomía práctica.

La tradición (transmitida sobre todo a través de relatos posteriores) cuenta aproximadamente esto:

- En **Siena** (cerca de la actual Asuán), en un día concreto del año, el Sol de mediodía iluminaba el fondo de un pozo: los rayos caían **verticales**.
- En **Alejandría**, el mismo día a la misma hora, un gnomon (o una estaca vertical) proyectaba **sombra**: los rayos **no** eran verticales.
- Eratóstenes midió (o estimó) el **ángulo** que formaban esos rayos con la vertical en Alejandría.
- Conocía una estimación de la **distancia** entre Siena y Alejandría (a lo largo de un meridiano, en la medida de la época).

La idea geométrica: si los rayos del Sol se consideran **paralelos**, ese ángulo coincide con el ángulo central que separa ambas ciudades en la Tierra. Entonces la distancia Alejandría–Siena es una **fracción** de la circunferencia terrestre, y esa fracción es la misma que el ángulo medido respecto de 360° (o una vuelta completa).

Con proporcionalidad:

$$\frac{\text{distancia entre ciudades}}{\text{circunferencia de la Tierra}} = \frac{\text{ángulo medido}}{360^{\circ}}$$

Así obtuvo una estimación del tamaño de la Tierra notablemente buena para los medios de la época.

**Matices honestos para el aula (evitar mito plano):**

- Los datos exactos (ángulo, distancia, unidades) varían según las fuentes; no hace falta fijar un único número «oficial» en la primera sesión.
- La Tierra no es una esfera perfecta; el modelo es una **idealización** útil.
- Lo importante didácticamente no es memorizar el resultado, sino la **cadena**: observación → modelo geométrico → proporción → estimación.

---

## 3. Intentos y debate

Antes de formalizar, recoge en la pizarra:

- ¿Qué habría que medir?
- ¿Por qué importa que los rayos se consideren paralelos?
- ¿Qué figura dibujarías (Tierra, rayos, estaca, ángulo)?

Errores productivos frecuentes: creer que hay que medir el radio «directamente»; olvidar que el ángulo en la superficie se relaciona con el centro; mezclar radio y circunferencia.

---

## 4. Idea matemática

- Ángulo central y arco.
- **Proporcionalidad** entre arco y ángulo.
- Modelo: Tierra ≈ círculo máximo; rayos ≈ paralelos.

---

## 5. Formalización (nivel ESO)

1. Dibujo: circunferencia, dos radios, ángulo central $\alpha$, arco $d$.  
2. Relación:

$$\frac{d}{C} = \frac{\alpha}{360^{\circ}} \quad \Rightarrow \quad C = d \cdot \frac{360^{\circ}}{\alpha}$$

3. Si se conoce $C$, el radio es $R = C / (2\pi)$ (cuando el curso ya trabaja $\pi$).  
4. (Opcional 3.º–4.º) Conectar con sombra y tangente: $\tan \alpha = \frac{\text{sombra}}{\text{altura del gnomon}}$.

---

## 6. Problema para el alumnado

**Versión base**

> Supón que el ángulo medido es $7{,}2^{\circ}$ y la distancia entre las dos ciudades es $800$ km (números redondos de trabajo, no «históricos exactos»). Estima la circunferencia de la Tierra. ¿Qué radio obtendrías?

**Versión con sombra**

> Un gnomon de $1$ m proyecta $0{,}125$ m de sombra. Estima el ángulo y, con una distancia dada entre ciudades, la circunferencia.

**Ampliación**

> ¿Qué ocurre en la estimación si el ángulo se mide con un error de $0{,}5^{\circ}$? Discute la sensibilidad del modelo.

**Refuerzo**

> Completa un dibujo etiquetado (Sol, rayos paralelos, Alejandría, Siena, ángulo) y explica con tus palabras por qué el ángulo de la sombra «es el mismo» que el del centro.

---

## 7. Criterios LOMLOE (orientación)

Modelizar una situación; usar proporcionalidad y geometría; representar; comunicar el razonamiento; analizar si el resultado es razonable (orden de magnitud del radio terrestre ≈ 6000 km).

---

## 8. Precauciones docentes

- No presentar la historia como un cuento cerrado e inmutable: es una **reconstrucción didáctica** de un método.
- Evitar ridiculizar a quienes «no sabían» en la Antigüedad: el logro es precisamente estimar con geometría y medida.
- Si hay alumnado sensible a temas religiosos o culturales sobre la forma de la Tierra, centrase en el **modelo matemático** y la evidencia de medida.

---

## 9. Material relacionado en el repo

- [Banco de generatrices (geometría)](../../../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/banco-problemas/generatrices.md)
- [Bloque 8 — Resolución de problemas](../../../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/apuntes/08-resolucion-de-problemas.md)
- [Bloque 9 — Génesis escolar](../../../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/apuntes/09-genesis-escolar-objetos-matematicos.md)
