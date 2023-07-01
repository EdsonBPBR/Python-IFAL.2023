#Lista de Exercício 3 - Questão 6
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

class NumerosPrinter:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def imprimir_numeros_abaixo(self):
        for num in range(self.inicio, self.fim + 1):
            print(num)

    def imprimir_numeros_lado_a_lado(self):
        for num in range(self.inicio, self.fim + 1):
            print(num, end=' ')


def executar_programa():
    try:
        inicio = int(input("Informe o número de início: "))
        fim = int(input("Informe o número de fim: "))

        printer = NumerosPrinter(inicio, fim)

        print("Números abaixo um do outro:")
        printer.imprimir_numeros_abaixo()

        print("\nNúmeros lado a lado:")
        printer.imprimir_numeros_lado_a_lado()

    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de inserir números inteiros.")

    resposta = input("\nDeseja repetir o programa? (s/n): ")
    if resposta.lower() == "s":
        executar_programa()


executar_programa()

