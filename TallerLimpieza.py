import pandas as pd
import numpy as np

ConectadosWifiTunja = pd.read_csv('WifiTunjaDataset.csv')

df = pd.DataFrame({"nombre": ['Alfred', 'Batman', 'Catwoman'],
                   "apellido": [np.nan, 'Batmobile', 'Bullwhip'],
                   "equipo": [pd.NaT, "G2 Esports",
                            pd.NaT]})

# Regresa un objeto del mismo tamaño, indicando si los valores son NA, osea todo lo que sea distinto de None o NaN
print(ConectadosWifiTunja.isnull().head(10))
print("------")

# Borra todos los indices en los que haya al menos un NA
print(ConectadosWifiTunja.dropna(axis=0, how='any').head(10))
print("------")

# Borra todos los indices en los que toda la informacion sea NA  
print(ConectadosWifiTunja.dropna(axis=0, how='all').head(10))
print("------")

# Borra todos las columnas en los que haya al menos un NA
print(df.dropna(axis=1, how='any'))
print("------")

# Borra todos las columnas en los que haya al menos un NA
print(ConectadosWifiTunja.fillna(value=3).head(10))
print("------")

