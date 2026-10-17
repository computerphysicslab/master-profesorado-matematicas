# Situación de aprendizaje: Las diez caras de *e*

**Asignatura:** Diseño curricular e instruccional de Matemáticas  
**Nivel prioritario:** 1.º Bachillerato (Matemáticas I o Matemáticas aplicadas a las CCSS I)  
**Extensión opcional:** 2.º Bachillerato (Matemáticas II: serie, números complejos, identidad de Euler)  
**Duración orientativa:** 6–8 sesiones  
**Enfoque:** ascenso de lo abstracto a lo concreto (Elkonin-Davydov)  
**Material visual:** [The 10 Faces of e (SVG)](10-faces-of-e.svg)  
**Marco TFM:** [Idea 21 — orden abstracto→concreto](../../trabajo-fin-de-master/ideas-interesantes/21-elkonin-davydov-abstracto-concreto.md)

---

## 1. Justificación didáctica

La constante *e* es un objeto matemático que concentra varias representaciones (límite, serie, función igual a su derivada, inversa del logaritmo natural, ley de crecimiento/decaimiento) y aparece en contextos muy distintos (finanzas, física, probabilidad).

Una secuencia **concreto-primero** (empezar por el interés compuesto o por la radiactividad y «descubrir» *e*) corre el riesgo de dejar el modelo abstracto diluido o tardío. Esta situación de aprendizaje **invierte el orden**:

1. Se presenta y consolida el **modelo abstracto** (límite / serie / propiedad diferencial).
2. Se especializa en **dos aplicaciones** (interés continuo y decaimiento).
3. Se cierra con la **síntesis**: la misma estructura bajo distintas «caras».

Así se alinea con la tesis de la ficha 21: la educación secundaria debe aprovechar la ventana evolutiva de la adolescencia para el pensamiento teórico, sin convertir la contextualización en fin en sí mismo. Las aplicaciones son necesarias y significativas; no son el punto de partida exclusivo.

---

## 2. Objetivos de aprendizaje

Al finalizar la situación, el alumnado será capaz de:

1. **Definir** *e* como límite \(\displaystyle e = \lim_{n\to\infty}\bigl(1+\frac{1}{n}\bigr)^n\) y/o como serie \(\displaystyle e = \sum_{n=0}^{\infty}\frac{1}{n!}\), y aproximar su valor.
2. **Reconocer** que la función \(f(x)=e^x\) es (salvo factor constante) la única que coincide con su derivada, y relacionarla con \(\ln\) como inversa.
3. **Modelizar** situaciones de crecimiento o decaimiento continuo mediante \(A = P e^{rt}\) o \(N(t)=N_0 e^{-\lambda t}\), interpretando parámetros.
4. **Transferir** el modelo a un contexto nuevo no trabajado en clase (transferencia lejana).
5. **Explicar** qué se mantiene invariante al pasar de una «cara» de *e* a otra (estructura de crecimiento proporcional a la cantidad presente).

---

## 3. Saberes básicos y competencias (orientación LOMLOE / Bachillerato)

| Dimensión | Contenido orientativo |
|-----------|----------------------|
| **Saberes** | Límites de sucesiones; número *e*; función exponencial y logarítmica; derivada de \(e^x\); modelos de crecimiento/decaimiento continuo |
| **Competencias específicas** | Modelización; sentido algebraico; sentido de la medida; resolución de problemas; comunicación matemática |
| **Criterios de evaluación (ideas)** | Definir y aproximar *e*; derivar e integrar \(e^x\) en casos simples; plantear y resolver un modelo continuo; argumentar la invariancia estructural entre contextos |

*Ajustar al decreto autonómico de Bachillerato vigente (Aragón u otra CCAA).*

---

## 4. Secuencia sesión a sesión

### Sesión 1 — El modelo: límite y aproximación (cara 3)

