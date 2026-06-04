#1.O atiributo de classe é definido diretamente no corpo da classe, então todos os atributos daquela classe compartilham o mesmo valor. Já o atributo de instância é definido dentro do método contrutor da classe, então cada objeto tem aquela "cópia" do atributo, mudando apenas os seus valores.
#2.Demonstração:
import os
os.system("clear" if os.name != "nt" else "cls")

class Funcionario():
    #Todos os objetos compartilham o mesmo atributo padrão
    inss = 0.075
    def __init__(self, nome, salario_bruto):
        #Cada objeto terá o próprio atributo de instânciamento
        self.nome = nome
        self.salario_bruto = salario_bruto

    def exibir_salario(self):
        desconto = self.salario_bruto * self.inss
        print(f"Nome - {self.nome} | Taxa INSS - {self.inss * 100}% | Desconto - R${desconto:.2f}")

f1 = Funcionario("Luis", 4000)
f2 = Funcionario("Pedro", 2000)
#Comportamento padrão
f1.exibir_salario()
f2.exibir_salario()

#Mudança do atributo de instância
f1.nome = "Daniel"
f1.exibir_salario()
f2.exibir_salario()

#Mudança do atributo de classe
Funcionario.inss = 0.11
f1.exibir_salario()
f2.exibir_salario()
