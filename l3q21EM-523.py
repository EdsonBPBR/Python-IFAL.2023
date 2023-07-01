#Lista de Exercício 3 - Questão 21
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda


#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

class PrimoChecker:
    def verificar_numero_primo(self, numero):
        if numero < 2:
            return False

        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False

        return True


def main():
    primo_checker = PrimoChecker()

    while True:
        try:
            numero = int(input("Digite um número inteiro (ou digite 0 para sair): "))

            if numero == 0:
                break

            if primo_checker.verificar_numero_primo(numero):
                print(f"{numero} é um número primo.")
            else:
                print(f"{numero} não é um número primo.")

        except ValueError:
            print("Valor inválido. Digite um número inteiro válido.")


if __name__ == "__main__":
    main()

