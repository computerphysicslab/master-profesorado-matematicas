# Plantilla de notebook escolar (Markdown)

Copia esta estructura a un `.ipynb` (o parte de [plantilla-notebook-escolar.ipynb](plantilla-notebook-escolar.ipynb)).  
Cada bloque `###` puede ser una **celda Markdown**; los bloques de código, celdas de código.

---

## Celda 0 — Título y metadatos

```text
# [Título de la actividad]

**Curso:** …  
**Objeto matemático:** …  
**Modo didáctico:** exploración / modelización / verificación / auditoría IA  
**CE prioritarias:** …  
**Tiempo orientativo:** … min  
**Plan B sin ordenador:** …

> Predice *antes* de ejecutar. Interpreta *después*. El notebook no sustituye la justificación.
```

---

## Celda 1 — Pregunta matemática

Enunciado en lenguaje natural (el mismo que en papel).  
Sin pedir “programa esto” como objetivo único.

---

## Celda 2 — Predicción (obligatoria)

Responde a mano o escribe aquí **antes** de correr código:

- ¿Qué resultado esperas (orden de magnitud, quién “gana”, forma de la gráfica)?  
- ¿Qué puede salir mal?

---

## Celda 3 — Modelo (supuestos)

- Variables y unidades.  
- Fórmulas o relaciones.  
- Qué simplificas a propósito.

---

## Celda 4 — Código mínimo

```python
# Imports solo los necesarios
# Parámetros con nombres claros (m_a, n_a, ...)
# Una idea por celda cuando sea posible
```

---

## Celda 5 — Resultados / gráfica

Ejecutar. Si hay gráfica: título, ejes con magnitudes, leyenda si hay series.

---

## Celda 6 — Interpretación y validación

- ¿Coincide con la predicción?  
- ¿Tiene sentido en el contexto?  
- ¿Qué límite tiene el modelo?

---

## Celda 7 — Looking back

- ¿Cómo lo harías solo con papel?  
- ¿Qué aportó el ordenador y qué no?

---

## Notas de entorno

| Opción | Cuándo |
|--------|--------|
| **Google Colab** | Aula con cuentas y red; cero instalación |
| **Jupyter local / Anaconda** | Control del entorno; sin depender de Google |
| **JupyterLite** | Experimentar en navegador; límites de paquetes |

Privacidad: no subir listados de alumnos ni notas. Ver [marco didáctico](../python-criterio-didactico.md).
