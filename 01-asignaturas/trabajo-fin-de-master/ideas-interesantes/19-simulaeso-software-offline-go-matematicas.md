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
| Errores previsibles | Diagnóstico didáctico (banco de malentendidos del escenario) |
| Pistas | Andamiaje gradual |
| Condiciones de avance | Cuándo se pasa de fase |
| Evidencias | Qué se registra (elecciones, intentos, tiempo, justificación, tipo de error) |
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

Ejemplo concreto del esquema (**DSL v0.1**): [Anexo A — Ordenación de fracciones](#anexo-a--ejemplo-dsl-v01-ordenación-de-fracciones).

### 2.3. Capa de ejecución — motor SimulaESO

El motor interpreta el escenario:

```text
presentar situación → proponer tarea → recibir respuesta / planteamiento
  → evaluar → clasificar error (si procede) → ofrecer pista → registrar evidencia
  → decidir siguiente fase → finalizar → generar informe / exportar
```

Principios didácticos embebidos en el motor (no opcionales en el DSL):

- Situación antes que fórmula.
- Espacio para **planteamientos** evaluables, no solo respuesta final.
- Pistas graduadas.
- Registro de trayectoria (intentos, tiempos, ayudas usadas, códigos de error del banco del escenario).

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
INFORME LOCAL (SQLite) + EXPORTACIÓN (CSV/JSON)
   ↓
PROFESOR
   ↓  consulta listados + añade observación cualitativa
EVALUACIÓN PROFESIONAL (el software no sustituye al docente)
```

**Distinción clave:** el programa **automatiza la recogida y organización de evidencias** y puede preparar informes semi-estructurados; la interpretación cualitativa (actitud, estrategias, circunstancias) permanece en manos del profesor. Así se alinea también con la reducción de fricción burocrática sin pretender evaluación automática total.

---

## 3. Repositorio comunitario de escenarios y licencias

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
- `errores.yaml` — banco de errores típicos / malentendidos del escenario;
- `recursos/` — datos CSV, imágenes 2D ligeras;
- `metadatos.yaml` — curso, saberes, autoría, **licencia del contenido**, versión.

### 3.1. Licencia dual (código vs. contenidos)

| Capa | Licencia recomendada | Motivo |
|------|----------------------|--------|
| **Código del motor** (Go, UI, validador) | **GPL-3.0** | Garantiza que mejoras del software sigan siendo libres |
| **Escenarios didácticos** (fichas, YAML, recursos educativos) | **CC BY-SA 4.0** (o compatible) | Facilita que el profesorado copie, adapte y remezcle SdA citando autoría |

Así el repositorio de escenarios puede crecer como **bien común docente** sin obligar a que cada adaptación de una ficha de fracciones herede las obligaciones de copyleft del código ejecutable. En `metadatos.yaml` debe figurar siempre la licencia del contenido. Los ficheros YAML del escenario se tratan como **contenido** (CC BY-SA), no como código del motor.

Crecimiento posterior (fuera del MVP del TFM): rankings por uso, resultados educativos agregados y anónimos, revisión por pares de escenarios.

---

## 4. Identidad del alumnado, persistencia, informes y exportación

- **Identificador único** por alumno/a en el ámbito del centro o del grupo (código interno; no basta nombre+apellido).
- **Persistencia local:** **SQLite** embebido (p. ej. `modernc.org/sqlite`) — portable, sin servidor, coherente con el diseño offline. El esquema de tablas debe documentarse en la implementación (ver también §19).
- **Informes en la aplicación:** por alumno, por grupo; el profesor completa con anotaciones subjetivas combinadas con evidencias automáticas en el mismo informe.
- **Exportación interoperable (sin LMS):** CSV y JSON; post-MVP, PDF/XLSX si aporta (§19).
- **RGPD:** datos en local; sin telemetría obligatoria; consentimiento y minimización de datos en el piloto.

---

## 5. Banco de errores típicos (didáctica del error)

Cada escenario declara un **banco de malentendidos** versionado. Ejemplo en el [Anexo A](#anexo-a--ejemplo-dsl-v01-ordenación-de-fracciones).

En el **MVP**, la clasificación automática solo debe aplicarse cuando sea **fiable** (p. ej. opción múltiple con mapeo explícito). Códigos ambiciosos sobre texto libre se dejan en gran medida a `E_SIN_CLASIFICAR` + observación docente; el enriquecimiento del banco es línea post-MVP (§19).

---

## 6. Punto de partida y fundamentación

### 6.1. Contexto curricular (Aragón / LOMLOE)

- Sentido **computacional** y **estocástico**; competencias y criterios evaluables.
- Competencia digital: entornos seguros y sostenibles; local frente a remoto.
- STEM: herramientas digitales para conjeturar y comprobar.

Normativa: Orden ECD/1172/2022 (ESO) y ECD/1173/2022 (Bachillerato) en Aragón.

### 6.2. Por qué Go y UI 2D ligera

| Criterio | Ventaja |
|----------|---------|
| Despliegue USB / aula | Binario único; `GOOS`/`GOARCH` |
| Equipos modestos | Bajo consumo; sin GPU |
| Offline real | Sin servidor en tiempo de ejecución |
| Motor + validación DSL | Go adecuado para CLIs, parsers y binarios estáticos |
| Soberanía | GPL-3.0 (código); escenarios CC BY-SA; SQLite local |

UI candidatas: Fyne v2, Gio, SDL2 software. Gráficas: `gonum/plot`.

### 6.3. Encaje con otras ideas del repo

- [02 — tecnoestrés](02-tecnoestres-digital.md)
- [01](01-penalizacion-aprendizaje-ia-generativa.md) / [05](05-esfuerzo-cognitivo-y-pensamiento-critico.md)
- [03 — burocracia docente](03-burocratizacion-docente-y-carga-administrativa.md)
- [14 — datos reales](14-datos-reales-vs-libro-estadistica.md)

---

## 7. Preguntas de investigación

### Variante A — Arquitectura

> ¿Puede un motor + DSL mínimo ejecutar un escenario nuevo definido solo por especificación formal, sin recompilar el motor?

### Variante B — Viabilidad de aula

> ¿Reduce el paquete offline el tiempo de preparación y las interrupciones por red respecto a herramientas cloud?

### Variante C — Evaluación docente

> ¿Percibe el profesorado que los informes y la exportación CSV/JSON agilizan la recogida de evidencias sin sustituir su juicio?

### Variante D — Aprendizaje (opcional)

> ¿Hay diferencias de rendimiento o de calidad de justificación entre experimental y control?

**Recomendación:** A + B como eje; C con feedback breve; D solo si el piloto lo permite.

---

## 8. Hipótesis posibles

- **H1.** Un escenario adicional se incorpora solo con ficheros de especificación, no con código Go del motor.
- **H2.** Mejoran tiempo de arranque y fallos de red frente al flujo cloud en el mismo hardware.
- **H3.** Informe local + CSV reducen el tiempo percibido de «poner evidencias en limpio».
- **H4.** Mayor completitud de fases sin dependencia de login/red.
- **H5.** El agregado de códigos de error (cuando sea fiable) ayuda a planificar la siguiente sesión.

---

## 9. Variables

| Dimensión | Indicadores |
|-----------|-------------|
| Arquitectura | Escenarios sin recompilar; errores de validación del DSL |
| Eficiencia de aula | Arranque; fallos de red; tiempo hasta primera tarea útil |
| Completitud | % de fases terminadas |
| Focalización | Observación / autodeclaración |
| Evaluación docente | Utilidad del informe; uso del CSV/JSON |
| Didáctica del error | Frecuencias de códigos; coherencia con observación |
| Usabilidad | SUS breve |
| Réplica en casa | Ejecución sin ayuda técnica |

---

## 10. MVP técnico y didáctico del TFM

| Pieza | Contenido mínimo |
|-------|------------------|
| Motor | Carga de escenario, fases, pistas, registro de errores fiables |
| DSL | [Anexo A](#anexo-a--ejemplo-dsl-v01-ordenación-de-fracciones) + limitaciones A.8 |
| Validación | Rechazo de escenarios mal formados |
| Escenarios | 2–3 |
| SQLite + export | Informe + CSV/JSON |
| UI 2D | Situación, respuesta, feedback |
| Documentación | Guía de autoría + protocolo de Prácticum |

**Experimento de arquitectura:** tercer escenario solo con YAML nuevos.

Fuera del MVP: lo listado en [§19](#19-mejoras-previstas-para-versiones-avanzadas-post-mvp).

---

## 11. Protocolo de Prácticum

| Momento | Acción | Datos |
|---------|--------|-------|
| Antes | Binario + escenario; alta de grupo | Tiempo de preparación |
| Sesión 0 (opc.) | Familiarización | Usabilidad |
| Experimental | SimulaESO | Arranque; red; % fases; focalización |
| Control | Cloud/navegador habitual | Mismos indicadores |
| Después | Export CSV + 3–5 notas docentes | Utilidad del informe |
| Cierre | Cuestionario breve | Satisfacción; barreras |

**Ética:** consentimiento; IDs locales; sin subir SQLite a la nube.

---

## 12. Alcance realista y riesgos

| Riesgo | Mitigación |
|--------|------------|
| Plataforma total | MVP acotado; §19 es post-MVP |
| IA que genera basura formal | Esquema cerrado + validación |
| Evaluación automática total | Observación docente obligatoria en el discurso |
| Clasificación de errores frágil | Solo mapeos fiables; resto sin clasificar (A.8) |
| Privacidad | SQLite local |
| Efecto novedad | Medir fricción técnica |

---

## 13. Potencial y títulos posibles

- **SimulaESO: un motor offline de situaciones de aprendizaje para Matemáticas de ESO**
- **Del diseño didáctico al escenario ejecutable: DSL y motor open source para el aula de Matemáticas**
- **Situaciones de aprendizaje como datos: arquitectura y pilotaje de un entorno local en Go**

---

## 14. Palabras clave

Motor de escenarios · SdA · DSL · offline · Go · GPL-3.0 · CC BY-SA · SQLite · CSV/JSON · banco de errores · LOMLOE · Prácticum · soberanía tecnológica

---

## 15. Encaje con Atlas y bibliometría

| Evitar | Apostar |
|--------|--------|
| App de ejercicios cableados | SdA como dato + motor |
| IA que enseña mates | IA solo en autoría formal |
| Evaluación automática total | Evidencias + juicio docente |
| Solo código sin aula | Protocolo de Prácticum |

---

## 16. Estado y siguientes pasos

1. Ajustar Anexo A (incl. correcciones A.8 si hay margen).
2. Motor mínimo + validación.
3. Segundo escenario sin tocar el motor.
4. UI + SQLite + export.
5. Protocolo de Prácticum.
6. Memoria (DSL, licencias, líneas futuras §19).

---

## 17. Bibliografía y recursos semilla

- Orden ECD/1172/2022 y ECD/1173/2022 (Aragón).
- Go · Fyne / Gio · gonum · SQLite (`modernc.org/sqlite`).
- GPL-3.0 · CC BY-SA 4.0 · RGPD/AEPD.
- Software libre en educación matemática; análisis de errores; diseño de DSL.

---

## 18. Pregunta guía

> **Si una situación de aprendizaje bien diseñada pudiera ejecutarse como un escenario validado —sin reprogramar el aula digital cada vez— ¿qué motor, qué lenguaje formal y qué evidencias de aula demuestran que ese camino es mejor que depender de la nube o de actividades cableadas en el código?**

---

## 19. Mejoras previstas para versiones avanzadas (post-MVP)

El MVP del TFM debe permanecer acotado (motor + DSL v0.1 + 2–3 escenarios + piloto). Lo siguiente es **hoja de ruta posterior**, útil como sección de «líneas futuras» en la memoria.

### 19.1. Robustez del DSL y la validación
- **JSON Schema** (o equivalente) del DSL para validación máquina-legible y posibles editores.
- Política explícita ante **tipos de fase desconocidos** (rechazo en validación por defecto).
- **Validadores paramétricos** (p. ej. `multiplo_comun` de una lista de denominadores) en lugar de listas cerradas `[30, 60, 90]`.
- **Parser de fracciones y órdenes** con normalización (`1/2 < 3/5 < 2/3`).
- `error_por_defecto` por fase; versionado semántico del DSL con compatibilidad hacia atrás.

### 19.2. Pedagogía y feedback
- Registrar avance **por acierto** vs. **por agotamiento de intentos**.
- **Feedback específico por código de error** además de pistas graduadas.
- Banco de errores con ejemplos y patrones solo cuando la detección sea fiable.
- Ítems breves de **metacognición** (confianza / estrategia) al cierre de fase.
- Modos **práctica** vs. **evaluación** (pistas y tiempo configurables).

### 19.3. Datos, informes y arquitectura
- **Esquema SQL documentado** (`alumno`, `sesion`, `fase_intento`, `evidencia`, …).
- Exportación a **PDF** (e XLSX si aporta).
- Servidor **solo LAN** opcional para centralizar resultados del aula sin Internet.
- Tipos de fase ampliables y más dominios (álgebra, geometría, estadística).

### 19.4. Ecosistema (largo plazo)
- Editor visual de escenarios que genere YAML.
- Análisis de trayectorias y frecuencias de error por grupo.
- Compilación a **WebAssembly** (navegador local sin instalación).
- Catálogo de escenarios (descarga puntual; ejecución offline).
- Multiidioma.

> **Criterio:** nada de esta lista debe ampliar el alcance del piloto del TFM.

---

## Anexo A — Ejemplo DSL v0.1: ordenación de fracciones

> **Estado:** propuesta de esquema para el MVP.  
> **Carpeta prevista:** `escenarios/aritmetica/ordenacion-fracciones/`

### A.1. Estructura de ficheros

```text
escenarios/aritmetica/ordenacion-fracciones/
├── metadatos.yaml
├── ficha.md
├── escenario.yaml
├── errores.yaml
└── recursos/
```

### A.2. `metadatos.yaml`

```yaml
id: aritmetica.ordenacion-fracciones
version: "0.1.0"
titulo: Ordenación de fracciones
curso: "1 ESO"
tematica: aritmetica
saberes_basicos:
  - fracciones
  - orden_y_comparacion
  - comun_denominador
idioma: es
autor: "Propuesta TFM SimulaESO"
licencia: CC-BY-SA-4.0
dsl_version: "0.1"
duracion_minutos_orientativa: 45
```

### A.3. `errores.yaml`

```yaml
dsl_version: "0.1"
errores:
  - codigo: E_DENOM_IGUAL
    descripcion: Compara numeradores o denominadores sin común denominador / misma unidad.
    gravedad: alta
  - codigo: E_ENTEROS
    descripcion: Trata numerador y denominador como enteros independientes.
    gravedad: alta
  - codigo: E_INV_ORDEN
    descripcion: Invierte el orden de magnitud.
    gravedad: media
  - codigo: E_EQUIV_NO_REC
    descripcion: No reconoce fracciones equivalentes.
    gravedad: media
  - codigo: E_SIN_JUSTIFICAR
    descripcion: Orden sin criterio o justificación cuando se pide.
    gravedad: baja
  - codigo: E_SIN_CLASIFICAR
    descripcion: Incorrecto o incompleto sin malentendido identificable de forma fiable.
    gravedad: baja
```

### A.4. `escenario.yaml` (extracto estructural)

```yaml
dsl_version: "0.1"
id: aritmetica.ordenacion-fracciones
errores_ref: errores.yaml

situacion:
  titulo: "Reparto de pizza en la excursión"
  texto: >
    Tres grupos: A ha comido 2/3, B 3/5 y C 1/2 de una misma pizza unitaria.
    Hay que ordenar de menor a mayor la cantidad comida.

fases:
  - id: fase_1_estimacion
    tipo: eleccion_orden
    enunciado: "¿Cuál es el orden de menor a mayor (A=2/3, B=3/5, C=1/2)?"
    opciones:
      - {id: o1, etiqueta: "C < B < A"}   # correcto: 1/2 < 3/5 < 2/3
      - {id: o2, etiqueta: "B < C < A"}
      - {id: o3, etiqueta: "C < A < B"}
      - {id: o4, etiqueta: "A < B < C"}
    respuesta_correcta: o1
    error_por_defecto: E_SIN_CLASIFICAR
    errores_si_falla: {o2: E_INV_ORDEN, o3: E_DENOM_IGUAL, o4: E_INV_ORDEN}
    pistas:
      - {nivel: 1, texto: "¿Cuál se acerca más a un entero y cuál a la mitad?"}
      - {nivel: 2, texto: "1/2 es la mitad; sitúa 2/3 y 3/5 respecto a 1/2."}
    avance: {tipo: tras_respuesta, max_intentos: 3, siguiente: fase_2_comun_denominador}

  - id: fase_2_comun_denominador
    tipo: respuesta_corta
    enunciado: "Propón un denominador común para comparar 1/2, 3/5 y 2/3."
    # MVP simplificado (ver limitaciones A.8): lista acotada.
    # Post-MVP preferible: validacion.tipo = multiplo_comun, denominadores: [2,3,5]
    validacion: {tipo: entero_en_conjunto, valores_aceptados: [30, 60, 90]}
    error_por_defecto: E_DENOM_IGUAL
    pistas:
      - {nivel: 1, texto: "Denominadores 2, 5 y 3: busca un múltiplo común."}
      - {nivel: 2, texto: "Prueba con 2×3×5."}
    avance: {tipo: tras_correcta, max_intentos: 4, siguiente: fase_3_orden_justificado}

  - id: fase_3_orden_justificado
    tipo: orden_y_texto
    enunciado: "Escribe el orden (p. ej. 1/2 < 3/5 < 2/3) y una frase con el criterio."
    validacion:
      orden_esperado: ["1/2", "3/5", "2/3"]  # post-MVP: parser de fracciones
      texto_justificacion: {obligatorio: true, min_caracteres: 15}
    error_por_defecto: E_SIN_CLASIFICAR
    errores_si_falla: {orden_incorrecto: E_INV_ORDEN, sin_texto: E_SIN_JUSTIFICAR}
    pistas:
      - {nivel: 1, texto: "Con den. 30: 15/30, 18/30, 20/30."}
    avance: {tipo: tras_respuesta, max_intentos: 3, siguiente: fin}

fin:
  mensaje: "Revisa pistas y errores en el informe; el profesor completará la valoración."

evidencias_registradas: [fase_id, intento_n, respuesta_bruta, correcta, codigo_error, pistas_usadas, tiempo_segundos, tipo_avance]
observacion_docente: [actitud, trabajo_en_pareja, notas_libres]
```

### A.5. Campos mínimos que el validador debe exigir

| Campo | Obligatorio |
|-------|-------------|
| `dsl_version`, `id` | sí |
| `situacion.texto` | sí |
| `fases[]` (≥1), `fases[].id`, `tipo`, `enunciado`, `avance.siguiente` | sí |
| `error_por_defecto` por fase (o global) | recomendado en v0.1; sí en v0.2 |
| `errores_ref` o errores embebidos | sí |
| `evidencias_registradas`, `observacion_docente` | recomendado |

**Política por defecto (fijada):** tipos de fase desconocidos → **rechazo en validación** (no ejecución silenciosa).

### A.6. Boceto de `ficha.md`

Capa humana: situación, objetivos, errores previsibles (enlace a `errores.yaml`), evidencias automáticas vs. observación docente.

### A.7. Uso por el motor

1. Leer metadatos + escenario + errores.  
2. Validar.  
3. Ejecutar fases y registrar evidencias.  
4. Exportar; el profesor completa observación.

### A.8. Limitaciones conscientes del ejemplo v0.1

| Punto | Problema | Corrección prioritaria |
|-------|----------|-------------------------|
| Fase 2 lista `[30,60,90]` | Falsos negativos (p. ej. 120) | `multiplo_comun: [2,3,5]` |
| Fase 3 por cadenas | Fallos por formato/espacios | Parser / normalización de fracciones |
| Sin `error_por_defecto` | Casos indefinidos | Campo explícito → `E_SIN_CLASIFICAR` |
| Tipos desconocidos | Comportamiento ambiguo | Rechazo en validación |
| Códigos ricos en texto libre | Poco fiables | Solo mapeos claros; resto sin clasificar + docente |
| Justificación por longitud | Texto vacío de contenido | Aceptable en MVP; post-MVP palabras clave o revisión |
| SQLite sin tablas aquí | Implementación incompleta | Documentar esquema en la memoria |
| YAML del escenario | ¿Código o contenido? | **Contenido CC BY-SA**; motor GPL-3.0 |
