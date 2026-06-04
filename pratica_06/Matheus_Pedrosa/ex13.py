class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descricao(self):
        return f"{self.marca} {self.modelo}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas

    def descricao(self):
        return f"{super().descricao()} - {self.num_portas} portas"


carro = Carro("Toyota", "Corolla", 4)
print(carro.descricao())
