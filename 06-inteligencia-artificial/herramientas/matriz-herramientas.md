# Matriz comparativa de herramientas de IA para Matemáticas

**Ámbito:** orientación para elegir herramientas en Secundaria y Bachillerato.  
**Fecha de referencia:** octubre 2026. Las condiciones de acceso, precio y privacidad **cambian**; verificar siempre en el centro antes de usar con alumnado.

Complementa el listado orientativo en [herramientas-ia-educacion.md](herramientas-ia-educacion.md).

---

## 1. Matriz orientativa

| Herramienta | Para generar / hacer qué | Acceso típico | Coste orientativo | Privacidad (menores) | Capacidad matemática | Notas para el aula |
|-------------|--------------------------|---------------|-------------------|----------------------|----------------------|--------------------|
| **ChatGPT** (OpenAI) | Texto, pasos, código Python, variantes de problemas | Web / app | Freemium | Datos en servidores externos; versión educativa según acuerdo | Buena en explicación; falla en aritmética y demostraciones | Mejor con prompts restringidos; no pegar datos de alumnos |
| **Claude** (Anthropic) | Texto largo, análisis de resoluciones, tono cuidadoso | Web | Freemium | Servidores externos; revisar condiciones educativas | Fuerte en razonamiento y revisión de textos | Útil para «analiza esta resolución» |
| **Gemini** (Google) | Texto, integración con búsqueda / Workspace | Web / Workspace | Freemium | Depende de cuenta Google del centro | Variable según versión | Coordinar con política de Google Workspace del centro |
| **Copilot** (Microsoft) | Código en IDE, apoyo en documentos | IDE / Microsoft 365 | Freemium / licencia centro | Entorno Microsoft del centro si está configurado | Código y fórmulas; menos «teoría» pura | Interesante si el centro ya usa M365 |
| **Wolfram\|Alpha** | Cálculo simbólico, gráficas, paso a paso (pro) | Web / app | Freemium | Empresa Wolfram; no es un LLM clásico | **Excelente** en cálculo y verificación | Ideal para *contrastar* resultados de un chat |
| **GeoGebra** | Construcciones, álgebra, estadística, CAS | Web / app offline | Gratuito | Buena opción; datos locales posibles | Geometría y representaciones fiables | Complemento natural de la IA generativa |
| **Desmos** | Gráficas, actividades | Web | Gratuito (aula) | Revisar política educativa | Visualización y exploración | Muy usable en Secundaria |
| **Photomath / Symbolab** | Resolución paso a paso desde foto o enunciado | App | Freemium | Apps comerciales; precaución con menores | Procedimental; riesgo de uso pasivo | Mejor como verificación puntual, no como método de estudio |
| **Modelos locales / abiertos** (p. ej. vía Ollama u otras) | Chat y código sin salir del equipo | Local | Software libre + hardware | **Máximo control** de datos | Variable según modelo y hardware | Requiere instalación y mantenimiento del centro |

> **Wolfram\|Alpha y GeoGebra no son intercambiables con un chatbot:** sirven sobre todo para **verificar** y representar, no para redactar ensayos o pistas socráticas.

---

## 2. Criterios de selección según contexto

| Situación | Prioridad | Opciones más razonables |
|-----------|-----------|-------------------------|
| Aula **sin conexión** o con red muy limitada | Offline / instalado | GeoGebra app, materiales descargados, modelos locales si el centro los tiene |
| Aula con **30 alumnos** y pocos dispositivos | Licencias libres o cuenta de centro coordinada | GeoGebra, Desmos, una única herramienta de chat autorizada por el centro |
| **Evaluación** (evidencia de comprensión) | Control y sin «copiar del chat» | Papel, defensa oral, Wolfram/GeoGebra solo para comprobar un resultado ya razonado |
| Alumnado con **NEE / DUA** | Accesibilidad y reformulación | Chat para reformular enunciados (revisado por el docente) + representaciones en GeoGebra/Desmos |
| **Preparación docente** (en casa) | Productividad con revisión profesional | Cualquier chat + contraste con Wolfram/libro |
| Máxima **privacidad** | No enviar datos de menores fuera del centro | Modelos locales; prohibir pegar nombres, notas o listas |

---

## 3. Setup mínimo seguro en el aula (notas)

1. **No compartir contraseñas** de cuentas personales con el alumnado.
2. Preferir **cuenta institucional** o acceso gestionado por el centro cuando exista.
3. **Prohibir** pegar nombres, fotos de exámenes con datos personales o listados de clase en servicios externos no autorizados.
4. Si se guarda historial de prompts para auditar el proceso, que sea en un espacio del **centro** (o portfolio del alumno bajo norma clara), no en cuentas personales del docente de forma improvisada.
5. En evaluación, reservar evidencias **sin dispositivo** (ver [evaluar-con-ia.md](../evaluacion/evaluar-con-ia.md)).

---

## 4. Combinaciones potentes (recordatorio)

| Combinación | Para qué |
|-------------|----------|
| Chat + **Wolfram\|Alpha** | El chat propone; Wolfram verifica el cálculo |
| Chat + **GeoGebra / Desmos** | El chat sugiere; el software valida gráfica y coherencia |
| Chat + **papel** | Proceso visible; defensa oral |
| Chat + **Python/Jupyter** (`05-python-jupyter`) | Código generado + ejecución controlada |

---

## 5. Mantenimiento de esta ficha

- Revisar **una vez por curso** (o cuando el centro cambie de plataforma).
- No perseguir cada modelo nuevo: mantener un **conjunto pequeño** conocido por el equipo docente.
- Actualizar filas concretas solo con información verificable (acceso en el centro, coste real, política de menores).

---

*Orientativo. La decisión final de uso con alumnado corresponde al centro y al marco normativo aplicable.*
