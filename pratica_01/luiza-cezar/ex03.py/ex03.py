
##################################################
#                                                #
#               by: Luiza Cezar                  #
#                                                #
##################################################


total_fatias = int(input("Digite o número total de fatias: "))
programadores = int(input("Digite o número de programadores na equipe: "))

fatias_por_pessoa = total_fatias // programadores
sobra = total_fatias % programadores

print(f"Cada programador comerá {fatias_por_pessoa} fatias inteiras.")
print(f"Sobrarão {sobra} fatias na caixa.")