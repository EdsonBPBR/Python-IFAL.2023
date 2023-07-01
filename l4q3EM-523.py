#Lista de Exercício 4 - Questão 3
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda
#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

def main():
    notas = []
    for i in range(4):
        try:
            nota = float(input("Digite a nota: "))
            notas.append(nota)
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            return

    print("Notas:")
    for nota in notas:
        print(nota)

    media = calcular_media(notas)
    print("Média: ", media)

if __name__ == '__main__':
    main()