#Lista de Exercício 3 - Questão 8
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia 5 números e informe a soma e a média dos números.


class SomaMediaCalculator:
    def __init__(self):
        self.numeros = []

    def ler_numeros(self):
        for i in range(5):
            while True:
                try:
                    numero = float(input("Digite um número: "))
                    self.numeros.append(numero)
                    break

                except ValueError:
                    print("Erro: Entrada inválida. Digite um número válido.")

    def calcular_soma(self):
        if not self.numeros:
            return None

        return sum(self.numeros)

    def calcular_media(self):
        if not self.numeros:
            return None

        return sum(self.numeros) / len(self.numeros)


def executar_programa():
    calculator = SomaMediaCalculator()

    calculator.ler_numeros()

    soma = calculator.calcular_soma()
    media = calculator.calcular_media()

    if soma is not None and media is not None:
        print("A soma dos números é:", soma)
        print("A média dos números é:", media)
    else:
        print("Nenhum número foi inserido.")


executar_programa()
