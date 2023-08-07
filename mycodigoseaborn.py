import pandas as pd
import matplotlib.pyplot as plt

data = {'Regiao': ['Norte', 'Sul', 'Sudeste', 'Centro-Oeste'],
        'Vendas': [200, 150, 300, 180]}
df = pd.DataFrame(data)
import seaborn as sns
# Criando um gráfico de barras usando Seaborn
sns.barplot(x='Regiao', y='Vendas', data=df)
plt.xlabel('Região')
plt.ylabel('Vendas')
plt.title('Distribuição das Vendas por Região')
plt.show()
