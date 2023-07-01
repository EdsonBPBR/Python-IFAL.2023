#Lista de Exercício 3 - Questão 46
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Rodrigo Curvêllo

#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m#

#Melhor salto:  6.5 m
#Pior salto: 5.3 m
#Média dos demais saltos: 5.9 m

#Resultado final:
#Rodrigo Curvêllo: 5.9 m



class Atleta:
    def __init__(self, nome):
        self.nome = nome
        self.saltos = []

    def adicionar_salto(self, distancia):
        self.saltos.append(distancia)

    def calcular_media_saltos(self):
        melhores_saltos = sorted(self.saltos)[1:-1]  # Remove o melhor e pior salto
        media_saltos = sum(melhores_saltos) / len(melhores_saltos)
        return media_saltos


def obter_saltos(atleta):
    for i in range(1, 6):
        while True:
            try:
                distancia = float(input(f"{i}º Salto: "))
                atleta.adicionar_salto(distancia)
                break
            except ValueError:
                print("Valor inválido! Digite novamente.")

def exibir_resultado_final(atleta):
    media_saltos = atleta.calcular_media_saltos()
    print("\nResultado final:")
    print(f"{atleta.nome}: {media_saltos} m\n")

def exibir_relatorio(atletas):
    print("Relatório de todos os atletas:")
    for atleta in atletas:
        media_saltos = atleta.calcular_media_saltos()
        print(f"{atleta.nome}: {media_saltos} m")


def main():
    atletas = []
    while True:
        nome = input("Nome do atleta: ")
        if nome == "":
            break

        atleta = Atleta(nome)
        obter_saltos(atleta)
        exibir_resultado_final(atleta)

        atletas.append(atleta)

    exibir_relatorio(atletas)


if __name__ == "__main__":
    main()
