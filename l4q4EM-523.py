#Lista de Exercício 4 - Questão 4
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda
#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes #foram lidas. Imprima as consoantes.


def contar_consoantes(vetor):
    consoantes = 0
    consoantes_list = []
    for char in vetor:
        if char.isalpha() and char.lower() not in 'aeiou':
            consoantes += 1
            consoantes_list.append(char)
    return consoantes, consoantes_list

def main():
    vetor = []
    for i in range(10):
        char = input("Digite um caractere: ")
        vetor.append(char)

    total_consoantes, consoantes_list = contar_consoantes(vetor)

    print("Consoantes encontradas:")
    for char in consoantes_list:
        print(char)

    print("Total de consoantes: ", total_consoantes)


if __name__ == '__main__':
    main()
