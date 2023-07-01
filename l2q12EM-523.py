#Lista de Exercício 2 - Questão 12 NÃO RODOU
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o #exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
      #  Salário Bruto: (5 * 220)        : R$ 1100,00
       # (-) IR (5%)                     : R$   55,00
      #  (-) INSS ( 10%)                 : R$  110,00
        #FGTS (11%)                      : R$  121,00
      #  Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00


class FolhaPagamento:
    def __init__(self, valor_hora, horas_trabalhadas):
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario_bruto(self):
        return self.valor_hora * self.horas_trabalhadas

    def calcular_desconto_ir(self, salario_bruto):
        if salario_bruto <= 900:
            return 0
        elif salario_bruto <= 1500:
            return salario_bruto * 0.05
        elif salario_bruto <= 2500:
            return salario_bruto * 0.1
        else:
            return salario_bruto * 0.2

    def calcular_desconto_inss(self, salario_bruto):
        return salario_bruto * 0.1

    def calcular_deposito_fgts(self, salario_bruto):
        return salario_bruto * 0.11

    def calcular_salario_liquido(self, salario_bruto, total_descontos):
        return salario_bruto - total_descontos

    def imprimir_folha_pagamento(self):
        try:
            salario_bruto = self.calcular_salario_bruto()
            desconto_ir = self.calcular_desconto_ir(salario_bruto)
            desconto_inss = self.calcular_desconto_inss(salario_bruto)
            deposito_fgts = self.calcular_deposito_fgts(salario_bruto)
            total_descontos = desconto_ir + desconto_inss

            salario_liquido = self.calcular_salario_liquido(salario_bruto, total_descontos)

            print("Salário Bruto: R$ {:.2f}".format(salario_bruto))
            print("(-) IR (5%): R$ {:.2f}".format(desconto_ir))
            print("(-) INSS (10%): R$ {:.2f}".format(desconto_inss))
            print("FGTS (11%): R$ {:.2f}".format(deposito_fgts))
            print("Total de descontos: R$ {:.2f}".format(total_descontos))
            print("Salário Líquido: R$ {:.2f}".format(salario_liquido))
        except Exception as e:
            print("Ocorreu um erro ao calcular a folha de pagamento:", str(e))


def main():
    try:
        valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
        horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

        folha_pagamento = FolhaPagamento(valor_hora, horas_trabalhadas)
        folha_pagamento.imprimir_folha_pagamento()
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um número válido.")
    except Exception as e:
        print("Ocorreu um erro:", str(e))


if __name__ == "__main__":
    main()
