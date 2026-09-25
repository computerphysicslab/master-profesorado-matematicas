# El problema de Monty Hall

| Campo | Contenido |
|-------|-----------|
| **Nivel** | Bachillerato · 4.º ESO con simulación |
| **Conceptos** | Probabilidad condicionada; intuición vs cálculo |
| **Sentidos** | Estocástico |
| **Tiempo** | 1 sesión (simular antes de formalizar) |

---

## 1. Pregunta generatriz

> Tres puertas: detrás de una, un coche; detrás de las otras, cabras. Eliges la 1. El presentador (que sabe qué hay) abre la 3 y muestra una cabra. ¿Te conviene **cambiar** a la 2?

---

## 2. Historia

Popularizado por el concurso *Let’s Make a Deal* (presentador Monty Hall) y por un artículo de Marilyn vos Savant (1990) que generó enorme controversia: mucha gente (incluso matemáticos) rechazó al principio que cambiar duplique la probabilidad de ganar.

No es un teorema del s. XVII, pero es el **mejor laboratorio escolar** de probabilidad condicionada y de conflicto intuición–razón.

---

## 3. Idea matemática

- Al elegir al principio: probabilidad $1/3$ de haber acertado.  
- Si acertaste ($1/3$), al cambiar pierdes.  
- Si fallaste ($2/3$), el presentador revela la otra cabra y al cambiar **ganas**.  
- Por tanto, cambiar gana con probabilidad $2/3$.

Simulación con cartas o Python refuerza más que la fórmula sola.

---

## 4. Problema

> Repite el experimento 30 veces (cambiar siempre). ¿Qué frecuencia de éxitos obtienes?

---

## 5. Precauciones

El presentador **siempre** abre una puerta con cabra y nunca la del concursante. Sin esas reglas el problema cambia. Enlace a [Bayes](bayes.md).

## 6. Relacionado

[Pascal](pascal-problema-puntos.md) · [Catálogo](../indices/catalogo.md)
