#Lista de Exercício 3 - Questão 7
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda


#Faça um programa que leia 5 números e informe o maior número.

class MaiorNumeroFinder:
    def __init__(self):
        self.numeros = []

    def ler_numeros(self):
        for i in range(5):
            while True:
                try:
                    numero = float(input("Digite um número: "))
                    self.numeros.append(numero)
                    break

                except ValueError:
                    print("Erro: Entrada inválida. Digite um número válido.")

    def encontrar_maior_numero(self):
        if not self.numeros:
            return None

        return max(self.numeros)


def executar_programa():
    finder = MaiorNumeroFinder()

    finder.ler_numeros()

    maior_numero = finder.encontrar_maior_numero()
    if maior_numero is not None:
        print("O maior número é:", maior_numero)
    else:
        print("Nenhum número foi inserido.")


executar_programa()
