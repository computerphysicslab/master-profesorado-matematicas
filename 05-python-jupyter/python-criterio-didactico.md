# Python y Jupyter con criterio didáctico

**Ámbito:** laboratorio computacional para el Máster de Profesorado · Matemáticas (ESO/Bachillerato)  
**Carpeta:** [05-python-jupyter](.)  
**No es:** un curso genérico de programación ni un sustituto de GeoGebra en geometría dinámica.

> Python/Jupyter es un **medio** para modelizar, simular, representar datos y **verificar** (también código sugerido por IA). El objetivo de aprendizaje sigue siendo matemático: comprender, argumentar, validar.

**Enlaces del repo:** [Unidad tarifas](../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/ejemplo-unidad-tarifas-exigencia-cognitiva.md) · [Unidad perímetro–área](../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/ejemplo-unidad-geometria-perimetro-area.md) · [Modelización](../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/modelizacion-matematica-aula.md) · [GeoGebra didáctico](../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/geogebra-criterio-didactico.md) · [Exigencia cognitiva](../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/exigencia-cognitiva-disciplina-razonamiento.md) · [IA en el aula](../02-apuntes/tecnologia-educativa/ia-en-el-aula-matematicas.md) · [Matriz herramientas IA](../06-inteligencia-artificial/herramientas/matriz-herramientas.md)

---

## 1. Qué aporta (y qué no)

| Aporta | No aporta por sí solo |
|--------|------------------------|
| Automatizar tablas, barridos de parámetros, simulaciones | Comprensión automática del modelo |
| Gráficas reproducibles a partir de datos o fórmulas | Sustituto de la argumentación |
| Verificar un cálculo o un código generado por IA | Criterio de evaluación LOMLOE |
| Pensamiento computacional (descomponer, patrones, depurar) | Equidad si solo una parte del grupo tiene dispositivo |
| Conectar mates con datos reales (CSV sencillos) | Garantía de que el alumno *pensó* el problema |

**Regla práctica:** si la tarea se resuelve *solo* ejecutando celdas sin predecir ni interpretar, el diseño es débil — igual que un GeoGebra de “solo arrastrar”.

---

## 2. Python / Jupyter vs otras herramientas

| Necesitas… | Prioriza |
|------------|----------|
| Geometría dinámica, arrastre, construcciones | **GeoGebra** (o Desmos) |
| Exploración rápida de funciones en Secundaria | Desmos / GeoGebra |
| Barrido sistemático, simulación, datos tabulares, bucles | **Python / Jupyter** |
| Cálculo simbólico fiable puntual | Wolfram\|Alpha (verificación) |
| Sin ordenador | Papel, estimaciones, contraejemplos |

Python **complementa** GeoGebra; no lo reemplaza en el núcleo de geometría dinámica ([criterio GeoGebra](../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/geogebra-criterio-didactico.md)).

---

## 3. Cuatro modos de uso (elige uno por tramo)

| Modo | Intención | El alumno… | El profesor… |
|------|-----------|------------|--------------|
| **A. Exploración / conjetura** | Ver “qué pasa si…” | Cambia un parámetro; formula una regularidad | No regala la fórmula al inicio |
| **B. Modelización** | Traducir situación → código → interpretación | Declara supuestos; valida el resultado | Exige producto *fuera* del notebook |
| **C. Verificación** | Comprobar lo ya razonado en papel | Primero plan o estimación; luego ejecuta | Prohíbe empezar por el código si el objetivo es el plan |
| **D. Auditoría de código (IA)** | Pensamiento crítico digital | Explica qué hace cada bloque; corrige errores | El entregable es el razonamiento + código comentado |

Misma lógica que los modos A–D de GeoGebra y que la **tercera vía** (fluidez al servicio del razonamiento, no al revés).

---

## 4. Criterios para usar Python en *esta* sesión

Úsalo si al menos dos son verdaderas:

- [ ] El **barrido**, la simulación o los datos serían tediosos o opacos solo a mano.  
- [ ] Puedes exigir **predicción** antes de ejecutar y **interpretación** después.  
- [ ] Hay **plan B** (tabla en papel, GeoGebra, calculadora).  
- [ ] El objetivo enlaza con CE de modelizar, representar, computacional o analizar soluciones.

**No lo uses** (o solo demo breve) si:

- pierdes media clase en instalaciones y contraseñas;  
- la demanda real es solo aplicar una fórmula una vez;  
- vas a evaluar solo el `.ipynb` sin defensa ni interpretación;  
- el centro no autoriza el entorno (Colab, cuentas, red).

---

## 5. Orquestación realista

| Escenario | Cómo |
|-----------|------|
| **Solo proyector** | Modo demo: el docente escribe/ejecuta; alumnos predicen en papel |
| **Aula de informática** | Parejas; plantilla ya abierta; consigna matemática en la primera celda Markdown |
| **1:1 / BYOD** | Colab o JupyterLite; norma de uso; evidencia en cuaderno |
| **Pocos PC** | Estaciones: un grupo en Python, otros en papel/GeoGebra; rotación |
| **Sin red** | JupyterLite, notebooks descargados, o abandono elegante del plan digital |

