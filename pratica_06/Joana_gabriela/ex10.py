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

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)

    def listar_estudantes(self):
        print(f"\n=== Turma: {self.nome} ===")
        if len(self.estudantes) == 0:
            print("Nenhum estudante cadastrado.")
            return
        for e in self.estudantes:
            print(f"  {e.nome:<12} Matrícula: {e.matricula}")
        print(f"  Total: {len(self.estudantes)} estudante(s)")


# Criando turma e estudantes
turma_a = Turma("3º Ano A")

e1 = Estudante("Ana",   "2024001")
e2 = Estudante("Bruno", "2024002")
e3 = Estudante("Carla", "2024003")

turma_a.adicionar_estudante(e1)
turma_a.adicionar_estudante(e2)
turma_a.adicionar_estudante(e3)

turma_a.listar_estudantes()

# Testando turma vazia
turma_b = Turma("3º Ano B")
turma_b.listar_estudantes()