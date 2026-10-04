# Idea de TFM: SimulaESO — software educativo offline en Go para Matemáticas de la ESO

## 1. Idea central

Diseñar, desarrollar y evaluar **SimulaESO**: una aplicación **open source**, **100 % local**, multiplataforma (Windows/Linux), implementada preferentemente en **Go (Golang)**, con interfaz **gráfica 2D ligera** (sin dependencia de aceleración 3D ni GPU dedicada), orientada a simulación, resolución interactiva de problemas y estadística en Matemáticas de ESO.

La idea responde a tres fricciones reales del aula digital:

1. **Dependencia de red y plataformas cloud** — interrupciones, cuellos de botella y desigualdad de acceso.
2. **Software pesado o solo-navegador** — equipos antiguos o sin GPU quedan fuera; arranques lentos fragmentan la sesión.
3. **Privacidad, RGPD y tecnoansiedad** — datos en la nube, notificaciones y entornos web que compiten con la atención matemática.

**Pregunta central:** ¿En qué medida una herramienta offline, ligera y portable mejora la viabilidad de las actividades matemáticas digitales (tiempo de arranque, completitud de tareas, focalización y réplica en casa) respecto al uso habitual de software en la nube o en el navegador?

---

## 2. Punto de partida y fundamentación

### 2.1. Contexto curricular (Aragón / LOMLOE)

- Sentido **computacional** y **estocástico** (saberes básicos): algoritmos sencillos, simulación, organización de datos.
- Competencia digital: entornos seguros y sostenibles; comprensión de lo local frente a lo remoto.
- STEM: uso crítico de herramientas digitales para formular y comprobar conjeturas.

Normativa de referencia: Orden ECD/1172/2022 (ESO) y ECD/1173/2022 (Bachillerato) en Aragón.

### 2.2. Por qué Go y UI 2D ligera

| Criterio educativo | Ventaja técnica de Go + UI 2D |
|--------------------|--------------------------------|
| Despliegue en aula / USB | Binario único; compilación cruzada (`GOOS`/`GOARCH`) |
| Equipos modestos | Bajo consumo; sin runtime pesado ni GPU |
| Offline real | Sin servidor ni cuenta de usuario |
| Mantenibilidad | Código legible; ecosistema `gonum` para cálculo y gráficas |
| Soberanía tecnológica | GPL-3.0; código auditable; datos en CSV/SQLite local |

**Opciones de UI (prioridad: 2D, CPU o OpenGL mínimo):** Fyne v2, Gio, o SDL2 con renderizador software. Gráficas: `gonum/plot` (PNG/SVG). Persistencia: SQLite puro Go (`modernc.org/sqlite`) o CSV/JSON.

### 2.3. Encaje con otras ideas del repo

Complementa [02 — tecnoestrés digital](02-tecnoestres-digital.md) (higiene digital y atención) y matiza [01](01-penalizacion-aprendizaje-ia-generativa.md) / [05](05-esfuerzo-cognitivo-y-pensamiento-critico.md): no se trata de «más tecnología», sino de **tecnología acotada** que no compite con la memoria de trabajo ni con la red del centro.

---

## 3. Posibles preguntas de investigación

### Variante A — Viabilidad de aula (recomendada para TFM)

> ¿Reduce SimulaESO el tiempo de preparación y las interrupciones por red respecto a una misma secuencia con herramientas en la nube, manteniendo o mejorando la tasa de completitud de tareas matemáticas?

### Variante B — Focalización y distracción

> ¿Se observa menor dispersión (observación sistemática / autodeclaración) en sesiones con software offline sin navegador frente a sesiones con plataformas web?

### Variante C — Aprendizaje matemático

> ¿Hay diferencias en el rendimiento en tareas de estadística / probabilidad / funciones entre grupo experimental (SimulaESO) y control (software habitual), controlando el contenido?

### Variante D — Diseño de software educativo

> ¿Qué requisitos de arquitectura (binario portable, UI 2D, módulos curriculares) maximizan la adopción por profesorado no especialista en informática?

Las variantes A–B son las más viables en un TFM de un curso; C exige diseño experimental más cuidoso; D orienta el trabajo hacia innovación tecnológica documentada.

