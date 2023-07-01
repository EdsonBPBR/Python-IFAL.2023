#Lista de Exercício 2 - Questão 22
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda


#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

class Paridade:
    def __init__(self, numero):
        self.numero = numero

    def verificar_paridade(self):
        if self.numero % 2 == 0:
            return "par"
        else:
            return "ímpar"


def main():
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
    else:
        paridade = Paridade(numero)
        resultado = paridade.verificar_paridade()
        print(f"O número é {resultado}.")


main()
