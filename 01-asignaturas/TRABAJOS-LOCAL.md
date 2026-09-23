# Trabajos personales — solo en local

Todas las carpetas `**/trabajos/` están en **`.gitignore`**.

## Por qué

Durante el máster, los trabajos, ensayos, memorias y entregas no deben subirse al repositorio público (riesgo de plagio, copias entre compañeros y filtrado de material evaluable).

## Qué hacer

1. Escribe y guarda tus entregas en la carpeta `trabajos/` de cada asignatura (ya existe en el árbol local).
2. **No** hagas `git add` de esas carpetas: Git las ignorará automáticamente.
3. Haz copia de seguridad por tu cuenta (disco, nube privada), no vía este repo público.
4. El material **plantilla y anonimizado** del Practicum compartido vive en `01-asignaturas/practicum/` (sí versionable). Lo personal del Practicum I/II va en `practicum-i/trabajos` y `practicum-ii/trabajos` (ignorado).

## Comprobar

```bash
git check-ignore -v 01-asignaturas/psicologia-del-desarrollo-y-de-la-educacion/trabajos/ensayo-ejemplo.md
# Debe indicar que coincide con .gitignore
```

Cuando termine el máster, si quieres publicar algún trabajo con licencia abierta, muévelo fuera de `trabajos/` o ajusta `.gitignore` de forma consciente.