---

## 4. Hipótesis posibles

### H1. Tiempo de arranque y fricción

Un binario local portable reduce el tiempo medio de puesta en marcha de la actividad frente a login + carga web en el mismo hardware de aula.

### H2. Interrupciones de red

En condiciones de red inestable o saturada, el grupo offline completa más tareas en el tiempo lectivo disponible.

### H3. Focalización

La ausencia de navegador y notificaciones web se asocia con menos microinterrupciones observadas durante la resolución de problemas.

### H4. Réplica en casa

El alumnado puede repetir la actividad en casa sin depender de conexión de alta velocidad ni de cuentas institucionales.

---

## 5. Variables que podrían estudiarse

| Dimensión | Indicadores posibles |
|-----------|----------------------|
| Eficiencia de aula | Tiempo de arranque; nº de fallos de red; tiempo hasta primera tarea útil |
| Completitud | % de actividades terminadas en la sesión |
| Focalización | Escala observacional; interrupciones autodeclaradas |
| Aprendizaje (opcional) | Pretest/postest en el bloque curricular (p. ej. estadística 3.º–4.º) |
| Usabilidad | SUS o cuestionario breve profesorado/alumnado |
| Réplica | % que logra ejecutar el binario en casa sin ayuda técnica |
| Hardware | Tipo de equipo; presencia/ausencia de GPU; SO |

---

## 6. Descripción técnica de SimulaESO (alcance TFM)

### 6.1. Requisitos de producto

- **Licencia:** GPL-3.0.
- **Plataformas:** Windows 10/11 y Linux x86_64 (ARM opcional).
- **Mínimos orientativos:** CPU 1 GHz, 2 GB RAM, ~100 MB disco; **sin** GPU dedicada; **sin** Internet en tiempo de ejecución.
- **Distribución:** binario portable (USB / carpeta compartida LAN) + código fuente.

### 6.2. Módulos didácticos prioritarios (MVP para TFM)

No hace falta cubrir todo el currículo. Un MVP creíble:

1. **Funciones y gráficas** — tablas, parámetros, representación 2D.
2. **Estadística descriptiva** — CSV, medidas, histograma / boxplot.
3. **Probabilidad y Monte Carlo** — experimentos aleatorios, frecuencias.
4. **Datos locales** — importar CSV; opcional SQLite muy simple.
5. **Modo actividad** — plantilla de tarea exportable (enunciado + datos + captura de resultados).

Álgebra simbólica avanzada o CAS completo **queda fuera** del alcance realista de un TFM (salvo como línea futura).

### 6.3. Arquitectura (capas)

```text
Presentación   → UI 2D (Fyne / Gio / SDL2 software) + gráficas (gonum/plot)
Aplicación     → módulos curriculares (funciones, estadística, probabilidad)
Dominio        → cálculo (gonum), simulación, validación de entradas
Persistencia   → CSV / JSON / SQLite local
```

---

## 7. Diseño de validación en el aula

Diseño **cuasi-experimental** viable:

| Fase | Acción |
|------|--------|
| 1. Diseño | MVP + 1–2 situaciones de aprendizaje (LOMLOE Aragón) en un bloque (p. ej. estadística o probabilidad) |
| 2. Pilotaje | Grupo experimental (SimulaESO) vs. control (herramienta cloud/navegador habitual) |
| 3. Datos | Tiempos, completitud, observación de focalización; opcional pretest/postest; cuestionario usabilidad |
| 4. Análisis | Comparación descriptiva; limitaciones explícitas de muestra y causalidad |

**Ética / RGPD:** procesamiento local; logs anónimos si los hay; consentimiento familias/centro; no subir datos de alumnado a servicios externos.

---

## 8. Alcance realista y riesgos

