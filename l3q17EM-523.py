#Lista de Exercício 3 - Questão 17
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

class FatorialCalculator:
    def __init__(self):
        self.n = 0

    def obter_numero(self):
        try:
            self.n = int(input("Digite um número inteiro para calcular o fatorial: "))

            if self.n < 0:
                raise ValueError("O número deve ser não negativo.")
        except ValueError as e:
            print("Erro:", e)

    def calcular_fatorial(self):
        fatorial = 1

        for i in range(1, self.n + 1):
            fatorial *= i

        return fatorial


def main():
    calculator = FatorialCalculator()
    calculator.obter_numero()

    resultado = calculator.calcular_fatorial()
    print(f"O fatorial de {calculator.n} é: {resultado}")


if __name__ == "__main__":
    main()
