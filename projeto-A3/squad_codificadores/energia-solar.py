print("="*45)
print(f"{'SUNSHADE CORPORATION':^45}")
print("="*45)

class PainelSolar:
    def _init_(self, nome, potencia_w, preco):
        self.nome = nome
        self.potencia_w = potencia_w
        self.preco = preco


catalogo = [
    PainelSolar("Painel Solar 500W", 500, 800),
    PainelSolar("Painel Solar 550W", 550, 950),
    PainelSolar("Painel Solar 600W", 600, 1100)
]


tipo = input("Sistema (1 = On-Grid | 2 = Off-Grid): ")

while tipo != "1" and tipo != "2":
    print("Opção inválida!")
    tipo = input("Digite 1 para On-Grid ou 2 para Off-Grid: ")


consumo = float(input("Consumo mensal (kWh): "))

while consumo <= 0:
    print("Valor inválido!")
    consumo = float(input("Digite novamente: "))

hsp = float(input("HSP (horas de sol pleno): "))

while hsp <= 0:
    print("Valor inválido!")
    hsp = float(input("Digite novamente: "))


potencia_escolhida = int(input("Digite a potência da placa (W): "))

painel_escolhido = None

for painel in catalogo:
    if painel.potencia_w == potencia_escolhida:
        painel_escolhido = painel

while painel_escolhido == None:

    print("Painel não encontrado no catálogo!")

    potencia_escolhida = int(input("Digite novamente a potência da placa (W): "))

    for painel in catalogo:
        if painel.potencia_w == potencia_escolhida:
            painel_escolhido = painel


potencia_painel = painel_escolhido.potencia_w
preco_painel = painel_escolhido.preco


custo_inversor = float(input("Custo do inversor: "))

while custo_inversor <= 0:
    print("Valor inválido!")
    custo_inversor = float(input("Digite novamente: "))

custo_mao_obra = float(input("Custo da mão de obra: "))

while custo_mao_obra <= 0:
    print("Valor inválido!")
    custo_mao_obra = float(input("Digite novamente: "))

tarifa = float(input("Tarifa de energia (R$/kWh): "))

while tarifa <= 0:
    print("Valor inválido!")
    tarifa = float(input("Digite novamente: "))


if tipo == "2":

    autonomia = float(input("Autonomia (dias): "))

    while autonomia <= 0:
        print("Valor inválido!")
        autonomia = float(input("Digite novamente: "))

    tensao = float(input("Tensão do sistema (V): "))

    while tensao <= 0:
        print("Valor inválido!")
        tensao = float(input("Digite novamente: "))


consumo_diario = consumo / 30

eficiencia = 0.80

pot_pico = consumo_diario / (hsp * eficiencia)

# Conversão W -> kW
potencia_painel_kw = potencia_painel / 1000

if potencia_painel_kw == 0:
    qtd = 0
else:
    qtd = pot_pico / potencia_painel_kw


qtd_paineis = int(qtd)

if qtd > qtd_paineis:
    qtd_paineis = qtd_paineis + 1


custo_total = (
    (qtd_paineis * preco_painel)
    + custo_inversor
    + custo_mao_obra
)


economia_mensal = consumo * tarifa


if economia_mensal == 0:
    payback = 0
else:
    payback = custo_total / economia_mensal


if tipo == "2":

    profundidade_descarga = 0.80

    capacidade_baterias = (
        consumo_diario * 1000 * autonomia
    ) / (tensao * profundidade_descarga)


print("\n" + "="*50)
print(f"{'PROPOSTA DE SISTEMA SOLAR':^50}")
print("="*50)

if tipo == "1":
    tipo_sistema = "On-Grid"
else:
    tipo_sistema = "Off-Grid"

print(f"{'Tipo de Sistema:':<25}{tipo_sistema}")
print(f"{'Painel Escolhido:':<25}{painel_escolhido.nome}")

print("-"*50)

print(f"{'Consumo Diário:':<25}{consumo_diario:.2f} kWh/dia")
print(f"{'Potência do Sistema:':<25}{pot_pico:.2f} kWp")
print(f"{'Qtd de Painéis:':<25}{qtd_paineis}")

print("-"*50)

print(f"{'Custo Total:':<25}R$ {custo_total:.2f}")
print(f"{'Economia Mensal:':<25}R$ {economia_mensal:.2f}")

anos = int(payback // 12)
meses = int(payback % 12)

print(f"{'Payback:':<25}{anos} anos e {meses} meses")


if tipo == "2":
    print("-"*50)
    print(f"{'Banco de Baterias:':<25}{capacidade_baterias:.2f} Ah")

print("="*50)
print(f"{'Obrigado!':^50}")
print("="*50)
