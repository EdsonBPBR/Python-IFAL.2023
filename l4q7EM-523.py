#Lista de Exercício 4 - Questão 7
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda
#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
def main():
    vetor = []
    for i in range(5):
        try:
            num = int(input("Digite um número inteiro: "))
            vetor.append(num)
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")
            return

    soma = sum(vetor)
    multiplicacao = 1
    for num in vetor:
        multiplicacao *= num

    print("Números:", vetor)
    print("Soma:", soma)
    print("Multiplicação:", multiplicacao)


if __name__ == '__main__':
    main()

