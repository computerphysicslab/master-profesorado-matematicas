# Ejemplos para distinguir las competencias específicas de Matemáticas (ESO)

**Asignatura:** Diseño curricular e instruccional de Matemáticas  
**Marco normativo:** Real Decreto 217/2022 (ESO) · competencias específicas de Matemáticas  
**Uso:** material de apoyo para diseñar y evaluar actividades con una competencia protagonista clara.

---

## 1. Principio de diseño

La clave para distinguir las competencias específicas es diseñar actividades en las que la **acción matemática principal** sea diferente en cada caso. No basta con cambiar el contexto de un problema: hay que cambiar **qué hace el alumnado** y **qué evidencia** demuestra que ha desarrollado esa competencia.

Las diez competencias **no son compartimentos estancos**. Resolver un problema puede requerir razonar, representar y comunicar. La separación absoluta no es realista. Lo que sí puede conseguirse es que cada actividad tenga una **competencia protagonista inequívoca**, reduciendo al mínimo el peso evaluativo de las demás.

Para cada ejemplo se indican:

| Campo | Pregunta que responde |
|-------|------------------------|
| **Acción matemática observable** | ¿Qué debe hacer el alumno? |
| **Evidencia concreta** | ¿Qué producto o comportamiento se observa? |
| **Qué no se está evaluando** | ¿Qué se deja fuera a propósito para no mezclar competencias? |

---

## 2. Correspondencia orientativa con los ejes del currículo

| Código | Competencia (formulación abreviada) | Eje habitual |
|--------|-------------------------------------|--------------|
| **CE.M.1** | Interpretar, modelizar y resolver problemas | Resolución de problemas |
| **CE.M.2** | Analizar y validar soluciones | Resolución de problemas |
| **CE.M.3** | Formular y comprobar conjeturas | Razonamiento y prueba |
| **CE.M.4** | Pensamiento computacional / algoritmos | Razonamiento y prueba |
| **CE.M.5** | Conexiones entre elementos matemáticos | Conexiones |
| **CE.M.6** | Matemáticas en otras materias y la realidad | Conexiones |
| **CE.M.7** | Representar información matemática | Comunicación y representación |
| **CE.M.8** | Comunicar razonamiento matemático | Comunicación y representación |
| **CE.M.9** | Gestionar el error y la frustración | Socioafectivo |
| **CE.M.10** | Colaborar matemáticamente | Socioafectivo |

> **Nota:** la numeración y el texto literal de cada competencia específica pueden variar ligeramente según el decreto autonómico; el esquema de diez desempeños es el del marco estatal (RD 217/2022). Conviene contrastar siempre con el currículo de la comunidad autónoma de aplicación.

---

## 3. Diez ejemplos, competencia por competencia

### CE.M.1 — Resolver un problema

**Actividad.** Un autobús tiene 52 plazas. Viajan 37 alumnos y 3 profesores. ¿Cuántos alumnos más pueden subir si cada profesor ocupa una plaza?

**Solución:** $52 - 37 - 3 = 12$. Pueden subir 12 alumnos más.

| Campo | Contenido |
|-------|-----------|
| **Acción** | Identificar datos pertinentes, elegir operaciones y obtener la solución. |
| **Evidencia** | Resultado numérico correcto y, si se pide, breve justificación de las operaciones. |
| **Qué no se evalúa** | Validar una solución ajena (CE.M.2), conjeturar una regla general (CE.M.3) ni explicar el razonamiento a un compañero (CE.M.8). |

**Qué la distingue:** el objetivo es **encontrar** una solución a una situación planteada, no juzgar una solución ya propuesta.

---

### CE.M.2 — Validar una solución

**Actividad.** Un alumno afirma que $3(x+4)=21$ tiene como solución $x=3$. Comprueba si tiene razón sustituyendo ese valor en la ecuación original.

**Solución:** $3(3+4)=21$, es decir $21=21$. La solución es correcta.

