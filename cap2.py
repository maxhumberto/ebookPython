def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        print("Operação inválida.")
        return

    print("Resultado:", resultado)

# Teste da calculadora
calculadora()


################################################################


def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def conversor_temperatura():
    valor = float(input("Digite a temperatura: "))
    unidade_origem = input("Digite a unidade de origem (C ou F): ").upper()

    if unidade_origem == "C":
        resultado = celsius_para_fahrenheit(valor)
        unidade_destino = "Fahrenheit"
    elif unidade_origem == "F":
        resultado = fahrenheit_para_celsius(valor)
        unidade_destino = "Celsius"
    else:
        print("Unidade inválida.")
        return

    print(f"O valor convertido é {resultado:.2f} {unidade_destino}.")

# Teste do conversor de temperatura
conversor_temperatura()


################################################################




