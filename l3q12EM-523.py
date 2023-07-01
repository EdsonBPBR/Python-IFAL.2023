#Lista de Exercício 3 - Questão 12
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50

class TabuadaGenerator:
    def __init__(self):
        self.numero = 0

    def obter_numero(self):
        try:
            self.numero = int(input("Digite um número inteiro entre 1 e 10: "))
        except ValueError:
            print("Erro: Valor inválido. Digite um número inteiro.")

    def gerar_tabuada(self):
        print(f"Tabuada de {self.numero}:")
        for i in range(1, 11):
            resultado = self.numero * i
            print(f"{self.numero} X {i} = {resultado}")


def main():
    tabuada_gen = TabuadaGenerator()
    tabuada_gen.obter_numero()

    if 1 <= tabuada_gen.numero <= 10:
        tabuada_gen.gerar_tabuada()
    else:
        print("Erro: O número deve estar entre 1 e 10.")


if __name__ == "__main__":
    main()

