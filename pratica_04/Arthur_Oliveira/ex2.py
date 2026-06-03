nome_completo = "Maria Clara Souza"

partes = nome_completo.split()
print(partes)

nome_hifenizado = "-".join(partes)
print(nome_hifenizado)

primeiro = partes[0]
ultimo   = partes[-1]
print(f"Primeiro: {primeiro} | Último: {ultimo}")