| Elemento | Detalle |
|----------|--------|
| **Arranque** | Mostrar la infografía [10 Faces of e](10-faces-of-e.svg) sin explicar aún las aplicaciones. Pregunta: «¿Qué tienen en común todas estas fórmulas?» |
| **Desarrollo** | Definición \(e = \lim_{n\to\infty}(1+1/n)^n\). Tabla de valores para \(n=1,2,5,10,100,1000\). Interpretación como interés compuesto con capitalización cada vez más frecuente (solo como *motivación*, no como destino). |
| **Cierre** | *e* es un número concreto (~2,718…) definido por una estructura de límite. |
| **Producto** | Tabla de aproximaciones + frase: «*e* es el límite de…» |

### Sesión 2 — Serie y derivada (caras 4 y 5)

| Elemento | Detalle |
|----------|--------|
| **Arranque** | «Otra cara del mismo número»: serie \(e = \sum 1/n!\). Cálculo de sumas parciales. |
| **Desarrollo** | Propiedad \(\frac{d}{dx}e^x = e^x\). Argumento informal (serie término a término) o a partir de la definición de derivada. Contraste con \(a^x\) cuando \(a\neq e\). |
| **Cierre** | *e* caracteriza la función que es su propia tasa de cambio. |
| **Producto** | Demostración/justificación breve o ejercicios de derivación de \(e^{kx}\). |

### Sesión 3 — Logaritmo natural e integral (caras 6 y 7)

