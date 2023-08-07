def validar_senha():
    senha1 = input("Crie uma senha: ")
    senha2 = input("Digite a senha novamente para confirmar: ")

    if senha1 == senha2:
        print("Senha criada com sucesso!")
    else:
        print("As senhas não coincidem. Tente novamente.")

# Teste da validação de senha
validar_senha()