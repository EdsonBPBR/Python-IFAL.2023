#Lista de Exercício 3 - Questão 23
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
class PrimoChecker:
    def verificar_numero_primo(self, numero):
        if numero < 2:
            return False

        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False

        return True


def encontrar_primos(n):
    primo_checker = PrimoChecker()
    primos = []
    num_divisoes = 0

    for numero in range(2, n + 1):
        if primo_checker.verificar_numero_primo(numero):
            primos.append(numero)
        num_divisoes += 1

    return primos, num_divisoes


def main():
    try:
        n = int(input("Digite um número inteiro: "))

        primos, num_divisoes = encontrar_primos(n)

        print(f"Os números primos até {n} são: {primos}")
        print(f"Total de divisões realizadas: {num_divisoes}")

    except ValueError:
        print("Valor inválido. Digite um número inteiro válido.")


if __name__ == "__main__":
    main()
