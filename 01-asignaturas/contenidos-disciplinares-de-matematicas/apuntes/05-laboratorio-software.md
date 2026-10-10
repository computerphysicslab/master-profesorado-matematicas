# Laboratorio de software matemático

**Asignatura:** Contenidos disciplinares de Matemáticas  
**Bloque de referencia:** Parte 4 — Laboratorio de software matemático: aplicación en aspectos prácticos relacionados con los contenidos de las partes 1, 2 y 3.

> El software no sustituye el razonamiento: lo **amplía**. Este apunte organiza el uso de herramientas digitales ya presentes en el repositorio y propone prácticas alineadas con la visión histórica, la geometría sintética/proyectiva y la reflexión curricular.

---

## 1. Criterio de uso

| Principio | Consecuencia práctica |
|-----------|----------------------|
| El software es medio, no fin | Cada sesión responde a una pregunta matemática o didáctica |
| Conectar con el currículo | Priorizar objetos de ESO/Bachillerato (complejos, cónicas, transformaciones, iteración…) |
| Hacer visible el concepto | La pantalla debe ayudar a **ver** lo que el lápiz solo sugiere |
| Evitar la caja negra | El alumnado (y el docente) debe poder explicar qué hace el programa |
| Reutilizar lo existente | No duplicar: enlazar materiales y notebooks del repo |

---

## 2. Herramientas prioritarias

### 2.1. GeoGebra
- **Fortalezas:** geometría dinámica, algebraica y gráfica en un mismo entorno; ideal para construcciones euclidianas, transformaciones, cónicas y planos complejos.
- **Uso recomendado en esta asignatura:**
  - Construcciones con regla y compás (legado euclidiano, T-CD-02).
  - Puntos de fuga y recta del infinito (acercamiento proyectivo, T-CD-03).
  - Representación de complejos y rotaciones.
  - Exploración de cónicas y su corte con la recta del infinito.
- **Criterio didáctico en el repo:** ver materiales de Diseño curricular (`geogebra-criterio-didactico.md` cuando exista en esa carpeta).

### 2.2. Python + Jupyter
- **Fortalezas:** cálculo, iteración, visualización, verificación de conjeturas, fractales, series.
- **Uso recomendado:**
  - Iteración $z_{n+1}=z_n^2+c$ (Mandelbrot / Julia).
  - Rotaciones y visualización de complejos.
  - Pequeños scripts de apoyo a demostraciones o a datos.
- **Marco del repo:** carpeta `05-python-jupyter/` (criterio didáctico, plantillas, notebooks de tarifas y perímetro-área).

### 2.3. Otras herramientas (opcionales)
- Calculadoras gráficas / CAS cuando el centro las use.
- Software de dibujo técnico para perspectiva (enlace cultural con el origen de la proyectiva).

---

## 3. Prácticas alineadas con las partes 1–3

### 3.1. Visión histórica → laboratorio
| Idea histórica | Práctica con software |
|----------------|----------------------|
| Ampliaciones numéricas (reales → complejos) | Plano de Argand en GeoGebra o Python; rotaciones por multiplicación |
| Iteración y fractales (siglo XX) | Taller Mandelbrot / Julia (material ya escrito) |
| Perspectiva y puntos de fuga | Construcción de perspectivas en GeoGebra; identificación de puntos del infinito |

**Materiales listos:**
- [Aplicaciones de números complejos](../materiales/aplicaciones-numeros-complejos-bachillerato.md)
- [Fractales Mandelbrot / Julia](../materiales/fractales-mandelbrot-bachillerato.md)
- [Hipercomplejos / cuaterniones](../materiales/hipercomplejos-cuaterniones-videojuegos.md) (ampliación STEM)

### 3.2. Geometría sintética (Euclides) → laboratorio
| Concepto | Práctica |
|----------|----------|
| Criterios de congruencia | Construcciones y arrastre en GeoGebra; comprobar invariancia |
| Paralelas y ángulos | Explorar el quinto postulado de forma dinámica (¿qué pasa si…?) |
| Área y exhausción (idea) | Aproximar áreas con polígonos; comparar con herramientas de medida |

Objetivo: que el software **refuerce** la distinción entre “se ve” y “se demuestra”, no que la diluya.

### 3.3. Geometría proyectiva → laboratorio
| Concepto | Práctica |
|----------|----------|
| Puntos del infinito | Rectas paralelas que “se cortan” en un punto de fuga (GeoGebra 3D o vista 2D con horizonte) |
| Dualidad (idea) | Intercambiar el rol de puntos y rectas en configuraciones sencillas |
| Cónicas unificadas | Clasificar cónicas según corte con una recta “del infinito”; deformar una elipse en hipérbola por proyectividad (nivel avanzado) |

