"""
Mapeo de STRATUM → región (CCAA) y tipo de centro (público / privado-concertado).
Genera pisa2018_esp_qci_regions.parquet.
"""
from pathlib import Path
import pandas as pd
import numpy as np

DOWNLOADS = Path("/home/jips/Downloads")
df = pd.read_parquet(DOWNLOADS / "pisa_analytic_min.parquet")
# Si se partió de pisa2018_esp_qci.parquet, ajustar la ruta anterior.

print("Shape:", df.shape)
print("CNT:", df["CNT"].value_counts().to_string())

region_map = {
    "01": "Andalucía",
    "02": "Aragón",
    "03": "Asturias",
    "04": "Islas Baleares",
    "05": "Canarias",
    "06": "Cantabria",
    "07": "Castilla y León",
    "08": "Castilla-La Mancha",
    "09": "Cataluña",
    "10": "Comunidad Valenciana",
    "11": "Extremadura",
    "12": "Galicia",
    "13": "Madrid",
    "14": "Murcia",
    "15": "Navarra",
    "16": "País Vasco",
    "17": "La Rioja",
    "18": "Ceuta",
    "19": "Melilla",
}

def get_region(stratum):
    if pd.isna(stratum) or not str(stratum).startswith("ESP"):
        return "Otro"
    code = str(stratum)[3:5]
    if code == "90":
        s = str(stratum)
        if s in {"ESP9001", "ESP9002"}:
            return "Andalucía"
        if s.startswith("ESP90"):
            return "Madrid"  # mayoría de 90xx = Madrid (oversampling)
        return "España (90xx)"
    return region_map.get(code, f"Desconocido ({code})")

df["region"] = df["STRATUM"].apply(get_region)

def get_school_type(stratum):
    if pd.isna(stratum):
        return "desconocido"
    s = str(stratum)
    last = s[-1]
    if last in "13579":
        return "público"
    if last in "02468":
        return "privado/concertado"
    return "desconocido"

df["school_type"] = df["STRATUM"].apply(get_school_type)

print("\n=== n por región (España) ===")
esp = df[df["CNT"] == "ESP"]
print(esp["region"].value_counts().to_string())

print("\n=== n región × tipo centro (España) ===")
print(pd.crosstab(esp["region"], esp["school_type"]).to_string())

print("\n=== Aragón detalle ===")
aragon = esp[esp["region"] == "Aragón"]
print("n Aragón:", len(aragon))
print(aragon["school_type"].value_counts().to_string())
print("STRATUM Aragón:\n", aragon["STRATUM"].value_counts().to_string())

out = DOWNLOADS / "pisa2018_esp_qci_regions.parquet"
df.to_parquet(out, index=False)
print("\nGuardado:", out)
print("Columnas nuevas: region, school_type")
