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


class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.estudantes = []

    def matricular(self, estudante):
        if not isinstance(estudante, Estudante):
            raise TypeError("Apenas objetos Estudante podem ser matriculados.")
        if estudante in self.estudantes:
            return
        self.estudantes.append(estudante)

    def media_geral(self):
        if len(self.estudantes) == 0:
            return 0
        soma = 0
        for estudante in self.estudantes:
            soma += estudante.calcular_media()
        return soma / len(self.estudantes)

    def relatorio(self):
        print("=" * 48)
        print(f"{'RELATÓRIO — ' + self.nome:^48}")
        print("=" * 48)
        print(f"  {'Nome':<12} {'Média':>6}  {'Situação':<12} {'Notas'}")
        print("-" * 48)

        aprovados   = 0
        recuperacao = 0

        for e in self.estudantes:
            media = e.calcular_media()
            sit   = e.situacao()
            icone = "✅" if sit == "Aprovado" else "⚠️ "

            if sit == "Aprovado":
                aprovados += 1
            else:
                recuperacao += 1

            print(f"  {e.nome:<12} {media:>6.2f}  {icone} {sit:<12} {e.notas}")

        print("=" * 48)
        print(f"  Média geral   : {self.media_geral():.2f}")
        print(f"  Aprovados     : {aprovados}")
        print(f"  Recuperação   : {recuperacao}")
        print(f"  Total         : {len(self.estudantes)}")
        print("=" * 48)


# Criando estudantes
e1 = Estudante("Ana",   "2024001")
e2 = Estudante("Bruno", "2024002")
e3 = Estudante("Carla", "2024003")
e4 = Estudante("Diego", "2024004")

for nota in [8.0, 7.5, 9.0]:  e1.adicionar_nota(nota)
for nota in [5.0, 6.0, 4.5]:  e2.adicionar_nota(nota)
for nota in [9.0, 10.0, 8.5]: e3.adicionar_nota(nota)
for nota in [6.5, 7.0, 6.0]:  e4.adicionar_nota(nota)

turma = Turma("3º Ano A")
for e in [e1, e2, e3, e4]:
    turma.matricular(e)

turma.relatorio()