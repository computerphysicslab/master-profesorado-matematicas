"""
Medias de Matemáticas y ESCS por tipo de centro (Aragón y España).
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

def group_stats(g):
    means = [weighted_mean(g[c], g[wt]) for c in pv_cols]
    math_mean = np.nanmean(means)
    escs_mean = weighted_mean(g["ESCS"], g[wt])
    n = int(len(g))
    return {
        "n": n,
        "MATH": round(math_mean, 1),
        "ESCS": round(escs_mean, 3) if pd.notna(escs_mean) else np.nan
    }

print("=== Aragón por tipo de centro ===")
ara = df[(df["CNT"] == "ESP") & (df["region"] == "Aragón")]
for tipo, g in ara.groupby("school_type"):
    s = group_stats(g)
    print(f"{tipo:20s}  n={s['n']:4d}  MATH={s['MATH']:.1f}  ESCS={s['ESCS']:.3f}")

print("\n=== España por tipo de centro ===")
esp = df[df["CNT"] == "ESP"]
for tipo, g in esp.groupby("school_type"):
    s = group_stats(g)
    print(f"{tipo:20s}  n={s['n']:5d}  MATH={s['MATH']:.1f}  ESCS={s['ESCS']:.3f}")
