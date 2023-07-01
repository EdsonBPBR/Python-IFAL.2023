#Lista de Exercício 4 - Questão 8
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda
#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

def main():
    idades = []
    alturas = []

    for i in range(5):
        try:
            idade = int(input("Digite a idade da pessoa: "))
            altura = float(input("Digite a altura da pessoa: "))
            idades.append(idade)
            alturas.append(altura)
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            return

    print("Idades (em ordem inversa):", idades[::-1])
    print("Alturas (em ordem inversa):", alturas[::-1])


if __name__ == '__main__':
    main()


