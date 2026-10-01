# Infografía — Diseño curricular e instruccional de Matemáticas

Resumen visual de la asignatura (compatible con Mermaid en el sitio del repositorio).

---

## 1. Hilo conductor

```mermaid
flowchart LR
  A[Currículo oficial] --> B[Diseño curricular]
  B --> C[Programación didáctica]
  C --> D[Diseño instruccional]
  D --> E[Tareas]
  E --> F[Aprendizaje]
  F --> G[Evaluación]
```

---

## 2. Nueve bloques del programa

```mermaid
flowchart TB
  subgraph Marco
    B1[1. Finalidades]
    B2[2. Evolución LGE→LOMLOE]
    B3[3. Elementos LOMLOE]
  end
  subgraph Puente
    B4[4. Programación didáctica]
  end
  subgraph Didáctica
    B5[5. Epistemología y fenomenología]
    B6[6. Transposición didáctica]
    B7[7. Dificultades y obstáculos]
    B8[8. Resolución de problemas]
    B9[9. Génesis escolar de objetos]
  end
  B1 --> B2 --> B3 --> B4
  B4 --> B5 --> B6 --> B7 --> B8 --> B9
```

---

## 3. Piezas del currículo LOMLOE (Matemáticas)

```mermaid
flowchart TB
  PS[Perfil de salida / competencias clave] --> CE[Competencias específicas]
  CE --> CR[Criterios de evaluación]
  CE --> SB[Saberes básicos / sentidos]
  CR --> SA[Situaciones de aprendizaje]
  SB --> SA
  SA --> EV[Evidencias de aprendizaje]
```

**Cinco ejes de las CE (ESO):** resolución de problemas · razonamiento y prueba · conexiones · comunicación y representación · socioafectivo.

**Sentidos:** numérico · medida · espacial · algebraico · estocástico · socioafectivo.

---

## 4. Tres capas del currículo (Remillard & Heck)

```mermaid
flowchart TB
  P[Previsto / designado
  normas y documentos] --> I[Implementado / enacted
  lo que pasa en el aula]
  I --> A[Alcanzado
  lo que se aprende]
```

El trabajo docente está sobre todo en el paso del **previsto** al **implementado** (tareas, contrato didáctico, evaluación).

---

## 5. Transposición didáctica (idea central)

```mermaid
flowchart LR
  SS[Saber sabio / de referencia] --> SA[Saber a enseñar]
  SA --> SE[Saber enseñado]
  SE --> AP[Saber aprendido]
```

---

## 6. De la norma al aula (checklist mental)

```text
□ ¿Qué competencia(s) específica(s) trabajo?
□ ¿Qué criterios voy a evidenciar?
□ ¿Qué saberes / sentidos movilizo?
□ ¿La tarea es situación de aprendizaje o solo ejercicio cerrado?
□ ¿Qué es preceptivo y qué decido yo?
□ ¿Cómo veré el aprendizaje (no solo la respuesta final)?
```

---

## 7. Versión ASCII (una pantalla)

```text
┌─────────────────────────────────────────────────────────┐
│  DISEÑO CURRICULAR E INSTRUCCIONAL DE MATEMÁTICAS       │
├─────────────────────────────────────────────────────────┤
│  Currículo → PD → Unidades → Tareas → Evaluación        │
├──────────────┬──────────────┬───────────────────────────┤
│  MARCO       │  PUENTE      │  DIDÁCTICA DE OBJETOS     │
│  Finalidades │  Programación│  Epistemología            │
│  Evolución   │  didáctica   │  Transposición            │
│  LOMLOE      │              │  Obstáculos / contrato    │
│              │              │  RP · Génesis escolar     │
└──────────────┴──────────────┴───────────────────────────┘
│  CE → Criterios → Saberes/sentidos → SA → Evidencias    │
└─────────────────────────────────────────────────────────┘
```

---

*Relacionado: [introducción for dummies](../introduccion-for-dummies.md) · [glosario](../glosario.md) · [apuntes](../apuntes/).*
