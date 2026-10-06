# Actividad completa: Cazador de alucinaciones

**Nivel orientativo:** 3.º–4.º ESO y Bachillerato (adaptable a 1.º–2.º ESO con errores más visibles).  
**Duración:** 50–55 minutos (una sesión) o 2 × 25 min.  
**Tema:** cualquiera del momento (ecuaciones, funciones, geometría, probabilidad…).  
**Rol de la IA:** *objeto de análisis*, no resolutor del alumno.

Enlaces: [limitaciones y casos](../ia-generativa/limitaciones-alucinaciones.md) · [rúbricas](../evaluacion/rubricas-uso-ia.md) · [catálogo de prompts](../prompts/catalogo-prompts-matematicas.md)

---

## 1. Objetivos

| Tipo | Objetivo |
|------|----------|
| **Matemático** | Detectar errores en una resolución y reescribir una versión correcta y justificada |
| **Metacognitivo** | Explicitar estrategias de verificación (casos numéricos, dominio, coherencia) |
| **Sobre IA** | Comprender que un texto formal y confiado puede ser falso |

**Criterios de evaluación (orientativos LOMLOE):** los del bloque de la unidad en curso (resolución de problemas, razonamiento, comunicación); esta actividad **no sustituye** la evaluación del saber matemático de la unidad, la complementa.

---

## 2. Materiales

- Una **resolución con 1–2 errores sutiles** (preparada por el docente; ver §4).
- Hoja de análisis (o plantilla digital): pasos / dudoso / por qué / corrección.
- [Rúbrica de análisis de resolución de IA](../evaluacion/rubricas-uso-ia.md) (sección 2), compartida al inicio.
- Opcional: calculadora, GeoGebra o libro para contrastar.

---

## 3. Secuencia paso a paso

| Tiempo | Fase | Qué hace el docente | Qué hace el alumnado |
|--------|------|---------------------|----------------------|
| 5 min | **Marco** | Explica el objetivo: «No es pillar a la IA por deporte; es entrenar verificación.» Entrega la rúbrica. | Escucha; pregunta dudas sobre la rúbrica |
| 5 min | **Problema** | Presenta el *problema original* (sin la resolución errónea). | Intenta 2–3 minutos en silencio o pareja (opcional, si hay tiempo) |
| 25 min | **Análisis** | Entrega la resolución «de una IA» con errores. Circula, no resuelve. | En parejas: (1) numeran pasos, (2) marcan dudosos, (3) justifican, (4) reescriben la parte incorrecta |
| 10 min | **Puesta en común** | Recoge 2–3 estrategias de detección distintas. | Comparten qué les hizo sospechar (orden de magnitud, dominio, un paso sin justificación…) |
| 5 min | **Cierre** | Conecta con la norma de aula: «Si usáis IA fuera de clase, el mismo checklist.» | Anotan 2 preguntas de verificación para el próximo problema |

---

## 4. Cómo preparar la resolución «contaminada»

### Opción A — Prompt para generar errores a propósito

```
Eres un generador de materiales didácticos de Matemáticas para [nivel].
Problema:
[pegar problema del tema actual]

Genera una resolución paso a paso que parezca cuidada y formal, pero introduce exactamente 2 errores sutiles (elige entre: aritmética intermedia incorrecta, olvido de dominio, aplicación incorrecta de una propiedad, inconsistencia entre un cálculo y la conclusión).
No indiques los errores en el texto principal.
Al final, en una sección separada llamada «ERRORES PARA EL DOCENTE», lista los errores y la corrección breve.
```

### Opción B — Usar un fallo real

Pedir la resolución a un chatbot *sin* pedir errores; si aparece un fallo usable, guardarlo. Más auténtico; menos control del tipo de error.

### Opción C — Casos tipo

Usar como inspiración los [casos A–F de limitaciones](../ia-generativa/limitaciones-alucinaciones.md) (datos contradictorios, Rolle/Lagrange, tabla–fórmula inconsistente, etc.).

**Recomendación:** 1 error «casi invisible» + 1 error detectables con comprobación numérica. Evitar 5 fallos evidentes (trivializa la actividad).

---

## 5. Evidencias a recoger

1. Hoja de análisis por pareja (marcas + justificaciones).
2. Resolución corregida (individual o por pareja).
3. Opcional (2 min): un alumno explica oralmente el error principal.

**No evaluar** solo si «pillaron a la IA»: evaluar la **calidad de la justificación matemática** y la corrección.

---

## 6. Rúbrica rápida (alineada con la del repo)

| Criterio | Excelente | Adecuado | En desarrollo | Insuficiente |
|----------|-----------|----------|---------------|--------------|
| Detección | Localiza los errores relevantes | Localiza la mayoría | Solo errores secundarios | No detecta errores claros |
| Justificación | Explica matemáticamente por qué falla | Explicación correcta y breve | Vaga | No justifica |
| Corrección | Versión correcta y clara | Globalmente correcta | Parcial | Incorrecta o ausente |

---

## 7. Posibles problemas y gestión

| Problema | Qué hacer |
|----------|-----------|
| «No encontramos ningún error» | Pista graduada: «Mirad el paso 3 sustituyendo x = …» |
| Se centran en el estilo del texto, no en la matemática | Reconducir: «¿Este paso se deduce del anterior? ¿Con qué propiedad?» |
| Un miembro de la pareja domina y el otro copia | Exigir que cada uno marque al menos un paso y lo explique |
| La IA del aula «ya no comete ese error» | Tener preparada la versión contaminada en papel/PDF; no depender del modelo en vivo |
| Alumnado frustrado («entonces no sirve para nada») | Cierre: sirve *si* verificas; igual que una calculadora mal usada |

---

## 8. Variantes

- **1.º–2.º ESO:** un solo error aritmético o de signos; más tiempo de corrección guiada.
- **Bachillerato:** demostración o problema de optimización con un salto lógico.
- **Comparar dos modelos:** cada pareja analiza la salida de un chat distinto y contrastan fallos.
- **Error en el enunciado:** datos inconsistentes (caso C); primero detectar si el problema es posible.

---

## 9. Diferenciación (DUA)

| Necesidad | Ajuste |
|-----------|--------|
| Dificultades de lectura | Resolución en pasos muy cortos; resaltar operaciones |
| Alta capacidad | Pedir un *segundo* error posible o un contraejemplo relacionado |
| Ansiedad ante el error | Enfatizar que el fallo está *plantado*; el éxito es detectar y explicar |

---

## 10. Después de la sesión

- Guardar 1–2 resoluciones contaminadas buenas en la carpeta de la unidad (reutilizables).
- Si la norma de aula permite IA en casa, recordar el checklist de verificación en la siguiente tarea.
- Opcional: enlazar con la [plantilla de proceso con IA](../evaluacion/plantilla-proceso-ia.md) cuando haya tareas *con* uso permitido.

---

*Actividad de apoyo para el Máster de Profesorado · Matemáticas. Adaptar al grupo y a la programación de aula.*
