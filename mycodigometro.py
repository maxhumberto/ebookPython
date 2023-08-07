import pandas as pd

data = {'Data': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01'],
        'Vendas': [100, 120, 150, 180]}
df = pd.DataFrame(data)


import matplotlib.pyplot as plt

# Convertendo a coluna 'Data' para o tipo datetime
df['Data'] = pd.to_datetime(df['Data'])

# Criando um gráfico de linhas usando Matplotlib
plt.plot(df['Data'], df['Vendas'])
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.title('Tendência de Crescimento das Vendas')
plt.xticks(rotation=45)
plt.show()
