# Classe base (pai)
class Animal:
    def emitir_som(self):
        pass

# Classes derivadas (filhas)
class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

# Polimorfismo
cachorro = Cachorro()
gato = Gato()

print(cachorro.emitir_som())  # Resultado: "Au Au!"
print(gato.emitir_som())  # Resultado: "Miau!"
