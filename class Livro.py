class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_informacoes(self):
        print(f"Título: {self.titulo},  Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}")

# Teste da classe Livro
meu_livro = Livro("Aprendendo Python", "John Doe", 2021)
meu_livro.exibir_informacoes()  # Resultado: "Título: Aprendendo Python,
# Autor: John Doe, Ano de Publicação: 2021"
