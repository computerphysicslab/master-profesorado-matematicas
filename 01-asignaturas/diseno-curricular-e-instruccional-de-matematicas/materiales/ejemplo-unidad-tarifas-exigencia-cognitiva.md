# Ejemplo de unidad · Tarifas y función afín (tercera vía)

**Curso orientativo:** 3.º ESO (adaptable a 2.º con menos formalización / 4.º con más rigor)  
**Sesiones:** 6 (+ 1 de reserva)  
**Objeto:** relación afín $y = mx + n$ como **modelo** de tarifas (fijo + variable)  
**Propósito de este documento:** mostrar en una programación real la **tercera vía**: práctica de fluidez *y* problemas de alta demanda cognitiva, con evaluación alineada — sin caricaturizar “solo repetición” ni “solo descubrimiento”.

**Unidad hermana (misma arquitectura, otro objeto):** [Geometría · perímetro y área](ejemplo-unidad-geometria-perimetro-area.md)

**Laboratorio Python (sesión 4 o reserva, *después* de predecir en papel):**  
[Notebook tarifas](../../../05-python-jupyter/matematicas/tarifas-funcion-afin.ipynb) · [Ficha de actividad](../../../05-python-jupyter/actividades/actividad-tarifas-python.md) · [Criterio Python](../../../05-python-jupyter/python-criterio-didactico.md)

**Marcos del repo:** [Exigencia cognitiva y disciplina](exigencia-cognitiva-disciplina-razonamiento.md) · [Thinking Classrooms](thinking-classrooms-liljedahl.md) · [Modelización](modelizacion-matematica-aula.md) · [Duval](registros-representacion-duval.md) · [Función lineal](fichas-objetos/funcion-lineal.md) · [Plantilla UD](plantillas/unidad-didactica.md) · [Heurísticas](banco-problemas/heuristicas-y-mediacion.md)

---

## 1. Identificación

| Campo | Contenido |
|-------|-----------|
| Título | *¿Qué tarifa conviene?* Modelos afines y decisión |
| Materia / curso | Matemáticas · 3.º ESO |
| Posición | Tras proporcionalidad directa; antes de sistemas formales (o en paralelo) |
| Sesiones | 6 + 1 reserva |

---

## 2. Intención didáctica

Al terminar, el alumnado debería poder:

1. **Modelizar** una tarifa (cuota fija + coste por unidad) en tabla, gráfica y expresión $y = mx + n$.  
2. **Interpretar** $m$ (ritmo de cambio) y $n$ (coste fijo / valor inicial) en contexto.  
3. **Comparar** dos tarifas y argumentar a partir de qué consumo conviene cada una.  
4. **Validar** si un resultado o una gráfica tienen sentido (unidades, extremos, letra pequeña).  
5. **Comunicar** el razonamiento (no solo el número del punto de corte).

### Saberes (por sentidos, orientativo)

| Sentido | Saberes |
|---------|--------|
| Algebraico | Patrones; expresión de dependencias; parámetros |
| Numérico | Operaciones con decimales; estimación |
| Espacial / gráfico | Lectura y construcción de gráficas de rectas |
| Socioafectivo | Perseverancia ante el bloqueo; error como información |

### CE prioritarias (2–4 por unidad, no las diez)

| CE | Foco en esta unidad |
|----|---------------------|
| **1** | Modelizar y resolver la decisión de tarifas |
| **2** | Analizar y validar la solución en contexto |
| **7** | Coordinar tabla ↔ gráfica ↔ símbolo |
| **8** | Explicar la elección de tarifa |
| **9** | (transversal) Sostener el esfuerzo en el problema abierto |

### Criterios → evidencias (síntesis; adapta códigos de tu CCAA)

| Qué se observa | Evidencia |
|----------------|-----------|
| Traduce la situación a un modelo | Tabla + expresión o gráfica coherentes |
| Interpreta parámetros | Frase sobre $m$ y $n$ en euros y unidades |
| Compara y decide | Punto de corte justificado (álgebra o gráfica) |
| Valida | Comentario sobre un extremo o un supuesto |
| Comunica | Explicación oral 1–2 min o párrafo escrito |

---

## 3. Análisis breve del objeto

| Pregunta | Respuesta |
|----------|-----------|
| Tipo de objeto | Concepto + modelo (dependencia regular) |
| Significados prioritarios | Modelo de tarifa; $m$ = coste por unidad; $n$ = fijo |
| Fenómenos | Móvil, luz, suscripciones, taxi |
| Representaciones | Verbal, tabular, gráfica, simbólica (Duval) |
| Obstáculos | Confundir $m$ con altura; extrapolación ciega; “la más barata” sin mirar el uso |

Detalle: [ficha función lineal](fichas-objetos/funcion-lineal.md).

---

## 4. Hilo conductor

> Dos (o tres) ofertas reales o realistas de datos / móvil. El alumnado debe **decidir** qué conviene según el uso mensual y **explicar** la decisión con más de una representación. Al final, critica un anuncio que diga “la más barata del mercado” sin condiciones.

Nivel de modelización: **2–3** ([modelización](modelizacion-matematica-aula.md)).

---

## 5. Lógica de la tercera vía en la secuencia

