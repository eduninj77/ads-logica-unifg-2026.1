import os
os.system("clear" if os.name != "nt" else "cls")

lista = []
lista.append("estudar Python")
lista.append("resolver exercícios")
lista.append("revisar código")
lista.append("enviar atividade")
lista.append("falar com Anderson")

print(lista)
print(f"Foram cadastradas no total {len(lista)} tarefas.")