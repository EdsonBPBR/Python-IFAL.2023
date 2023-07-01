#Lista de Exercício 5 - Questão 10
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda



#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random

class CrapsGame:
    def __init__(self):
        self.ponto = None

    def lancar_dados(self):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        return dado1, dado2

    def jogar(self):
        dado1, dado2 = self.lancar_dados()
        soma_dados = dado1 + dado2
        print(f"Você lançou os dados: {dado1} + {dado2} = {soma_dados}")

        if self.ponto is None:
            if soma_dados == 7 or soma_dados == 11:
                print("Natural! Você ganhou!")
            elif soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
                print("Craps! Você perdeu!")
            else:
                self.ponto = soma_dados
                print(f"Ponto! Seu objetivo é fazer {self.ponto} novamente.")
        else:
            if soma_dados == self.ponto:
                print("Você fez o Ponto! Você ganhou!")
                self.ponto = None
            elif soma_dados == 7:
                print("Sete! Você perdeu!")
                self.ponto = None

def jogar_craps():
    jogo = CrapsGame()
    print("Bem-vindo ao jogo de Craps!")
    while True:
        escolha = input("Deseja jogar? (s/n): ")
        if escolha.lower() == 's':
            jogo.jogar()
        else:
            break

# Inicia o jogo de Craps
jogar_craps()
