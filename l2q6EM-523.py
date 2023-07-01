
#Lista de Exercício 2 - Questão 6
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia três números e mostre o maior deles.


class Numeros:
    def __init__(self, numero1, numero2, numero3):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3

    def encontrar_maior_numero(self):
        if self.numero1 >= self.numero2 and self.numero1 >= self.numero3:
            return self.numero1
        elif self.numero2 >= self.numero1 and self.numero2 >= self.numero3:
            return self.numero2
        else:
            return self.numero3

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    numero3 = float(input("Digite o terceiro número: "))

    numeros = Numeros(numero1, numero2, numero3)
    maior = numeros.encontrar_maior_numero()

    print(f"O maior número é: {maior}")

except ValueError as e:
    print(f"Erro: {e}")

