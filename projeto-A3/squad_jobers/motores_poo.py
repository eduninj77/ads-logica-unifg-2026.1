from fisica_maquinas import calcular_ns, calcular_escorregamento, torque_kloss

class MotorInducao:
    banco = []

    def __init__(self, nome, frequencia, polos, torque_max, s_max):
        self.nome = nome
        self.frequencia = frequencia
        self.polos = polos
        self.torque_max = torque_max
        self.s_max = s_max
        self.Ns = calcular_ns(frequencia, polos)  # calculado automaticamente
        MotorInducao.banco.append(self)

    def calcular_ponto(self, N):
        s = calcular_escorregamento(self.Ns, N)
        torque = torque_kloss(s, self.s_max, self.torque_max)
        return s, torque

    def __str__(self):
        return f"{self.nome} | {self.polos} polos | Ns={self.Ns:.0f} RPM | T_max={self.torque_max} Nm"
