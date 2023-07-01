#Lista de Exercício 2 - Questão 7
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia três números e mostre o maior e o menor deles.

class Numeros:
    def __init__(self, numero1, numero2, numero3):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3

    def encontrar_maior_menor(self):
        maior = self.numero1
        menor = self.numero1

        if self.numero2 > maior:
            maior = self.numero2
        if self.numero3 > maior:
            maior = self.numero3

        if self.numero2 < menor:
            menor = self.numero2
        if self.numero3 < menor:
            menor = self.numero3

        return maior, menor

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    numero3 = float(input("Digite o terceiro número: "))

    numeros = Numeros(numero1, numero2, numero3)
    maior, menor = numeros.encontrar_maior_menor()

    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")

except ValueError as e:
    print(f"Erro: {e}")
