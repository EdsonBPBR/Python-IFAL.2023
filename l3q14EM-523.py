#Lista de Exercício 3 - Questão 14
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

class ParImparCounter:
    def __init__(self):
        self.numeros = []

    def obter_numeros(self):
        for i in range(10):
            try:
                numero = int(input(f"Digite o {i+1}º número inteiro: "))
                self.numeros.append(numero)
            except ValueError:
                print("Erro: Valor inválido. Digite um número inteiro.")

    def contar_pares_impares(self):
        pares = 0
        impares = 0

        for numero in self.numeros:
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1

        return pares, impares


def main():
    counter = ParImparCounter()
    counter.obter_numeros()

    pares, impares = counter.contar_pares_impares()
    print(f"A quantidade de números pares é: {pares}")
    print(f"A quantidade de números ímpares é: {impares}")


if __name__ == "__main__":
    main()
