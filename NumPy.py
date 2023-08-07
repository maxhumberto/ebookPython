import numpy as np

# Criando um array NumPy com números aleatórios
data = np.random.rand(100)

# Calculando a média, mediana e desvio padrão
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

print("Média:", mean)
print("Mediana:", median)
print("Desvio Padrão:", std_dev)