| Campo | Contenido |
|-------|-----------|
| **Acción** | Verificar la corrección matemática de una respuesta ya propuesta. |
| **Evidencia** | Sustitución correcta y conclusión explícita (válida / no válida). |
| **Qué no se evalúa** | Resolver la ecuación desde cero (CE.M.1) ni diseñar un método general (CE.M.4). |

**Qué la distingue:** el alumnado **no tiene que descubrir** la solución; tiene que **comprobarla**. Para evaluar también la idoneidad contextual, puede añadirse una restricción de la situación real (p. ej. «¿tiene sentido esa solución en el contexto del problema?»).

---

### CE.M.3 — Formular y comprobar una conjetura

**Actividad.** Calcula la suma de dos números impares consecutivos en varios casos y conjetura si el resultado es siempre múltiplo de 4.

**Ejemplos:** $3+5=8$, $7+9=16$, $11+13=24$.

**Conjetura y comprobación:** dos impares consecutivos pueden escribirse como $2n+1$ y $2n+3$. Su suma es $4n+4=4(n+1)$, siempre divisible entre 4.

| Campo | Contenido |
|-------|-----------|
| **Acción** | Formular una regla general a partir de casos y comprobarla. |
| **Evidencia** | Enunciado de la conjetura + comprobación (por más casos o por razonamiento). |
| **Qué no se evalúa** | Diseñar un algoritmo general para otra tarea (CE.M.4) ni solo calcular sumas sueltas (CE.M.1). |

**Advertencia didáctica:** la demostración algebraica completa puede ir más allá de lo imprescindible en los primeros cursos de ESO; basta evaluar la **formulación** y una **comprobación guiada** (más casos o justificación informal).

---

### CE.M.4 — Diseñar un algoritmo

**Actividad.** Escribe un algoritmo que determine cuántas cifras tiene un número entero positivo, sin convertirlo a texto.

**Solución propuesta:**

1. Inicializar `cifras = 0`.
2. Mientras el número sea mayor que cero, dividirlo entre 10 (parte entera).
3. Incrementar `cifras` en cada repetición.
4. Devolver `cifras`.

**Ejemplo:** para 583, las divisiones enteras producen 58, 5 y 0 → el algoritmo devuelve 3.

| Campo | Contenido |
|-------|-----------|
| **Acción** | Descomponer la tarea en instrucciones ordenadas con repetición. |
| **Evidencia** | Secuencia de pasos que funciona con **varios** valores de prueba. |
| **Qué no se evalúa** | Conjeturar una propiedad numérica (CE.M.3) ni solo obtener el resultado de un caso (CE.M.1). |

**Advertencia:** conviene exigir que el algoritmo funcione con distintos valores, no solo que se describa una secuencia de pasos sin comprobarla.

---

### CE.M.5 — Conectar ideas matemáticas

**Actividad.** Un rectángulo mide 8 cm de largo y 5 cm de ancho. Relaciona su área con la de los dos triángulos iguales que se obtienen al trazar una diagonal.

**Solución:** el rectángulo tiene área $8\cdot 5=40\,\text{cm}^2$. Cada triángulo tiene área $40/2=20\,\text{cm}^2$. La fórmula del área del triángulo ($A=bh/2$) se relaciona con la del rectángulo ($A=bh$).

| Campo | Contenido |
|-------|-----------|
| **Acción** | Hacer explícita una relación entre conceptos geométricos. |
| **Evidencia** | Explicación de la conexión entre las dos fórmulas (no solo el cálculo numérico). |
| **Qué no se evalúa** | Solo calcular un área sin relacionar fórmulas, ni conectar con otra materia (CE.M.6). |

**Qué la distingue:** el objetivo es la **conexión intramatemática**, no el cálculo aislado ni el vínculo con Física u otra disciplina.

---

### CE.M.6 — Conectar matemáticas y otra materia

