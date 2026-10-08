---
layout: default
title: "El vuelo de la abeja (distancias)"
parent: Situaciones de aprendizaje
nav_order: 23
---

# SA — El vuelo de la abeja: de la gráfica de distancias a la trayectoria

## 0. Metadatos

| Campo | Contenido |
|-------|-----------|
| **Título de la SA** | Volando voy: reconstruir el vuelo a partir de dos distancias |
| **Nivel / curso** | **2.º ESO** (núcleo); ampliación formal en 4.º ESO / 1.º Bach. / máster |
| **Duración** | 3–4 sesiones × 50–55 min (o 1 sesión intensiva de olimpiada + ampliación) |
| **Origen** | Final de la XXX Olimpiada Matemática de 2.º ESO (Aragón) |
| **Fecha / versión** | 2026-10 / v1.0 |
| **Contexto de uso** | Diseño curricular · Practicum · banco de problemas ricos |

**Palabras clave:** lugares geométricos, mediatriz, circunferencia, distancia, gráfica vs trayectoria, problem-solving, modelización, números complejos (ampliación)

**Fuente del problema:** Beltrán-Pellicer, P., & Muñoz-Escolano, J. M. (2023). *Volando voy (Graphing Bee)*: Final de la XXX Olimpiada Matemática de 2.º ESO. *Entorno Abierto*, 50, 4–7.  
[Publicación](https://tierradenumeros.com/publication/202301-ea-olimpiada-vuelo-abeja/)

---

## 1. Pregunta guía / reto

> *La gráfica representa la **distancia** a la que se encuentra una abeja de dos flores (una **rosa** y una **margarita**). Describe y dibuja su trayectoria de vuelo.*

**Producto final esperado:** dibujo de una trayectoria espacial coherente con la gráfica, con **leyenda de tramos** (mediatriz, arco de circunferencia, segmento entre flores, rayo…) y un párrafo que explique por qué **la gráfica no es el mapa del vuelo**.

---

## 2. Claridad conceptual (lo que hay que no confundir)

| Idea errónea frecuente | Idea correcta |
|------------------------|---------------|
| «La gráfica roja *es* el camino de la abeja en el jardín» | La gráfica vive en el **plano de distancias**: eje horizontal = distancia a la rosa ($r$); eje vertical = distancia a la margarita ($m$). |
| «Es la gráfica de una función $y=f(x)$ como en álgebra» | Es una **relación** entre dos magnitudes que cambian a la vez (pueden pensarse como funciones del tiempo, no una de la otra de forma “habitual”). |
| «Hay una sola trayectoria posible» | En el plano hay **al menos dos** (simétricas respecto a la recta que une las flores). Sin tiempo ni sentido de avance, el problema es **abierto**. |
| «Hay que usar números complejos en 2.º» | En 2.º se resuelve con **lugares geométricos**. Los complejos formalizan la misma idea en ampliación. |

**Desigualdad del triángulo (siempre en el fondo):** si la distancia entre flores es $d$, entonces

$$|r - m| \le d \le r + m,\qquad r\ge 0,\; m\ge 0.$$

---

## 3. Justificación y sentido educativo

- Problema **rico y abierto**: exige interpretar una representación no estándar y traducirla a geometría del plano.
- Conecta **sentido espacial**, **medida** y **representación** (Duval: cambio de registro gráfica ↔ dibujo espacial).
- Ideal para **Thinking Classroom**: pizarra vertical, debate de tramos, varias soluciones aceptables si están bien argumentadas.
- Sirve de puente hacia elipses/hipérbolas (definición por distancias a focos) sin nombrarlas aún en 2.º.

---

## 4. Objetivos de aprendizaje

1. Distinguir el **plano de distancias** $(r,m)$ del **plano del jardín** (posición de la abeja).
2. Asociar tramos de la gráfica a **lugares geométricos** clásicos.
3. Reconstruir (dibujar) una trayectoria continua coherente con la gráfica.
4. Argumentar por qué el problema admite **más de una** trayectoria.
5. *(Ampliación)* Formalizar la reconstrucción con intersección de circunferencias / números complejos.

---

## 5. Competencias específicas y criterios

| CE | Criterios (síntesis) | Evidencia |
|----|----------------------|----------|
| **CE1–CE2** | Interpretar y validar | Traducción gráfica → trayectoria |
| **CE3** | Conjeturar | Hipótesis por tramos antes del dibujo final |
| **CE5–CE6** | Conexiones | Distancia + geometría del plano |
| **CE7–CE8** | Representar y comunicar | Dibujo con leyenda + explicación oral/escrita |
| **CE9–CE10** | Socioafectivo | Tolerar ambigüedad; debatir sin “una sola respuesta del libro” |

---

## 6. Saberes y sentidos

| Sentido | Saberes | Prioridad |
|---------|---------|----------|
| Espacial | Mediatriz; circunferencia (centro–radio); rectas; simetría | Alta |
| De la medida | Distancia; desigualdad triangular | Alta |
| Algebraico (ligero) | Segmentos de recta en el plano $(r,m)$: $m=\mathrm{cte}$, $r=m$, $r+m=d$, $r-m=d$ | Media |
| Socioafectivo | Problema abierto; varias soluciones razonables | Alta |

---

## 7. Solución esperada en 2.º ESO (lugares geométricos)

Sea $d$ la distancia entre la rosa $R$ y la margarita $M$. Coloca $R$ y $M$ en el papel. Cada punto de la gráfica es un par $(r,m)$: la abeja está en la **intersección** de la circunferencia de centro $R$ y radio $r$ con la de centro $M$ y radio $m$ (si existe).

### Tabla de tramos (diccionario gráfica → jardín)

| Tramo en la gráfica $(r,m)$ | Condición | Lugar geométrico en el jardín | Cómo vuela la abeja |
|-----------------------------|-----------|-------------------------------|---------------------|
| Horizontal | $m = \mathrm{cte}$ | Circunferencia de centro $M$ | Arco (o tramo) a **distancia fija** de la margarita |
| Vertical | $r = \mathrm{cte}$ | Circunferencia de centro $R$ | Arco a distancia fija de la rosa |
| Sobre la bisectriz | $r = m$ | **Mediatriz** del segmento $RM$ | Línea recta equidistante de ambas flores |
| Une cortes con los ejes (típico) | $r + m = d$ | **Segmento** $RM$ | Entre las dos flores (elipse degenerada) |
| Paralelo a la bisectriz (ej. $m = r - d$) | $r - m = d$ | **Rayo** que sale de $M$ alejándose de $R$ | Línea recta “más allá” de la margarita |
| Simétrico | $m - r = d$ | Rayo desde $R$ alejándose de $M$ | Más allá de la rosa |

### Lectura cualitativa típica del enunciado olímpico

Sin fijar la figura exacta del año, el análisis del artículo y de las figuras de apoyo suele combinar, en algún orden:

1. un tramo a **distancia constante** de una flor (arco de circunferencia),
2. un tramo en la **mediatriz** ($r=m$),
3. un tramo **entre las flores** ($r+m=d$),
4. un tramo en **línea recta alejándose** de una flor pasando por la otra ($|r-m|=d$).

**Construcción en papel (2.º):**

1. Dibujar $R$ y $M$ (elige una $d$ cómoda, p. ej. 2 unidades de cuadrícula).
2. Para cada tramo de la gráfica, dibujar el lugar geométrico correspondiente.
3. Encadenar los tramos **sin saltos** (continuidad): la abeja no se teletransporta.
4. Elegir un lado de la recta $RM$ (arriba o abajo) y mantenerlo, salvo que un tramo fuerce el paso por el segmento.

**Mensaje de cierre para el alumnado:**  
> No buscamos “la” trayectoria del libro; buscamos **cualquier vuelo continuo** cuya pareja de distancias reproduzca la gráfica.

---

## 8. Secuencia de sesiones

| Sesión | Fase | Actividad | Rol docente |
|--------|------|-----------|-------------|
| 1 | Conflicto | Mostrar la gráfica; pedir que dibujen “el vuelo” sin pistas | Recoger dibujos literales de la gráfica roja |
| 1–2 | Reencuadre | “¿Qué miden los ejes?” Colocar dos puntos $R$, $M$ en la pizarra | Forzar la distinción gráfica ≠ mapa |
| 2 | Diccionario | Completar en grupos la tabla tramo → lugar geométrico | Preguntas tipo «si $m$ no cambia, ¿qué curva es?» |
| 3 | Reconstrucción | Dibujar una trayectoria completa + leyenda | Contrastar simétricos arriba/abajo |
| 4 (opc.) | Ampliación | Intersección de circunferencias; esbozo con GeoGebra | Solo quienes avancen; ver §10 |

---

## 9. Evaluación

### Formativa
- Señal de alarma: el dibujo copia la forma de la gráfica en el jardín.
- Pregunta clave: «¿Qué significa un punto del eje horizontal ($m=0$)?» → la abeja está **sobre la margarita**.

### Sumativa (rúbrica breve)

| Nivel | Indicadores |
|-------|-------------|
| Logrado | Distingue planos; al menos 3 tramos bien traducidos; trayectoria continua; admite simetría |
| En proceso | Traduce 1–2 tramos; mezcla aún gráfica y mapa |
| Iniciado | Copia la gráfica como camino espacial |

---

## 10. Ampliación: ¿se puede resolver con números complejos?

**Sí.** No es necesario en 2.º, pero es una formalización elegante (Bachillerato / máster).

### 10.1. Modelo

Coloca la rosa en $0$ y la margarita en $d\in\mathbb{R}^+$ del plano complejo. La abeja está en $z=x+iy$. Entonces

$$r = |z|,\qquad m = |z-d|.$$

La gráfica del problema es una curva de pares $(r,m)$. Para cada par compatible con la desigualdad triangular,

$$
x = \frac{r^{2}-m^{2}+d^{2}}{2d},\qquad
y = \pm\sqrt{r^{2}-x^{2}}.
$$

(Es la **intersección de dos circunferencias**; el $\pm$ son las dos hojas simétricas.)

### 10.2. Coordenadas polares con cada flor como origen

- Origen en la rosa: $z = r\,e^{i\theta}$.
- Origen en la margarita: $z = d + m\,e^{i\varphi}$.

Ley de los cosenos (ángulo $\theta$ en $R$ entre $RM$ y $RP$):

$$m^{2} = r^{2} + d^{2} - 2rd\cos\theta
\quad\Rightarrow\quad
\cos\theta = \frac{r^{2}+d^{2}-m^{2}}{2rd}.$$

Así, cada tramo de la gráfica se traduce en restricciones sobre $(r,\theta)$ o $(m,\varphi)$.

| Condición | Consecuencia polar / compleja |
|-----------|-------------------------------|
| $r=m$ | $\operatorname{Re}(z)=d/2$ (mediatriz) |
| $m=c$ | $|z-d|=c$ (circunferencia centro $M$) |
| $r+m=d$ | $\theta=0$ y $z$ en el segmento $[0,d]$ |
| $r-m=d$ | $\theta=0$ y $z$ en el rayo $[d,+\infty)$ |

### 10.3. ¿“Transformación al plano bi-complejo”?

**No en sentido estricto.** Lo natural es la aplicación

$$
T:\; (x,y)\longmapsto (r,m)=\big(|z|,|z-d|\big)
$$

del plano del jardín al **plano real de distancias**. Su jacobiano es

$$\det DT = \frac{y\,d}{rm}$$

(se anula en $y=0$, la recta de las flores). En el interior de la región triangular, $T$ es **2 a 1**; la inversa exige la raíz $\pm$. Eso se describe mejor como **recubrimiento de dos hojas** (o dos trayectorias espejo), no como plano bi-complejo ($\mathbb{C}^{2}$ sin restricción). El par $(z,\,z-d)$ vive en una **recta compleja** dentro de $\mathbb{C}^{2}$ por la ligadura $z-(z-d)=d$.

**Visualización didáctica avanzada:** a la izquierda el jardín con $R$, $M$ y la trayectoria; a la derecha el plano $(r,m)$ con la gráfica del enunciado; flechas $T$; cuadrícula de circunferencias centradas en $R$ y en $M$ para ver el levantamiento tramo a tramo.

---

## 11. DUA y socioafectivo

| Principio | Medida |
|-----------|--------|
| Implicación | Problema de olimpiada “de verdad”; dibujo en gran formato |
| Representación | Tabla de tramos; GeoGebra (dos deslizadores $r$, $m$) opcional |
| Acción y expresión | Dibujo, oral en pizarra, o audio de 90 s explicando un tramo |

- Validar **varias trayectorias** bien argumentadas.
- Explicitar que “no sé por dónde empieza” no es fracaso: falta el tiempo o el sentido de recorrido.

---

## 12. Orientaciones al docente

- Empezar **sin** la tabla de lugares: dejar que surja el error “copiar la gráfica”.
- Fijar $d$ en la cuadrícula desde el principio.
- Si la figura del año muestra un tramo $m=r-d$, insistir en el rayo exterior (hipérbola degenerada: diferencia de distancias $=d$).
- GeoGebra: dos puntos fijos + punto $P$ + `Distancia(P,R)`, `Distancia(P,M)` y traza de $P$ al moverse con restricción.
- Conexión curricular: prepara definición de **elipse** ($r+m=\mathrm{cte}>d$) e **hipérbola** ($|r-m|=\mathrm{cte}<d$) en cursos posteriores.

---

## 13. Referencias

1. Beltrán-Pellicer, P., & Muñoz-Escolano, J. M. (2023). Volando voy (Graphing Bee). *Entorno Abierto*, 50, 4–7.  
2. RD 217/2022 — sentido espacial y de la medida; resolución de problemas.  
3. Materiales del repo: [registros de representación (Duval)](../../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/registros-representacion-duval.md), [GeoGebra con criterio didáctico](../../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/geogebra-criterio-didactico.md), [modelización](../../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/modelizacion-matematica-aula.md), [Thinking Classrooms](../../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/thinking-classrooms-liljedahl.md).

---

## 14. Anexo rápido — checklist del alumnado (2.º)

- [ ] Sé qué mide cada eje de la gráfica.  
- [ ] No he dibujado la gráfica roja “tal cual” en el jardín.  
- [ ] He colocado rosa y margarita y he marcado $d$.  
- [ ] Cada tramo tiene un nombre geométrico (mediatriz, circunferencia, segmento, rayo…).  
- [ ] Mi trayectoria se puede recorrer sin levantar el lápiz (continuidad).  
- [ ] He dicho si elijo el lado de arriba o el de abajo de la recta de las flores.
