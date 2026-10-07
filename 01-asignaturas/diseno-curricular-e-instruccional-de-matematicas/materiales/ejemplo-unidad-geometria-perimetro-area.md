# Ejemplo de unidad · Perímetro, área y razonamiento geométrico (tercera vía)

**Curso orientativo:** 1.º–2.º ESO (núcleo); ampliable a 3.º con argumentación más formal  
**Sesiones:** 6 (+ 1 de reserva)  
**Objeto:** relación entre **perímetro** y **área** en rectángulos (y extensión a figuras compuestas); distinción de magnitudes; argumentación y contraejemplos  
**Propósito:** misma lógica que la [unidad de tarifas](ejemplo-unidad-tarifas-exigencia-cognitiva.md): exploración de alta demanda → formalización → fluidez acotada → validación/error plantado → evaluación mixta.

**Laboratorio Python (sesión 4 o reserva, *después* de conjetura en papel):**  
[Notebook perímetro–área](../../../05-python-jupyter/matematicas/perimetro-area-rectangulos.ipynb) · [Ficha de actividad](../../../05-python-jupyter/actividades/actividad-perimetro-area-python.md) · [Criterio Python](../../../05-python-jupyter/python-criterio-didactico.md)

**Marcos del repo:** [Exigencia cognitiva](exigencia-cognitiva-disciplina-razonamiento.md) · [Thinking Classrooms](thinking-classrooms-liljedahl.md) · [Duval](registros-representacion-duval.md) · [Bloque 8](../apuntes/08-resolucion-de-problemas.md) · [Problemas ricos](banco-problemas/problemas-ricos.md) · [Plantilla UD](plantillas/unidad-didactica.md) · [Gestión de aula](../../procesos-y-contextos-educativos/materiales/gestion-aula-disrupcion-matematicas.md)

---

## 1. Identificación

| Campo | Contenido |
|-------|-----------|
| Título | *¿Misma área, mismo perímetro?* Magnitudes, argumentación y diseño |
| Materia / curso | Matemáticas · 1.º–2.º ESO (adaptar rigor) |
| Posición | Tras unidades de longitud y sentido de la medida; antes o junto a áreas de triángulos/compuestas |
| Sesiones | 6 + 1 reserva |

---

## 2. Intención didáctica

Al terminar, el alumnado debería poder:

1. **Distinguir** perímetro (longitud) y área (superficie) y no usar las fórmulas de forma intercambiable.  
2. **Calcular** perímetro y área de rectángulos (y de alguna figura compuesta sencilla) con unidades coherentes.  
3. **Argumentar** con un **contraejemplo** que igual área no implica igual perímetro (y, si se trabaja, el recíproco).  
4. **Diseñar** rectángulos con una condición fija (área o perímetro dado) y explorar lo que varía.  
5. **Comunicar** la justificación (dibujo + números + frase), no solo el resultado numérico.

### Saberes (por sentidos, orientativo)

| Sentido | Saberes |
|---------|--------|
| De la medida | Perímetro, área; unidades; estimación |
| Espacial | Figuras planas; composición; visualización |
| Numérico | Producto, suma; relaciones entre lados |
| Algebraico (ligero) | Expresar perímetro/área con lados $a$, $b$ |
| Socioafectivo | Perseverar; usar el error como información |

### CE prioritarias

| CE | Foco en esta unidad |
|----|---------------------|
| **1** | Resolver problemas de medida y diseño |
| **2** | Analizar la validez de afirmaciones («si misma área…») |
| **3** | Conjeturar y comprobar con casos |
| **7** | Representar (dibujo acotado, tabla de lados, expresión) |
| **8** | Argumentar el contraejemplo |
| **9** | Sostener el esfuerzo cuando la intuición falla |

### Criterios → evidencias

| Qué se observa | Evidencia |
|----------------|-----------|
| Calcula con sentido | Perímetro/área correctos + unidades |
| Distingue magnitudes | No confunde u.l. con u.l.² en la explicación |
| Contraejemplo | Dos rectángulos distinta forma, misma área, perímetros distintos |
| Diseño bajo restricción | Tabla o dibujos de varios rectángulos de área 24 |
| Comunicación | Justificación oral o escrita del «no necesariamente» |

---

## 3. Análisis breve del objeto

