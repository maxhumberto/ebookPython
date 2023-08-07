def formatar_cpf(cpf):
    # Remover caracteres não numéricos do CPF
    cpf_limpo = "".join(filter(str.isdigit, cpf))

    # Inserir a máscara "###.###.###-##"
    cpf_formatado = f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
    return cpf_formatado

# Teste da função
cpf1 = "123.456.789-00"
cpf2 = "98765432101"
print(formatar_cpf(cpf1))  # Resultado: "123.456.789-00"
print(formatar_cpf(cpf2))  # Resultado: "987.654.321-01"
