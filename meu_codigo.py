import pandas as pd

# Lendo o arquivo CSV para um DataFrame
df = pd.read_csv('C:/Users/RAZER/Desktop/eboo/dados_vendas.cs   v')

print(df.head())

# Filtrando os registros com vendas acima de 150
df_filtrado = df[df['Vendas'] > 150]

print(df_filtrado)
