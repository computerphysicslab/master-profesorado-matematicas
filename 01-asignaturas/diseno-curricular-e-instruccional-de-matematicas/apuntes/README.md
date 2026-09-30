# Integración Tema 3 — Elementos curriculares LOMLOE y evolución histórica

Paquete listo para incorporar al repositorio  
[master-profesorado-matematicas](https://github.com/computerphysicslab/master-profesorado-matematicas)

## Contenido del paquete

| Archivo | Destino en el repo | Descripción |
|---------|-------------------|-------------|
| `03-elementos-curriculo-lomloe.md` | `01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/apuntes/` | Apunte completo del Tema 3 (evolución LGE→LOMLOE, referentes, elementos LOMLOE) |
| `RESUMEN-VISUAL-Tema3.md` | `01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/apuntes/` (o `materiales/`) | Resumen visual con diagramas Mermaid |
| `apuntes-README.md` | `.../apuntes/README.md` | Índice de apuntes actualizado |
| `asignatura-README.md` | `.../diseno-curricular-e-instruccional-de-matematicas/README.md` | README de la asignatura actualizado |

## Cómo integrar

```bash
# Desde la raíz del repo clonado
cp 03-elementos-curriculo-lomloe.md \
   01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/apuntes/

cp RESUMEN-VISUAL-Tema3.md \
   01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/apuntes/

# Opcional: actualizar índices
cp apuntes-README.md \
   01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/apuntes/README.md
cp asignatura-README.md \
   01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/README.md

git add 01-asignaturas/diseno-curricular-e-instruccional-de-matematicas/
git commit -m "Integra Tema 3 DCI: evolución LGE–LOMLOE, referentes y elementos LOMLOE + resumen visual"
git push
```

## Qué incluye el apunte principal

1. **Evolución histórica** LGE (1970) → LOGSE → LOE → LOMCE → LOMLOE  
2. **Referentes:** Piaget, Brousseau, Freudenthal, Niss (KOM), NCTM, CEMAT  
3. **Arquitectura LOMLOE:** perfil de salida, competencias clave, competencias específicas (5 ejes), criterios, saberes/sentidos, situaciones de aprendizaje  
4. Preceptivo vs margen docente, ESO vs Bachillerato, orientaciones, glosario, test y tarea

Los diagramas Mermaid del resumen visual se renderizan automáticamente en GitHub.
