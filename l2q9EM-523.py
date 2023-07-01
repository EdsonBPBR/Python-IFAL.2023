#Lista de Exercício 2 - Questão 9
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia três números e mostre-os em ordem decrescente.

class Numeros:
    def __init__(self):
        self.numeros = []

    def ler_numeros(self):
        try:
            for i in range(3):
                numero = float(input(f"Digite o {i+1}º número: "))
                self.numeros.append(numero)
        except ValueError as e:
            print(f"Erro: {e}. Certifique-se de digitar apenas números.")

    def ordenar_decrescente(self):
        self.numeros.sort(reverse=True)

    def mostrar_numeros(self):
        print("Números em ordem decrescente:")
        for numero in self.numeros:
            print(numero)

numeros = Numeros()
numeros.ler_numeros()
numeros.ordenar_decrescente()
numeros.mostrar_numeros()
