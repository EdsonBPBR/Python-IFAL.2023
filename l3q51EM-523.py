#Lista de Exercício 3 - Questão 51
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que mostre os n termos da Série a seguir:
#S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
#Imprima no final a soma da série.

class Serie:
    def __init__(self):
        self.n = 0
        self.soma = 0

    def obter_valor_n(self):
        while True:
            try:
                self.n = int(input("Digite o valor de N: "))
                if self.n > 0:
                    break
                else:
                    print("O valor de N deve ser maior que zero. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Tente novamente.")

    def calcular_serie(self):
        m = 1

        for i in range(1, self.n + 1):
            self.soma += i / m
            m += 2

    def exibir_serie(self):
        print(f"A série com {self.n} termos é: {self.soma}")


def main():
    serie = Serie()
    serie.obter_valor_n()
    serie.calcular_serie()
    serie.exibir_serie()


if __name__ == "__main__":
    main()


