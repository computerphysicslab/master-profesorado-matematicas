# Scripts de limpieza

Eliminan del repositorio:

- Referencias a **UNIZAR** / **Universidad de Zaragoza**
- Códigos numéricos de asignaturas (`63200`, `63305`, …)
- Prefijos numéricos en nombres de carpetas
- Referencias al curso **2026–2027**
- **Grupos**, **turnos** y **créditos ECTS**

## Uso rápido

```bash
bash scripts/clean_all.sh --dry-run   # simular
bash scripts/clean_all.sh             # aplicar
```

## Scripts

| Script | Función |
|--------|---------|
| `rename_asignaturas.sh` | Renombra carpetas con prefijo numérico |
| `clean_references.py` | Purga textos (UNIZAR, códigos, año, ECTS, grupos, turnos) |
| `rewrite_templates.py` | Reescribe README canónicos limpios |
| `clean_all.sh` | Orquesta los tres pasos |
