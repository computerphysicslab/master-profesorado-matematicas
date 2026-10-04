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

Así el repositorio de escenarios puede crecer como **bien común docente** sin obligar a que cada adaptación de una ficha de fracciones herede las obligaciones de copyleft del código ejecutable. En `metadatos.yaml` debe figurar siempre la licencia del contenido.

Crecimiento posterior (fuera del MVP del TFM): rankings por uso, resultados educativos agregados y anónimos, revisión por pares de escenarios.

---

## 4. Identidad del alumnado, persistencia, informes y exportación

- **Identificador único** por alumno/a en el ámbito del centro o del grupo (código interno; no basta nombre+apellido).
- **Persistencia local:** **SQLite** embebido (p. ej. `modernc.org/sqlite`) — portable, sin servidor, coherente con el diseño offline.  
  *Nota:* Redis u otras bases cliente-servidor **no** encajan en el núcleo offline; quedarían para una eventual arquitectura multiusuario futura.
- **Informes en la aplicación:** por alumno, por grupo; el profesor completa con anotaciones subjetivas.
- **Exportación interoperable (sin LMS):**  
  - **CSV** — listados de resultados, evidencias por criterio, frecuencias de error; pensado para abrir en hojas de cálculo o plantillas de evaluación del centro.  
  - **JSON** — volcado estructurado de sesión (fases, intentos, códigos de error, tiempos) para archivo o análisis posterior.  
  - Objetivo: **no depender de un campus virtual**; el profesor pega o importa en la herramienta que ya use el centro.
- **RGPD:** datos en local; sin telemetría obligatoria; consentimiento y minimización de datos en el piloto.

---

## 5. Banco de errores típicos (didáctica del error)

