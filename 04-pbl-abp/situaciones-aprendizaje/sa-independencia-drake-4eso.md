---
layout: default
title: "Lotería, independencia y la ecuación de Drake"
parent: Situaciones de aprendizaje
nav_order: 24
---

# SA — Si ya me tocó… ¿me toca otra vez? (independencia, lotería y Drake)

## 0. Metadatos

| Campo | Contenido |
|-------|----------|
| **Nivel** | 4.º ESO / 1.º Bach |
| **Duración** | 7 sesiones |
| **Versión** | 2026-10 / v1.0 |

**Palabras clave:** independencia, probabilidad condicional, falacia del jugador, Drake, $f_l$

## 1. Pregunta guía

> *Si te toca la lotería esta semana, ¿$P(\text{ganar la que viene})=1$? ¿Y si la Tierra «ya ganó» el sorteo de la vida, podemos poner $f_l=1$ en Drake?*

## Núcleo matemático

$$
P(W_1\cap W_2)=p^2,\qquad P(W_2\mid W_1)=P(W_2)=p \neq 1.
$$

## Drake

$$
N=R_*\,f_p\,n_e\,f_l\,f_i\,f_c\,L
$$

Poner $f_l=1$ porque «hubo vida en la Tierra» confunde hecho observado con fracción desconocida.

## Sensibilidad (ejemplo)

Con factores fijos ilustrativos, $N(f_l)=40\cdot f_l$:

| $f_l$ | $N$ |
|---------|-----|
| $1$ | 40 |
| $10^{-3}$ | 0,04 |
| $10^{-6}$ | $\sim10^{-5}$ |

## Secuencia (7 sesiones)

1. Encuesta 0 / $p$ / 1  
2. Formalización lotería  
3. Falacias  
4. Drake  
5. Tabla $N(f_l)$  
6. Argumento $f_l=1$  
7. Informe y debate

**No** demuestra que no hay ETI: muestra el impacto de tratar $f_l=1$ como dato.

Relacionada: [Paradoja del cumpleaños](sa-paradoja-cumpleanos-3eso.md).
