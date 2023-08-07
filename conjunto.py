# Criando um conjunto
numeros = {1, 2, 3, 4, 5}

# Adicionando elementos
numeros.add(6)
numeros.update({7, 8})

# Removendo elementos
numeros.remove(3)

# Verificando se um elemento está no conjunto
if 5 in numeros:
    print("Sim, 5 está no conjunto.")
else:
    print("Não, 5 não está no conjunto.")
