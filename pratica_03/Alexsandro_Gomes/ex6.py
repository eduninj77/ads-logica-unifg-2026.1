taxa_alfandega = 0.20
preco_placa_de_Video = 3500

def preco_final_importacao(produto_Chines):
    cupom_de_desconto = 15.00
    preco_com_desconto = produto_Chines - cupom_de_desconto
    valor_taxado = preco_com_desconto * taxa_alfandega

    return preco_com_desconto + valor_taxado

total = preco_final_importacao(preco_placa_de_Video)

print(f"Preço original do site: R$ {preco_placa_de_Video:.2f}")
print(f"Preço total com taxa e desconto: R$ {total:.2f}")

#1 A variavel global e a 'taxa_alfandega' e o 'preco_placa_de_video' pois estão fora da função e podem ser acessadas de qualquer lugar
#2 As variáveis locais são o 'cupom_de_desconto' , 'preco_com_desconto' e 'valor taxado', pois foiram criadas dentro da função e so existem dentro dela
#3 O programa vai dar erro e não vai rodar, avisando que a variável não foi definida. Porquetem sua área de alcance limitada ao lado de dentro da função