#Lista de Exercício 4 - Questão 2
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.



def ler_vetor():
    vetor = []
    for i in range(10):
        try:
            num = float(input("Digite um número real: "))
            vetor.append(num)
        except ValueError:
            print("Entrada inválida. Digite apenas números reais.")
            return None
    return vetor

def mostrar_vetor_inverso(vetor):
    if vetor is not None:
        print("Vetor na ordem inversa:")
        for num in reversed(vetor):
            print(num)

def main():
    vetor = ler_vetor()
    mostrar_vetor_inverso(vetor)


if __name__ == '__main__':
    main()