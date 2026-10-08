---
layout: default
title: "Mutaciones, biosfera y supercomputación"
parent: Situaciones de aprendizaje
nav_order: 25
---

# SA — ¿Puede la supercomputación actual contar toda la evolución mutacional de la biosfera?

## 0. Metadatos

| Campo | Contenido |
|-------|-----------|
| **Título de la SA** | Mutaciones históricas vs capacidad de cómputo |
| **Nivel / curso** | **3.º–4.º ESO** (núcleo numérico); **1.º–2.º Bach.** (sensibilidad, logaritmos, modelo integral) |
| **Duración** | 4–6 sesiones × 50–55 min |
| **Fecha / versión** | 2026-10 / v1.0 |
| **Contexto de uso** | Diseño curricular · STEM · pensamiento computacional · germen de TFM |

**Palabras clave:** órdenes de magnitud, notación científica, modelización, biosfera, mutación, supercomputación, FLOPS, problema abierto, sensibilidad de parámetros

---

## 1. Pregunta guía / reto

> **¿Es posible simular mutación a mutación toda la historia evolutiva de la Tierra con la tecnología informática actual? ¿Qué habría que suponer para que fuera posible?**

**Hipótesis a poner a prueba (no a memorizar como hecho):**

> El número acumulado de mutaciones heredables en la historia de la biosfera es del orden de $10^{36}$–$10^{40}$. Incluso un supercomputador de clase *exaescala* ($\sim 10^{18}$ operaciones/s) solo alcanza del orden de $10^{25}$ operaciones **por año**, de modo que no podría «procesar» individualmente cada mutación en un tiempo humano razonable si se dedicara *una* operación elemental a cada una.

**Idea clave:** no se busca un número exacto, sino **modelizar, acotar, comparar y justificar** si la hipótesis se sostiene bajo distintos supuestos biológicos y computacionales.

**Producto final esperado**

- Informe científico breve (hipótesis → modelo → cálculos → conclusión → límites).
- Hoja de cálculo o script Python con parámetros editables ($N_{\mathrm{cel}}$, $\bar g$, $u$).
- Póster o presentación con la comparación de órdenes de magnitud.
- Reflexión: ¿qué significa que la biosfera sea un «procesador» masivamente paralelo?

---

## 2. Justificación y sentido educativo

- Entrena **órdenes de magnitud** con un contexto STEM real (biología + computación), no con ejercicios artificiales de potencias.
- Obliga a distinguir **dato medido**, **estimación publicada** y **suposición del modelo**.
- Conecta sentido numérico, modelización y pensamiento computacional (coste, paralelismo, «no hace falta simular cada átomo»).
- Problema **abierto**: cambiar $u$ o $\bar g$ un orden de magnitud mueve la conclusión… o no; hay que verlo.

---

## 3. Objetivos de aprendizaje

1. Expresar y multiplicar potencias de 10 en notación científica.
2. Estimar $N_{\mathrm{mut}}$ con un modelo producto y acotar un intervalo.
3. Estimar operaciones/año de un PC y de un supercomputador *exaescala*.
4. Comparar $N_{\mathrm{mut}}$ con $C_{\mathrm{año}}$ (cuántas «veces mayor»).
5. *(Bach.)* Usar logaritmos y análisis de sensibilidad; formular el modelo integral.
6. Argumentar por qué la biología computacional **no** simula mutación a mutación toda la historia.

---

## 4. Competencias específicas y criterios

| CE | Criterios (síntesis) | Evidencia |
|----|----------------------|----------|
| **CE1–CE2** | Modelizar y validar | Cálculo de $N_{\mathrm{mut}}$ y de $C_{\mathrm{año}}$ |
| **CE3** | Conjeturar | Hipótesis inicial vs resultado tras sensibilidad |
| **CE4** | Pensamiento computacional | Coste; paralelismo; alternativa estocástica |
| **CE5–CE6** | Conexiones | Biología ↔ matemáticas ↔ informática |
| **CE7–CE8** | Comunicar | Informe + póster con órdenes de magnitud |
| **CE9–CE10** | Socioafectivo | Tolerar incertidumbre; no fingir precisión falsa |

