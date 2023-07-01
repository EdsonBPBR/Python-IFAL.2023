#Lista de Exercício 1 - Questão 12
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

class Pessoa:
    def __init__(self, altura):
        self.altura = altura

    def calcular_peso_ideal(self):
        peso_ideal = (72.7 * self.altura) - 58
        return peso_ideal

    def exibir_peso_ideal(self):
        peso_ideal = self.calcular_peso_ideal()
        print("O peso ideal para uma pessoa com altura", self.altura, "é", peso_ideal, "quilogramas.")


def obter_altura():
    while True:
        try:
            altura = float(input("Digite a altura em metros: "))
            return altura
        except ValueError:
            print("Erro: A altura deve ser um número válido.")


def main():
    altura = obter_altura()
    pessoa = Pessoa(altura)
    pessoa.exibir_peso_ideal()


if __name__ == '__main__':
    main()
