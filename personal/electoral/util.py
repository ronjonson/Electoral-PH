import pandas as pd

PROVINCES = "data\provinces-svg.txt"

def get_provinces():
    return pd.read_csv(PROVINCES, sep=':', header=None).values.tolist()