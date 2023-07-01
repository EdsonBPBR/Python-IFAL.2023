
#Lista de Exercício 6 - Questão 11
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

#Digite uma letra: A
#-> Você errou pela 1ª vez. Tente de novo!

#Digite uma letra: O
#A palavra é: _ _ _ _ O

#Digite uma letra: E
#A palavra é: _ E _ _ O

#Digite uma letra: S
#-> Você errou pela 2ª vez. Tente de novo!


import random

class JogoForca:
    def __init__(self, palavras):
        self.palavras = palavras
        self.palavra_secreta = self.selecionar_palavra()
        self.letras_certas = []
        self.letras_erradas = []
        self.tentativas_restantes = 6

    def selecionar_palavra(self):
        return random.choice(self.palavras)

    def exibir_palavra(self):
        palavra_exibida = ""
        for letra in self.palavra_secreta:
            if letra in self.letras_certas:
                palavra_exibida += letra + " "
            else:
                palavra_exibida += "_ "
        return palavra_exibida

    def adivinhar_letra(self, letra):
        if letra in self.letras_certas or letra in self.letras_erradas:
            raise ValueError("Você já tentou essa letra. Tente outra.")
        elif letra in self.palavra_secreta:
            self.letras_certas.append(letra)
            print("Você acertou!")
        else:
            self.letras_erradas.append(letra)
            self.tentativas_restantes -= 1
            print(f"Você errou pela {7 - self.tentativas_restantes}ª vez.")

    def jogar(self):
        print("Jogo da Forca - Adivinhe a palavra!")
        print(f"A palavra possui {len(self.palavra_secreta)} letras.")
        print("Você pode errar no máximo 6 vezes.")

        while self.tentativas_restantes > 0:
            print("\nPalavra:", self.exibir_palavra())
            try:
                letra = input("Digite uma letra: ").upper()
                self.adivinhar_letra(letra)
            except ValueError as error:
                print("Erro:", str(error))

            if self.exibir_palavra().find("_") == -1:
                print("\nParabéns! Você adivinhou a palavra corretamente:", self.palavra_secreta)
                return

        print("\nVocê foi enforcado! A palavra correta era:", self.palavra_secreta)


def main():
    # Lista de palavras para o jogo
    palavras = ["PYTHON", "PROGRAMACAO", "FORCA", "JOGO", "COMPUTADOR", "OPENAI"]

    jogo = JogoForca(palavras)
    jogo.jogar()


if __name__ == "__main__":
    main()
