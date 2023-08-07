import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 7, 8],
        'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

# Removendo registros com valores ausentes
df_cleaned = df.dropna()

# Preenchendo valores faltantes com zeros
df_filled = df.fillna(0)

print("DataFrame sem valores ausentes:")
print(df_cleaned)

print("\nDataFrame com valores preenchidos com zeros:")
print(df_filled)
