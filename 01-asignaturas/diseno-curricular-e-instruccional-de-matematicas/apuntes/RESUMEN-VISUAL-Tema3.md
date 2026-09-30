# Resumen visual · Tema 3  
## Elementos curriculares LOMLOE y evolución histórica

**Asignatura:** Diseño curricular e instruccional de Matemáticas  
**Bloques del programa:** 2 (cambios curriculares) + 3 (elementos LOMLOE)

---

## 1. Línea temporal de leyes y enfoques

```mermaid
timeline
    title Evolución del currículo de Matemáticas en España
    1970 : LGE
         : Matemática moderna
         : Formalismo · Conjuntos · Estructuras
    1990 : LOGSE
         : Constructivismo
         : Saber hacer · Procedimientos · RP
    2006 : LOE
         : Competencias básicas
         : PISA · KOM (Niss)
    2013 : LOMCE
         : Estándares de aprendizaje
         : Evaluación atomizada
    2020 : LOMLOE
         : Competencias específicas
         : Sentidos · Situaciones · DUA
```

| Ley | Enfoque dominante | Elementos clave | Problema / límite |
|-----|-------------------|-----------------|-------------------|
| **LGE** | Estructural / New Math | Objetivos operativos, conjuntos | Fracaso escolar, lejanía de la realidad |
| **LOGSE** | Constructivista | Conceptos / procedimientos / actitudes | — |
| **LOE** | Competencial (básicas) | 8 competencias básicas | Distancia competencia ↔ materia |
| **LOMCE** | Competencial + estándares | Estándares evaluables | Atomización de la evaluación |
| **LOMLOE** | Competencial + sentidos | CE, criterios, saberes, situaciones | Implementación (ámbitos, formación) |

---

## 2. Referentes que alimentan la LOMLOE

```mermaid
mindmap
  root((LOMLOE<br/>Matemáticas))
    Psicología y didáctica
      Piaget
        Estadios · Concreto→Formal
      Brousseau
        Situaciones didácticas
        Devolución · Institucionalización
      Freudenthal
        Matemáticas como actividad
        Matematización H + V
      Niss / KOM
        8 subcompetencias
        Base de PISA
    Institucionales
      NCTM 2000
        6 principios
        Procesos: resolver · razonar · comunicar · conectar · representar
      CEMAT 2021
        Sentidos matemáticos
        Grandes ideas
        Pensamiento computacional
    Marcos internacionales
      PISA / OCDE
      DUA
```

### Eco curricular de cada referente

| Referente | Idea nuclear | Huella en LOMLOE |
|-----------|--------------|------------------|
| **Piaget** | Construcción activa, estadios | Ritmos, manipulación, respeto cognitivo |
| **Brousseau** | Situación adidáctica + devolución | Situaciones de aprendizaje con sentido |
| **Freudenthal** | Matematización horizontal y vertical | Contexto real ↔ abstracción; sentidos |
| **Niss** | Competencia = usar matemáticas en contextos | Competencias específicas |
| **NCTM** | Procesos matemáticos | Ejes de las CE (salvo socioafectivo) |
| **CEMAT** | Sentidos + grandes ideas | Organización de saberes básicos |

---

## 3. Arquitectura curricular LOMLOE

```mermaid
flowchart TB
  subgraph N1["NIVEL 1 · Finalidades de etapa"]
    OBJ[Objetivos de etapa]
  end

  subgraph N2["NIVEL 2 · Perfil de salida"]
    CK[Competencias clave]
    DO[Descriptores operativos]
    CK --> DO
  end

  subgraph N3["NIVEL 3 · Materia Matemáticas"]
    CE[Competencias específicas<br/>5 ejes]
    CR[Criterios de evaluación]
    SB[Saberes básicos<br/>por sentidos]
    OD[Orientaciones didácticas]
    SA[Situaciones de aprendizaje]
    CE --> CR
    CE --> SB
    CR --> SA
    SB --> SA
    OD -.-> SA
  end

  OBJ --> CK
  DO --> CE
```

**Prescriptivo (norma estatal):** CE, criterios, saberes.  
**Margen docente / currículo designado (CCAA + centro):** orientaciones, ejemplos de situaciones, secuenciación fina, materiales.

---

## 4. Los cinco ejes de las competencias específicas

```mermaid
flowchart LR
  subgraph EJES["Competencias específicas · Matemáticas"]
    direction TB
    E1["① Resolución de problemas<br/>CE.M.1 · CE.M.2"]
    E2["② Razonamiento y prueba<br/>CE.M.3 · CE.M.4<br/>(+ pensamiento computacional)"]
    E3["③ Conexiones<br/>CE.M.5 intramatemáticas<br/>CE.M.6 con otras materias / realidad"]
    E4["④ Comunicación y representación<br/>CE.M.7 · CE.M.8"]
    E5["⑤ Socioafectivo<br/>CE.M.9 personales<br/>CE.M.10 sociales"]
  end
```

