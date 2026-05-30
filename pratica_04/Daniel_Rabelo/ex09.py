tarefas = []

tarefas.append("Estudar Python")
tarefas.append("Resolver exercícios")
tarefas.append("Revisar código")
tarefas.append("Enviar atividade")

# ---- Desafio: quinta tarefa ----
tarefas.append("Assistir aula gravada")

print("---- Minhas tarefas ----")
for i, tarefa in enumerate(tarefas, start=1):
    print(f"{i}. {tarefa}")

print(f"\nTotal de tarefas: {len(tarefas)}")