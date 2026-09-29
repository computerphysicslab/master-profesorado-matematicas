# Ingrid Daubechies: wavelets y la matemática que comprime el mundo

| Campo | Contenido |
|-------|-----------|
| **Nivel** | Bachillerato (relato + idea); ESO divulgativo |
| **Conceptos** | Ondículas (wavelets); análisis multiescala; compresión de imagen; bases |
| **Sentidos** | Algebraico; conexiones con tecnología |
| **Tiempo** | 45–60 min |

---

## 1. Pregunta generatriz

> ¿Cómo cabe una fotografía de alta resolución en un archivo pequeño sin que «se note» demasiado? ¿Qué matemáticas hay detrás del JPEG 2000 o del análisis de señales?

---

## 2. Historia

**Ingrid Daubechies** (Houthalen, Bélgica, 1954). Física y matemática; doctora en física teórica; carrera en Estados Unidos (AT&T Bell Labs, Princeton, Duke). Primera mujer presidenta de la **Unión Matemática Internacional** (2011–2014).

En la década de 1980 construye familias de **ondículas (wavelets) ortogonales con soporte compacto** — las *Daubechies wavelets* — que permiten descomponer señales e imágenes en distintas escalas con propiedades matemáticas limpias (ortogonalidad, localización en tiempo/frecuencia).

Impacto práctico enorme: compresión, denoising, análisis de datos, visionado médico, entre otros. Su trabajo conecta **análisis armónico**, álgebra lineal y aplicaciones industriales.

---

## 3. Idea matemática (escolar)

Sin formalismo de $L^2$ ni filtros de Quadrature Mirror:

- Una imagen es una tabla de números (píxeles).
- Se puede reescribir como **promedios + detalles** a varias resoluciones (idea multiescala).
- Si muchos «detalles» son casi cero, se pueden **comprimir** (guardar menos números).
- Las wavelets son un tipo de «piezas de lego» matemáticas mejores que un solo tipo de onda (Fourier) cuando la señal cambia de forma local (bordes en una foto).

Puente con Bachillerato: bases, combinaciones lineales, matrices; con ESO: promedios, patrones, pixelado.

---

## 4. Problema / actividad

**Base**

> Toma una fila de 8 números (simula píxeles). Calcula promedios de parejas y diferencias. ¿Cuánta información «nueva» aportan las diferencias si la fila es casi constante?

**Tecnología**

> ¿Qué se pierde cuando comprimes una imagen al máximo? Relaciona con la idea de descartar coeficientes pequeños.

**Historia**

> ¿Por qué importa que una matemática lidere la IMU? Compara con [Noether](emmy-noether.md), [Mirzakhani](mirzakhani.md), [Johnson](katherine-johnson.md).

---

## 5. Precauciones

- No convertir la sesión en tutorial de Photoshop: el centro es la **idea de base multiescala**.  
- No afirmar que «inventó el JPEG» (JPEG clásico usa DCT; JPEG 2000 sí se relaciona con wavelets).  
- Enlace a [Mandelbrot](mandelbrot.md) (geometría y escala), [Fourier/Laplace](laplace-demonio.md) solo como contraste divulgativo, [Ada Lovelace](ada-lovelace.md).

## 6. Relacionado

[Catálogo](../indices/catalogo.md) · [Mandelbrot](mandelbrot.md) · [Turing](turing.md) · [Mirzakhani](mirzakhani.md)
