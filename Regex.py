import re

texto = "Entre em contato pelo email: contato@example.com ou suporte@example.com"
padrao_email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

emails_encontrados = re.findall(padrao_email, texto)
print(emails_encontrados)  # Resultado: ['contato@example.com', 'suporte@example.com']
