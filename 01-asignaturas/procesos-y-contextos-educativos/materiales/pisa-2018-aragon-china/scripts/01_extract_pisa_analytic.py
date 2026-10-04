"""
Extracción mínima de microdatos PISA 2018 (estudiantes).
Filtra España + comparadores de interés (QCI, SGP, MAC, HKG, TAP, JPN, KOR)
y guarda un parquet ligero con las variables analíticas.
"""
from pathlib import Path
import pyreadstat
import pandas as pd

DOWNLOADS = Path("/home/jips/Downloads")  # Ajustar a la ruta local

cands = sorted(DOWNLOADS.rglob("*.sav"))
print("=== .sav encontrados ===")
for p in cands:
    print(f"{p.stat().st_size/1e9:.2f} GB  {p}")

if not cands:
    raise SystemExit("No hay .sav en Downloads (ni subcarpetas).")

stu = max(cands, key=lambda p: p.stat().st_size)
print("\nUsando (más grande):", stu)

df_cnt, _ = pyreadstat.read_sav(str(stu), usecols=["CNT"])
print("\n=== CNT (conteos) ===")
vc = df_cnt["CNT"].value_counts().sort_index()
print(vc.to_string())

print("\n=== Candidatos China / Asia este ===")
for code in sorted(df_cnt["CNT"].dropna().unique(), key=str):
    s = str(code).upper()
    if s.startswith("Q") or s in {"QCN", "QCI", "CHN", "SGP", "MAC", "HKG", "TAP", "JPN", "KOR"}:
        print(f"  {code}: {int(vc.get(code, 0))}")

want = (
    ["CNT", "STRATUM", "ESCS", "W_FSTUWT"]
    + [f"W_FSTURWT{i}" for i in range(1, 81)]
    + [f"PV{i}MATH" for i in range(1, 11)]
)

print("\nLeyendo columnas analíticas…")
df, meta = pyreadstat.read_sav(str(stu), usecols=want)

interest = ["ESP", "QCN", "QCI", "SGP", "MAC", "HKG", "TAP", "JPN", "KOR"]
present = [c for c in interest if c in set(df["CNT"].dropna().unique())]
out = df[df["CNT"].isin(present)].copy()

out_path = DOWNLOADS / "pisa_analytic_min.parquet"
out.to_parquet(out_path, index=False)

print("Filas extraídas:", len(out))
print("CNT en salida:\n", out.groupby("CNT").size().to_string())
print("Guardado:", out_path)
print("Columnas:", list(out.columns)[:8], "… total", len(out.columns))
