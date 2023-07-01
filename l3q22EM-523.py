
#Lista de Exercício 3 - Questão 22
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.



class PrimoChecker:
    def verificar_numero_primo(self, numero):
        if numero < 2:
            return False

        divisores = []
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                divisores.append(i)

        if divisores:
            return divisores
        else:
            return True


def main():
    primo_checker = PrimoChecker()

    while True:
        try:
            numero = int(input("Digite um número inteiro (ou digite 0 para sair): "))

            if numero == 0:
                break

            resultado = primo_checker.verificar_numero_primo(numero)
            if resultado is True:
                print(f"{numero} é um número primo.")
            else:
                divisores = ', '.join(map(str, resultado))
                print(f"{numero} não é um número primo. É divisível por: {divisores}.")

        except ValueError:
            print("Valor inválido. Digite um número inteiro válido.")


if __name__ == "__main__":
    main()
