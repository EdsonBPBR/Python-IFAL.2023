#Lista de Exercício 6 - Questão 2
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda


#Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.



class NameReverser:
    def __init__(self):
        self.name = ""

    def get_name(self):
        self.name = input("Digite o seu nome: ")

    def reverse_name(self):
        try:
            reversed_name = self.name[::-1].upper()
            return reversed_name
        except Exception as e:
            print("Ocorreu um erro:", e)

if __name__ == "__main__":
    reverser = NameReverser()
    reverser.get_name()
    reversed_name = reverser.reverse_name()
    if reversed_name:
        print("Nome ao contrário em maiúsculas:", reversed_name)
