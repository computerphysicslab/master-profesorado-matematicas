# Zenón: Aquiles, la dicotomía y las sumas infinitas

| Campo | Contenido |
|-------|-----------|
| **Nivel** | 4.º ESO (tabla + progresión) · Bachillerato (serie geométrica, límite) |
| **Conceptos** | Infinitos tramos; suma finita; progresión / serie geométrica $\|r\|<1$ |
| **Sentidos** | Numérico, algebraico; conexiones (historia del infinito y del cálculo) |
| **Tiempo** | 1 sesión (relato + cálculo); 2 si se enlaza con límites formales |

---

## 1. Pregunta generatriz

> Para recorrer 1 km debes pasar antes por el punto medio, luego por el punto medio de lo que queda, y así **sin fin**. ¿Es imposible llegar?

O:

> Aquiles corre diez veces más rápido que una tortuga que sale con ventaja. Cada vez que Aquiles llega a donde estaba la tortuga, ella ya se ha movido un poco. ¿Puede **alcanzarla**?

---

## 2. Historia (relato para el aula)

**Zenón de Elea** (s. V a. e. c.) formuló varios argumentos —las **paradojas del movimiento**— en apoyo de la escuela de **Parménides**: el cambio y la pluralidad serían ilusorios o contradictorios si se aceptan ciertas ideas sobre el espacio y el tiempo divisibles hasta el infinito.

Las dos más útiles en clase de Matemáticas:

### Dicotomía

Para ir de $A$ a $B$ hay que llegar antes al punto medio $M_1$, luego al medio del resto $M_2$, etc. Hay **infinitos** tramos. Zenón concluye que el movimiento no puede completarse.

### Aquiles y la tortuga

Aquiles da ventaja a la tortuga. Cuando llega a la posición inicial de ella, la tortuga ha avanzado; cuando llega a esa nueva posición, ella ha vuelto a avanzar… Parece que **nunca** la alcanza.

**Matiz histórico:** Zenón no estaba “equivocado en aritmética” que aún no existía como hoy. Planteaba un **desafío filosófico**. La respuesta escolar moderna no es lo que él buscaba; es una **herramienta matemática** (sumas infinitas convergentes, límites) que muestra que *infinitos pasos no implican tiempo o distancia infinitos*.

Otras paradojas (la flecha, el estadio) pueden mencionarse; en ESO/Bach. bastan dicotomía y Aquiles.

---

## 3. Intentos y debate

- ¿“Infinitos trozos” = “nunca se acaba”?  
- ¿El tiempo de cada trozo es el mismo?  
- Diferencia entre *número de etapas* e *magnitud total* (longitud o tiempo).

Error productivo: creer que cualquier suma de infinitos términos positivos “se hace infinita”.

---

## 4. Idea matemática

Una sucesión infinita de distancias (o tiempos)

$$\frac{1}{2},\ \frac{1}{4},\ \frac{1}{8},\ \frac{1}{16},\ \ldots$$

puede tener **suma finita**:

$$\sum_{n=1}^{\infty} \frac{1}{2^n} = 1.$$

Las sumas parciales $s_N = 1 - 2^{-N}$ se acercan a 1 tanto como se quiera: el “último” paso no hace falta para que el total sea 1 en el límite.

**Serie geométrica** (Bachillerato): si $\lvert r \rvert < 1$,

$$\sum_{n=0}^{\infty} ar^n = \frac{a}{1-r}.$$

---

## 5. Formalización por nivel

### 4.º ESO

1. Tabla de la dicotomía (distancia total 1):

| Etapa | Distancia del tramo | Distancia acumulada |
|-------|---------------------|---------------------|
| 1 | $1/2$ | $0{,}5$ |
| 2 | $1/4$ | $0{,}75$ |
| 3 | $1/8$ | $0{,}875$ |
| 4 | $1/16$ | $0{,}9375$ |
| … | … | se acerca a 1 |

2. Reconocer razón $1/2$.  
3. Conclusión en lenguaje natural: *hay infinitos tramos, pero la suma se acerca a un total finito*.

### Bachillerato

1. $s_N = \sum_{n=1}^{N} (1/2)^n = 1 - 2^{-N}$.  
2. $\lim_{N\to\infty} s_N = 1$.  
3. **Aquiles (números):** ventaja $d$, velocidades $v$ y $v/k$ ($k>1$). El tiempo hasta dar alcance es

$$T = \frac{d}{v - v/k} = \frac{kd}{(k-1)v},$$

finito; la serie de tiempos parciales suma $T$.

**Ejemplo numérico:** ventaja 9 m; Aquiles 10 m/s; tortuga 1 m/s.

- Tiempos de las etapas: $0{,}9$ s, $0{,}09$ s, $0{,}009$ s, …  
- Suma: $0{,}9 + 0{,}09 + 0{,}009 + \cdots = 1$ s.  
- En 1 s Aquiles recorre 10 m y la tortuga 1 m: se encuentran a 10 m del inicio de Aquiles.

---

## 6. Problemas para el alumnado

**Base (ESO)**

> Completa la tabla de la dicotomía hasta 6 etapas. ¿A qué número se acerca la distancia acumulada?

**Aquiles**

> Ventaja 100 m; Aquiles 10 m/s; tortuga 1 m/s. Escribe los tres primeros tiempos de etapa y la distancia a la que se encuentran (fórmula o serie).

**Contraste**

> ¿Qué pasaría si la tortuga fuera *más rápida* que Aquiles? (La “serie” de alcances no describe un encuentro: la tortuga se aleja.)

**Historia**

> En tres frases: qué decía Zenón, qué calculamos hoy, y por qué no es lo mismo “infinitos pasos” e “imposible llegar”.

**Puente al cálculo**

> Relaciona esta suma con la idea de límite. ¿En qué se parece a “aproximar un área con infinitos rectángulos”?

---

## 7. Criterios LOMLOE (orientación)

Modelizar; reconocer patrones geométricos; interpretar el infinito como proceso; comunicar la distinción entre cardinal de etapas y medida total; conectar con el análisis en Bachillerato.

---

## 8. Precauciones docentes

- No afirmar “Zenón se equivocaba y ya está”: el argumento era filosófico; la serie es una respuesta *posterior* en otro lenguaje.  
- No dejar la sensación de misterio sin cálculo: **tabla o $s_N$** obligatorios.  
- Separar: paradoja de Zenón ≠ hotel de Hilbert (aquí el foco es *suma de magnitudes*, no solo cardinalidad).  
- Evitar la flecha en ESO si no se va a hablar de instantes y velocidad.

---

## 9. Material relacionado

- [Hilbert — hotel infinito](hilbert-hotel.md) (otro rostro del infinito)  
- [Cantor](cantor-infinitos.md)  
- [Newton y Leibniz](newton-leibniz.md) (límites, cambio continuo)  
- [Galileo](galileo-caida.md) (movimiento y medida)  
- [Catálogo](../indices/catalogo.md)
