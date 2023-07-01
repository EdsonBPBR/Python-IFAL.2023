# Lista de Exercício 4 - Questão 17
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

class Atleta:
    def __init__(self, nome):
        self.nome = nome
        self.saltos = []

    def adicionar_salto(self, distancia):
        self.saltos.append(distancia)

    def calcular_media_saltos(self):
        return sum(self.saltos) / len(self.saltos)

    def exibir_resultado_final(self):
        print("Atleta:", self.nome)
        print("Saltos:", " - ".join(str(salto) + " m" for salto in self.saltos))
        print("Média dos saltos:", self.calcular_media_saltos(), "m")


def ler_distancia_salto(numero_salto):
    while True:
        try:
            distancia = float(input("Distância do {}º salto: ".format(numero_salto)))
            return distancia
        except ValueError:
            print("Erro: Digite um valor numérico válido.")


def main():
    atletas = []

    while True:
        nome = input("Nome do atleta: ")
        if not nome:
            break

        atleta = Atleta(nome)

        for i in range(1, 6):
            distancia = ler_distancia_salto(i)
            atleta.adicionar_salto(distancia)

        atletas.append(atleta)

    for atleta in atletas:
        print()
        atleta.exibir_resultado_final()

    print("Programa encerrado.")


if __name__ == "__main__":
    main()
