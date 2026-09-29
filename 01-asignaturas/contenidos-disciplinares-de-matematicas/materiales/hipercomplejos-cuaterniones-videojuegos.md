# Hipercomplejos y entornos 3D de videojuegos

**Asignatura:** Contenidos disciplinares de Matemáticas  
**Nivel de uso:** ampliación Bachillerato / formación del profesorado / puentes STEM  
**Enfoque:** de los números complejos (currículo) a los cuaterniones (práctica en motores 3D)

---

## 1. Qué son los números hipercomplejos

Los **hipercomplejos** generalizan los números complejos a más dimensiones. En gráficos 3D y videojuegos el sistema relevante es el de los **cuaterniones**.

| Sistema | Dimensiones | Uso principal en videojuegos |
|---------|-------------|------------------------------|
| Complejos | 2 | Rotaciones en el plano |
| **Cuaterniones** | 4 | **Rotaciones 3D** (estándar de facto) |
| Octoniones | 8 | Casi nunca en tiempo real |
| Duales / cuaterniones duales | Varios | Cinemática rígida, IK avanzado (poco frecuente en AAA) |

Un cuaternión (Hamilton, 1843) se escribe:

$$q = w + xi + yj + zk$$

con las reglas

$$i^2 = j^2 = k^2 = ijk = -1.$$

Para rotaciones se usan **cuaterniones unitarios** ($\|q\| = 1$), que parametrizan el grupo de rotaciones del espacio de forma eficiente.

---

## 2. Por qué se usan en videojuegos 3D

### 2.1. Evitan el *gimbal lock*

Las rotaciones con **ángulos de Euler** (yaw, pitch, roll) pueden «bloquearse» cuando dos ejes se alinean: se pierde un grado de libertad y la orientación se vuelve singular. Los cuaterniones representan rotaciones de forma **continua y sin singularidades**.

### 2.2. Interpolación suave (Slerp)

Para animaciones, cámaras o transiciones de orientación se usa *Spherical Linear Interpolation*:

$$\operatorname{Slerp}(q_1, q_2, t) = \frac{\sin((1-t)\theta)}{\sin\theta}\, q_1 + \frac{\sin(t\theta)}{\sin\theta}\, q_2$$

donde $\theta$ es el ángulo entre $q_1$ y $q_2$ en la 3-esfera. Produce trayectorias de rotación naturales en:

- cámaras cinematográficas;
- animación de personajes;
- orientación de proyectiles o vehículos;
- VR / AR.

### 2.3. Eficiencia y representación compacta

| Aspecto | Ventaja típica del cuaternión |
|---------|-------------------------------|
| Memoria | 4 floats (frente a 9 de una matriz 3×3) |
| Composición | Multiplicar dos cuaterniones es más barato que componer matrices 3×3/4×4 |
| Normalización | Muy sencilla (necesario tras muchas operaciones numéricas) |
| GPU | Se convierte a matriz de rotación cuando hace falta enviar al *pipeline* |

### 2.4. Comparación rápida

| Aspecto | Ángulos de Euler | Matrices 3×3 / 4×4 | Cuaterniones |
|---------|------------------|--------------------|--------------|
| *Gimbal lock* | Sí | No | No |
| Interpolación suave | Difícil | Posible, costosa | Excelente (Slerp) |
| Tamaño | 3 floats | 9–16 floats | 4 floats |
| Normalización | No aplica | Costosa | Muy fácil |
| Uso real en motores | UI / input | Interno (GPU) | **Estándar de facto** |

---

## 3. Dónde aparecen en un motor

| Sistema del juego | Uso típico de cuaterniones |
|-------------------|----------------------------|
| Transformaciones de objetos | Orientación (`Transform.rotation` en Unity; `FQuat` en Unreal) |
| Cámaras | *Look-at*, órbita, cámaras cinemáticas |
| Animación esquelética | Rotación de huesos (*joint orientations*) |
| Física | Orientación de cuerpos rígidos |
| Redes / multiplayer | Interpolación de orientaciones entre clientes |
| VR / *head tracking* | Casco y controladores |
| Animación procedural | IK, *look-at* targets |

### Ejemplo orientativo (Unity / C#)

```csharp
// Rotar 90° alrededor del eje Y
transform.rotation = Quaternion.Euler(0, 90, 0);

// Interpolación suave entre dos orientaciones
transform.rotation = Quaternion.Slerp(startRot, endRot, t);

// Mirar hacia un punto
transform.rotation = Quaternion.LookRotation(target.position - transform.position);
```

