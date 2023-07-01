#Lista de Exercício 3 - Questão 34
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

class NumeroPrimo:
    def __init__(self, numero):
        self.numero = numero

    def is_primo(self):
        if self.numero < 2:
            return False

        for i in range(2, int(self.numero ** 0.5) + 1):
            if self.numero % i == 0:
                return False

        return True


def main():
    try:
        numero = int(input("Digite um número inteiro: "))

        primo = NumeroPrimo(numero)
        if primo.is_primo():
            print(f"{numero} é um número primo.")
        else:
            print(f"{numero} não é um número primo.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro válido.")


if __name__ == "__main__":
    main()