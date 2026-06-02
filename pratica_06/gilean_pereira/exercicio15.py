class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print("Erro: Saldo insuficiente para o saque.")
            return False

conta = ContaBancaria("Helena", 200.0)

print(f"Saldo atual: R${conta.saldo:.2f}")
sucesso = conta.sacar(50.0)
print(f"Saque realizado? {sucesso} | Novo saldo: R${conta.saldo:.2f}\n")

sucesso_invalido = conta.sacar(300.0)
print(f"Saque realizado? {sucesso_invalido} | Saldo final: R${conta.saldo:.2f}")