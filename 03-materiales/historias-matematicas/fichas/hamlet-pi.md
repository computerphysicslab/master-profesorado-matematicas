# Hamlet y los dígitos de π

| Campo | Contenido |
|-------|-----------|
| **Nivel** | 3.º–4.º ESO (ampliable a Bachillerato con normalidad de π y órdenes de magnitud) |
| **Conceptos** | Codificación, probabilidad, órdenes de magnitud, números irracionales, pensamiento computacional |
| **Sentidos** | Numérico, estocástico, algebraico (representación) |
| **Tiempo de aula** | 1–2 sesiones (enigma progresivo); posible ampliación con búsqueda computacional |

---

## 1. Pregunta generatriz

> ¿Está la frase «ser o no ser» escondida en los dígitos de π?

Deja que el alumnado proponga ideas: «π es infinito, así que sí», «depende de cómo se escriba», «imposible de comprobar», «hay que buscarla en internet»… Antes de formalizar, recoge en la pizarra qué entenderían por «estar dentro de π».

---

## 2. Historia / enigma (relato para el aula)

La pregunta parece literaria, pero es un **enigma matemático** sobre codificación, azar y números irracionales.

π es un número irracional (y se conjetura que es *normal*): su expansión decimal no termina ni se repite de forma periódica. Si sus dígitos se comportan «como si fueran aleatorios», cualquier secuencia finita de dígitos debería aparecer tarde o temprano… pero **¿dónde?** y **¿con qué codificación del texto?**

El enigma consiste en convertir la frase de Hamlet en una cadena de dígitos y preguntarse:

1. Cómo codificar texto solo con dígitos 0–9.
2. Cuál es la longitud de esa cadena.
3. Cuál es la probabilidad de encontrarla en una posición concreta de π.
4. Cuántos dígitos de π tendríamos que examinar, en promedio.
5. Cuántos dígitos de π se han calculado realmente.
6. Si, con lo que conocemos hoy, podríamos haberla encontrado ya.

**Matices honestos para el aula:**

- No está *demostrado* que π sea normal (aunque los billones de dígitos calculados se comportan de forma muy cercana a una secuencia aleatoria).
- «Aparecer con probabilidad 1 en una secuencia infinita» no equivale a «aparecer en los dígitos que conocemos».
- El lugar que ocupa la frase depende por completo de **cómo** la convertimos en números.

---

## 3. Intentos y debate

Antes de proponer la codificación oficial del enigma, pide diseños propios:

- ¿A=1, B=2… Z=26?
- ¿ASCII / Unicode?
- ¿Solo letras, o también espacios y números?

Errores productivos frecuentes: creer que «π contiene todas las frases» implica que ya están en los dígitos calculados; confundir probabilidad por posición con certeza de aparición; olvidar que distintas codificaciones producen cadenas de longitudes muy distintas.

---

## 4. Idea matemática

### 4.1. Codificación alfanumérica de 37 símbolos

Definimos un alfabeto con **37 símbolos**, cada uno representado por **dos dígitos** (porque $10^1 < 37 < 10^2$):

| Código | Símbolo |
|--------|---------|
| 00–09 | dígitos 0–9 |
| 10–35 | letras a–z |
| 36 | espacio |

Normalizamos la frase (minúsculas, sin tildes ni puntuación):

```text
ser o no ser he ahi la cuestion
```

Tiene **31 caracteres** → cadena de **62 dígitos**:

```text
28142736243623243628142736171436101718362110361230142829182423
```

(Verificación rápida: `s`→28, `e`→14, `r`→27, espacio→36, `o`→24, …)

### 4.2. Probabilidad y posición esperada

Si los dígitos de π se comportan como independientes y uniformes en $\{0,\ldots,9\}$, una secuencia concreta de 62 dígitos tiene probabilidad

$$P = 10^{-62}$$

en cada posición de partida.

La distancia media esperada hasta la primera aparición es del orden de

$$\boxed{10^{62}}$$

posiciones (cien tredecillones de dígitos, en nomenclatura española de escala corta).

### 4.3. Cuántos dígitos de π conocemos

Récord Guinness (18 de noviembre de 2025), StorageReview y Micron Technology:

$$\boxed{314\,000\,000\,000\,000} = 3{,}14 \times 10^{14}$$

dígitos (314 billones).

Comparación de escalas:

$$\frac{10^{62}}{3{,}14 \times 10^{14}} \approx 3{,}2 \times 10^{47}$$

Es decir: el espacio de búsqueda *esperado* para esta cadena es unas **$3 \times 10^{47}$ veces mayor** que todos los dígitos de π calculados hasta ahora.

