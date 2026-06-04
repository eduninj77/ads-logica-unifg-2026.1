class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError(f"Nota inválida: {nota}. Deve ser entre 0 e 10.")
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        if self.calcular_media() >= 7:
            return "Aprovado"
        return "Recuperação"

e1 = Estudante("Ana", "2024001")

# Notas válidas
e1.adicionar_nota(8.0)
e1.adicionar_nota(7.5)
print(f"Notas: {e1.notas}")

# Testando notas inválidas
testes = [10.0, 0.0, -1.0, 11.0, 5.5]

print("\n--- Testes de validação ---")
for nota in testes:
    try:
        e1.adicionar_nota(nota)
        print(f"✅ Nota {nota:5.1f} aceita")
    except ValueError as e:
        print(f"❌ Nota {nota:5.1f} recusada → {e}")

print(f"\nNotas finais : {e1.notas}")
print(f"Média        : {e1.calcular_media():.2f}")
print(f"Situação     : {e1.situacao()}")