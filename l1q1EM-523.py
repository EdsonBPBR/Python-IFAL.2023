#Lista de Exercício 1 - Questão 1
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda


#Faça um Programa que mostre a mensagem "Alo mundo" na tela.

class Mensagem:
    def __init__(self):
        self.mensagem = "Alo mundo"

    def exibir_mensagem(self):
        print(self.mensagem)

try:
    mensagem = Mensagem()
    mensagem.exibir_mensagem()
except Exception as error:
    print("Ocorreu um erro:", error)
