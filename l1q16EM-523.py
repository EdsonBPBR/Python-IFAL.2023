#Lista de Exercício 1 - Questão 16
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

class LojaTintas:
    def __init__(self):
        self.cobertura_litro = 3
        self.capacidade_lata = 18
        self.preco_lata = 80.00

    def calcular_latas_e_preco(self, area):
        litros_necessarios = math.ceil(area / self.cobertura_litro)
        latas_necessarias = math.ceil(litros_necessarios / self.capacidade_lata)
        preco_total = latas_necessarias * self.preco_lata
        return latas_necessarias, preco_total

try:
    loja_tintas = LojaTintas()

    area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
    if area <= 0:
        raise ValueError("A área precisa ser maior que zero.")

    latas, preco = loja_tintas.calcular_latas_e_preco(area)

    print(f"\nQuantidade de latas de tinta a serem compradas: {latas}")
    print(f"Preço total: R$ {preco:.2f}")

except ValueError as error:
    print(f"Erro: {error}")
except Exception as exception:
    print(f"Ocorreu um erro inesperado: {exception}")