Cada escenario declara un **banco de malentendidos** versionado (en la ficha pedagógica y en la capa formal). Ejemplo completo en el [Anexo A](#anexo-a--ejemplo-dsl-v01-ordenación-de-fracciones).

**Uso en el ciclo:**

1. El motor intenta **clasificar** la respuesta o el planteamiento (cuando sea posible de forma fiable).
2. El informe del alumno y el del **grupo** agregan frecuencias por código de error.
3. El profesor ve de un vistazo qué malentendidos dominan la clase y orienta la siguiente sesión (no solo “aprobado / suspenso”).

Esto conecta SimulaESO con la tradición de **análisis de errores** en didáctica de las Matemáticas y da valor añadido al informe frente a un simple score.

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

- [02 — tecnoestrés](02-tecnoestres-digital.md): menos navegador y menos ruido digital.
- [01](01-penalizacion-aprendizaje-ia-generativa.md) / [05](05-esfuerzo-cognitivo-y-pensamiento-critico.md): la IA asiste al **autor** del escenario, no sustituye el pensamiento del alumno en la ejecución.
- [03 — burocracia docente](03-burocratizacion-docente-y-carga-administrativa.md): informes y export CSV como alivio de carga, no como evaluación opaca.
- [14 — datos reales](14-datos-reales-vs-libro-estadistica.md): escenarios de estadística con CSV locales.

---

## 7. Preguntas de investigación

### Variante A — Arquitectura (núcleo del TFM de innovación)

> ¿Puede un motor + DSL mínimo ejecutar un escenario nuevo (p. ej. ordenación de fracciones) definido solo por especificación formal, sin recompilar ni alterar el código del motor?

### Variante B — Viabilidad de aula

> ¿Reduce el paquete offline (motor + escenarios locales) el tiempo de preparación y las interrupciones por red respecto a la misma secuencia en herramientas cloud?

### Variante C — Evaluación docente

> ¿Percibe el profesorado que los informes y la exportación CSV/JSON agilizan la recogida de evidencias sin sustituir su juicio profesional?

### Variante D — Aprendizaje (opcional / ambiciosa)

> ¿Hay diferencias de rendimiento o de calidad de justificación entre grupo experimental y control a igualdad de contenidos?

**Recomendación:** A + B como eje del TFM; C con entrevista/cuestionario breve; D solo si el piloto lo permite.

---

## 8. Hipótesis posibles

- **H1.** Un escenario adicional se incorpora al sistema modificando únicamente ficheros de especificación (y recursos), no el código Go del motor.
- **H2.** El tiempo de arranque y la tasa de fallos por red mejoran frente al flujo cloud habitual en el mismo hardware.
- **H3.** El informe local y la exportación CSV reducen el tiempo percibido de «poner evidencias en limpio» sin eliminar la observación docente.
- **H4.** El alumnado completa más fases de la SdA en el tiempo lectivo cuando no hay dependencia de login/red.
- **H5.** El agregado de códigos de error del banco del escenario resulta útil al docente para planificar la siguiente sesión.

---

## 9. Variables

| Dimensión | Indicadores |
|-----------|-------------|
| Arquitectura | Escenarios cargados sin recompilar; errores de validación del DSL |
| Eficiencia de aula | Tiempo de arranque; fallos de red; tiempo hasta primera tarea útil |
| Completitud | % de fases / escenarios terminados en la sesión |
| Focalización | Observación / autodeclaración de interrupciones |
| Evaluación docente | Tiempo percibido; utilidad del informe; uso real del CSV/JSON exportado |
| Didáctica del error | Frecuencia de códigos de error; coherencia con observación del profesor |
| Usabilidad | SUS breve; nº de clics hasta empezar |
| Réplica en casa | Ejecución del binario + escenario sin ayuda técnica |

---

## 10. MVP técnico y didáctico del TFM

No hace falta una biblioteca enorme de actividades. Basta demostrar el concepto:

| Pieza | Contenido mínimo |
|-------|------------------|
| Motor | Carga de escenario formal, bucle de fases, evaluación simple, pistas, registro de errores |
| DSL | Esquema documentado (campos obligatorios + grafo de fases + códigos de error) — ver [Anexo A](#anexo-a--ejemplo-dsl-v01-ordenación-de-fracciones) |
| Validación | CLI o paso previo que rechace escenarios mal formados |
| Escenarios | **2–3** (ordenación de fracciones + estadística CSV + probabilidad/Monte Carlo) |
| Identidad + SQLite | Altas de grupo; sesión; informe por alumno |
| Exportación | CSV (listado grupo) + JSON (sesión detallada) |
| UI 2D | Situación, respuesta, feedback |
| Documentación | Guía de autoría + especificación del DSL + **protocolo de Prácticum** |

**Experimento de arquitectura del TFM:** crear el tercer escenario **solo** tocando la especificación (y recursos), no el motor.

Fuera de alcance del MVP: CAS simbólico completo, multiusuario en red, Redis, rankings comunitarios en producción, Android, integración nativa con un LMS concreto.

---

## 11. Protocolo de Prácticum (validación en el aula)

Diseño operativo inspirado en los protocolos de las ideas 06 y 11: una secuencia breve, medible y éticamente viable durante el Prácticum.

| Momento | Acción | Datos a recoger |
|---------|--------|-----------------|
| **Antes** | Instalar/copiar binario + 1 escenario; alta de grupo con IDs | Tiempo de preparación; incidencias técnicas |
| **Sesión 0 (opcional)** | Familiarización 10–15 min | Usabilidad percibida |
| **Sesión experimental** | Misma SdA con SimulaESO (grupo E) | Arranque; fallos de red (0 esperados); % fases completadas; observación de focalización |
| **Sesión control** | Misma SdA con herramienta cloud/navegador habitual (grupo C o semana alterna) | Mismos indicadores |
| **Después** | Exportar CSV; el tutor completa 3–5 observaciones cualitativas | Utilidad del informe; tiempo “en limpio”; impresión sobre el banco de errores |
| **Cierre** | Cuestionario breve alumnado (4–6 ítems) + nota de campo del profesor en prácticas | Satisfacción; barreras |

**Rúbrica mínima de observación (ejemplo):** interrupciones por técnica / por distracción; pide ayuda de contenido vs. de “cómo va el programa”; termina la fase con justificación o solo con resultado.

**Ética:** consentimiento familias/centro; IDs no equivalentes a datos personales innecesarios; sin subir la base SQLite a la nube.

---

## 12. Alcance realista y riesgos

| Riesgo | Mitigación |
|--------|------------|
| Ambición de «plataforma total» | MVP = motor + DSL + 2–3 escenarios + export |
| IA que genera basura formal | Esquema cerrado + validación estricta; IA solo asistida |
| Confundir informe automático con evaluación | Campos de observación docente; discurso claro en la memoria |
| Clasificación de errores poco fiable | Códigos solo cuando la detección sea clara; resto “sin clasificar” |
| Identidad y privacidad | IDs locales; SQLite en carpeta del profesor; sin cuentas cloud |
| Curva Go/UI | Plan B: motor CLI + UI mínima |
| Efecto novedad | Medir fricción técnica, no solo motivación |

---

## 13. Potencial para TFM y títulos posibles

- Innovación **tecnológica y educativa** (motor + lenguaje + piloto).
- Transferencia: repo de escenarios (CC BY-SA), código GPL-3.0, documentación de autoría.
- Escalabilidad social: comunidad de profesores-autores si el núcleo funciona.

**Títulos posibles:**

- **SimulaESO: un motor offline de situaciones de aprendizaje para Matemáticas de ESO**
- **Del diseño didáctico al escenario ejecutable: DSL y motor open source para el aula de Matemáticas**
- **Situaciones de aprendizaje como datos: arquitectura y pilotaje de un entorno local en Go**

---

## 14. Palabras clave

- Motor de escenarios
- Situaciones de aprendizaje (SdA)
- DSL educativo
- Software offline
- Go / Golang
- Open source (GPL-3.0)
- Contenidos CC BY-SA
- UI 2D ligera
- SQLite
- Exportación CSV/JSON
- Banco de errores / didáctica del error
- Evaluación formativa / evidencias
- Repositorio de escenarios
- LOMLOE Aragón
- Prácticum
- Soberanía tecnológica

---

## 15. Encaje con Atlas y bibliometría

| Evitar | Apostar |
|--------|--------|
| Otra app de ejercicios cerrados | **SdA como dato + motor reutilizable** |
| «IA que enseña mates» | IA solo en **autoría formal** del escenario |
| Evaluación automática total | Evidencias + export + **juicio docente** |
| Solo código sin aula | **Protocolo de Prácticum** con indicadores de fricción |

---

## 16. Estado y siguientes pasos

**Estado:** propuesta elaborada; candidata fuerte a TFM de **innovación** (arquitectura + piloto). El [Anexo A](#anexo-a--ejemplo-dsl-v01-ordenación-de-fracciones) fija un **DSL v0.1 de referencia** (provisional).

1. Validar/ajustar el esquema del Anexo A con el tutor del TFM.
2. Implementar motor mínimo + validación + registro de códigos de error.
3. Segundo escenario **sin tocar el motor** (prueba de arquitectura).
4. UI 2D + SQLite + informe + **export CSV/JSON**.
5. Aplicar el **protocolo de Prácticum** (sección 11).
6. Memoria (especificación DSL, licencias duales, guía de autoría).

---

## 17. Bibliografía y recursos semilla

- Orden ECD/1172/2022 y ECD/1173/2022 (currículo Aragón).
- Go: https://go.dev · Fyne / Gio · gonum / gonum/plot.
- SQLite embebido en Go (`modernc.org/sqlite`).
- GPL-3.0 · Creative Commons BY-SA 4.0 (contenidos).
- RGPD / AEPD — protección de datos en centros educativos.
- Literatura sobre software libre en educación matemática; carga cognitiva y entornos digitales (idea 02).
- Análisis de errores en educación matemática; sistemas autor y lenguajes de dominio (DSL): posicionar SimulaESO como **autoría didáctica → ejecución local**, no como LMS cloud.

---

## 18. Pregunta guía

> **Si una situación de aprendizaje bien diseñada pudiera ejecutarse como un escenario validado —sin reprogramar el aula digital cada vez— ¿qué motor, qué lenguaje formal y qué evidencias de aula demuestran que ese camino es mejor que depender de la nube o de actividades cableadas en el código?**

---

## Anexo A — Ejemplo DSL v0.1: ordenación de fracciones

> **Estado:** propuesta de esquema para el MVP. No es una API cerrada; puede evolucionar a v0.2 tras el primer prototipo.  
> **Carpeta prevista:** `escenarios/aritmetica/ordenacion-fracciones/`

### A.1. Estructura de ficheros

```text
escenarios/aritmetica/ordenacion-fracciones/
├── metadatos.yaml
├── ficha.md              # capa pedagógica (humana)
├── escenario.yaml        # capa formal (motor)
├── errores.yaml          # banco de malentendidos
└── recursos/             # opcional (imágenes, CSV)
```

### A.2. `metadatos.yaml`

```yaml
id: aritmetica.ordenacion-fracciones
version: "0.1.0"
titulo: Ordenación de fracciones
curso: "1 ESO"          # orientativo; adaptable
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

### A.3. `errores.yaml` (banco de errores)

```yaml
dsl_version: "0.1"
errores:
  - codigo: E_DENOM_IGUAL
    descripcion: Compara numeradores (o denominadores) sin reducir a común denominador o a la misma unidad.
    gravedad: alta
  - codigo: E_ENTEROS
    descripcion: Trata numerador y denominador como cantidades independientes (como enteros sueltos).
    gravedad: alta
  - codigo: E_INV_ORDEN
    descripcion: Invierte el orden (coloca la fracción menor como mayor o al revés).
    gravedad: media
  - codigo: E_EQUIV_NO_REC
    descripcion: No reconoce fracciones equivalentes (p. ej. 1/2 y 2/4).
    gravedad: media
  - codigo: E_SIN_JUSTIFICAR
    descripcion: Da un orden plausible pero no aporta criterio o justificación cuando se pide.
    gravedad: baja
  - codigo: E_SIN_CLASIFICAR
    descripcion: Respuesta incorrecta o incompleta que el motor no puede asociar a un malentendido concreto.
    gravedad: baja
```

### A.4. `escenario.yaml` (capa formal ejecutable)

```yaml
dsl_version: "0.1"
id: aritmetica.ordenacion-fracciones

# Referencia al banco de errores del mismo directorio
errores_ref: errores.yaml

situacion:
  titulo: "Reparto de pizza en la excursión"
  texto: >
    En la excursión, tres grupos han pedido pizza. El grupo A ha comido 2/3 de una pizza,
    el grupo B 3/5 y el grupo C 1/2. Antes de pedir más, la clase debe ordenar de menor
    a mayor qué grupo ha comido más cantidad de pizza (misma pizza unitaria).
  # Principio didáctico: situación antes que fórmula

fases:
  - id: fase_1_estimacion
    tipo: eleccion_orden
    enunciado: >
      Sin hacer todavía cálculos largos, ¿cuál crees que es el orden de menor a mayor
      cantidad comida (A = 2/3, B = 3/5, C = 1/2)?
    opciones:
      - id: o1
        etiqueta: "C < B < A"
      - id: o2
        etiqueta: "B < C < A"
      - id: o3
        etiqueta: "C < A < B"
      - id: o4
        etiqueta: "A < B < C"
    respuesta_correcta: o1
    # Orden real: 1/2 < 3/5 < 2/3
    pistas:
      - nivel: 1
        texto: "Piensa qué fracción se acerca más a un entero completo (casi 1) y cuál se queda más cerca de la mitad."
      - nivel: 2
        texto: "1/2 es exactamente la mitad. ¿2/3 y 3/5 están por encima o por debajo de la mitad?"
    errores_si_falla:
      # Mapeo opcional opción → código (si no, E_SIN_CLASIFICAR)
      o2: E_INV_ORDEN
      o3: E_DENOM_IGUAL
      o4: E_INV_ORDEN
    avance:
      tipo: tras_respuesta   # o: tras_correcta | tras_max_intentos
      max_intentos: 3
      siguiente: fase_2_comun_denominador

  - id: fase_2_comun_denominador
    tipo: respuesta_corta
    enunciado: >
      Propón un denominador común que te permita comparar 1/2, 3/5 y 2/3.
      Escribe solo el número (denominador común).
    validacion:
      tipo: entero_en_conjunto
      valores_aceptados: [30, 60, 90]   # múltiplos útiles; 30 es el mcm
      # El motor puede aceptar cualquier común múltiplo de 2,3,5 en v0.2;
      # en v0.1 se acota para simplificar la implementación.
    pistas:
      - nivel: 1
        texto: "Los denominadores son 2, 5 y 3. Busca un número en el que quepan los tres."
      - nivel: 2
        texto: "Prueba con 2×3×5."
    errores_si_falla:
      por_defecto: E_DENOM_IGUAL
    avance:
      tipo: tras_correcta
      max_intentos: 4
      siguiente: fase_3_orden_justificado

  - id: fase_3_orden_justificado
    tipo: orden_y_texto
    enunciado: >
      Escribe el orden de menor a mayor usando las fracciones (por ejemplo: 1/2 < 3/5 < 2/3)
      y en una frase indica el criterio que has usado.
    validacion:
      orden_esperado: ["1/2", "3/5", "2/3"]
      texto_justificacion:
        obligatorio: true
        min_caracteres: 15
    pistas:
      - nivel: 1
        texto: "Con denominador 30: 1/2 = 15/30, 3/5 = 18/30, 2/3 = 20/30."
    errores_si_falla:
      orden_incorrecto: E_INV_ORDEN
      sin_texto: E_SIN_JUSTIFICAR
    avance:
      tipo: tras_respuesta
      max_intentos: 3
      siguiente: fin

fin:
  mensaje: >
    Has comparado fracciones en un contexto de reparto. Revisa en el informe
    cuántas pistas usaste y qué tipo de errores aparecieron; el profesor completará
    la valoración con lo observado en clase.

evidencias_registradas:
  - fase_id
  - intento_n
  - respuesta_bruta
  - correcta
  - codigo_error      # de errores.yaml o E_SIN_CLASIFICAR
  - pistas_usadas
  - tiempo_segundos

observacion_docente:
  # Campos que el software deja vacíos para el profesor
  - actitud
  - trabajo_en_pareja
  - notas_libres
```

### A.5. Esquema mínimo del DSL v0.1 (campos que el validador debe exigir)

| Campo / estructura | Obligatorio | Notas |
|--------------------|-------------|--------|
| `dsl_version` | sí | Debe coincidir con la que entiende el motor |
| `id` | sí | Único en el repositorio |
| `situacion.texto` | sí | No empezar por “Calcula…” sin contexto |
| `fases[]` | sí (≥1) | Grafo con `siguiente` sin ciclos |
| `fases[].id` | sí | Identificador estable |
| `fases[].tipo` | sí | Catálogo v0.1: `eleccion_orden`, `respuesta_corta`, `orden_y_texto` |
| `fases[].enunciado` | sí | |
| `fases[].avance.siguiente` | sí | `fin` o id de otra fase |
| `errores_ref` o errores embebidos | sí | Códigos estables |
| `evidencias_registradas` | recomendado | Contrato con SQLite/export |
| `observacion_docente` | recomendado | Recuerda que el juicio es humano |

Tipos de fase adicionales se añaden en **v0.2** sin romper escenarios v0.1 (el motor ignora tipos desconocidos o los rechaza en validación según política elegida).

### A.6. Boceto de `ficha.md` (capa humana, extracto)

```markdown
# SdA: Ordenación de fracciones (excursión y pizzas)

**Curso:** 1.º ESO (adaptable)  
**Saberes:** fracciones; orden; común denominador  
**Competencias:** STEM, CD (uso de entorno local seguro)

## Situación
[Texto narrativo alineado con escenario.yaml]

## Objetivos
- Comparar fracciones con distinto denominador en un contexto significativo.
- Justificar el orden con un criterio explícito (no solo intuición).

## Errores previsibles
Ver errores.yaml (E_DENOM_IGUAL, E_ENTEROS, …).

## Evaluación
- Evidencias automáticas: intentos, pistas, códigos de error.
- Observación docente: actitud, colaboración, calidad de la explicación oral.
```

### A.7. Cómo lo usa el motor (resumen)

1. Lee `metadatos.yaml` + `escenario.yaml` + `errores.yaml`.
2. Valida el esquema (campos obligatorios, `siguiente` existente, códigos de error declarados).
3. Ejecuta `fase_1` → … → `fin`, registrando evidencias en SQLite.
4. Exporta CSV/JSON; el profesor rellena `observacion_docente`.

Con este anexo, el experimento de arquitectura del TFM queda acotado: **implementar el motor para este DSL v0.1** y demostrar que un segundo escenario (p. ej. proporcionalidad) se añade solo con nuevos YAML, sin recompilar la lógica de fases.
