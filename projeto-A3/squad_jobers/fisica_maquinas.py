def calcular_ns(frequencia, polos):
    return (120 * frequencia) / polos

def calcular_escorregamento(Ns, N):
    if Ns == 0:
        return 0
    return (Ns - N) / Ns

def torque_kloss(s, s_max, torque_max):
    if s == 0:
        return 0
    return (2 * torque_max) / ((s / s_max) + (s_max / s))
