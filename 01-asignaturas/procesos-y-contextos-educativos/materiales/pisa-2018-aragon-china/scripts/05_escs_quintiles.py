"""
Medias de Matemáticas por quintiles de ESCS (cortes de España).
"""
from pathlib import Path
import pandas as pd
import numpy as np

DOWNLOADS = Path("/home/jips/Downloads")
df = pd.read_parquet(DOWNLOADS / "pisa2018_esp_qci_regions.parquet")

pv_cols = [f"PV{i}MATH" for i in range(1, 11)]
wt = "W_FSTUWT"

def weighted_mean(series, weights):
    mask = series.notna() & weights.notna() & (weights > 0)
    if mask.sum() == 0:
        return np.nan
    return np.average(series[mask], weights=weights[mask])

def math_mean(g):
    means = [weighted_mean(g[c], g[wt]) for c in pv_cols]
    return np.nanmean(means)

df = df[df["ESCS"].notna()].copy()

esp = df[df["CNT"] == "ESP"]
cuts = pd.qcut(esp["ESCS"], 5, retbins=True)[1]
df["ESCS_q"] = pd.cut(df["ESCS"], bins=cuts, labels=["Q1 (bajo)", "Q2", "Q3", "Q4", "Q5 (alto)"], include_lowest=True)

print("=== MATH por quintil de ESCS (cortes de España) ===\n")

for name, mask in [
    ("España", df["CNT"] == "ESP"),
    ("Aragón", (df["CNT"] == "ESP") & (df["region"] == "Aragón")),
    ("QCI", df["CNT"] == "QCI"),
]:
    g = df[mask]
    print(f"--- {name} ---")
    for q in ["Q1 (bajo)", "Q2", "Q3", "Q4", "Q5 (alto)"]:
        sub = g[g["ESCS_q"] == q]
        if len(sub) == 0:
            print(f"  {q:12s}:  n=0")
            continue
        m = math_mean(sub)
        n = len(sub)
        escs_m = weighted_mean(sub["ESCS"], sub[wt])
        print(f"  {q:12s}:  n={n:5d}  MATH={m:6.1f}  ESCS={escs_m:6.3f}")
    print()

print("=== Gaps en Q3 y Q5 ===")
for q in ["Q3", "Q5 (alto)"]:
    esp_m = math_mean(df[(df["CNT"] == "ESP") & (df["ESCS_q"] == q)])
    ara_m = math_mean(df[(df["CNT"] == "ESP") & (df["region"] == "Aragón") & (df["ESCS_q"] == q)])
    qci_m = math_mean(df[(df["CNT"] == "QCI") & (df["ESCS_q"] == q)])
    print(f"{q}:")
    print(f"  Aragón – España: {ara_m - esp_m:+.1f}")
    print(f"  QCI – España:    {qci_m - esp_m:+.1f}")
    print(f"  QCI – Aragón:    {qci_m - ara_m:+.1f}")
    print()
