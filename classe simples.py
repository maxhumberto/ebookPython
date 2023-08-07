# Criando uma classe simples
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Criando objetos da classe Pessoa
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

# Chamando um método do objeto
mensagem1 = pessoa1.cumprimentar()  # Resultado: "Olá, meu nome é João e eu tenho 30 anos."
mensagem2 = pessoa2.cumprimentar()  # Resultado: "Olá, meu nome é Maria e eu tenho 25 anos."
