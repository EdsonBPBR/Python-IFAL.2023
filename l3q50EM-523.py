
#Lista de Exercício 3 - Questão 50
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

class CalculadoraH:
    def __init__(self, n):
        self.n = n

    def calcular_h(self):
        soma = 0
        for i in range(1, self.n + 1):
            soma += 1 / i
        return soma


def obter_valor_n():
    while True:
        try:
            n = int(input("Digite o valor de N: "))
            if n > 0:
                return n
            else:
                print("O valor de N deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")


def main():
    n = obter_valor_n()
    calculadora = CalculadoraH(n)
    valor_h = calculadora.calcular_h()
    print(f"O valor de H com {n} termos é: {valor_h}")


if __name__ == "__main__":
    main()
