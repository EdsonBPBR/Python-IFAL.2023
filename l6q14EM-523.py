
#Lista de Exercício 6 - Questão 14
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.


class LeetTranslator:
    def __init__(self):
        self.letras = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}

    def translate(self, texto):
        leet_texto = ''

        for letra in texto:
            if letra.lower() in self.letras:
                leet_texto += self.letras[letra.lower()]
            else:
                leet_texto += letra

        return leet_texto


def main():
    translator = LeetTranslator()
    texto = input("Digite um texto: ")

    try:
        texto_leet = translator.translate(texto)
        print("Texto em Leet Speak:", texto_leet)
    except Exception as e:
        print("Ocorreu um erro:", str(e))


if __name__ == '__main__':
    main()
