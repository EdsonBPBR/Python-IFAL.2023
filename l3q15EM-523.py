#Lista de Exercício 3 - Questão 15
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

class FibonacciGenerator:
    def __init__(self):
        self.n = 0

    def obter_n(self):
        try:
            self.n = int(input("Digite o valor de n para gerar a série de Fibonacci: "))

            if self.n <= 0:
                raise ValueError("O valor de n deve ser maior que zero.")
        except ValueError as e:
            print("Erro:", e)

    def gerar_fibonacci(self):
        fibonacci = [1, 1]




        for i in range(2, self.n):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci


def main():
    generator = FibonacciGenerator()
    generator.obter_n()

    resultado = generator.gerar_fibonacci()
    print(f"A série de Fibonacci até o {generator.n}º termo é: {resultado}")


if __name__ == "__main__":
    main()
