# Idea de TFM: SimulaESO — motor offline de situaciones de aprendizaje para Matemáticas de la ESO

## 1. Idea central

Diseñar, desarrollar y evaluar **SimulaESO**: no solo «una app de Matemáticas», sino un **motor abierto de situaciones de aprendizaje (SdA)** — aplicación **open source**, **100 % local**, multiplataforma (Windows/Linux), preferentemente en **Go (Golang)**, con interfaz **gráfica 2D ligera** (sin aceleración 3D ni GPU dedicada).

El salto conceptual es pasar de:

> «Programar actividades una a una»

a:

> **«Diseñar un lenguaje y un motor capaces de convertir diseños didácticos en experiencias educativas ejecutables.»**

Cada SdA es un **dato** que el motor interpreta, no un programa nuevo. Un escenario nuevo debería poder incorporarse **sin modificar el código del motor**.

La idea responde además a tres fricciones del aula digital:

1. **Dependencia de red y plataformas cloud** — interrupciones y desigualdad de acceso.
2. **Software pesado o solo-navegador** — equipos modestos fuera de juego; arranques lentos.
3. **Privacidad, RGPD y tecnoansiedad** — datos en la nube y entornos web que compiten con la atención matemática.

**Pregunta central (doble):**

1. *Arquitectura:* ¿Es viable un motor + DSL mínimo que ejecute escenarios didácticos definidos fuera del código fuente?
2. *Aula:* ¿Mejora ese enfoque offline la viabilidad de las actividades (arranque, completitud, focalización, réplica en casa, apoyo a la evaluación docente) frente al uso habitual de software en la nube?

---

## 2. Arquitectura conceptual en tres capas

### 2.1. Capa pedagógica — ficha humana (SdA documental)

El profesorado describe la situación en lenguaje didáctico, alineado con LOMLOE (competencias, criterios, saberes básicos). Ejemplo: **«Ordenación de fracciones»**.

Elementos que la ficha debería contemplar de forma casi obligatoria (aprendizaje moderno, no «fórmula → cálculo»):

| Bloque | Contenido |
|--------|-----------|
| Identidad | Título, curso, temática, duración orientativa |
| Currículo | Competencias, criterios de evaluación, saberes básicos |
| Situación | Contexto real o realista presentado al alumnado |
| Objetivos | Qué se espera que piense / decida / justifique |
| Metodología | Trabajo individual / parejas; uso de pistas; ensayo-error |
| Fases | Secuencia cronológica de la actividad |
| Preguntas / tareas | Enunciados; posibles planteamientos del alumno |
| Respuestas esperadas | Criterios de corrección (no solo «la solución») |
| Errores previsibles | Diagnóstico didáctico |
| Pistas | Andamiaje gradual |
| Condiciones de avance | Cuándo se pasa de fase |
| Evidencias | Qué se registra (elecciones, intentos, tiempo, justificación) |
| Instrumentos | Rúbrica / checklist para el informe |
| Observación docente | Campos abiertos que **no** automatiza el programa |

### 2.2. Capa formal — escenario computacional (DSL)

La ficha humana se transforma en una **especificación rígida, validable**, en un esquema/DSL universal para todos los escenarios:

```text
ficha didáctica  →  (IA asistida + plantilla)  →  especificación formal
                 →  validación sintáctica/semántica  →  escenario ejecutable
```

Puntos de diseño importantes:

- La IA **no inventa el juego libremente**: traduce la intención pedagógica a un **esquema predefinido** (JSON/YAML u otro formato documentado).
- El resultado debe poder **validarse** antes de cargarse en el motor (campos obligatorios, tipos, grafo de fases acíclico, etc.).
- La transformación puede ser asistida por IA en el flujo de autoría; la **ejecución en el aula sigue siendo offline** (el escenario ya validado viaja con el binario o en carpeta local).

### 2.3. Capa de ejecución — motor SimulaESO

El motor interpreta el escenario:

```text
presentar situación → proponer tarea → recibir respuesta / planteamiento
  → evaluar → ofrecer pista (si procede) → registrar evidencia
  → decidir siguiente fase → finalizar → generar informe
```

