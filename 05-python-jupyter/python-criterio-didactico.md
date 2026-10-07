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

**Regla práctica:** si la tarea se resuelve *solo* ejecutando celdas sin predecir ni interpretar, el diseño es débil.

---

## 2. Python / Jupyter vs otras herramientas

| Necesitas… | Prioriza |
|------------|----------|
| Geometría dinámica, arrastre | **GeoGebra** / Desmos |
| Barrido sistemático, simulación, datos | **Python / Jupyter** |
| Sin ordenador | Papel, estimaciones, contraejemplos |

---

## 3. Cuatro modos de uso

| Modo | Intención |
|------|-----------|
| **A. Exploración** | «Qué pasa si…» |
| **B. Modelización** | Situación → código → interpretación |
| **C. Verificación** | Comprobar lo ya razonado en papel |
| **D. Auditoría de código (IA)** | Explicar y corregir código generado |

---

## 4–8. Orquestación, plantilla, evaluación, IA, CE

Detalle operativo en las secciones del historial del archivo y en la [plantilla](jupyter/plantilla-notebook-escolar.ipynb): predicción → modelo → código → interpretación → *looking back*.

Evaluar interpretación y supuestos, no solo que el `.ipynb` ejecute.

---

## 9. Conexión con unidades publicadas

| Unidad | Notebook | Momento |
|--------|----------|--------|
| [Tarifas / afín](../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/ejemplo-unidad-tarifas-exigencia-cognitiva.md) | [tarifas-funcion-afin.ipynb](matematicas/tarifas-funcion-afin.ipynb) | Sesión 4 o reserva, tras predecir el cruce |
| [Perímetro–área](../01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/materiales/ejemplo-unidad-geometria-perimetro-area.md) | [perimetro-area-rectangulos.ipynb](matematicas/perimetro-area-rectangulos.ipynb) | Sesión 4 (huerto) o reserva, tras conjetura en papel |

---

## 10. Checklist docente

- [ ] Objetivo matemático en una frase  
- [ ] Modo A/B/C/D  
- [ ] Predicción o producto sin depender del notebook  
- [ ] Entorno / plan B  
- [ ] Norma de dispositivos y privacidad  

---

## 11. Mapa de la carpeta

| Ruta | Contenido |
|------|-----------|
| [README](README.md) · [INDICE](INDICE.md) | Entrada |
| Este archivo | Criterio didáctico |
| [jupyter/](jupyter/) | Plantillas |
| [matematicas/](matematicas/) | Notebooks escolares |
| [actividades/](actividades/) | Fichas de sesión |

---

*Orientativo para el Máster de Profesorado · Matemáticas.*
