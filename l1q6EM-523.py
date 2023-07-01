#Lista de Exercício 1 - Questão 6
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

    def obter_raio(self):
        while True:
            try:
                raio = float(input("Digite o raio do círculo: "))
                if raio <= 0:
                    print("O raio deve ser um valor positivo!")
                    continue
                self.raio = raio
                break
            except ValueError:
                print("Entrada inválida! Digite um número válido para o raio.")

circulo = Circulo(0)  # Cria uma instância de Circulo com raio inicial zero
circulo.obter_raio()  # Solicita ao usuário o raio do círculo
area = circulo.calcular_area()  # Calcula a área do círculo
print("A área do círculo é:", area)