| Riesgo | Mitigación |
|--------|------------|
| Ambición de «CAS completo en un año» | MVP de 2–3 módulos; el TFM evalúa impacto de aula, no el producto comercial |
| Curva de aprendizaje del autor en Go/UI | Prototipo CLI o web estática local como plan B técnico |
| Adopción del profesorado | Guía didáctica de 2 páginas + binario «doble clic» |
| Comparabilidad grupo control | Misma SdA y mismos criterios de evaluación |
| Efecto novedad | Medir también fricción técnica (arranque, fallos), no solo motivación |
| Confusión con «anti-tecnología» | Enmarcar como **soberanía tecnológica y reducción de fricción**, no como rechazo a lo digital |

---

## 9. Potencial para TFM

- **Innovación:** producto + SdA + evidencia de aula (no solo memoria teórica).
- **Actualidad:** debate sobre pantallas, nube, privacidad y equidad digital.
- **Transferencia:** código público, guía didáctica, posible uso en otros centros.
- **Líneas futuras:** WebAssembly offline; Android; ampliación a Física/Tecnología; accesibilidad.

### Posibles títulos

- **SimulaESO: diseño y evaluación de una herramienta offline en Go para el sentido estocástico en ESO**
- **Software matemático local y ligero frente a plataformas en la nube: un estudio piloto en el aula de Secundaria**
- **Soberanía tecnológica en el aula de Matemáticas: desarrollo open source y validación didáctica de una aplicación 2D offline**

---

## 10. Palabras clave

- Software educativo offline
- Go / Golang
- Open source (GPL-3.0)
- UI 2D ligera
- Simulación Monte Carlo
- Estadística ESO
- Sentido computacional
- Privacidad / RGPD
- Brecha digital
- Portable / USB
- LOMLOE Aragón
- Situaciones de aprendizaje

---

## 11. Encaje con Atlas, Bibliometría y otras ideas

| Evitar (saturado) | Apostar (nicho) |
|-------------------|-----------------|
| «Uso de GeoGebra para motivar» genérico | **Restricción offline + portabilidad + medición de fricción de aula** |
| App educativa sin evaluación | Producto **y** indicadores (arranque, red, completitud) |
| Solo desarrollo informático | Anclaje curricular LOMLOE + SdA + piloto |

**Conexiones:**

- [02 — Tecnoestrés digital](02-tecnoestres-digital.md)
- [01 — IA generativa y aprendizaje](01-penalizacion-aprendizaje-ia-generativa.md)
- [05 — Esfuerzo cognitivo y pensamiento crítico](05-esfuerzo-cognitivo-y-pensamiento-critico.md)
- [14 — Datos reales vs. libro](14-datos-reales-vs-libro-estadistica.md) (módulo estadística + CSV)
- [Atlas de nichos](../atlas-nichos/) · [Bibliometría TFM](../bibliometria-tfm/)

---

## 12. Estado actual de la idea

**Estado:** propuesta elaborada / candidata fuerte a TFM de **innovación** con componente de desarrollo.

**No es todavía:** software terminado ni ensayo clínico de eficacia.

### Siguiente paso recomendado

1. Congelar el **MVP** (módulos + una sola UI candidata, p. ej. Fyne).
2. Escribir **una** SdA completa (3–5 sesiones) alineada con un saber concreto.
3. Prototipo compilable Windows+Linux en USB antes del piloto.
4. Definir instrumentos de observación (tiempos, checklist de interrupciones) compatibles con el Prácticum.

---

## 13. Bibliografía y recursos semilla

- Orden ECD/1172/2022 y Orden ECD/1173/2022 (currículo ESO y Bachillerato, Aragón).
- Documentación Go: https://go.dev
- Fyne: https://fyne.io · Gio · gonum / gonum/plot: https://www.gonum.org
- RGPD y guías de protección de datos en centros educativos (AEPD).
- Trabajos sobre software libre en educación matemática y sobre carga cognitiva / entornos digitales (conectar con idea 02).
- Comparar con herramientas existentes offline o ligeras: GeoGebra (instalable), Octave, R, aplicaciones HTML5 locales — no para copiar, sino para posicionar el nicho de SimulaESO.

---

## 14. Pregunta que puede guiar la evolución

> **Si la mejor herramienta digital del aula de Matemáticas es la que menos interrumpe el razonamiento y menos depende de la red, ¿qué arquitectura de software y qué evidencias de aula demuestran que merece la pena construirla?**
