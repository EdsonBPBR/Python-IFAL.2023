#Lista de Exercício 4 - Questão 10
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda
def main():
    vetor1 = []
    vetor2 = []
    vetor3 = []

    print("Digite os elementos do primeiro vetor:")
    for i in range(10):
        try:
            num = int(input("Elemento {}: ".format(i+1)))
            vetor1.append(num)
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")
            return

    print("Digite os elementos do segundo vetor:")
    for i in range(10):
        try:
            num = int(input("Elemento {}: ".format(i+1)))
            vetor2.append(num)
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")
            return

    for i in range(10):
        vetor3.append(vetor1[i])
        vetor3.append(vetor2[i])

    print("Vetor 1:", vetor1)
    print("Vetor 2:", vetor2)
    print("Vetor 3 (intercalado):", vetor3)


if __name__ == '__main__':
    main()
