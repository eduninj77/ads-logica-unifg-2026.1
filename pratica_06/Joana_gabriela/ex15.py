class Veiculo:
    # atributo de CLASSE — compartilhado por todos os objetos
    total_veiculos = 0

    def __init__(self, modelo, velocidade_maxima):
        # atributos de INSTÂNCIA — únicos para cada objeto
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        Veiculo.total_veiculos += 1

v1 = Veiculo("Fusca",    140)
v2 = Veiculo("Civic",    220)
v3 = Veiculo("Caminhão", 110)

# Atributos de instância — cada um tem o seu
print("=== Atributos de instância ===")
print(f"v1: {v1.modelo:<12} {v1.velocidade_maxima} km/h")
print(f"v2: {v2.modelo:<12} {v2.velocidade_maxima} km/h")
print(f"v3: {v3.modelo:<12} {v3.velocidade_maxima} km/h")

# Atributo de classe — mesmo valor para todos
print("\n=== Atributo de classe ===")
print(f"Via classe    : Veiculo.total_veiculos = {Veiculo.total_veiculos}")
print(f"Via v1        : v1.total_veiculos      = {v1.total_veiculos}")
print(f"Via v2        : v2.total_veiculos      = {v2.total_veiculos}")

# Alterando instância — afeta só aquele objeto
print("\n=== Alterando atributo de instância ===")
v1.modelo = "Fusca 1970"
print(f"v1.modelo : {v1.modelo}")
print(f"v2.modelo : {v2.modelo}  ← não foi afetado")

# Alterando a classe — afeta todos
print("\n=== Alterando atributo de classe ===")
Veiculo.total_veiculos = 999
print(f"v1.total_veiculos : {v1.total_veiculos}")
print(f"v2.total_veiculos : {v2.total_veiculos}")
print(f"v3.total_veiculos : {v3.total_veiculos}")

#Diferença fundamental
#Atributo de classeAtributo de instânciaOnde é definidofora do __init__dentro do __init__ com selfPertence aà classe inteiraa cada objeto individualmenteCompartilhado?✅ todos os objetos❌ cada um tem o seuAlterado viaClasse.atributoobjeto.atributoUso típicocontadores, constantes, taxasnome, preço, notas, saldo