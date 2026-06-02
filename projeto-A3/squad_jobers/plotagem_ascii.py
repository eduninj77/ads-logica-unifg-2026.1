def plotar_curva(motor):
    print(f"\n=== Curva de Torque — {motor.nome} (Ns={motor.Ns:.0f} RPM) ===\n")
    passo = int(motor.Ns // 20)

    for N in range(0, int(motor.Ns) + 1, passo):
        s, torque = motor.calcular_ponto(N)
        barras = int((torque / motor.torque_max) * 40)
        print(f"{N:5} RPM | {'#' * barras} {torque:.1f} Nm")

    print()