**Tiempo:** cuenta fricción la primera vez (15–20 min). Mejor pocas sesiones potentes al trimestre que “Python todos los viernes” vacío.

---

## 6. Plantilla mental de toda actividad

1. **Pregunta matemática** (no “abre Python”).  
2. **Predicción** en papel o celda Markdown.  
3. **Modelo** (variables, fórmulas, supuestos).  
4. **Código mínimo** (legible; un parámetro claro).  
5. **Ejecución y lectura** del resultado/gráfica.  
6. **Interpretación y validación** en contexto.  
7. **Looking back:** ¿qué harías a mano? ¿qué limita el modelo?

Plantilla de notebook: [jupyter/plantilla-notebook-escolar.ipynb](jupyter/plantilla-notebook-escolar.ipynb) · [versión Markdown](jupyter/plantilla-notebook-escolar.md).

---

## 7. Evaluación: qué puntuar

| Evidencia sólida | Evidencia débil |
|------------------|-----------------|
| Interpretación del output | Notebook sin comentarios ni conclusión |
| Predicción vs resultado | Solo celdas copiadas de un chat |
| Supuestos y límites del modelo | Gráfica sin ejes ni unidades |
| Explicación oral o párrafo final | “Me salió en Python” |

En pruebas: Python puede ser **permitido para verificar** (modo C) o **prohibido** si mides el plan a mano. Coherencia con el criterio.

---

## 8. Python e inteligencia artificial

| Uso legítimo | Riesgo |
|--------------|--------|
| Pedir a la IA un esqueleto y **auditarlo** | Entregar código que el alumno no entiende |
| Depurar un error con ayuda y explicar el fallo | Pegar datos personales del alumnado en el chat |
| Generar variantes de parámetros | Sustituir el modelo mental por prueba-error en el chat |

Flujo recomendado: **enunciado → intento propio → (opcional) código de IA → ejecutar aquí → contrastar → explicar**.  
Detalle ético y de aula: [IA en Matemáticas](../02-apuntes/tecnologia-educativa/ia-en-el-aula-matematicas.md).

---

## 9. Competencias LOMLOE (orientación)

| CE | Cómo puede ayudar Python |
|----|--------------------------|
| **1** Modelizar / resolver | Implementar el modelo y explorar parámetros |
| **2** Analizar soluciones | Validar magnitudes, signos, extremos |
| **4** Pensamiento computacional | Descomponer, bucles, patrones, depurar |
| **7** Representar | Tablas y gráficas generadas con criterio |
| **8** Comunicar | Narrar en Markdown qué hace el modelo |

No hace falta “dar Python” como contenido autónomo del currículo de Matemáticas: se usa cuando **mejora** una de estas demandas.

---

## 10. Conexión con unidades ya publicadas

| Unidad del repo | Uso de Python |
|-----------------|---------------|
| [Tarifas / función afín](../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/ejemplo-unidad-tarifas-exigencia-cognitiva.md) | Tras predecir el cruce: tablas y gráficas de dos costes; sensibilidad a la cuota | Notebook: [matematicas/tarifas-funcion-afin.ipynb](matematicas/tarifas-funcion-afin.ipynb) |
| [Perímetro–área](../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/ejemplo-unidad-geometria-perimetro-area.md) | Barrido de lados con área fija; perímetro vs forma (sesión de ampliación o reserva) |

En la secuencia de tarifas, Python encaja sobre todo en **sesión 4** (después de la predicción y del modelo en papel), no en la apertura de la sesión 1.

---

## 11. Checklist docente (5 minutos)

- [ ] Objetivo matemático en una frase  
- [ ] Modo A/B/C/D elegido  
- [ ] Predicción o producto sin depender del notebook  
- [ ] Entorno probado (Colab / local / plan B)  
- [ ] Código mínimo y legible en la plantilla  
- [ ] Norma de dispositivos y privacidad  

---

## 12. Qué hay en esta carpeta (mapa)

| Ruta | Contenido |
|------|-----------|
| [README](README.md) · [INDICE](INDICE.md) | Puerta de entrada |
| Este archivo | Criterio didáctico |
| [jupyter/](jupyter/) | Plantilla de notebook y notas de entorno |
| [matematicas/](matematicas/) | Notebooks ligados a objetos escolares |
| [python/](python/), [numpy/](numpy/), [pandas/](pandas/), [visualizacion/](visualizacion/) | Mini-bases (se irán llenando) |
| [actividades/](actividades/) | Fichas de sesión (markdown) |
| [fisica/](fisica/) | Contextos STEM ligeros (opcional) |

---

*Orientativo para el Máster de Profesorado · Matemáticas. La herramienta no evalúa: evalúa el razonamiento que el diseño logra hacer visible.*
