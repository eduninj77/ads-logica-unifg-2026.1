class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial

conta = ContaBancaria("Fernanda", 500.0)
print(f"Titular da conta: {conta.titular}")
print(f"Saldo da conta: R${conta.saldo:.2f}")