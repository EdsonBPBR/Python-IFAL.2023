#Lista de Exercício 3 - Questão 49
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que mostre os n termos da Série a seguir:
  #S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
#Imprima no final a soma da série.


class SerieSoma:
    def __init__(self, n):
        self.n = n

    def calcular_serie(self):
        soma = 0
        m = 1

        for i in range(1, self.n + 1):
            termo = i / m
            soma += termo
            m += 2
            print(f"{i}/{m - 2}", end="")

            if i != self.n:
                print(" + ", end="")

        return soma


def obter_valor_n():
    while True:
        try:
            n = int(input("Digite o valor de n: "))
            if n > 0:
                return n
            else:
                print("O valor de n deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")


def main():
    n = obter_valor_n()
    serie = SerieSoma(n)
    soma_serie = serie.calcular_serie()
    print(f"\nA soma da série é: {soma_serie}")


if __name__ == "__main__":
    main()
