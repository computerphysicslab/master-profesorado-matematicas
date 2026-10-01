---
layout: default
title: "Lotería, independencia y la ecuación de Drake"
parent: Situaciones de aprendizaje
nav_order: 24
---

# SA — Si ya me tocó… ¿me toca otra vez? (independencia, lotería y Drake)

> **Bloque del programa (Diseño curricular):** Dificultades y obstáculos de aprendizaje.  
> Índice general: [situaciones-aprendizaje/README.md](../README.md)

## 0. Metadatos

| Campo | Contenido |
|-------|----------|
| **Nivel** | 4.º ESO / 1.º Bach |
| **Duración** | 7 sesiones |
| **Versión** | 2026-10 / v1.0 |

**Palabras clave:** independencia, probabilidad condicional, falacia del jugador, Drake, $f_l$, sesgo de selección

## 1. Pregunta guía

> *Si te toca la lotería esta semana, ¿$P(\text{ganar la que viene})=1$? ¿Y si la Tierra «ya ganó» el sorteo de la vida, podemos poner $f_l=1$ en Drake?*

**Producto:** (1) modelo lotería $P(W_1\cap W_2)=p^2$ vs $P(W_2\mid W_1)=p$; (2) $N(f_l)$ en varios escenarios; (3) conclusión sobre qué permite afirmar el dato «hay vida aquí».

## Núcleo matemático

$$
P(W_2\mid W_1)=P(W_2)=p \neq 1.
$$

## Drake y la falacia

$$
N=R_*\,f_p\,n_e\,f_l\,f_i\,f_c\,L
$$

Poner $f_l=1$ porque «hubo vida en la Tierra» confunde hecho observado (condicionado a que existamos) con fracción desconocida — análogo a $P=1$ tras ganar la lotería.

## Sensibilidad (ejemplo docente)

Con el resto de factores fijos de forma ilustrativa, $N(f_l)=40\cdot f_l$:

| $f_l$ | $N$ | Lectura |
|---------|-----|--------|
| $1$ | 40 | Decenas de civilizaciones |
| $10^{-3}$ | 0,04 | Casi ninguna *ahora* |
| $10^{-6}$ | $\sim10^{-5}$ | Vacío práctico |

## Secuencia (7 sesiones)

1. Encuesta 0 / $p$ / 1  
2. Formalización lotería  
3. Clasificar falacias  
4. Presentar Drake  
5. Tabla $N(f_l)$  
6. Argumento «vida aquí ⇒ $f_l=1$»  
7. Informe y debate

## Orientación

**No** es una prueba de que no hay ETI: es una prueba de que **fijar $f_l=1$ como dato** es una falacia con enorme impacto en $N$.

Relacionada: [Paradoja del cumpleaños](sa-paradoja-cumpleanos-3eso.md).
