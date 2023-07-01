
#Lista de Exercício 6 - Questão 13
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.



import random

class JogoPalavraEmbaralhada:
    def __init__(self):
        self.palavras = ['casa', 'carro', 'computador', 'elefante', 'banana', 'abacaxi', 'girafa', 'telefone']
        self.tentativas = 6

    def escolher_palavra(self):
        return random.choice(self.palavras)

    def embaralhar_palavra(self, palavra):
        letras = list(palavra)
        random.shuffle(letras)
        return ''.join(letras)

    def jogar(self):
        palavra = self.escolher_palavra()
        palavra_embaralhada = self.embaralhar_palavra(palavra)

        print("Bem-vindo ao Jogo da Palavra Embaralhada!")
        print("Tente adivinhar a palavra correta. Você tem", self.tentativas, "tentativas.")

        while self.tentativas > 0:
            print("\nPalavra embaralhada:", palavra_embaralhada)
            resposta = input("Digite sua resposta: ")

            if resposta.lower() == palavra:
                print("Parabéns! Você acertou a palavra.")
                return

            print("Resposta incorreta!")
            self.tentativas -= 1
            print("Tentativas restantes:", self.tentativas)

        print("\nSuas tentativas acabaram!")
        print("A palavra correta era:", palavra)


def main():
    jogo = JogoPalavraEmbaralhada()
    jogo.jogar()


if __name__ == '__main__':
    main()

