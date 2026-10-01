---
layout: default
title: "Lotería, independencia y la ecuación de Drake"
parent: Situaciones de aprendizaje
nav_order: 24
---

# SA — Si ya me tocó… ¿me toca otra vez? (independencia, lotería y Drake)

## 0. Metadatos

| Campo | Contenido |
|-------|-----------|
| **Título de la SA** | Lotería, independencia y la ecuación de Drake |
| **Nivel / curso** | 4.º ESO / 1.º Bachillerato (Matemáticas; conexión STEM) |
| **Duración** | 7 sesiones × 50–55 min |
| **Autor/a de la ficha** | Material del repositorio |
| **Fecha / versión** | 2026-10 / v1.0 |
| **Contexto de uso** | Diseño curricular · Practicum · germen de TFM interdisciplinar |

**Palabras clave:** independencia, probabilidad condicional, falacia del jugador, mano caliente, ecuación de Drake, $f_l$, zona habitable, sesgo de selección, sentido estocástico, modelización

---

## 1. Pregunta guía / reto

> *Si esta semana te toca la lotería y la que viene vuelves a jugar, ¿la probabilidad de que te toque de nuevo es 1? ¿Y si la Tierra «ya ganó» el sorteo de la vida, podemos poner $f_l = 1$ en la ecuación de Drake?*

**Producto final esperado:** informe de equipo con tres partes:

1. **Modelo de lotería:** distinguir $P(W_1\cap W_2)$, $P(W_2\mid W_1)$ y el hecho pasado «ya gané».
2. **Modelo Drake:** calcular $N$ con un escenario optimista ($f_l = 1$) y con varios $f_l \ll 1$; mostrar el cambio de órdenes de magnitud.
3. **Conclusión argumentada:** qué se puede (y qué no) afirmar sobre vida extraterrestre cuando solo disponemos del dato de que *aquí* hay vida.

---

## 2. Justificación y sentido educativo

- La confusión entre **hecho consumado**, **probabilidad conjunta** y **probabilidad condicional** es una de las falacias estocásticas más frecuentes.
- La misma estructura reaparece en divulgación científica: «la vida surgió en la Tierra ⇒ en cualquier planeta tipo Tierra la vida es casi segura» ($f_l \approx 1$).
- La ecuación de Drake es un **producto de factores inciertos**: un solo factor mal interpretado puede cambiar $N$ de «millones de civilizaciones» a «casi ninguna».
- Entrena pensamiento crítico STEM: no es negacionismo ni cinismo, es **separar evidencia, modelo y deseo**.

---

## 3. Objetivos de aprendizaje

1. Definir independencia de sucesos y aplicar $P(A\cap B)=P(A)P(B)$ cuando corresponde.
2. Calcular e interpretar $P(W_2\mid W_1)$ frente a $P(W_1\cap W_2)$.
3. Identificar la falacia del jugador, la de la mano caliente y la confusión «ya ocurrió ⇒ probabilidad 1 del próximo».
4. Reconocer los factores de la ecuación de Drake y el papel de $f_l$ (fracción de planetas habitables donde **surge** vida).
5. Explorar numéricamente cómo cambia $N$ al variar $f_l$ (y, opcionalmente, $f_i$).
6. Argumentar por qué el dato «hay vida en la Tierra» **no implica** por sí solo $f_l = 1$ (sesgo de selección / antrópico ligero, a nivel divulgativo).

---

## 4. Competencias específicas y criterios de evaluación

| CE (síntesis RD 217/2022) | Criterios prioritarios | Evidencia en esta SA |
|---------------------------|------------------------|----------------------|
| **CE1–CE2** Resolver / validar | Modelizar, comprobar coherencia | Cálculos de lotería y de $N$ |
| **CE3** Conjeturar | Formular y criticar hipótesis | Debate $f_l = 1$ vs $f_l \ll 1$ |
| **CE4** Pensamiento computacional | Descomponer el producto de Drake | Hoja de cálculo / tabla de escenarios |
| **CE5–CE6** Conexiones | Matemáticas ↔ astronomía / divulgación | Informe interdisciplinar |
| **CE7–CE8** Representar / comunicar | Lenguaje preciso; gráficos de órdenes de magnitud | Informe + exposición breve |
| **CE9–CE10** Socioafectivas | Tolerar la incertidumbre; rigor sin ridiculizar | Rúbrica de debate |

