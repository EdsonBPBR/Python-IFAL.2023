#Lista de Exercício 5 - Questão 2
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

class ImprimirPadrao:
    def __init__(self):
        self.n = 0

    def obter_valor_n(self):
        while True:
            try:
                self.n = int(input("Digite um valor para n: "))
                if self.n <= 0:
                    print("O valor de n deve ser um número inteiro positivo.")
                else:
                    break
            except ValueError:
                print("O valor de n deve ser um número inteiro.")

    def imprimir(self):
        for i in range(1, self.n+1):
            linha = ' '.join(str(j) for j in range(1, i+1))
            print(linha)


def executar_programa():
    padrao = ImprimirPadrao()
    padrao.obter_valor_n()
    padrao.imprimir()


executar_programa()