**Actividad.** En un experimento de Física, una pelota recorre 6 metros en 2 segundos a velocidad constante. Calcula su velocidad media y expresa qué magnitud física has obtenido.

**Solución:** $v=d/t=6/2=3\,\text{m/s}$. Se ha obtenido la velocidad media.

| Campo | Contenido |
|-------|-----------|
| **Acción** | Aplicar una relación matemática a una magnitud de otra materia e interpretar el resultado. |
| **Evidencia** | Cálculo correcto **con unidades** e identificación de la magnitud física. |
| **Qué no se evalúa** | Conexiones solo entre conceptos matemáticos (CE.M.5) ni solo el cálculo sin contexto disciplinar. |

**Qué la distingue:** la relación distancia–tiempo–velocidad pertenece a un **contexto científico externo** a las matemáticas.

---

### CE.M.7 — Representar información matemática

**Actividad.** Representa en unos ejes cartesianos los puntos $(1,2)$, $(2,4)$, $(3,6)$ y $(4,8)$.

**Resultado esperado:** los cuatro puntos aparecen alineados sobre la recta $y=2x$.

| Campo | Contenido |
|-------|-----------|
| **Acción** | Construir una representación gráfica fiel a los datos. |
| **Evidencia** | Colocación correcta de las coordenadas en el plano. |
| **Qué no se evalúa** | Explicar por qué están alineados o redactar una conclusión (CE.M.8). |

**Qué la distingue:** se pide **construir la representación**, no argumentar sobre ella.

---

### CE.M.8 — Comunicar razonamiento matemático

**Actividad.** Explica por escrito por qué la suma de dos números pares siempre es par, de modo que otro alumno pueda comprender el argumento.

**Respuesta modelo:** todo número par puede expresarse como $2a$ o $2b$, con $a,b$ enteros. Su suma es $2a+2b=2(a+b)$. Como $a+b$ es entero, la suma es múltiplo de 2 y, por tanto, par.

| Campo | Contenido |
|-------|-----------|
| **Acción** | Elaborar una explicación matemática comprensible para otra persona. |
| **Evidencia** | Claridad, precisión del vocabulario y coherencia del argumento. |
| **Qué no se evalúa** | La dificultad del contenido (aquí es deliberadamente sencillo) ni solo el resultado final sin explicación. |

**Qué la distingue:** lo evaluado es **cómo se hace comprensible** el razonamiento, no el descubrimiento de un resultado nuevo.

---

### CE.M.9 — Gestionar el error y la frustración

**Actividad.** Un alumno resuelve mal $2(x+3)=14$, se bloquea y afirma: «Soy incapaz de hacer ecuaciones». Se le pide registrar qué siente, identificar el paso que le genera dificultad y aplicar una estrategia para volver a intentarlo.

**Respuesta esperada (modelo):** «Me he frustrado al obtener un resultado incorrecto. Voy a dividir ambos miembros entre 2 y después restar 3: $x+3=7$, luego $x=4$».

| Campo | Contenido |
|-------|-----------|
| **Acción** | Reconocer la emoción, evitar un juicio global sobre la propia capacidad y perseverar con una estrategia. |
| **Evidencia** | Registro de la dificultad + estrategia concreta de reintento (observable). |
| **Qué no se evalúa** | La rapidez ni la corrección del primer intento; tampoco se exige revelar emociones íntimas más allá de lo necesario para la autorregulación. |

**Qué la distingue:** se evalúa la **autorregulación ante la dificultad**, no el dominio técnico inicial.

---

### CE.M.10 — Colaborar matemáticamente

**Actividad.** En parejas, un alumno dicta una serie de coordenadas y el otro las marca en una cuadrícula sin ver la hoja original. Después intercambian los roles y comprueban si ambas representaciones coinciden.

| Campo | Contenido |
|-------|-----------|
| **Acción** | Escuchar, respetar turnos, distribuir roles, pedir aclaraciones y asumir responsabilidad en una tarea compartida. |
| **Evidencia** | Proceso de colaboración observable (turnos, aclaraciones, comprobación conjunta). |
| **Qué no se evalúa** | Solo que cada estudiante sepa representar puntos de forma individual (CE.M.7), ni solo el producto final del equipo sin observar el proceso. |

