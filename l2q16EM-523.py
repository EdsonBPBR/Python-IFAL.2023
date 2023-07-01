#Lista de Exercício 2 - Questão 16
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#a.Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#b.Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#c.Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#d.Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;


import math

class EquacaoSegundoGrau:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_delta(self):
        return self.b**2 - 4*self.a*self.c

    def calcular_raizes(self):
        if self.a == 0:
            raise ValueError("A equação não é do segundo grau.")

        delta = self.calcular_delta()

        if delta < 0:
            raise ValueError("A equação não possui raízes reais.")
        elif delta == 0:
            raiz = -self.b / (2*self.a)
            return raiz
        else:
            raiz1 = (-self.b + math.sqrt(delta)) / (2*self.a)
            raiz2 = (-self.b - math.sqrt(delta)) / (2*self.a)
            return raiz1, raiz2

try:
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    equacao = EquacaoSegundoGrau(a, b, c)
    raizes = equacao.calcular_raizes()

    if isinstance(raizes, float):
        print("A equação possui uma raiz real:", raizes)
    else:
        print("A equação possui duas raízes reais:", raizes[0], "e", raizes[1])

except ValueError as error:
    print("Erro:", str(error))

