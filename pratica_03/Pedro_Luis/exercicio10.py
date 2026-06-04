import os
os.system("clear" if os.name != "nt" else "cls")

def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total

#chamada
calcular_total(50, 2)


### Tabela de Execução - Teste de Mesa

#| Linha do Código | preco | quantidade | subtotal | desconto | total | Retorno / Saída |
#| **Chamada da Função** | 50 | 2 | - | - | - | *Entrada de parâmetros* |
#| 'subtotal' = preco * quantidade` | 50 | 2 | **100.0** | - | - | |
#| 'desconto' = subtotal * 0.1` | 50 | 2 | 100.0 | **10.0** | - | |
#| 'total' = subtotal - desconto` | 50 | 2 | 100.0 | 10.0 | **90.0** | |
#| 'return total' | 50 | 2 | 100.0 | 10.0 | 90.0 | **Retorna: 90.0** |

#Casos normais:
print(calcular_total(100, 4))
print(calcular_total(20, 3))

#Caso limitrofe:
print(calcular_total(20,0))

#Caso extremo:
print(calcular_total(-80,3))