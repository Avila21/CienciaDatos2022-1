import pandas as pd
import numpy as np

# --------------> Limpiar datos <---------------------

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

# Llena todas las casillas con un NA con el valor dispuesto
print(ConectadosWifiTunja.fillna(value=3).head(10))
print("------")

# Llena todas las casillas con un NA con el valor medio de las casillas con valor
print(ConectadosWifiTunja.fillna(value=ConectadosWifiTunja.mean()).head(10))
print("------")

# Llena todas las casillas con un NA utilizando metodo especifico "bfill" toma el siguiente valor valido, limit nos indica el numero
# de NaN consecutivos 
print(ConectadosWifiTunja.fillna(method="bfill", limit=1).head(10))
print("------")

# --------------> Filtrado y Consulta de datos <---------------------

# Retorna bool en todos los id en los que se cumple la condicion
print(ConectadosWifiTunja['ANIO'] > 2021)
print("------")

# Retorna el objeto en todas las columnas donde se cumple la condicion
print(ConectadosWifiTunja[ConectadosWifiTunja['ANIO'] > 2021])
print("------")

# Retorna la columna con todos los id que cumplen la condicion
print(ConectadosWifiTunja['ANIO'][ConectadosWifiTunja['ANIO'] > 2021])
print("------")

# Retorna el objeto en todas las columnas donde se cumplen las condiciones dadas
print(ConectadosWifiTunja[(ConectadosWifiTunja['ANIO'] > 2021) & (ConectadosWifiTunja['SECTOR'] < 5)])
print("------")

# --------------> Where, Mask, Isin, Query, Eval <---------------------

# Reemplaza todos los valores en los que la condición es False
print(ConectadosWifiTunja.where(ConectadosWifiTunja['ANIO'] > 2021))
print("------")

# Reemplaza todos los valores en los que la condición es True
print(ConectadosWifiTunja.mask(ConectadosWifiTunja['ANIO'] > 2021))
print("------")

# La diferencia principal es que uno reemplaza los valores con la condicion en True y el otro con las condiciones en False
# No solo se puede hacer el relleno con NaN tambien se puede hacer con escalares u otros Dataframe

print(ConectadosWifiTunja.isin([5, 2021]))
print("------")

# La diferencia de pasarle como parametro una lista es que lo tomara directamente en todo el objeto y por valores
# Mientras que si le pasamos un diccionario podemos hacer el filtro por columnas especificas

print(ConectadosWifiTunja.eval('SUMALATLONG = LATITUD + LONGITUD '))
print("------")

# La diferencia principal entre eval y query es que eval, evalua un string con alguna expresion
# Mientras que query realiza el filtro mediante una expresion booleana especificamente