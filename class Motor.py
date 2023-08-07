class Motor:
    def __init__(self, potencia, combustivel):
        self.potencia = potencia
        self.combustivel = combustivel

class Carro:
    def __init__(self, marca, modelo, ano, potencia_motor, tipo_combustivel):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = Motor(potencia_motor, tipo_combustivel)

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")
        print(f"Motor - Potência: {self.motor.potencia}, Combustível: {self.motor.combustivel}")
# Teste da composição de classes
meu_carro = Carro("Ford", "Focus", 2020, 150, "Gasolina")
meu_carro.exibir_informacoes()
# Resultado: # Marca: Ford, Modelo: Focus, Ano: 2020
# Motor - Potência: 150, Combustível: Gasolina