**Competencias clave:** STEM, CCL, CPSAA, CD.

---

## 5. Saberes básicos y sentidos matemáticos

| Sentido | Saberes / contenidos | Prioridad |
|---------|----------------------|----------|
| Estocástico | Independencia; condicional; falacias; producto de probabilidades | Alta |
| Numérico | Órdenes de magnitud; notación científica; potencias de 10 | Alta |
| Algebraico | Producto de factores; sensibilidad de un modelo | Alta |
| De la medida | Escalas cósmicas (estrellas, años) | Media |
| Socioafectivo | Humildad epistémica; crítica de titulares | Alta |

**Conexiones interdisciplinares:** Física/Astronomía (zona habitable, exoplanetas), Filosofía de la ciencia (sesgo de selección), Lengua (análisis de un texto divulgativo).

---

## 6. Secuencia de aprendizaje

| Sesión | Fase | Actividad del alumnado | Rol docente | Agrupamiento |
|--------|------|------------------------|-------------|--------------|
| 1 | Activación | Encuesta anónima: «Si te tocó esta semana, P(te toque la que viene) = ¿0, p o 1?» | Recoger sin juzgar; no revelar aún | Individual → clase |
| 2 | Lotería formal | Definir $W_1,W_2$; calcular $P(W_1\cap W_2)=p^2$ y $P(W_2\mid W_1)=p$ | Pizarra guiada; ejemplo numérico | Parejas |
| 3 | Falacias | Clasificar frases reales (jugador / mano caliente / confusión conjunto-condicional) | Banco de frases (anexo) | Equipos |
| 4 | Drake | Presentar $N = R_*\,f_p\,n_e\,f_l\,f_i\,f_c\,L$; asignar valores «de libro» optimistas | Explicar cada factor en una frase | Grupo-clase → equipos |
| 5 | Sensibilidad | Recalcular $N$ con $f_l = 1,\;0{,}1,\;10^{-3},\;10^{-6},\;10^{-12}$ | Facilitar hoja de cálculo plantilla | Equipos |
| 6 | El argumento falaz | Analizar el razonamiento «hubo vida aquí ⇒ $f_l=1$»; analogía con la lotería | Preguntas socráticas | Equipos + debate |
| 7 | Producto | Informe + mini-exposición (3 min): *qué cambia en las conclusiones sobre ETI* | Rúbrica visible | Equipos |

**Hito intermedio (sesión 5):** tabla de escenarios con $N(f_l)$ entregada al docente.

---

## 7. Metodología y organización

- **Enfoque:** conflicto cognitivo → formalización → transferencia a un modelo científico mediático.
- **Agrupamientos:** parejas (sesiones 2–3); equipos de 3–4 (4–7).
- **Espacios:** aula; opcional aula de informática (hoja de cálculo).
- **Materiales:** calculadora; plantilla Drake (anexo); 1–2 párrafos de divulgación que asuman $f_l\approx 1$ (seleccionados por el docente).

---

## 8. Evaluación

### 8.1. Formativa
- Ticket de salida sesión 2: «En una frase, ¿por qué $P(W_2\mid W_1)$ no es 1?»
- Revisión de la tabla $N(f_l)$ en sesión 5.

### 8.2. Sumativa (informe)

| Criterio | Indicadores |
|----------|-------------|
| Independencia | Distinguen conjunta / condicional / hecho pasado con un ejemplo numérico |
| Falacias | Identifican al menos dos falacias con ejemplo propio |
| Drake | Calculan $N$ en ≥ 3 valores de $f_l$ y comentan el orden de magnitud |
| Transferencia | Explican por qué «vida en la Tierra» no fuerza $f_l=1$ |
| Comunicación | Lenguaje preciso; evitan titulares engañosos |

