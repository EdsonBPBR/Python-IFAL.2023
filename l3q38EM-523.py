#Lista de Exercício 3 - Questão 38
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.


class Funcionario:
    def __init__(self, salario_inicial):
        self.salario_inicial = salario_inicial
        self.salario_atual = self.calcular_salario_atual()

    def calcular_salario_atual(self):
        salario = self.salario_inicial
        percentual_aumento = 1.5

        for ano in range(1996, 2023):
            aumento = salario * (percentual_aumento / 100)
            salario += aumento
            percentual_aumento *= 2

        return salario


def obter_salario_inicial():
    while True:
        try:
            salario_inicial = float(input("Digite o salário inicial do funcionário: "))
            return salario_inicial
        except ValueError:
            print("Erro: Insira um valor numérico válido.")


salario_inicial = obter_salario_inicial()
funcionario = Funcionario(salario_inicial)

print("O salário atual do funcionário é R$", funcionario.salario_atual)
