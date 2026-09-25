# Pascal y el problema de los puntos

| Campo | Contenido |
|-------|-----------|
| **Nivel** | Bachillerato (probabilidad); ESO (3.º–4.º con andamiaje, casos numéricos simples) |
| **Conceptos** | Reparto justo, casos favorables, esperanza matemática; nacimiento de la probabilidad |
| **Sentidos** | Estocástico; conexiones (historia de la ciencia) |
| **Tiempo de aula** | 1 sesión (relato + problema numérico); enlace natural con [Fermat](fermat.md) y [Laplace](laplace-demonio.md) |

---

## 1. Pregunta generatriz

> Dos jugadores, de igual habilidad, juegan a un juego de azar. Han apostado la misma cantidad. La partida se **interrumpe** cuando uno va ganando (por ejemplo, 2 a 1 en un juego a 3 puntos). ¿Cómo **repartir el bote** de forma justa?

No basta con “quien va delante se lo lleva todo”: aún no ha terminado la partida.

---

## 2. Historia (relato para el aula)

**Blaise Pascal** (Clermont-Ferrand, 1623 – París, 1662) fue matemático, físico, inventor y pensador religioso. Prodigio educado por su padre; a los dieciséis años ya trabajaba en cónicas. Inventó la **Pascalina** (calculadora mecánica, años 1640) para ayudar en el cálculo de impuestos. Estudió el vacío y la presión (la unidad *pascal* lleva su nombre). Escribió el *Traité du triangle arithmétique* (triángulo de Pascal / coeficientes binomiales) y, en su etapa final, las *Pensées*.

### El caballero de Méré y el problema de los puntos

Hacia 1654, el aficionado a los juegos **Antoine Gombaud** (caballero de Méré) plantea a Pascal cuestiones de apuestas. Una de ellas —el **problema de los puntos** o del *reparto de las apuestas*— llevaba más de un siglo sin solución convincente (Pacioli, Cardano, Tartaglia habían propuesto reglas discutibles).

Pascal escribe a **Pierre de Fermat**. En el verano de 1654 intercambian cartas: dos caminos distintos, **misma respuesta justa**. Esa correspondencia se considera el **nacimiento de la probabilidad matemática** moderna.

**Idea compartida:** lo justo no depende solo del marcador pasado, sino de las **formas posibles** en que la partida *podría haber continuado* hasta coronar a un ganador.

- **Fermat:** enumera todas las continuaciones posibles (con la misma longitud máxima) y cuenta en cuántas gana cada uno.  
- **Pascal:** razona por **esperanza** (valor esperado) y, en la práctica, por una recursión hacia atrás: si empataran, mitad y mitad; si a uno le falta un punto y al otro dos, etc.

Poco después, **Huygens** sistematiza estas ideas en *De ratiociniis in ludo aleae* (1657), primer tratado público de probabilidad.

### Hilo con el resto de la colección

```text
Pascal ↔ Fermat (1654)  →  probabilidad como cálculo de lo justo bajo incertidumbre
         ↓
    Huygens, Bernoulli…
         ↓
    Laplace (s. XVIII–XIX)  →  probabilidad como herramienta científica y “demonio” / determinismo
```

Fermat aporta el contaje de casos; Pascal, el lenguaje de la **esperanza**; Laplace integrará la probabilidad en la visión científica del azar y del conocimiento incompleto ([ficha Laplace](laplace-demonio.md)).

---

## 3. Ejemplo numérico de aula (clásico)

Juego a **3 puntos** (gana quien primero llega a 3). Se interrumpe con marcador **2–1** a favor de A. Cada uno puso 32 unidades (bote = 64).

**Continuaciones posibles** (como máximo faltan 2 rondas; se pueden listar 4 resultados equiprobables si se “juegan” siempre dos partidas más, aunque a veces sobren):

| Ronda 1 | Ronda 2 | Ganador |
|---------|---------|---------|
| A | (lo que sea) | A |
| B | A | A |
| B | B | B |

En el conteo de Fermat (cuatro ramas AA, AB, BA, BB): A gana en 3 de 4 → le corresponden $3/4$ del bote.

**Reparto:** A recibe 48, B recibe 16 (si el bote es 64).

**Pascal (idea):** si A gana el siguiente punto, se lleva todo (64); si pierde, empatan a 2 y entonces se parte 32–32. Esperanza de A:

$$\frac{1}{2}\cdot 64 + \frac{1}{2}\cdot 32 = 48.$$

Misma cifra, dos razonamientos.

---

## 4. Intentos y debate

- ¿Por qué “repartir proporcional al marcador” (2:1 → 2/3 y 1/3) es injusto aquí?  
- ¿Qué cambia si el juego fuera a 10 puntos y el marcador 9–8?  
- ¿Esperanza vs “solo el que iba ganando”?

Error productivo: mirar solo el pasado; olvidar que ambos jugadores aún tienen posibilidades.

---

## 5. Formalización (nivel Bachillerato / 4.º ESO)

1. Casos posibles equiprobables.  
2. Proporción de casos favorables → parte del bote.  
3. Esperanza: $\mathbb{E} = \sum p_i x_i$.  
4. (Ampliación) Triángulo de Pascal y coeficientes binomiales como conteo de caminos.

---

## 6. Problema para el alumnado

**Base**

> Juego a 3 puntos; marcador 2–0 a favor de A; bote 64. ¿Cómo repartir? (Lista continuaciones o usa esperanza.)

**Transferencia**

> Misma lógica con monedas o dados: partida interrumpida, apuesta común, reparto justo.

**Historia**

> En un párrafo: ¿qué aportó Pascal y qué Fermat? ¿Por qué esta correspondencia “abre” la probabilidad?

**Puente a Laplace**

> ¿En qué se parece “repartir sin saber cómo habría terminado el juego” a “asignar probabilidad cuando no conocemos todas las causas”?

---

## 7. Criterios LOMLOE (orientación)

Sentido estocástico; modelizar situaciones de incertidumbre; argumentar un reparto; comunicar dos estrategias (conteo vs esperanza).

---

## 8. Precauciones docentes

- No reducir a Pascal al triángulo o a la Pascalina: el núcleo de *esta* ficha es el **reparto justo**.  
- El problema de Méré sobre dados (ventaja de “al menos un 6 en 4 tiradas” vs “doble 6 en 24”) puede ser ampliación, no el centro.  
- Evitar moralina sobre el juego: el interés es matemático (equidad bajo azar).

---

## 9. Material relacionado

- [Fermat](fermat.md)  
- [Laplace — demonio e incertidumbre](laplace-demonio.md)  
- [Ficha de objeto · Probabilidad](../../../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/fichas-objetos/probabilidad.md)  
- [Problemas ricos P4, P7](../../../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/banco-problemas/problemas-ricos.md)  
- [Catálogo](../indices/catalogo.md)