Principios didácticos embebidos en el motor (no opcionales en el DSL):

- Situación antes que fórmula.
- Espacio para **planteamientos** evaluables, no solo respuesta final.
- Pistas graduadas.
- Registro de trayectoria (intentos, tiempos, ayudas usadas).

### 2.4. Ciclo completo (profesor ↔ alumno)

```text
PROFESOR
   ↓  diseña SdA (capa pedagógica)
FICHA DIDÁCTICA
   ↓  IA + DSL (capa formal)
ESCENARIO FORMAL → validación
   ↓
MOTOR SIMULAESO (offline)
   ↓
ALUMNO (identificado de forma única)
   ↓  respuestas, decisiones, evidencias
INFORME LOCAL (SQLite)
   ↓
PROFESOR
   ↓  consulta listados + añade observación cualitativa
EVALUACIÓN PROFESIONAL (el software no sustituye al docente)
```

**Distinción clave:** el programa **automatiza la recogida y organización de evidencias** y puede preparar informes semi-estructurados; la interpretación cualitativa (actitud, estrategias, circunstancias) permanece en manos del profesor. Así se alinea también con la reducción de fricción burocrática sin pretender evaluación automática total.

---

## 3. Repositorio comunitario de escenarios

Al ser software libre, el valor a medio plazo no es solo el motor, sino una **biblioteca de escenarios** versionada (p. ej. en el mismo repo o en uno hermano):

```text
escenarios/
├── aritmetica/
│   ├── ordenacion-fracciones/
│   └── proporcionalidad/
├── algebra/
│   └── ecuaciones-primer-grado/
├── funciones/
├── geometria/
├── estadistica/
├── probabilidad/
└── sentido-computacional/
```

Cada carpeta de escenario puede contener:

- `ficha.md` — capa pedagógica;
- `escenario.yaml` (o `.json`) — capa formal;
- `recursos/` — datos CSV, imágenes 2D ligeras;
- `metadatos.yaml` — curso, saberes, autoría, licencia, versión.

Crecimiento posterior (fuera del MVP del TFM): rankings por uso, resultados educativos agregados y anónimos, revisión por pares de escenarios.

---

## 4. Identidad del alumnado, persistencia e informes

- **Identificador único** por alumno/a en el ámbito del centro o del grupo (código interno; no basta nombre+apellido).
- **Persistencia local:** **SQLite** embebido (p. ej. `modernc.org/sqlite`) — portable, sin servidor, coherente con el diseño offline.  
  *Nota:* Redis u otras bases cliente-servidor **no** encajan en el núcleo offline; quedarían para una eventual arquitectura multiusuario futura.
- **Informes:** por alumno, por grupo, exportables (CSV/PDF simple); el profesor completa con anotaciones subjetivas.
- **RGPD:** datos en local; sin telemetría obligatoria; consentimiento y minimización de datos en el piloto.

---

## 5. Punto de partida y fundamentación

### 5.1. Contexto curricular (Aragón / LOMLOE)

- Sentido **computacional** y **estocástico**; competencias y criterios evaluables.
- Competencia digital: entornos seguros y sostenibles; local frente a remoto.
- STEM: herramientas digitales para conjeturar y comprobar.

Normativa: Orden ECD/1172/2022 (ESO) y ECD/1173/2022 (Bachillerato) en Aragón.

### 5.2. Por qué Go y UI 2D ligera

| Criterio | Ventaja |
|----------|---------|
| Despliegue USB / aula | Binario único; `GOOS`/`GOARCH` |
| Equipos modestos | Bajo consumo; sin GPU |
| Offline real | Sin servidor en tiempo de ejecución |
| Motor + validación DSL | Go adecuado para CLIs, parsers y binarios estáticos |
| Soberanía | GPL-3.0; SQLite local |

UI candidatas: Fyne v2, Gio, SDL2 software. Gráficas: `gonum/plot`.

### 5.3. Encaje con otras ideas del repo