---

## 5. Saberes y sentidos

| Sentido | Saberes | Prioridad |
|---------|---------|----------|
| Numérico | Notación científica; potencias de 10; órdenes de magnitud | Alta |
| Algebraico | Modelo producto; sensibilidad a parámetros | Alta |
| De la medida | Tiempo (s, año); tasas (mutaciones/generación) | Media |
| Estocástico *(Bach.)* | Modelos agregados vs enumeración completa | Media |
| Socioafectivo | Humildad epistémica ante sistemas complejos | Alta |

---

## 6. Modelo matemático (versión de aula)

### 6.1. Estimación de mutaciones acumuladas

Modelo **producto** (simplificación didáctica):

$$
N_{\mathrm{mut}} \approx N_{\mathrm{cel}} \times \bar{g} \times u
$$

| Símbolo | Significado | Valor orientativo | Naturaleza |
|---------|-------------|-------------------|------------|
| $N_{\mathrm{cel}}$ | Células vivas «típicas» en la biosfera (orden actual) | $\sim 10^{30}$ | Estimación publicada (procariontes) |
| $\bar{g}$ | Generaciones / divisiones «efectivas» acumuladas por línea celular a lo largo de la historia (parámetro grueso) | $10^{9}$–$10^{11}$ | **Suposición de modelo** (muy incierta) |
| $u$ | Mutaciones heredables por genoma y división | $\sim 10^{-3}$ (bacterias tipo *E. coli*) | Estimación experimental de orden |

**Cálculo de referencia:**

$$
N_{\mathrm{mut}} \sim 10^{30} \times 10^{10} \times 10^{-3} = 10^{37}.
$$

Variando $u\in[10^{-3},10^{-2}]$ y $\bar{g}\in[10^{9},10^{11}]$ se obtiene un intervalo del tipo

$$
N_{\mathrm{mut}} \sim 10^{36}\text{ a }10^{40}
$$

(orden de magnitud; no un valor preciso).

**Advertencia al alumnado:** $\bar{g}$ no es un dato de libro de texto. El modelo **mezcla** un stock actual de células ($N_{\mathrm{cel}}$) con una historia de divisiones. Una formulación más limpia (Bachillerato) es integrar en el tiempo:

$$
N_{\mathrm{mut}} = \int_{t_0}^{t_{\mathrm{hoy}}} N_{\mathrm{cel}}(t)\,\gamma(t)\,u(t)\,\mathrm{d}t,
$$

donde $\gamma(t)$ es el ritmo de divisiones por célula y unidad de tiempo. Estudios recientes estiman el número *acumulado de células que han existido* del orden de $10^{39}$–$10^{40}$; si cada una aporta $\sim u$ mutaciones al dividirse, se recupera un orden compatible con $10^{36}$–$10^{40}$ de eventos mutacionales (según $u$).

### 6.2. Capacidad de cómputo

Sea $\nu$ el ritmo de operaciones elementales por segundo (FLOPS u operaciones/s, según el discurso de aula).

$$
C_{\mathrm{año}} \approx \nu \times 3{,}15\times 10^{7}.
$$

| Sistema | $\nu$ (orden) | $C_{\mathrm{año}}$ (orden) |
|---------|----------------|-----------------------------|
| PC convencional | $10^{11}$ | $\sim 3\times 10^{18}$ |
| Supercomputador *exaescala* | $10^{18}$ | $\sim 3\times 10^{25}$ |

(*Exaescala* = al menos $10^{18}$ operaciones en coma flotante por segundo en el sentido de los benchmarks TOP500; máquinas reales como Frontier / El Capitan están en ese orden.)

### 6.3. Comparación

| Magnitud | Orden |
|----------|-------|
| $N_{\mathrm{mut}}$ | $10^{36}$–$10^{40}$ |
| $C_{\mathrm{año}}$ (PC) | $10^{18}$–$10^{19}$ |
| $C_{\mathrm{año}}$ (exaescala) | $10^{25}$–$10^{26}$ |