Peso orientativo: proceso 30 % · producto 50 % · exposición/debate 20 %.

### 8.3. Autoevaluación y coevaluación
- Comparar la encuesta de la sesión 1 con la postura final del equipo.
- Coevaluación del rigor del debate (no del «creer o no en ETI»).

---

## 9. Atención a la diversidad y DUA

| Principio DUA | Medida concreta |
|---------------|-----------------|
| Implicación | Pregunta de lotería cercana; misterio cósmico |
| Representación | Diagrama de árbol; tabla; analogía; fórmula |
| Acción y expresión | Informe escrito, podcast de 90 s o póster de escenarios |

**Refuerzo:** solo lotería + un único recálculo de Drake con dos valores de $f_l$.  
**Ampliación:** variar también $f_i$ o $L$; leer un extracto de la hipótesis de la Tierra rara frente a un texto optimista tipo «cosmos lleno de vida».

---

## 10. Dimensión socioafectiva

- Separar **identidad** («me gusta pensar que no estamos solos») de **inferencia** («¿qué permite el modelo?»).
- En el debate, norma de aula: se critica el *argumento*, no a quien lo sostiene.
- CE9–CE10: tolerar que la respuesta honesta sea «no lo sabemos; el factor $f_l$ domina la incertidumbre».

---

## 11. Orientaciones para la implementación

- **No** presentar la SA como «demostración de que no hay vida extraterrestre». El mensaje es: *las conclusiones mediáticas optimistas suelen ocultar un $f_l$ puesto a 1 sin evidencia suficiente*.
- Cuidado con el sesgo antrópico: en 4.º ESO basta la analogía de la lotería («solo hablan los que ganaron»). En Bachillerato se puede nombrar *selection bias*.
- Homogeneizar unidades en Drake (misma estimación de $R_*$, $L$, etc.) al comparar escenarios; lo que debe variar de forma controlada es $f_l$.
- Variante corta (4 sesiones): 1–2 (lotería) + 4–5 (Drake numérico) + conclusión oral.

---

## 12. Referencias

### Normativa
- [RD 217/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-4975) · [RD 243/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-5521)

### Didáctica y recursos
1. Ecuación de Drake (formulación clásica SETI / NASA education).
2. SA hermanas: [paradoja del cumpleaños](sa-paradoja-cumpleanos-3eso.md), [exoplanetas](sa-exoplanetas-transito-4eso.md), [Kepler III](sa-kepler-ley-planetas-4eso.md).
3. Para el docente: distinguir optimismo tipo Sagan de la incertidumbre real sobre abiogénesis ($f_l$).

---

## 13. Anexo — Guía docente

### A. Lotería (números redondos)

Sea $p = 1/1000$.

$$
P(W_1\cap W_2)=p^2=10^{-6},\qquad
P(W_2\mid W_1)=\frac{P(W_1\cap W_2)}{P(W_1)}=p=10^{-3}.
$$

| Afirmación | ¿Correcta? | Lectura |
|------------|------------|--------|
| «Como ya gané, la próxima es segura ($P=1$)» | No | Confunde hecho pasado con el siguiente ensayo |
| «Como ya gané, la próxima es imposible» | No | Falacia del jugador |
| «Como ya gané, estoy de suerte: $P>p$» | No* | Mano caliente (*en sorteo independiente) |
| «La próxima sigue teniendo probabilidad $p$» | Sí | Independencia |
| «Ganar *las dos* semanas es mucho más raro que ganar una» | Sí | $p^2\ll p$ |

\*Si el sorteo estuviera **sesgado** o hubiera **trampa**, la independencia fallaría: por eso se discute el *modelo*.

### B. Ecuación de Drake (recordatorio)

$$
N = R_* \cdot f_p \cdot n_e \cdot f_l \cdot f_i \cdot f_c \cdot L
$$

