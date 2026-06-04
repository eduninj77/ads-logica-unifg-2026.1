class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def criar_conta(self, numero, titular, saldo_inicial=0):
        conta = {"numero": numero, "titular": titular, "saldo": saldo_inicial}
        self.contas.append(conta)

    def depositar(self, numero, valor):
        for conta in self.contas:
            if conta["numero"] == numero:
                conta["saldo"] += valor
                return True
        return False

    def sacar(self, numero, valor):
        for conta in self.contas:
            if conta["numero"] == numero:
                if conta["saldo"] >= valor:
                    conta["saldo"] -= valor
                    return True
        return False

    def consultar_saldo(self, numero):
        for conta in self.contas:
            if conta["numero"] == numero:
                return conta["saldo"]
        return None


banco = Banco("Banco XYZ")
banco.criar_conta("001", "Matheus", 1000)
banco.depositar("001", 500)
print(f"Saldo: {banco.consultar_saldo('001')}")
banco.sacar("001", 200)
print(f"Saldo após saque: {banco.consultar_saldo('001')}")