**Razón (ejemplo con $N_{\mathrm{mut}}=10^{37}$ y exaescala $3\times 10^{25}$):**

$$
\frac{N_{\mathrm{mut}}}{C_{\mathrm{año}}} \sim \frac{10^{37}}{3\times 10^{25}} \approx 3\times 10^{11}
$$

→ del orden de **cientos de miles de millones de años** de un solo supercomputador *exaescala* si se dedicara **una** operación a cada mutación (y eso **sin** contar memoria, E/S ni el coste de *simular* el efecto de la mutación).

**Conclusión provisional del modelo:** la hipótesis se sostiene bajo supuestos razonables: la brecha de órdenes de magnitud no se cierra con hardware actual si el objetivo es *enumerar* cada mutación histórica.

---

## 7. Retos por nivel

### 7.1. ESO (3.º–4.º)

1. Escribir $N_{\mathrm{cel}}$, $\bar g$, $u$ y $C_{\mathrm{año}}$ en notación científica.
2. Calcular $N_{\mathrm{mut}}$ con el producto de referencia.
3. Completar la tabla de comparación PC vs supercomputador vs $N_{\mathrm{mut}}$.
4. Responder: **¿cuántas veces mayor** es $N_{\mathrm{mut}}$ que $C_{\mathrm{año}}$ de un PC?
5. Póster: pregunta motriz + tres números + una frase de límite del modelo.

### 7.2. Bachillerato

1. Comparar con logaritmos: $\log_{10} N_{\mathrm{mut}} - \log_{10} C_{\mathrm{año}}$.
2. Sensibilidad: tabla con $u\in\{10^{-4},10^{-3},10^{-2}\}$ y $\bar g\in\{10^{9},10^{10},10^{11}\}$.
3. Escribir el modelo integral y discutir qué habría que saber de $N_{\mathrm{cel}}(t)$.
4. Pensamiento computacional: paralelismo (¿y si usamos $10^{6}$ supercomputadores?); complejidad; por qué Monte Carlo / coalescencia no enumeran todo.
5. Extensión física: energía por operación (orden de Landauer o de un centro de datos real) — ¿es factible energéticamente?

---

## 8. Secuencia orientativa

| Sesión | Fase | Actividad |
|--------|------|-----------|
| 1 | Activación | «¿Cuántas células hay en la Tierra?» Apuestas; revelar $10^{30}$ |
| 2 | Modelo | Construir $N_{\mathrm{mut}}\approx N_{\mathrm{cel}}\bar g u$; primer cálculo |
| 3 | Cómputo | De FLOPS a operaciones/año; tabla comparativa |
| 4 | Sensibilidad | Cambiar parámetros; ¿se salva la conclusión? |
| 5 | Producto | Informe + póster; debate «¿qué no hace falta simular?» |
| 6 (opc.) | Python / hoja de cálculo | Script con deslizadores de parámetros |

---

## 9. Evaluación

| Criterio | Indicadores |
|----------|-------------|
| Magnitudes | Notación científica correcta; potencias bien multiplicadas |
| Fuentes del modelo | Distingue dato / estimación / suposición (sobre todo $\bar g$) |
| Comparación | Razón $N_{\mathrm{mut}}/C_{\mathrm{año}}$ interpretada en lenguaje claro |
| Límites | Explica al menos un límite del modelo o de la hipótesis «1 op. = 1 mutación» |
| Comunicación | Informe o póster legible; sin fingir exactitud de 40 cifras |

---

## 10. DUA y socioafectivo

| Principio | Medida |
|-----------|--------|
| Implicación | Pregunta «imposible» con gancho de superordenadores |
| Representación | Tabla de órdenes; recta numérica logarítmica; analogías («granos de arena») |
| Acción y expresión | Póster, informe o notebook |

- Norma de aula: **estar inseguro del valor exacto es correcto**; estar seguro sin justificar parámetros no lo es.
- Evitar lecturas anticientíficas («la evolución no se puede estudiar»): se estudia con **modelos agregados**, no con enumeración exhaustiva.

