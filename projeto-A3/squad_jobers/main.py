from motores_poo import MotorInducao
from plotagem_ascii import plotar_curva

def cadastrar_motor():
    nome = input("Nome do motor: ")
    frequencia = float(input("Frequência (Hz): "))

    while True:
        polos = int(input("Número de polos (par): "))
        if polos > 0 and polos % 2 == 0:
            break
        print("Polos inválidos! Use 2, 4, 6...")

    torque_max = float(input("Torque máximo (Nm): "))
    s_max = float(input("Escorregamento máximo (ex: 0.2): "))

    motor = MotorInducao(nome, frequencia, polos, torque_max, s_max)
    print(f"Motor cadastrado! Ns = {motor.Ns:.0f} RPM")

while True:
    print("\n[1] Cadastrar motor")
    print("[2] Listar motores")
    print("[3] Gerar curva")
    print("[0] Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        cadastrar_motor()

    elif opcao == "2":
        if not MotorInducao.banco:
            print("Nenhum motor cadastrado.")
        for i, m in enumerate(MotorInducao.banco):
            print(f"[{i}] {m}")

    elif opcao == "3":
        for i, m in enumerate(MotorInducao.banco):
            print(f"[{i}] {m}")
        idx = int(input("Número do motor: "))
        plotar_curva(MotorInducao.banco[idx])

    elif opcao == "0":
        break
