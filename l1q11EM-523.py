#Lista de Exercício 1 - Questão 11
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a.o produto do dobro do primeiro com metade do segundo .
#b.a soma do triplo do primeiro com o terceiro.
#c.o terceiro elevado ao cubo.

class Calculadora:
    def __init__(self, num_int1, num_int2, num_real):
        self.num_int1 = num_int1
        self.num_int2 = num_int2
        self.num_real = num_real

    def calcular_produto(self):
        return (2 * self.num_int1) * (self.num_int2 / 2)

    def calcular_soma(self):
        return (3 * self.num_int1) + self.num_real

    def calcular_cubo(self):
        return self.num_real ** 3


try:
    # Solicitar os números ao usuário
    numero_inteiro1 = int(input("Digite o primeiro número inteiro: "))
    numero_inteiro2 = int(input("Digite o segundo número inteiro: "))
    numero_real = float(input("Digite o número real: "))

    # Criar uma instância da classe Calculadora
    calculadora = Calculadora(numero_inteiro1, numero_inteiro2, numero_real)

    # Calcular os resultados usando os métodos da classe Calculadora
    resultado_produto = calculadora.calcular_produto()
    resultado_soma = calculadora.calcular_soma()
    resultado_cubo = calculadora.calcular_cubo()

    # Mostrar os resultados
    print("O produto do dobro do primeiro com metade do segundo é:", resultado_produto)
    print("A soma do triplo do primeiro com o terceiro é:", resultado_soma)
    print("O terceiro elevado ao cubo é:", resultado_cubo)

except ValueError:
    print("Erro: Certifique-se de digitar apenas números válidos.")
