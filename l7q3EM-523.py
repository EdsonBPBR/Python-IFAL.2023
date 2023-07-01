# Lista de Exercício 7 - Questão 3
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Classe Retangulo: Crie uma classe que modele um retangulo:
#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.



class Retangulo:
    def __init__(self, lado_a, lado_b):
        self._lado_a = None
        self._lado_b = None
        self.lado_a = lado_a
        self.lado_b = lado_b

    @property
    def lado_a(self):
        return self._lado_a

    @lado_a.setter
    def lado_a(self, novo_lado_a):
        if novo_lado_a <= 0:
            raise ValueError("O lado A do retângulo deve ser maior que zero.")
        self._lado_a = novo_lado_a

    @property
    def lado_b(self):
        return self._lado_b

    @lado_b.setter
    def lado_b(self, novo_lado_b):
        if novo_lado_b <= 0:
            raise ValueError("O lado B do retângulo deve ser maior que zero.")
        self._lado_b = novo_lado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)


def calcular_quantidade_pisos(area):
    # Considerando que um piso cobre uma área de 1 metro quadrado
    return area


def calcular_quantidade_rodapes(perimetro):
    # Considerando que o rodapé tem a altura de 0.10 metros
    altura_rodape = 0.10
    return perimetro * altura_rodape


def main():
    try:
        lado_a = float(input("Digite o valor do lado A do retângulo: "))
        lado_b = float(input("Digite o valor do lado B do retângulo: "))

        meu_retangulo = Retangulo(lado_a, lado_b)

        area = meu_retangulo.calcular_area()
        perimetro = meu_retangulo.calcular_perimetro()

        print("Área do retângulo:", area)
        print("Perímetro do retângulo:", perimetro)

        quantidade_pisos = calcular_quantidade_pisos(area)
        print("Quantidade de pisos necessários:", quantidade_pisos)

        quantidade_rodapes = calcular_quantidade_rodapes(perimetro)
        print("Quantidade de rodapés necessários:", quantidade_rodapes)

    except ValueError as e:
        print("Erro:", str(e))


if __name__ == "__main__":
    main()
