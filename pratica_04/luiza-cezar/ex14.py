def padronizar_nomes(nomes_bruto):
    nomes = []
    for nome in nomes_bruto:
        nomes.append(nome.strip().title())
    return nomes


def filtrar_aprovados(notas, limite=7.0):
    aprovados = []
    for nota in notas:
        if nota >= limite:
            aprovados.append(nota)
    return aprovados


def verificar_presenca(nomes, consulta):
    consulta_padronizada = consulta.strip().title()
    return consulta_padronizada in nomes, consulta_padronizada


def gerar_relatorio(nomes_padronizados, aprovados, nome_consulta, esta_presente):
    relatorio = []
    relatorio.append("--- Relatório Final ---")
    relatorio.append(f"Estudantes cadastrados: {', '.join(nomes_padronizados)}")
    relatorio.append(f"Notas aprovadas (>= 7.0): {aprovados}")
    relatorio.append(f"Total de aprovados: {len(aprovados)}")
    relatorio.append(f"Consulta de presença: {nome_consulta}")
    relatorio.append("Presença confirmada." if esta_presente else "Estudante não localizado.")
    return "\n".join(relatorio)


def main():
    nomes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "carla"]
    notas = [6.5, 7.2, 8.0, 5.9, 9.1]

    nomes_padronizados = padronizar_nomes(nomes_bruto)
    aprovados = filtrar_aprovados(notas)

    consulta = input("Digite o nome do estudante para verificar presença: ").strip()
    if not consulta:
        consulta = "joão"
    esta_presente, nome_consulta = verificar_presenca(nomes_padronizados, consulta)

    relatorio = gerar_relatorio(nomes_padronizados, aprovados, nome_consulta, esta_presente)
    print(relatorio)


if __name__ == "__main__":
    main()
