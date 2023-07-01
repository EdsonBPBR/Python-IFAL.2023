#Lista de Exercício 3 - Questão 18
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.


class EstatisticasConjunto:
    def __init__(self):
        self.numeros = []

    def obter_numeros(self):
        try:
            n = int(input("Digite a quantidade de números no conjunto: "))

            for i in range(n):
                numero = float(input(f"Digite o {i + 1}º número: "))
                self.numeros.append(numero)
        except ValueError:
            raise ValueError("Valor inválido. Digite um número válido.")

    def calcular_menor_valor(self):
        return min(self.numeros)

    def calcular_maior_valor(self):
        return max(self.numeros)

    def calcular_soma_valores(self):
        return sum(self.numeros)


def main():
    try:
        estatisticas = EstatisticasConjunto()
        estatisticas.obter_numeros()

        menor = estatisticas.calcular_menor_valor()
        maior = estatisticas.calcular_maior_valor()
        soma = estatisticas.calcular_soma_valores()

        print("Estatísticas do conjunto:")
        print(f"Menor valor: {menor}")
        print(f"Maior valor: {maior}")
        print(f"Soma dos valores: {soma}")

    except ValueError as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()
