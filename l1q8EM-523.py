#Lista de Exercício 1 - Questão 8
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

class Salario:
    def __init__(self):
        self.valor_hora = 0
        self.horas_trabalhadas = 0

    def calcular_salario(self):
        return self.valor_hora * self.horas_trabalhadas

    def obter_valor_hora(self):
        while True:
            try:
                self.valor_hora = float(input("Digite o valor da sua taxa horária: "))
                if self.valor_hora <= 0:
                    print("O valor da taxa horária deve ser um número positivo!")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite um número válido para a taxa horária.")

    def obter_horas_trabalhadas(self):
        while True:
            try:
                self.horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
                if self.horas_trabalhadas <= 0:
                    print("O número de horas trabalhadas deve ser um número positivo!")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite um número válido para as horas trabalhadas.")

    def exibir_salario(self):
        salario = self.calcular_salario()
        print("O total do seu salário no mês é:", salario)

salario = Salario()
salario.obter_valor_hora()
salario.obter_horas_trabalhadas()
salario.exibir_salario()
