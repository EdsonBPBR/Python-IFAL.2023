#Lista de Exercício 3 - Questão 16
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

class FibonacciGenerator:
    def __init__(self):
        self.fibonacci = [0, 1]

    def gerar_fibonacci(self):
        i = 2

        while self.fibonacci[i - 1] + self.fibonacci[i - 2] <= 500:
            self.fibonacci.append(self.fibonacci[i - 1] + self.fibonacci[i - 2])
            i += 1

    def obter_serie_fibonacci(self):
        return self.fibonacci


def main():
    generator = FibonacciGenerator()
    generator.gerar_fibonacci()

    resultado = generator.obter_serie_fibonacci()
    print("A série de Fibonacci até que o valor seja maior que 500:")
    print(resultado)


if __name__ == "__main__":
    main()
