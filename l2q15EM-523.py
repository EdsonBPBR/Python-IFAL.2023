#Lista de Exercício 2 - Questão 15
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def verificar_triangulo(self):
        if self.lado1 + self.lado2 > self.lado3 and self.lado1 + self.lado3 > self.lado2 and self.lado2 + self.lado3 > self.lado1:
            if self.lado1 == self.lado2 and self.lado1 == self.lado3:
                return "Triângulo Equilátero"
            elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
                return "Triângulo Isósceles"
            else:
                return "Triângulo Escaleno"
        else:
            return "Não é um triângulo"


def ler_lado(mensagem):
    while True:
        try:
            lado = float(input(mensagem))
            return lado
        except ValueError:
            print("Erro: Digite um valor numérico válido para o lado do triângulo.")


def main():
    lado1 = ler_lado("Digite o primeiro lado do triângulo: ")
    lado2 = ler_lado("Digite o segundo lado do triângulo: ")
    lado3 = ler_lado("Digite o terceiro lado do triângulo: ")

    triangulo = Triangulo(lado1, lado2, lado3)
    tipo_triangulo = triangulo.verificar_triangulo()
    print(tipo_triangulo)

main()
