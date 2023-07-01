#Lista de Exercício 1 - Questão 3
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça dois números e imprima a soma.

class Calculadora:
    def __init__(self):
        self.numero1 = None
        self.numero2 = None

    def solicitar_numeros(self):
        try:
            self.numero1 = float(input("Digite o primeiro número: "))
            self.numero2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Valores inválidos. Por favor, insira números válidos.")

    def somar_numeros(self):
        if self.numero1 is not None and self.numero2 is not None:
            return self.numero1 + self.numero2
        else:
            return None

try:
    calculadora = Calculadora()
    calculadora.solicitar_numeros()
    resultado = calculadora.somar_numeros()

    if resultado is not None:
        print("A soma dos números é:", resultado)
except Exception as error:
    print("Ocorreu um erro:", error)
