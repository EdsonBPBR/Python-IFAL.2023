# Lista de Exercício 3 - Questão 11
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Altere o programa anterior para mostrar no final a soma dos números.


class IntervaloNumeros:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        self.soma = 0

    def gerar_numeros_intervalo(self):
        try:
            if self.inicio <= self.fim:
                numeros = range(self.inicio, self.fim + 1)
            else:
                numeros = range(self.inicio, self.fim - 1, -1)

            for numero in numeros:
                print(numero)
                self.soma += numero
        except TypeError:
            print("Erro: Os valores fornecidos devem ser inteiros.")

    def exibir_soma(self):
        print("A soma dos números no intervalo é:", self.soma)


def obter_valores_intervalo():
    try:
        inicio = int(input("Digite o número de início do intervalo: "))
        fim = int(input("Digite o número de fim do intervalo: "))
        return inicio, fim
    except ValueError:
        print("Erro: Os valores fornecidos devem ser inteiros.")
        return None, None


def main():
    inicio, fim = obter_valores_intervalo()

    if inicio is not None and fim is not None:
        intervalo = IntervaloNumeros(inicio, fim)
        intervalo.gerar_numeros_intervalo()
        intervalo.exibir_soma()


if __name__ == "__main__":
    main()
