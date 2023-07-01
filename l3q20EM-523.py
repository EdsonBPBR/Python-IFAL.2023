# Lista de Exercício 3 - Questão 20
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

class FatorialCalculator:
    def calcular_fatorial(self, n):
        if n < 0 or n > 15:
            raise ValueError("O número deve ser um inteiro positivo menor que 16.")

        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i

        return fatorial


def main():
    fatorial_calculator = FatorialCalculator()

    while True:
        try:
            numero = int(input(
                "Digite um número inteiro positivo (menor que 16) para calcular o fatorial (ou digite 0 para sair): "))

            if numero == 0:
                break

            resultado = fatorial_calculator.calcular_fatorial(numero)
            print(f"O fatorial de {numero} é: {resultado}\n")

        except ValueError as e:
            print("Erro:", e)


if __name__ == "__main__":
    main()
