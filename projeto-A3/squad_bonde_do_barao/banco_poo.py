class DemonstracaoAnual:
    def __init__(
        self,
        ano,
        ativo_circulante,
        ativo_nao_circulante,
        passivo_circulante,
        passivo_nao_circulante,
        patrimonio_liquido,
        receita,
        estoque,
        lucro
    ):
        self.ano = ano
        self.ativo_circulante = ativo_circulante
        self.ativo_nao_circulante = ativo_nao_circulante
        self.passivo_circulante = passivo_circulante
        self.passivo_nao_circulante = passivo_nao_circulante
        self.patrimonio_liquido = patrimonio_liquido
        self.receita = receita
        self.estoque = estoque
        self.lucro = lucro

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.historico = []

    def adicionar_demonstracao(self, demonstracao):
        self.historico.append(demonstracao)