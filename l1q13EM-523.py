#Lista de Exercício 1 - Questão 13
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda



#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#a.Para homens: (72.7*h) - 58
#b.Para mulheres: (62.1*h) - 44.7

class Pessoa:
    def __init__(self, altura, genero):
        self.altura = altura
        self.genero = genero

    def calcular_peso_ideal(self):
        if self.genero == 'M':
            peso_ideal = (72.7 * self.altura) - 58
        elif self.genero == 'F':
            peso_ideal = (62.1 * self.altura) - 44.7
        else:
            raise ValueError("Gênero inválido. Use 'M' para masculino ou 'F' para feminino.")
        return peso_ideal

    def exibir_peso_ideal(self):
        try:
            peso_ideal = self.calcular_peso_ideal()
            print("O peso ideal para uma pessoa com altura", self.altura, "e gênero", self.genero, "é", peso_ideal,
                  "quilogramas.")

        except ValueError as e:
            print("Erro:", str(e))


def obter_altura():
    while True:
        try:
            altura = float(input("Digite a altura em metros: "))
            return altura
        except ValueError:
            print("Erro: A altura deve ser um número válido.")


def obter_genero():
    while True:
        genero = input("Digite o gênero (M/F): ").upper()
        if genero in ['M', 'F']:
            return genero
        print("Erro: Gênero inválido. Use 'M' para masculino ou 'F' para feminino.")


def main():
    altura = obter_altura()
    genero = obter_genero()
    pessoa = Pessoa(altura, genero)
    pessoa.exibir_peso_ideal()


if __name__ == '__main__':
    main()