**Qué la distingue:** el foco es la **coordinación entre ambos**, no la competencia individual de representación.

---

## 4. Competencias que más se confunden

| Par | Diferencia esencial |
|-----|---------------------|
| **CE.M.1 vs CE.M.2** | Obtener una solución frente a comprobar su corrección (y, en su caso, su idoneidad). |
| **CE.M.3 vs CE.M.4** | Investigar si una afirmación es cierta frente a diseñar un procedimiento sistemático. |
| **CE.M.5 vs CE.M.6** | Relacionar conceptos matemáticos entre sí frente a relacionar las matemáticas con otras materias o con la realidad. |
| **CE.M.7 vs CE.M.8** | Construir una representación frente a explicar o argumentar con lenguaje matemático. |
| **CE.M.9 vs CE.M.10** | Regular la propia respuesta emocional frente a colaborar eficazmente con otras personas. |

Esta distinción es coherente con el currículo estatal de ESO, que define las competencias específicas como **desempeños** y establece criterios de evaluación propios para cada una (RD 217/2022 y desarrollos autonómicos).

---

## 5. Advertencias didácticas por competencia

| Competencia | Mejora recomendada al diseñar la actividad |
|-------------|--------------------------------------------|
| **CE.M.1** | Preferir problemas de aplicación directa si se quiere observar la resolución sin exigir investigación abierta. |
| **CE.M.2** | Pedir validación de una respuesta ya dada; no confundir con la búsqueda inicial de la solución. |
| **CE.M.3** | En cursos bajos, priorizar formulación y comprobación guiada frente a la demostración formal completa. |
| **CE.M.4** | Exigir que el algoritmo funcione con distintos valores de prueba. |
| **CE.M.5** | Evaluar explícitamente la **conexión** entre conceptos, no solo el cálculo. |
| **CE.M.6** | Partir de una magnitud y una relación propias de la otra materia. |
| **CE.M.7** | Evaluar la fidelidad de la representación; no exigir explicación adicional. |
| **CE.M.8** | Valorar claridad y precisión del argumento; mantener sencilla la matemática de fondo. |
| **CE.M.9** | Centrarse en autorregulación y perseverancia **observables**; no exigir revelación emocional íntima. |
| **CE.M.10** | Observar el **proceso** de colaboración, no solo calificar el producto final del equipo. |

---

## 6. Plantilla rápida de ficha de evaluación

Para cualquier actividad nueva, conviene rellenar:

```text
Competencia protagonista: CE.M.__
Acción matemática observable:
Evidencia concreta:
Qué no se está evaluando (competencias secundarias descartadas):
```

Esa plantilla muestra con claridad por qué una actividad corresponde a una competencia determinada, aunque en la práctica pueda movilizar otras de forma secundaria.

---

## 7. Referencias

- Real Decreto 217/2022, de 29 de marzo, por el que se establece la ordenación y las enseñanzas mínimas de la Educación Secundaria Obligatoria (BOE). Anexo de Matemáticas: competencias específicas y criterios de evaluación.
- Desarrollos curriculares autonómicos correspondientes (decretos u órdenes de cada comunidad).

---

## Material relacionado

- [01 — Finalidades de la enseñanza de las Matemáticas](../apuntes/01-finalidades-ensenanza-matematicas.md)
- [02 — Evolución curricular y normativa](../apuntes/02-evolucion-curricular-y-normativa.md)
- [Ejemplos de contextos sociocríticos](ejemplos-contextos-sociocriticos-matematicas.md)
- [Modelización matemática en el aula](modelizacion-matematica-aula.md)
- [Exigencia cognitiva, disciplina y razonamiento](exigencia-cognitiva-disciplina-razonamiento.md)
