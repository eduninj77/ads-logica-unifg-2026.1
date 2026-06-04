estudantes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno ", " carla"]
notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]
busca_aluno = "JOÃO"

estudantes_limpos = []

for nome in estudantes_bruto:
    nome_formatado = nome.strip().lower()
    estudantes_limpos.append(nome_formatado)

aprovados = []
for nota in notas:
    if nota >= 7.0:
        aprovados.append(nota)

aluno_procurado = busca_aluno.strip().lower()
esta_presente = False

for aluno in estudantes_limpos:
    if aluno == aluno_procurado:
        esta_presente = True
        break

print("===RELATORIO DO PROJETO INTEGRADOR===")
print(f"lista de alunos cadastrados: {estudantes_limpos}")
print(f"notas que foram aprovadas: {aprovados}")
print(f"total de alunos que passaram: {len(aprovados)}")

if esta_presente:
    print(f"status da busca: o aluno '{busca_aluno}' gazeou a aula de hoje") #:P
else:
    print(f"status da busca: o aluno '{busca_aluno}' faltou")