- [02 — tecnoestrés](02-tecnoestres-digital.md): menos navegador y menos ruido digital.
- [01](01-penalizacion-aprendizaje-ia-generativa.md) / [05](05-esfuerzo-cognitivo-y-pensamiento-critico.md): la IA asiste al **autor** del escenario, no sustituye el pensamiento del alumno en la ejecución.
- [03 — burocracia docente](03-burocratizacion-docente-y-carga-administrativa.md): informes semi-preparados como alivio de carga, no como evaluación opaca.
- [14 — datos reales](14-datos-reales-vs-libro-estadistica.md): escenarios de estadística con CSV locales.

---

## 6. Preguntas de investigación

### Variante A — Arquitectura (núcleo del TFM de innovación)

> ¿Puede un motor + DSL mínimo ejecutar un escenario nuevo (p. ej. ordenación de fracciones) definido solo por especificación formal, sin recompilar ni alterar el código del motor?

### Variante B — Viabilidad de aula

> ¿Reduce el paquete offline (motor + escenarios locales) el tiempo de preparación y las interrupciones por red respecto a la misma secuencia en herramientas cloud?

### Variante C — Evaluación docente

> ¿Percibe el profesorado que los informes generados agilizan la recogida de evidencias sin sustituir su juicio profesional?

### Variante D — Aprendizaje (opcional / ambiciosa)

> ¿Hay diferencias de rendimiento o de calidad de justificación entre grupo experimental y control a igualdad de contenidos?

**Recomendación:** A + B como eje del TFM; C con entrevista/cuestionario breve; D solo si el piloto lo permite.

---

## 7. Hipótesis posibles

- **H1.** Un escenario adicional se incorpora al sistema modificando únicamente ficheros de especificación (y recursos), no el código Go del motor.
- **H2.** El tiempo de arranque y la tasa de fallos por red mejoran frente al flujo cloud habitual en el mismo hardware.
- **H3.** El informe local reduce el tiempo percibido de «poner notas/evidencias en limpio» sin eliminar la necesidad de observación docente.
- **H4.** El alumnado completa más fases de la SdA en el tiempo lectivo cuando no hay dependencia de login/red.

---

## 8. Variables

| Dimensión | Indicadores |
|-----------|-------------|
| Arquitectura | Escenarios cargados sin recompilar; errores de validación del DSL |
| Eficiencia de aula | Tiempo de arranque; fallos de red; tiempo hasta primera tarea útil |
| Completitud | % de fases / escenarios terminados en la sesión |
| Focalización | Observación / autodeclaración de interrupciones |
| Evaluación docente | Tiempo percibido; utilidad del informe; campos que el profesor edita a mano |
| Usabilidad | SUS breve; nº de clics hasta empezar |
| Réplica en casa | Ejecución del binario + escenario sin ayuda técnica |

---

## 9. MVP técnico y didáctico del TFM

No hace falta una biblioteca enorme de actividades. Basta demostrar el concepto:

| Pieza | Contenido mínimo |
|-------|------------------|
| Motor | Carga de escenario formal, bucle de fases, evaluación simple, pistas, registro |
| DSL | Esquema documentado (campos obligatorios + grafo de fases) |
| Validación | CLI o paso previo que rechace escenarios mal formados |
| Escenarios | **2–3** (p. ej. ordenación de fracciones; uno de estadística con CSV; uno de probabilidad/Monte Carlo) |
| Identidad + SQLite | Altas de grupo; sesión; informe por alumno |
| UI 2D | Suficiente para presentar situación, capturar respuesta y mostrar feedback |
| Documentación | Guía de autoría de fichas + especificación del DSL + guía rápida de aula |

**Experimento de arquitectura del TFM:** crear el tercer escenario **solo** tocando la especificación (y recursos), no el motor.

Fuera de alcance del MVP: CAS simbólico completo, multiusuario en red, Redis, rankings comunitarios en producción, Android.

---

## 10. Diseño de validación en el aula

