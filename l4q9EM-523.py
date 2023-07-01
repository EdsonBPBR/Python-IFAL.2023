#Lista de Exercício 4 - Questão 9
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda
#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
def main():
    vetor = []
    for i in range(10):
        try:
            num = int(input("Digite um número inteiro: "))
            vetor.append(num)
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")
            return

    soma_quadrados = sum([num**2 for num in vetor])

    print("Vetor A:", vetor)
    print("Soma dos quadrados dos elementos:", soma_quadrados)


if __name__ == '__main__':
    main()
