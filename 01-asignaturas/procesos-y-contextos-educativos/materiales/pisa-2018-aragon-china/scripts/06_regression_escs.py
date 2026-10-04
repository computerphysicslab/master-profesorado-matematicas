"""
Regresión lineal ponderada: MATH ~ ESCS + Aragón + QCI (+ privado).
"""
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

DOWNLOADS = Path("/home/jips/Downloads")
df = pd.read_parquet(DOWNLOADS / "pisa2018_esp_qci_regions.parquet")

pv_cols = [f"PV{i}MATH" for i in range(1, 11)]
df["MATH_avg"] = df[pv_cols].mean(axis=1)

df = df[df["ESCS"].notna() & df["MATH_avg"].notna() & (df["W_FSTUWT"] > 0)].copy()

df["is_Aragon"] = ((df["CNT"] == "ESP") & (df["region"] == "Aragón")).astype(int)
df["is_QCI"] = (df["CNT"] == "QCI").astype(int)
df["is_private"] = (df["school_type"] == "privado/concertado").astype(int)

X1 = df[["ESCS", "is_Aragon", "is_QCI"]]
y = df["MATH_avg"]
w = df["W_FSTUWT"]

reg1 = LinearRegression().fit(X1, y, sample_weight=w)
print("=== Modelo 1: MATH ~ ESCS + Aragón + QCI ===")
print(f"Intercepto (España, ESCS=0): {reg1.intercept_:.1f}")
print(f"ESCS (pendiente):            {reg1.coef_[0]:.1f}")
print(f"Aragón (vs España):          {reg1.coef_[1]:+.1f}")
print(f"QCI (vs España):             {reg1.coef_[2]:+.1f}")
print()

X2 = df[["ESCS", "is_Aragon", "is_QCI", "is_private"]]
reg2 = LinearRegression().fit(X2, y, sample_weight=w)
print("=== Modelo 2: MATH ~ ESCS + Aragón + QCI + privado ===")
print(f"Intercepto:                  {reg2.intercept_:.1f}")
print(f"ESCS:                        {reg2.coef_[0]:.1f}")
print(f"Aragón:                      {reg2.coef_[1]:+.1f}")
print(f"QCI:                         {reg2.coef_[2]:+.1f}")
print(f"Privado/concertado:          {reg2.coef_[3]:+.1f}")
