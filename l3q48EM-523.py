#Lista de Exercício 3 - Questão 48
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
#Exemplo:
#  12376489
#  => 98467321


class NumeroInvertido:
    def __init__(self, numero):
        self.numero = numero

    def inverter(self):
        numero_str = str(self.numero)
        numero_invertido_str = numero_str[::-1]
        numero_invertido = int(numero_invertido_str)
        return numero_invertido


def obter_numero():
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo: "))
            if numero > 0:
                return numero
            else:
                print("O número deve ser positivo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")


def main():
    numero = obter_numero()
    numero_obj = NumeroInvertido(numero)
    numero_invertido = numero_obj.inverter()
    print(f"O número invertido é: {numero_invertido}")


if __name__ == "__main__":
    main()
