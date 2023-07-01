# Lista de Exercício 6 - Questão 8
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.


def is_palindrome(string):
    # Remove espaços e pontuação da string
    string = "".join(char.lower() for char in string if char.isalnum())

    # Verifica se a string é igual à sua versão invertida
    if string == string[::-1]:
        return True
    else:
        return False


def main():
    sequence = input("Digite uma sequência de caracteres: ")
    if is_palindrome(sequence):
        print("A sequência é um palíndromo.")
    else:
        print("A sequência não é um palíndromo.")


if __name__ == "__main__":
    main()