---

## 11. Extensiones abiertas

- ¿Virus y transferencia horizontal de genes aumentan o replantean $N_{\mathrm{mut}}$?
- Solo eucariotas multicelulares: ¿cuántos órdenes baja el número?
- Energía para $10^{40}$ operaciones (límite físico vs ingeniería actual).
- ¿La computación cuántica cambia la *conclusión de enumeración*, o solo constantes?
- ¿Qué usa realmente la biología evolutiva computacional (filogenias, coalescencia, simulaciones de poblaciones)?

---

## 12. Orientaciones al docente

- Presentar $10^{30}$, $10^{-3}$ y $10^{18}$ como **órdenes respaldados**, no como constantes mágicas.
- Insistir: «1 operación por mutación» es una **cota inferior optimista** del coste de *contar*; simular efecto fenotípico sería mucho más caro.
- No transformar la SA en negacionismo evolutivo: el mensaje es de **escala y modelización**.
- Variante corta (3 sesiones): producto $N_{\mathrm{mut}}$ + $C_{\mathrm{año}}$ + póster.

---

## 13. Referencias (validadas / orientativas)

### Biología (órdenes de magnitud)
1. Whitman, W. B., Coleman, D. C., & Wiebe, W. J. (1998). Prokaryotes: The unseen majority. *PNAS*, 95(12), 6578–6583. — Estimación clásica $\sim 4$–$6\times 10^{30}$ células procariotas.  
2. Locey, K. J., & Lennon, J. T. (2016). Scaling laws predict global microbial diversity. *PNAS*. — Cita el orden $\sim 10^{30}$ células en la Tierra.  
3. Crockford, P. W., et al. (2023/2024, cobertura científica): estimaciones del orden de $10^{30}$ células *actuales* y $\sim 10^{39}$–$10^{40}$ células *acumuladas* en la historia de la Tierra (productividad primaria integrada). Útil para motivar el modelo integral.  
4. Lee, H., Popodi, E., Tang, H., & Foster, P. L. (2012). Rate and molecular spectrum of spontaneous mutations in *Escherichia coli*. *PNAS*, 109(41), E2774–E2783. — $\sim 1\times 10^{-3}$ mutaciones por genoma y generación en tipo salvaje.

### Computación
5. Definición de *exascale*: $\ge 10^{18}$ FLOPS (doble precisión) en el sentido TOP500 / comunidad HPC.  
6. TOP500 / sistemas Frontier, Aurora, El Capitan: rendimiento en el orden de $1$–$2$ exaFLOPS (valores de benchmark públicos; actualizar si se usa en clase con la lista vigente).

### Didáctica del repo
7. SA hermanas: [ecuación de Drake / independencia](sa-independencia-drake-4eso.md) (órdenes de magnitud y sensibilidad), [folio y Luna](sa-papel-luna-exponencial-2eso.md) (potencias de 10), [campana de Gauss](sa-campana-gaussiana-bach.md).
8. Laboratorio Python: [05-python-jupyter](../../05-python-jupyter/) (script de sensibilidad con parámetros).

### Normativa
- RD 217/2022 · RD 243/2022 (sentido numérico, modelización, pensamiento computacional).

---

## 14. Anexo — Mini-script Python (sensibilidad)

```python
# Órdenes de magnitud: mutaciones vs cómputo anual
N_cel = 1e30
g_bar = 1e10
u = 1e-3
ops_per_s_exascale = 1e18
seconds_per_year = 3.15e7

N_mut = N_cel * g_bar * u
C_year = ops_per_s_exascale * seconds_per_year

print(f\"N_mut ≈ {N_mut:.3e}\")
print(f\"C_año (exa) ≈ {C_year:.3e}\")
print(f\"N_mut / C_año ≈ {N_mut / C_year:.3e}\")
```

Invitar a cambiar `g_bar` y `u` y a registrar cuándo (si alguna vez) la razón baja de $10^{6}$.
