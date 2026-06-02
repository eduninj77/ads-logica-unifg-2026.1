class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

conta = ContaBancaria("Gabriel", 100.0)
print(f"Saldo inicial: R${conta.saldo:.2f}")

conta.depositar(150.0)
print(f"Saldo após depósito de R$150.00: R${conta.saldo:.2f}")