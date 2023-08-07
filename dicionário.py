# Criando um dicionário
contatos = {
    "João": "joao@email.com",
    "Maria": "maria@email.com",
    "Pedro": "pedro@email.com"
}

# Acessando elementos
email_maria = contatos["Maria"]  # Resultado: "maria@email.com"

# Adicionando e alterando elementos
contatos["Ana"] = "ana@email.com"
contatos["Pedro"] = "novo_pedro@email.com"

# Removendo elementos
del contatos["João"]

# Verificando se uma chave está no dicionário
if "Pedro" in contatos:
    print("Sim, Pedro está na lista de contatos.")
else:
    print("Não, Pedro não está na lista de contatos.")
