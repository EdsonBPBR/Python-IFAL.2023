
#Lista de Exercício 4 - Questão 1
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
class VetorNumeros:
    def __init__(self):
        self.vetor = []

    def ler_vetor(self):
        try:
            for i in range(5):
                num = int(input("Digite um número inteiro: "))
                self.vetor.append(num)
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

    def mostrar_vetor(self):
        print("Números digitados:")
        for num in self.vetor:
            print(num)


def main():
    vetor = VetorNumeros()
    vetor.ler_vetor()
    vetor.mostrar_vetor()


if __name__ == '__main__':
    main()