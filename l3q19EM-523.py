#Lista de Exercício 3 - Questão 19
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.


class EstatisticasConjunto:
    def __init__(self):
        self.numeros = []

    def obter_quantidade_numeros(self):
        try:
            n = int(input("Digite a quantidade de números no conjunto: "))

            if n < 0:
                raise ValueError("A quantidade de números deve ser um valor não negativo.")

            return n
        except ValueError as e:
            raise ValueError("Valor inválido. Digite um número válido.")

    def obter_numeros(self, n):
        try:
            for i in range(n):
                numero = float(input(f"Digite o {i + 1}º número: "))

                if numero < 0 or numero > 1000:
                    raise ValueError("Valor fora da faixa permitida. Digite um número entre 0 e 1000.")

                self.numeros.append(numero)
        except ValueError as e:
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

        n = estatisticas.obter_quantidade_numeros()
        estatisticas.obter_numeros(n)

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