| Pregunta | Respuesta |
|----------|-----------|
| Tipo de objeto | Conceptos de magnitud + relación no biunívoca entre ellas |
| Significados | Perímetro = contorno; área = región; independencia relativa |
| Fenómenos | Vallas y terrenos, marcos y cristales, packaging, huertos |
| Representaciones | Figural, numérica, tabular, verbal, simbólica ligera |
| Obstáculos | «Más perímetro ⇒ más área»; fórmulas sin magnitud; conteo erróneo en cuadrícula |

**Idea nuclear de alta demanda:**

> Dos rectángulos tienen la misma área. ¿Tienen necesariamente el mismo perímetro? Razona y da un contraejemplo si es falso.

---

## 4. Hilo conductor

> Un colegio quiere cercar un huerto rectangular de **24 m²**. Hay presupuesto limitado de valla (perímetro). ¿Todas las formas de 24 m² gastan la misma valla? ¿Qué forma minimiza la valla entre opciones razonables?

---

## 5. Lógica de la tercera vía

| Tipo de actividad | Función | Cuándo |
|-------------------|---------|--------|
| Problema rico / conjetura | Romper la intuición; alta demanda | Sesiones 1–2, 4 |
| Institucionalización | $P=2(a+b)$, $A=a·b$, unidades | Final 2–3 |
| Fluidez acotada | Cálculos variados | Sesión 3 |
| Diseño y validación | Área fija; error plantado | 4–5 |
| **Python (opcional)** | Tabla de divisores, gráfica $P(a)$ | Sesión 4 o reserva, *tras* papel |
| Evaluación mixta | Mecánico + argumentación | 6 |

---

## 6. Secuencia de sesiones

| Sesión | Objetivo | Actividad principal | Demanda |
|--------|----------|---------------------|--------|
| **1** | Contorno vs región | Cuadrícula: dos figuras de 12 cuadrados | Alta |
| **2** | Conjetura + contraejemplos | *¿Misma área ⇒ mismo perímetro?* | Alta |
| **3** | Fórmulas + fluidez | $A$, $P$; ítems acotados | Media |
| **4** | Huerto 24 m² | Tabla lados enteros; opcional [notebook](../../../05-python-jupyter/matematicas/perimetro-area-rectangulos.ipynb) | Alta |
| **5** | Error plantado | “Misma área ⇒ mismo coste de valla” | Alta |
| **6** | Evaluación | Prueba mixta | Mixta |
| **R** | Reserva | Compuestas, o laboratorio Python completo | — |

---

## 7. Tareas clave (resumen)

- **A:** cuadrícula 12 cuadrados.  
- **B:** afirmar/refutar con contraejemplo.  
- **C:** fluidez 15–20 min.  
- **D:** huerto 24 m² + presupuesto 22 m; extensión digital [actividad-perimetro-area-python.md](../../../05-python-jupyter/actividades/actividad-perimetro-area-python.md).  
- **E:** texto erróneo sobre coste de valla.

---

## 8. Evaluación

Instrumentos: productos 1–2 (formativo), fluidez 20 %, argumentación/huerto 40 %, prueba 30 %, metacognición 10 %.

Prueba: ítem mecánico + L + «mismo perímetro ⇒ misma área?» + validación de unidades.

Si se usa el notebook: valorar **predicción y contraejemplo**, no solo la ejecución.

---

## 9–13. Diversidad, gestión, familias, margen, autoevaluación

- Rutas de andamiaje; norma de aportar ejemplo.  
- Mensaje a familias: calcular **y** razonar sobre valla vs superficie.  
- Checklist: conjetura antes de solo mecanizar; fluidez acotada; argumentación evaluada.

---

## 14. Comparación con tarifas

| | Tarifas / afín | Geometría P–A |
|--|----------------|---------------|
| Conflicto | “La más barata” sin uso | “Misma área ⇒ misma valla” |
| Notebook | [tarifas-funcion-afin](../../../05-python-jupyter/matematicas/tarifas-funcion-afin.ipynb) | [perimetro-area-rectangulos](../../../05-python-jupyter/matematicas/perimetro-area-rectangulos.ipynb) |

---

## 15. Extensiones

- Mismo perímetro ⇒ ¿misma área?  
- GeoGebra: área constante y deslizador ([criterio](geogebra-criterio-didactico.md)).  
- Python: gráfica $P(a)$ en el notebook de esta unidad.

---

*Ejemplo orientativo para el Máster de Profesorado · Matemáticas.*
