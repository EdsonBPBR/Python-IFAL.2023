# Lista de Exercício 3 - Questão 10
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

class IntervaloNumeros:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def gerar_numeros_intervalo(self):
        try:
            if self.inicio <= self.fim:
                numeros = range(self.inicio, self.fim + 1)
            else:
                numeros = range(self.inicio, self.fim - 1, -1)

            for numero in numeros:
                print(numero)
        except TypeError:
            print("Erro: Os valores fornecidos devem ser inteiros.")


def main():
    try:
        inicio = int(input("Digite o número de início do intervalo: "))
        fim = int(input("Digite o número de fim do intervalo: "))

        intervalo = IntervaloNumeros(inicio, fim)
        intervalo.gerar_numeros_intervalo()
    except ValueError:
        print("Erro: Os valores fornecidos devem ser inteiros.")


if __name__ == "__main__":
    main()
