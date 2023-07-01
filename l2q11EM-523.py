#Lista de Exercício 2 - Questão 11
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

class Colaborador:
    def __init__(self, salario):
        self.salario = salario

    def calcular_reajuste(self):
        if self.salario <= 280.00:
            percentual_aumento = 20
        elif self.salario <= 700.00:
            percentual_aumento = 15
        elif self.salario <= 1500.00:
            percentual_aumento = 10
        else:
            percentual_aumento = 5

        aumento = self.salario * (percentual_aumento / 100)
        novo_salario = self.salario + aumento

        return percentual_aumento, aumento, novo_salario


def exibir_resultado(salario, percentual_aumento, aumento, novo_salario):
    print("Salário antes do reajuste: R$", salario)
    print("Percentual de aumento aplicado:", percentual_aumento, "%")
    print("Valor do aumento: R$", aumento)
    print("Novo salário após o aumento: R$", novo_salario)


salario_atual = float(input("Digite o salário atual do colaborador: "))

colaborador = Colaborador(salario_atual)
percentual_aumento, aumento, novo_salario = colaborador.calcular_reajuste()
exibir_resultado(salario_atual, percentual_aumento, aumento, novo_salario)
