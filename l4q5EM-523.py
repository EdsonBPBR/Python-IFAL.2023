#Lista de Exercício 4 - Questão 5
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda
#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

def separar_numeros_pares_impares(vetor):
    par = []
    impar = []
    for num in vetor:
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    return par, impar

def main():
    vetor = []
    for i in range(20):
        try:
            num = int(input("Digite um número inteiro: "))
            vetor.append(num)
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")
            return

    numeros_pares, numeros_impares = separar_numeros_pares_impares(vetor)

    print("Vetor completo:", vetor)
    print("Números pares:", numeros_pares)
    print("Números ímpares:", numeros_impares)


if __name__ == '__main__':
    main()
