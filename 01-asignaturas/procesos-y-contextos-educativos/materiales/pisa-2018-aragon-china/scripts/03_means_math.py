"""
Medias ponderadas de Matemáticas y ESCS para España, Aragón y QCI.
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
    n = len(g)
    n_w = g[wt].sum()
    return pd.Series({
        "n": n,
        "n_weighted": round(n_w),
        "MATH": round(math_mean, 1),
        "ESCS": round(escs_mean, 3) if pd.notna(escs_mean) else np.nan
    })

print("=== Medias ponderadas Matemáticas + ESCS ===\n")

groups = {
    "España": df[df["CNT"] == "ESP"],
    "Aragón": df[(df["CNT"] == "ESP") & (df["region"] == "Aragón")],
    "QCI (B-S-J-Z)": df[df["CNT"] == "QCI"],
}

rows = []
for name, g in groups.items():
    s = group_stats(g)
    s.name = name
    rows.append(s)

res = pd.DataFrame(rows)
print(res.to_string())
print()

esp_math = res.loc["España", "MATH"]
ara_math = res.loc["Aragón", "MATH"]
qci_math = res.loc["QCI (B-S-J-Z)", "MATH"]

print(f"Aragón – España: {ara_math - esp_math:+.1f} puntos")
print(f"QCI – España:    {qci_math - esp_math:+.1f} puntos")
print(f"QCI – Aragón:    {qci_math - ara_math:+.1f} puntos")

res.to_csv(DOWNLOADS / "pisa2018_means_summary.csv")
print("\nResumen guardado en pisa2018_means_summary.csv")