En Unreal Engine la API equivalente gira en torno a `FQuat`.

---

## 4. Otras estructuras hipercomplejas

- **Números duales y cuaterniones duales:** unifican rotación + traslación (movimientos rígidos). Aparecen en robótica y en sistemas de IK avanzados; raros en juegos AAA convencionales.
- **Octoniones:** no asociativos; casi no se usan en tiempo real.

---

## 5. Situación curricular (ESO / Bachillerato)

| Etapa | ¿Se estudian? | Notas |
|-------|---------------|-------|
| **ESO** | Complejos: **no** (solo se indica que discriminante negativo ⇒ sin solución real) | Hipercomplejos: no |
| **1.º Bachillerato (Mat. I, Ciencias/Tecnología)** | Complejos: **sí** (binómica, polar, Moivre, plano) | Contenido LOMLOE / Aragón |
| **2.º Bachillerato** | Complejos: no obligatorios de forma central | Hipercomplejos: no |
| **Universidad** | Cuaterniones en álgebra, geometría, gráficos, robótica, física | — |

**Aragón (Matemáticas I):** el temario autonómico incluye explícitamente números complejos en forma binómica y polar (criterio/saber de números y álgebra). Ver [temario Mat. I](../../diseno-curricular-e-instruccional-de-matematicas/materiales/temarios-matematicas-aragon/06_matematicas_i_1_bachillerato.md).

Los **cuaterniones no caben como contenido obligatorio** de secundaria, pero sí como:

- taller o proyecto de ampliación;
- trabajo interdisciplinar (Matemáticas + Tecnología / Informática);
- motivación tras el bloque de complejos («del plano al espacio»).

---

## 6. Interés didáctico para el máster

| Tema | Nivel recomendado | Formato | Interés del alumnado |
|------|-------------------|---------|----------------------|
| Aplicaciones de números complejos | 1.º Bachillerato | Unidad / taller | Alto |
| Introducción a cuaterniones (videojuegos / 3D) | 1.º–2.º Bachillerato | Taller / proyecto / ampliación | Muy alto si se enfoca en juegos/VR |
| Hipercomplejos avanzados | Universidad | — | — |

**Puente conceptual útil en clase:**

```text
Complejos  →  rotaciones en el plano (multiplicar por e^{iθ})
Cuaterniones  →  rotaciones en el espacio (sin gimbal lock, con Slerp)
```

No hace falta desarrollar todo el álgebra no conmutativa: basta con la idea de *objeto de 4 números que representa orientación*, la comparación con Euler/matrices y una demo en un motor o applet.

---

## 7. Ideas de actividad (ampliación)

1. **Del complejo al cuaternión:** multiplicar por $i$ rota 90° en el plano; preguntar «¿qué objeto matemático rota en 3D?».
2. **Gimbal lock visual:** animación con Euler vs. cuaternión (vídeo o Unity/Godot).
3. **Slerp a ojo:** interpolar dos orientaciones de una cámara o de un brazo articulado.
4. **Mini-proyecto:** script que oriente un objeto hacia un *target* (`LookRotation` / equivalente).
5. **Historia breve:** Hamilton y el puente de Brougham (1843) — enlace posible con [historias matemáticas](../../../03-materiales/historias-matematicas/).

---

## 8. Conclusión

Los **cuaterniones** son la representación estándar de rotaciones en prácticamente todos los motores 3D modernos (Unity, Unreal, Godot, motores propios). Explican por qué cámaras, personajes y objetos rotan de forma suave y sin bloqueo de ejes. Para el profesorado de Matemáticas son un ejemplo potente de **ampliación motivadora** anclada en el bloque curricular de números complejos de 1.º de Bachillerato.

---

## 9. Para seguir

- Aplicaciones de complejos en Bachillerato: [aplicaciones-numeros-complejos-bachillerato.md](aplicaciones-numeros-complejos-bachillerato.md)
- Temario oficial Mat. I (Aragón): [06_matematicas_i_1_bachillerato.md](../../diseno-curricular-e-instruccional-de-matematicas/materiales/temarios-matematicas-aragon/06_matematicas_i_1_bachillerato.md)
- Material transversal: [`03-materiales/matematicas/`](../../../03-materiales/matematicas/)