No hace falta un curso formal de proyectiva: basta con **experiencias** que den sentido al lenguaje.

### 3.4. Reflexión curricular → laboratorio
Usar el software para:
- Contrastar registros (Duval): gráfico, algebraico, numérico, geométrico del mismo objeto.
- Comprobar conjeturas antes de demostrar.
- Generar ejemplos y contraejemplos rápidamente.

---

## 4. Propuesta de secuencias cortas (laboratorio)

### Secuencia A — Complejos y rotaciones (2–3 sesiones)
1. Recordatorio binómica / polar (pizarra o GeoGebra).
2. Multiplicar por $e^{i\theta}$: rotación (GeoGebra + script mínimo en Python).
3. Aplicación: circuito CA (fasores) o fractal (enlace al material de fractales).
4. Cierre: ¿qué gana el currículo al incluir complejos más allá de la operatoria?

### Secuencia B — Cónicas y el infinito (1–2 sesiones)
1. Trazar elipse, parábola, hipérbola en GeoGebra.
2. Introducir una “recta del infinito” (horizonte) y observar cortes.
3. Discutir: ¿por qué en el plano proyectivo “todas las cónicas no degeneradas son equivalentes”?
4. Enlace opcional con perspectiva en arte/arquitectura.

### Secuencia C — Construcciones euclidianas dinámicas (1–2 sesiones)
1. Rehacer una construcción clásica (mediatriz, circuncentro, etc.).
2. Arrastrar vértices: ¿qué se conserva? ¿Qué es una demostración frente a una verificación visual?
3. Comparar con una prueba escrita breve.

---

## 5. Evaluación del laboratorio

No evaluar “saber pulsar botones”. Evaluar:

- **Explicación** del concepto que el software ilustra.
- **Conexión** con el currículo o con la historia del concepto.
- **Límites** de la herramienta (qué no demuestra, qué puede engañar).
- **Producto** mínimo: captura anotada, notebook comentado o informe breve (1–2 páginas).

---

## 6. Mapa de recursos del repositorio

| Recurso | Ubicación | Uso en el laboratorio |
|---------|-----------|------------------------|
| Aplicaciones de complejos | `materiales/aplicaciones-numeros-complejos-bachillerato.md` | Secuencia A |
| Fractales Mandelbrot/Julia | `materiales/fractales-mandelbrot-bachillerato.md` | Secuencia A / iteración |
| Hipercomplejos / cuaterniones | `materiales/hipercomplejos-cuaterniones-videojuegos.md` | Ampliación STEM |
| Python / Jupyter (marco + notebooks) | `05-python-jupyter/` | Iteración, visualización, verificación |
| Historias matemáticas | `03-materiales/historias-matematicas/` | Entradas narrativas a las prácticas |
| Apuntes 01–04 | esta carpeta `apuntes/` | Marco conceptual |

---

## 7. Orientaciones para el docente en formación

1. **Preparar la pregunta antes que el archivo.** ¿Qué quiero que descubran o confirmen?
2. **Limitar el tiempo de “exploración libre”** si el grupo se dispersa; alternar con momentos de puesta en común.
3. **Pedir siempre una frase de interpretación** (“esto muestra que…”).
4. **Cuidar la accesibilidad:** alternativas sin software cuando sea necesario (construcciones en papel, tablas).
5. **Documentar** en el TFM o en la memoria de prácticas qué aportó el software al aprendizaje del objeto matemático.

---

## 8. Relación con el resto de la asignatura

- **T-CD-01:** el laboratorio da cuerpo a problemas históricos (ampliaciones numéricas, iteración, perspectiva).
- **T-CD-02 / 03:** GeoGebra como entorno para geometría sintética y primeras ideas proyectivas.
- **T-CD-04:** el software ayuda a priorizar conceptos y a contrastar representaciones.
- **Diseño de actividades / Innovación:** las secuencias de este laboratorio pueden convertirse en actividades o en líneas de innovación documentadas.

---

## 9. Referencias y criterios

- Materiales internos citados arriba (no se inventan recursos externos no verificados).
- Documentación oficial de GeoGebra y de las bibliotecas Python usadas en los notebooks del repo.
- Criterio general del repositorio: el código y las construcciones deben poder **explicarse**, no solo ejecutarse.

---

**Estado del apunte:** primera versión (T-CD-05).  
Con este bloque, las cuatro partes del programa de referencia de Contenidos disciplinares quedan cubiertas a nivel de apuntes de estudio.