| Factor | Significado breve |
|--------|------------------|
| $R_*$ | Ritmo de formación de estrellas adecuadas (por año, en la galaxia) |
| $f_p$ | Fracción de esas estrellas con planetas |
| $n_e$ | Número medio de planetas *habitables* (zona «Ricitos de Oro») por sistema |
| $f_l$ | Fracción de esos planetas donde **surge** vida |
| $f_i$ | Fracción de biosferas que evolucionan inteligencia |
| $f_c$ | Fracción de civilizaciones que emiten señales detectables |
| $L$ | Tiempo (años) durante el que emiten |

**El punto crítico de esta SA es $f_l$.**  
Algunos relatos divulgativos razonan, en la práctica:

> «La Tierra está en zona habitable y tiene vida ⇒ si hay zona habitable, hay vida ⇒ $f_l = 1$.»

Eso equipara:

- un **caso observado** (condicionado a que existamos para observarlo), con  
- la **fracción desconocida** de planetas habitables donde la abiogénesis ocurre.

Es estructuralmente parecido a:

> «Me tocó la lotería esta semana ⇒ la probabilidad de que me toque *cualquier* semana es 1.»

### C. Escenario numérico de referencia (solo para el docente)

Valores *ilustrativos* (no «oficiales»):

$$
R_* = 1,\quad f_p = 1,\quad n_e = 0{,}2,\quad f_i = 1,\quad f_c = 0{,}2,\quad L = 10^3
$$

(interpretación: se fijan el resto de factores en un escenario ya optimista/simple para **aislar** $f_l$).

Entonces

$$
N(f_l) = (1)(1)(0{,}2)\,f_l\,(1)(0{,}2)(10^3) = 40 \cdot f_l.
$$

| $f_l$ | $N$ orientativo | Lectura divulgativa |
|---------|-------------------|---------------------|
| $1$ | $40$ | «Decenas de civilizaciones detectables en la galaxia» |
| $0{,}1$ | $4$ | Pocas |
| $10^{-3}$ | $0{,}04$ | Probablemente ninguna *ahora* detectable |
| $10^{-6}$ | $4\cdot 10^{-5}$ | Efectivamente vacío para fines prácticos |
| $10^{-12}$ | $\sim 10^{-11}$ | El producto «se va a cero» |

**Mensaje:** no hace falta que $f_l$ sea «cero mágico»; basta con que sea **moderadamente pequeño** para que el relato optimista se desinfle. El error no es usar Drake; es **fijar $f_l = 1$ como si fuera un dato** cuando es una hipótesis.

### D. Sobre «$p^2$» y el discurso del aula

En clase puede decirse, con rigor:

- La probabilidad de **dos** éxitos independientes encadenados es del orden $p^2$ (lotería dos semanas; o «planeta habitable *y* origen de la vida» si se modelan como factores separados ya desglosados en $n_e$ y $f_l$).
- Poner $f_l = 1$ equivale a afirmar que el segundo éxito (surgir vida) es **casi seguro** una vez dado el primero (planeta en zona habitable). Eso es exactamente la postura que la SA pone en duda.
- Si además $f_i$ también se pone a 1 («si hay vida, habrá inteligencia»), el producto acumula optimismos: $f_l\cdot f_i \approx 1$, cuando cada factor podría ser $\ll 1$ y el producto $p_1 p_2$ **sí** puede ser diminuto.

### E. Frases para clasificar (sesión 3)

1. «Llevo diez semanas sin ganar: la que viene *tiene* que tocar.»  
2. «Gané ayer: estoy en racha, repito.»  
3. «Gané ayer: ya está, no vuelvo a ganar nunca.»  
4. «Gané ayer; mañana la probabilidad es la misma que cualquier día.»  
5. «Hay vida en la Tierra, así que en todo planeta habitable habrá vida.»  
6. «Solo conocemos un planeta con vida; $f_l$ podría ser casi 0 o casi 1: aún no lo sabemos.»

(Solución docente: 1 jugador; 2 mano caliente; 3 jugador invertido; 4 correcta; 5 falacia tipo $f_l=1$; 6 postura epistémicamente cauta.)
