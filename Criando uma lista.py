# Criando uma lista
frutas = ["maçã", "banana", "laranja", "uva"]

# Acessando elementos
primeira_fruta = frutas[0]  # Resultado: "maçã"
ultima_fruta = frutas[-1]  # Resultado: "uva"
    
# Adicionando elementos
frutas.append("morango")
frutas.insert(2, "abacaxi")

# Removendo elementos
frutas.remove("banana")
frutas.pop(1)

# Verificando se um elemento está na lista
if "uva" in frutas:
    print("Sim, uva está na lista.")
else:
    print("Não, uva não está na lista.")