---

## 5. Formalización (nivel ESO / Bachillerato)

1. **Cardinalidad del alfabeto** → dígitos necesarios por símbolo: $\lceil \log_{10} 37 \rceil = 2$.
2. **Longitud de la cadena** = (n.º de caracteres) × 2.
3. **Modelo probabilístico**: en una secuencia i.i.d. uniforme, $P(\text{acierto en posición } k) = 10^{-L}$.
4. **Esperanza de la posición de la primera aparición** ≈ $10^{L}$ (para $L$ grande).
5. **Órdenes de magnitud**: comparar $10^{62}$ con $3{,}14 \times 10^{14}$.
6. **(Bachillerato)** Distinción entre:
   - conjetura de normalidad de π;
   - «probabilidad 1 de aparición en la expansión infinita»;
   - «aparición en el prefijo calculado».

---

## 6. Problema para el alumnado (enigma por etapas)

**🔐 Enigma: «Hamlet está escondido en π»**

1. Diseña una codificación que permita representar texto usando solo dígitos decimales.
2. ¿Cuántos símbolos necesitamos si queremos 10 dígitos + 26 letras + espacio?  
   → $10 + 26 + 1 = 37$.
3. ¿Cuántos dígitos hacen falta por símbolo? ¿Por qué?  
   → Dos, porque $10 < 37 < 100$.
4. Codifica: `ser o no ser he ahi la cuestion`.  
   → Cadena de 62 dígitos (la indicada arriba).
5. ¿Cuál es la probabilidad de encontrar exactamente esa secuencia en una posición concreta de π?  
   → $10^{-62}$.
6. ¿Cuántos dígitos de π esperaríamos tener que examinar, en promedio?  
   → Del orden de $10^{62}$.
7. ¿Cuántos dígitos de π se han calculado realmente (récord actual)?  
   → $3{,}14 \times 10^{14}$.
8. ¿Podría estar ya la frase en los dígitos conocidos? Compara las dos potencias de 10 y explica.

**Ampliación (Bachillerato / proyecto)**

- Prueba otras codificaciones (A=1…Z=26 sin espacios; ASCII) y recalcula $L$ y $10^{L}$.
- Busca cadenas *cortas* (p. ej. 6–10 dígitos) en un buscador de π en línea y discute por qué sí aparecen.
- Debate: si π es infinito y la probabilidad por posición es positiva, ¿«tiene» que aparecer la frase alguna vez? Distingue certeza matemática de conjetura.

**Refuerzo**

- Explica con tus palabras por qué cambiar la codificación cambia «el lugar» de Hamlet en π.

---

## 7. Criterios LOMLOE (orientación)

Modelizar una situación; usar potencias de 10 y órdenes de magnitud; interpretar probabilidad en un modelo simple; comunicar el razonamiento; analizar la razonabilidad de un resultado (comparar $10^{62}$ con $10^{14}$); conectar pensamiento computacional (codificación) con probabilidad y números irracionales.

---

## 8. Precauciones docentes

- No afirmar como hecho demostrado que «π contiene todas las obras de Shakespeare»: es una consecuencia *esperada* bajo la conjetura de normalidad, no un teorema.
- Evitar presentar el récord de dígitos como si bastara para buscar cualquier frase larga: el contraste de escalas es precisamente el punto didáctico.
- Si se usa un buscador online de π, limitar la búsqueda a cadenas cortas y comentar limitaciones de las bases de datos públicas.

---

## 9. Material relacionado en el repo

- **SA completa (5 sesiones):** [Hamlet y los dígitos de π](../../../04-pbl-abp/situaciones-aprendizaje/sa-hamlet-pi-4eso.md) — producto, CE, DUA, comparación de escalas
- [Pascal — problema de los puntos](pascal-problema-puntos.md) (probabilidad, esperanza)
- [Monty Hall](monty-hall.md) / [Bayes](bayes.md) (probabilidad condicionada y modelos)
- [Hilbert (hotel)](hilbert-hotel.md) / [Cantor](cantor-infinitos.md) (infinito y contrastes de cardinalidad/escala)
- [Ada Lovelace](ada-lovelace.md) / [Turing](turing.md) (codificación, algoritmos, computación)
- Sección de probabilidad y estadística en los temarios LOMLOE Aragón (Diseño curricular)

---

## 10. Referencias rápidas

- Guinness World Records: *Most accurate value of pi* — 314 000 000 000 000 dígitos (StorageReview & Micron, 18 nov 2025).
- Conjetura de normalidad de π (comportamiento estadístico de los dígitos; no demostrada).
