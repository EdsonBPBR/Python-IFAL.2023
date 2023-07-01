#Lista de Exercício 6 - Questão 3
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

#F
#U
#L
#A
#N
#O

class NomeVertical:
    def __init__(self):
        self.nome = ""

    def obter_nome(self):
        self.nome = input("Digite o seu nome: ")

    def imprimir_vertical(self):
        try:
            for letra in self.nome:
                print(letra.upper())
        except TypeError:
            print("Erro: nome inválido.")


# Exemplo de uso
nome_vertical = NomeVertical()
nome_vertical.obter_nome()
nome_vertical.imprimir_vertical()

