import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        tentativa = int(input("Digite um número: "))
        tentativas += 1

        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s).")
            break
        elif tentativa < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

# Teste do jogo de adivinhação
jogo_adivinhacao()
