# Declarando variáveis
idade = 25
nome = "Maria"
saldo = 300.50
is_estudante = True

# Expressões aritméticas
a = 5
b = 3

soma = a + b  # Resultado: 8
produto = a * b  # Resultado: 15
divisao = a / b  # Resultado: 1.6666666666666667
modulo = a % b  # Resultado: 2 (resto da divisão)
potencia = a ** b  # Resultado: 125
print(soma)


# Estrutura condicional
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


# Estrutura de repetição (while)
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

# Estrutura de repetição (for)
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)


# Função simples
def saudacao(nome):
    return "Olá, " + nome + "!"

mensagem = saudacao("Alice")  # Resultado: "Olá, Alice!"
print(mensagem)
