#Lista de Exercício 1 - Questão 15
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a.salário bruto.
#b.quanto pagou ao INSS.
#c.quanto pagou ao sindicato.
#d.o salário líquido.
#e.calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

class CalculadoraSalario:
    def __init__(self, valor_hora, horas_trabalhadas):
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario_bruto(self):
        return self.valor_hora * self.horas_trabalhadas

    def calcular_imposto_renda(self):
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto * 0.11

    def calcular_inss(self):
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto * 0.08

    def calcular_sindicato(self):
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto * 0.05

    def calcular_salario_liquido(self):
        salario_bruto = self.calcular_salario_bruto()
        imposto_renda = self.calcular_imposto_renda()
        inss = self.calcular_inss()
        sindicato = self.calcular_sindicato()
        return salario_bruto - imposto_renda - inss - sindicato


try:
    valor_hora = float(input("Informe o valor que você ganha por hora: "))
    horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))

    calculadora = CalculadoraSalario(valor_hora, horas_trabalhadas)

    salario_bruto = calculadora.calcular_salario_bruto()
    imposto_renda = calculadora.calcular_imposto_renda()
    inss = calculadora.calcular_inss()
    sindicato = calculadora.calcular_sindicato()
    salario_liquido = calculadora.calcular_salario_liquido()

    print("Salário Bruto: R$", salario_bruto)
    print("Imposto de Renda (11%): R$", imposto_renda)
    print("INSS (8%): R$", inss)
    print("Sindicato (5%): R$", sindicato)
    print("Salário Líquido: R$", salario_liquido)

except ValueError:
    print("Erro: Certifique-se de inserir valores numéricos para o valor da hora e as horas trabalhadas.")
