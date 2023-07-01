#Lista de Exercício 1 - Questão 7
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

class Quadrado:
    def __init__(self):
        self.lado = 0

    def calcular_area(self):
        return self.lado ** 2

    def obter_lado(self):
        while True:
            try:
                self.lado = float(input("Digite o valor do lado do quadrado: "))
                if self.lado <= 0:
                    print("O lado do quadrado deve ser um valor positivo!")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite um número válido para o lado do quadrado.")

    def exibir_resultados(self, area):
        print("A área do quadrado é:", area)
        print("O dobro da área do quadrado é:", 2 * area)

quadrado = Quadrado()
quadrado.obter_lado()
area = quadrado.calcular_area()
quadrado.exibir_resultados(area)