| Elemento | Detalle |
|----------|--------|
| **Arranque** | «Si \(e^x\) crece como ella misma, ¿quién deshace ese crecimiento?» |
| **Desarrollo** | \(\ln\) como inversa de \(e^x\). \(\int e^x\,dx = e^x+C\). Ecuación \(y'=ky\) y solución \(y=y_0 e^{kt}\). |
| **Cierre** | El modelo diferencial \(y'=ky\) es la estructura profunda. |
| **Producto** | Resolver \(y'=ky\) con condición inicial; graficar. |

### Sesión 4 — Especialización A: interés compuesto continuo (cara 8)

| Elemento | Detalle |
|----------|--------|
| **Arranque** | Del modelo \(A=P e^{rt}\) al banco: capitalización continua. |
| **Desarrollo** | Problemas con *P*, *r*, *t* dados; despejar tiempo o tipo; comparar con capitalización anual/mensual. |
| **Cierre** | La finanza es una *cara* del mismo modelo \(y'=ry\). |
| **Producto** | Informe breve (1 página): planteamiento, cálculo, interpretación. |

### Sesión 5 — Especialización B: decaimiento (cara 10)

| Elemento | Detalle |
|----------|--------|
| **Arranque** | Mismo modelo, signo negativo: \(N=N_0 e^{-\lambda t}\). |
| **Desarrollo** | Vida media / semiperiodo; problemas de radiactividad, enfriamiento o descarga de condensador (elegir uno). |
| **Cierre** | Crecimiento y decaimiento son dos orientaciones de la misma estructura. |
| **Producto** | Problema resuelto con gráfica e interpretación de \(\lambda\). |

### Sesión 6 — Transferencia lejana y síntesis

| Elemento | Detalle |
|----------|--------|
| **Arranque** | Contexto *nuevo* no visto en clase (p. ej. concentración de un fármaco, población de bacterias, o amortiguamiento simple). |
| **Desarrollo** | El alumnado identifica si cabe el modelo exponencial, escribe la ecuación y resuelve. |
| **Síntesis** | Volver a la infografía: localizar las caras trabajadas; redactar en 5–8 líneas qué se mantiene invariante. |
| **Producto final** | Mapa conceptual o póster «Las caras de *e* que conocemos» + resolución del contexto nuevo. |

### Sesiones 7–8 (opcional, 2.º Bach. Matemáticas II)

- Serie de Taylor de \(e^x\) con más rigor.  
- Fórmula de Euler \(e^{ix}=\cos x+i\sin x\) e identidad \(e^{i\pi}+1=0\) (caras 1 y 2).  
- Puente (cara 9) hacia la integral gaussiana y la campana de Gauss (solo motivación, sin demostración completa).

---

## 5. Evaluación

| Evidencia | Criterio principal | Instrumento |
|-----------|-------------------|-------------|
| Aproximación de *e* (límite o serie) | Define y aproxima con sentido | Ejercicio / tabla |
| Derivación e integración de \(e^{kx}\) | Aplica la propiedad diferencial | Prueba breve |
| Modelo de interés o decaimiento | Plantea, resuelve e interpreta | Informe / problema |
| Transferencia a contexto nuevo | Reconoce la estructura en situación no entrenada | Tarea de transferencia |
| Síntesis oral o escrita | Explica la invariancia entre caras | Póster + defensa breve |

**Evaluación formativa:** feedback en sesiones 1–3 sobre el uso correcto del límite/serie y de la notación; en 4–5 sobre la interpretación de parámetros (no solo el número final).

---

## 6. Principios didácticos aplicados (ficha 21)

| Principio | Cómo se concreta aquí |
|-----------|----------------------|
| **1. No confundir accesibilidad con concreción** | El límite y la serie se presentan aunque sean exigentes; se andamia con tablas y sumas parciales. |
| **2. Contextualizar para abstraer** | Finanzas y decaimiento *después* del modelo, para descubrir que son caras de la misma estructura. |
| **3. Diseñar para la transferencia lejana** | Sesión 6: contexto no ensayado. |
| **4. Fomentar el habla interna** | Exigir explicación verbal/escrita de «qué se mantiene» entre caras. |
| **5. Abstracción como competencia vital** | Anticipar (crecimiento futuro, semivida) es un uso de la estructura abstracta, no solo un truco de cálculo. |

---

## 7. Atención a la diversidad (DUA, orientativo)

- **Acceso:** tablas precalculadas de \((1+1/n)^n\); calculadora; gráficas GeoGebra de \(e^x\) y \(\ln x\).  
- **Andamiaje:** plantilla de modelización (identificar *P* o \(N_0\), *r* o \(\lambda\), *t*).  
- **Reto:** demostrar la derivada a partir de la serie; identidad de Euler (si el grupo lo permite).  
- **Expresión:** producto final puede ser póster, vídeo corto o informe escrito.

---

## 8. Recursos

- Infografía: [10-faces-of-e.svg](10-faces-of-e.svg)  
- GeoGebra: deslizador *n* para \((1+1/n)^n\); gráficas \(e^x\), \(\ln x\), \(N_0 e^{-\lambda t}\).  
- Calculadora científica / hoja de cálculo para sumas parciales de la serie.  
- Ficha TFM 21 (marco teórico abstracto→concreto).

---

## 9. Relación con la LOMLOE (matiz)

Esta situación **es** una situación de aprendizaje en el sentido de la norma: contextualizada, competencial, con producto y evaluación formativa.  
La diferencia de énfasis respecto a una lectura puramente pragmática es el **orden**:

- No se parte de «la vida real» para llegar, si acaso, al concepto.  
- Se parte del **modelo abstracto** y se desciende a las aplicaciones, de modo que la contextualización sea medio de comprensión y transferencia, no criterio único de selección de contenidos.

Eso es coherente con la tensión teórica de la ficha 21: justificación *desarrollista-emancipadora* de la abstracción (Davydov, Vygotsky, funciones ejecutivas) frente a una justificación *solo* pragmática (utilidad inmediata en contextos de vida real).

---

## 10. Referencias breves

- Davydov / tradición Elkonin-Davydov — ascenso de lo abstracto a lo concreto.  
- RD de Bachillerato vigente (enseñanzas mínimas y decreto autonómico).  
- [Idea TFM 21](../../trabajo-fin-de-master/ideas-interesantes/21-elkonin-davydov-abstracto-concreto.md).  
- Infografía adaptada a partir de material educativo de difusión sobre las «caras» de *e*.
