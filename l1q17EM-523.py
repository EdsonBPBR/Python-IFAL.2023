# Lista de Exercício 1 - Questão 17 pra corrigir
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradase os respectivos preçosem 3 situações: comprar
#apenas latas de 18 litros; comprar apenas galões de 3, 6 litros misturar latas e galões, de forma que o desperdícia de
#tinta seja menor.Acrescente 10 % de folga e sempre arredonde os valores para cima, isto é, considere lata scheias.

import math

class LojaTintas:
    def __init__(self):
        self.area = 0.0

    def obter_tamanho_area(self):
        try:
            self.area = float(input("Informe o tamanho da área a ser pintada (em metros quadrados): "))
            if self.area <= 0:
                raise ValueError("A área deve ser um valor positivo.")
        except ValueError as e:
            print(f"Erro: {str(e)}")
            return False

        return True

    def calcular_latas(self):
        litros_tinta = self.area / 6  # Calcula a quantidade de litros necessários
        latas = math.ceil(litros_tinta / 18)  # Arredonda para cima e calcula a quantidade de latas
        preco = latas * 80  # Calcula o preço total das latas
        return latas, preco

    def calcular_galoes(self):
        litros_tinta = self.area / 6  # Calcula a quantidade de litros necessários
        galoes = math.ceil(litros_tinta / 3.6)  # Arredonda para cima e calcula a quantidade de galões
        preco = galoes * 25  # Calcula o preço total dos galões
        return galoes, preco

    def calcular_mistura(self):
        litros_tinta = self.area / 6  # Calcula a quantidade de litros necessários
        latas = math.floor(litros_tinta / 18)  # Calcula a quantidade de latas inteiras
        sobra = litros_tinta % 18  # Calcula a quantidade de litros restantes após as latas inteiras
        galoes = math.ceil(sobra / 3.6)  # Arredonda para cima e calcula a quantidade de galões para a sobra
        preco = (latas * 80) + (galoes * 25)  # Calcula o preço total das latas e galões
        return latas, galoes, preco

    def exibir_resultados(self):
        if self.obter_tamanho_area():
            latas, preco_latas = self.calcular_latas()
            galoes, preco_galoes = self.calcular_galoes()
            latas_mistura, galoes_mistura, preco_mistura = self.calcular_mistura()

            print(f"\nOpção 1: Comprar apenas latas de 18 litros")
            print(f"Quantidade de latas: {latas}")
            print(f"Preço total: R$ {preco_latas:.2f}")

            print(f"\nOpção 2: Comprar apenas galões de 3,6 litros")
            print(f"Quantidade de galões: {galoes}")
            print(f"Preço total: R$ {preco_galoes:.2f}")

            print(f"\nOpção 3: Misturar latas e galões")
            print(f"Quantidade de latas: {latas_mistura}")
            print(f"Quantidade de galões: {galoes_mistura}")
            print(f"Preço total: R$ {preco_mistura:.2f}")

# Programa principal
if __name__ == "__main__":
    loja_tintas = LojaTintas()
    loja_tintas.exibir_resultados()

