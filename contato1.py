class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def remover_contato(self, contato):
        self.contatos.remove(contato)

    def exibir_contatos(self):
        for contato in self.contatos:
            print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")

# Teste da agenda de contatos
agenda = Agenda()
contato1 = Contato("João", "123456789", "joao@email.com")
contato2 = Contato("Maria", "987654321", "maria@email.com")

agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)
agenda.exibir_contatos()
# Resultado:
# Nome: João, Telefone: 123456789, Email: joao@email.com
# Nome: Maria, Telefone: 987654321, Email: maria@email.com

agenda.remover_contato(contato1)
agenda.exibir_contatos()
# Resultado:
# Nome: Maria, Telefone: 987654321, Email: maria@email.com
