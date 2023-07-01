
#Lista de Exercício 1 - Questão 5
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que converta metros para centímetros.

class ConversorMetrosCentimetros:
    def __init__(self):
        pass

    def metros_para_centimetros(self, metros):
        centimetros = metros * 100
        return centimetros

    def converter(self):
        try:
            metros = float(input("Digite o valor em metros: "))
            centimetros = self.metros_para_centimetros(metros)
            print(f"{metros} metros equivalem a {centimetros} centímetros.")
        except ValueError:
            print("Valor inválido. Certifique-se de digitar um número válido.")

conversor = ConversorMetrosCentimetros()
conversor.converter()
