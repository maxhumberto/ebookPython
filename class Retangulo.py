class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.altura * self.largura

    def calcular_perimetro(self):
        return 2 * (self.altura + self.largura)

# Teste da classe Retangulo
meu_retangulo = Retangulo(5, 10)
print("Área do Retângulo:", meu_retangulo.calcular_area())  # Resultado: 50
print("Perímetro do Retângulo:", meu_retangulo.calcular_perimetro())  # Resultado: 30

