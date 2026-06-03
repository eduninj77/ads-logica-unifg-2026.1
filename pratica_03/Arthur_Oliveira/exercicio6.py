x = 10

def teste():
    y = 5
    return x + y

print(teste())
print(y)  # ❌ ERRO!x = 10

#meu exemplo e global
nome_empresa = "TechCorp"   # global

def apresentar_funcionario():
    nome_funcionario = "Carlos"   # local
    print(f"{nome_funcionario} trabalha na {nome_empresa}")

apresentar_funcionario()
# Carlos trabalha na TechCorp

print(nome_empresa)       # ✅ funciona — é global
print(nome_funcionario)   # ❌ NameError — é local