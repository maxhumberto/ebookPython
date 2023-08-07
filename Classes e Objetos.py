# Criando uma classe para representar um carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        return "Carro acelerando..."

    def frear(self):
        return "Carro freando..."

# Criando um objeto da classe Carro
meu_carro = Carro("Ford", "Focus", 2020)

# Acessando atributos do objeto
print(f"Marca: {meu_carro.marca}, Modelo: {meu_carro.modelo}, Ano: {meu_carro.ano}")

# Chamando métodos do objeto
print(meu_carro.acelerar())  # Resultado: "Carro acelerando..."
print(meu_carro.frear())  # Resultado: "Carro freando..."