> En Bachillerato el eje ⑤ se agrupa en una sola CE.

**Novedad del socioafectivo:** no es solo “emociones positivas”. Incluye:
- Gestión del error y la incertidumbre
- Actitudes matemáticas (procesos, epistemología)
- Trabajo en equipos heterogéneos e identidad positiva como estudiante de matemáticas

---

## 5. Saberes básicos organizados en sentidos

```mermaid
pie showData
  title Sentidos matemáticos (organización de saberes)
  “Numérico” : 18
  “De la medida” : 14
  “Espacial” : 16
  “Algebraico” : 18
  “Estocástico” : 16
  “Socioafectivo” : 18
```

*Los pesos son orientativos para visualización; en el currículo no hay jerarquía numérica fija.*

| Sentido | Ideas clave |
|---------|-------------|
| **Numérico** | Cantidad, operaciones, proporcionalidad, estimación |
| **Medida** | Magnitud, medición, relaciones entre magnitudes |
| **Espacial** | Figuras, localización, movimientos, visualización |
| **Algebraico** | Patrones, variable, modelo, funciones, equivalencia |
| **Estocástico** | Distribución, incertidumbre, inferencia |
| **Socioafectivo** | Creencias, emociones, error, trabajo colaborativo |

**Grandes ideas** (CEMAT): patrones, modelo, variable, relaciones y funciones, movimientos, distribución, incertidumbre, magnitud…

---

## 6. De la competencia a la tarea (cadena de diseño)

```mermaid
flowchart LR
  CE[Competencia<br/>específica] --> CR[Criterio de<br/>evaluación]
  CR --> SB[Saberes<br/>de 1–2 sentidos]
  SB --> SA[Situación de<br/>aprendizaje]
  SA --> EV[Evidencias<br/>de desempeño]
```

**Regla práctica:** una situación de aprendizaje rica moviliza **varios criterios** y **al menos dos sentidos**.

---

## 7. Preceptivo vs margen docente

```mermaid
quadrantChart
    title Espacio de decisión del docente
    x-axis Bajo control --> Alto control
    y-axis Bajo impacto curricular --> Alto impacto curricular
    quadrant-1 Diseñar con libertad
    quadrant-2 Respetar y concretar
    quadrant-3 Evitar
    quadrant-4 Cuidar coherencia
    Competencias específicas: [0.2, 0.9]
    Criterios de evaluación: [0.25, 0.85]
    Saberes del curso: [0.3, 0.75]
    Secuenciación diaria: [0.85, 0.55]
    Contextos y ejemplos: [0.9, 0.45]
    Materiales y herramientas: [0.88, 0.4]
    Agrupamientos: [0.8, 0.35]
```

| No se puede | Sí se puede |
|-------------|-------------|
| Vaciar un sentido entero | Decidir *cómo* trabajarlo |
| Ignorar criterios de evaluación | Elegir instrumentos y evidencias |
| Sustituir CE por “temario del libro” | Secuenciar y contextualizar |

---

## 8. Mapa mental de una sola página (síntesis extrema)

```text
                    LOMLOE Matemáticas
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
    EVOLUCIÓN         REFERENTES        ELEMENTOS
    LGE→…→LOMLOE    Piaget·Brousseau    Perfil de salida
    Formal →        Freudenthal·Niss    Competencias clave
    Competencial    NCTM·CEMAT          Competencias específicas
                                        Criterios
                                        Saberes / sentidos
                                        Situaciones de aprendizaje
                           │
                    DISEÑO DOCENTE
                    CE → Criterio → Saberes → Situación → Evidencia
```

---

## 9. Checklist rápido para programar

- [ ] ¿Qué **competencia(s) específica(s)** trabajo?
- [ ] ¿Qué **criterios** voy a evidenciar?
- [ ] ¿Qué **saberes** de qué **sentidos** movilizo? (≥2 recomendable)
- [ ] ¿La tarea es una **situación de aprendizaje** (abierta, contextualizada) o solo un ejercicio?
- [ ] ¿Hay espacio para **comunicación, argumentación y error** (socioafectivo)?
- [ ] ¿Qué es **preceptivo** y qué decido yo?

---

*Resumen visual del Tema 3 · Diseño curricular e instruccional de Matemáticas · Universidad de Zaragoza*
