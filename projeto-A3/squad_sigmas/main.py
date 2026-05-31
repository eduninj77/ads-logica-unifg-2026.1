import cli_ingestao
import etl_transformer
import data_warehouse_poo
import dashboard_viz

banco = data_warehouse_poo.BancoDeDados()

# Formato: data,produto,quantidade,valor,estado
texto_bruto = cli_ingestao.coletar_dados()

matriz = etl_transformer.limpar_dados(texto_bruto)

if matriz:
    for linha in matriz:
        banco.adicionar(linha)

print("\n--- EXIBINDO DADOS ---")
banco.mostrar_tudo()

dashboard_viz.exibir_dashboard(banco.registros, lambda v: v.get_valor_total())