| Tipo de actividad | Función didáctica | Cuándo |
|-------------------|-------------------|--------|
| **Problema rico / exploración** | Construir necesidad del modelo; alta demanda cognitiva | Sesiones 1–2, 4 |
| **Institucionalización** | Fijar $y=mx+n$, vocabulario, notación | Finales de 2 y 3 |
| **Fluidez mecánica** | Automatizar cálculos de tabla y de $m$ dados dos puntos | Sesión 3 (acotada) |
| **Conversión de registros** | Profundidad (Duval), no solo cuentas | 2, 3, 5 |
| **Validación y comunicación** | CE.2 y CE.8 | 4, 5, 6 |
| **Python (opcional)** | Tabla, gráfica, sensibilidad a un parámetro | Sesión 4 o reserva, *tras* predicción en papel |

**No** es: 4 sesiones de ejercicios idénticos y un “problema de aplicación” el último día.  
**No** es: solo exploración sin formalizar ni practicar.

---

## 6. Secuencia de sesiones

| Sesión | Objetivo | Actividad principal | Demanda | Evidencia |
|--------|----------|---------------------|---------|-----------|
| **1** | Entrar en la situación; estructurar datos | Problema de dos tarifas *sin* anunciar “función afín”. Individual → parejas. Predicción: “¿quién gana si uso poco / mucho?” | **Alta** | Borrador de estrategia |
| **2** | Emerger tabla y gráfica; conjeturar el cruce | Thinking Classroom / vertical o pósters. Institucionalizar “punto de equilibrio” | **Alta** | Esquema / póster |
| **3** | Formalizar $y=mx+n$; fluidez controlada | Cierre simbólico + bloque corto de fluidez (8–10 ítems) | **Media** | Mini-quiz |
| **4** | Comparar tarifas; validar; opcional Python | Tercera tarifa o cambio de parámetro. Opcional: [notebook](../../../05-python-jupyter/matematicas/tarifas-funcion-afin.ipynb) *después* de predecir | **Alta** | Resolución + supuestos |
| **5** | Error plantado + comunicación | Gráfica y conclusión incoherentes; corregir | **Alta** | Texto + justificación |
| **6** | Evaluación + metacognición | Prueba mixta. *Looking back* | Mixta | Prueba |
| **R** | Reserva | Refuerzo, ampliación o laboratorio Python completo | — | — |

---

## 7. Detalle de tareas clave

### Tarea A — Apertura (sesión 1)

**Enunciado:**  
Tarifa A: 10 €/mes + 0,05 € por MB extra.  
Tarifa B: 6 €/mes + 0,12 € por MB extra.  
¿A partir de qué consumo mensual conviene cada una? ¿Qué harías si no pudieras “probar” de 10 en 10 MB?

| Campo | Contenido |
|-------|-----------|
| Función | Introducir (problema primero) |
| Mediación | «¿Qué es fijo y qué cambia?»; no regalar aún $y=mx+n$ |
| CE | 1, 9 |

### Tarea B — Fluidez acotada (sesión 3)

Completar tabla; hallar $m$ y $n$; leer gráfica. Límite 15–20 min.

### Tarea C — Alta demanda (sesión 4–5)

Anuncio “la más barata” con letra pequeña; supuestos del modelo; análogo estructural con [geometría P–A](ejemplo-unidad-geometria-perimetro-area.md).

**Extensión digital:** [actividad-tarifas-python.md](../../../05-python-jupyter/actividades/actividad-tarifas-python.md).

### Tarea D — Error plantado (sesión 5)

Gráfica y conclusión incompatible; localizar la ruptura del argumento.

---

## 8. Evaluación de la unidad

| Instrumento | Qué mide | Peso orientativo |
|-------------|----------|------------------|
| Productos sesiones 1–2 | Estrategias | Formativo |
| Mini-fluidez sesión 3 | Tabla, $m$, $n$ | 20 % |
| Resolución comentada | Modelizar, decidir, validar | 40 % |
| Prueba sesión 6 | Mixta | 30 % |
| Metacognición | Estrategia | 10 % |

Si se usa el notebook: valorar **interpretación y predicción**, no solo que el código ejecute.

### Prueba breve (modelo)

1. Mecánico: $y = 0{,}1x + 8$ para $x = 30$.  
2. Conversión: tabla → expresión.  
3. Alta demanda: corte en 80 MB; ¿quién conviene por debajo?  
4. Validación: coste −15 € → ¿qué concluyes?

### Rúbrica (producto de decisión)

| Dimensión | En desarrollo | Adecuado | Sólido |
|-----------|---------------|----------|--------|
| Modelo | Números sueltos | Expresión o gráfica usable | + interpretación $m$, $n$ |
| Decisión | Sin apoyo | Corte correcto | + para qué usuarios |
| Validación | Ausente | Un comentario | Supuestos o sensibilidad |
| Comunicación | Solo cifra | Claro | Argumento ordenado |

---

## 9–13. Diversidad, gestión, familias, margen, autoevaluación

Ver versiones anteriores del documento en el historial del repo si necesitas el detalle completo; criterios estables:

- Rutas A/B/C de andamiaje; misma CE.  
- Norma: el error se discute.  
- Mensaje a familias: modelizar y justificar, no solo cuentas.  
- Checklist docente: alta demanda real; fluidez acotada *después* del sentido; prueba no solo cálculo.

---

## 14. Mapa de lectura

```text
Exigencia cognitiva (marco)
        ↓
┌──────────────────┬────────────────────────────┐
│ Unidad tarifas   │ Unidad geometría P–A       │
└────────┬─────────┴────────────────────────────┘
         ↓
   Notebook Python (opcional, sesión 4)
```

---

*Ejemplo orientativo para el Máster de Profesorado · Matemáticas.*