| Fase | Acción |
|------|--------|
| 1 | DSL + motor + 2 escenarios + una SdA documentada completa |
| 2 | Piloto: experimental (SimulaESO) vs. control (cloud/navegador), mismo contenido |
| 3 | Tiempos, completitud, observación; cuestionario usabilidad; breve feedback docente sobre informes |
| 4 | Análisis descriptivo; limitaciones de muestra y de causalidad explícitas |

**Ética:** consentimiento; identificadores no equivalentes a datos personales innecesarios; sin subir datos a la nube.

---

## 11. Alcance realista y riesgos

| Riesgo | Mitigación |
|--------|------------|
| Ambición de «plataforma total» | MVP = motor + DSL + 2–3 escenarios |
| IA que genera basura formal | Esquema cerrado + validación estricta; IA solo asistida |
| Confundir informe automático con evaluación | Campos obligatorios de observación docente; discurso claro en la memoria |
| Identidad y privacidad | IDs locales; SQLite en carpeta del centro/profesor; sin cuentas cloud |
| Curva Go/UI | Plan B: motor CLI + UI mínima |
| Efecto novedad | Medir fricción técnica, no solo motivación |

---

## 12. Potencial para TFM y títulos posibles

- Innovación **tecnológica y educativa** (motor + lenguaje + piloto).
- Transferencia: repo de escenarios, licencia libre, documentación de autoría.
- Escalabilidad social: comunidad de profesores-autores si el núcleo funciona.

**Títulos posibles:**

- **SimulaESO: un motor offline de situaciones de aprendizaje para Matemáticas de ESO**
- **Del diseño didáctico al escenario ejecutable: DSL y motor open source para el aula de Matemáticas**
- **Situaciones de aprendizaje como datos: arquitectura y pilotaje de un entorno local en Go**

---

## 13. Palabras clave

- Motor de escenarios
- Situaciones de aprendizaje (SdA)
- DSL educativo
- Software offline
- Go / Golang
- Open source (GPL-3.0)
- UI 2D ligera
- SQLite
- Evaluación formativa / evidencias
- Repositorio de escenarios
- LOMLOE Aragón
- Sentido computacional / estocástico
- Soberanía tecnológica

---

## 14. Encaje con Atlas y bibliometría

| Evitar | Apostar |
|--------|--------|
| Otra app de ejercicios cerrados | **SdA como dato + motor reutilizable** |
| «IA que enseña mates» | IA solo en **autoría formal** del escenario |
| Evaluación automática total | Evidencias + **juicio docente** |
| Solo código sin aula | Piloto con indicadores de fricción y usabilidad |

---

## 15. Estado y siguientes pasos

**Estado:** propuesta elaborada; candidata fuerte a TFM de **innovación** (arquitectura + piloto).

1. Congelar el **esquema del DSL** (v0.1) y un ejemplo completo: *ordenación de fracciones*.
2. Implementar motor mínimo + validación.
3. Segundo escenario **sin tocar el motor** (prueba de arquitectura).
4. UI 2D suficiente + SQLite + informe.
5. Piloto breve en Prácticum + memoria con especificación y guía de autoría.

---

## 16. Bibliografía y recursos semilla

- Orden ECD/1172/2022 y ECD/1173/2022 (currículo Aragón).
- Go: https://go.dev · Fyne / Gio · gonum / gonum/plot.
- SQLite embebido en Go (`modernc.org/sqlite`).
- RGPD / AEPD — protección de datos en centros educativos.
- Literatura sobre software libre en educación matemática; carga cognitiva y entornos digitales (idea 02).
- Referencias de diseño de lenguajes de dominio (DSL) y de sistemas autor (e-learning): posicionar SimulaESO como **autoría didáctica → ejecución local**, no como LMS cloud.

---

## 17. Pregunta guía

> **Si una situación de aprendizaje bien diseñada pudiera ejecutarse como un escenario validado —sin reprogramar el aula digital cada vez— ¿qué motor, qué lenguaje formal y qué evidencias de aula demuestran que ese camino es mejor que depender de la nube o de actividades cableadas en el código?**
