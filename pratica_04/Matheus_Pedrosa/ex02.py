nome_completo = "Maria Clara Souza"

partes = nome_completo.split()
print(partes)

nome_hifen = "-".join(partes)
print(nome_hifen)

primeiro_nome = partes[0]
ultimo_sobrenome = partes[-1]
print(f"Primeiro nome: {primeiro_nome}")
print(f"Último sobrenome: {ultimo_sobrenome}")
