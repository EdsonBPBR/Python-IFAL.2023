#Lista de Exercício 3 - Questão 24
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda


#Faça um programa que calcule o mostre a média aritmética de N notas.

class CalculadoraMedia:
    def calcular_media_notas(self, n):
        soma = 0

        for i in range(n):
            nota = float(input(f"Digite a nota {i + 1}: "))
            soma += nota

        media = soma / n
        return media


def main():
    try:
        n = int(input("Digite a quantidade de notas: "))

        if n <= 0:
            print("A quantidade de notas deve ser maior que zero.")
            return

        calculadora = CalculadoraMedia()
        media = calculadora.calcular_media_notas(n)
        print(f"A média das {n} notas é: {media}")

    except ValueError:
        print("Valor inválido. Digite um número inteiro válido.")


if __name__ == "__main__":
    main()

