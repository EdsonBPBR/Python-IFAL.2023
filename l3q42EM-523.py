#Lista de Exercício 3 - Questão 42
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

class ContadorIntervalos:
    def __init__(self):
        self.intervalos = {
            "0-25": 0,
            "26-50": 0,
            "51-75": 0,
            "76-100": 0
        }

    def adicionar_numero(self, numero):
        if 0 <= numero <= 25:
            self.intervalos["0-25"] += 1
        elif 26 <= numero <= 50:
            self.intervalos["26-50"] += 1
        elif 51 <= numero <= 75:
            self.intervalos["51-75"] += 1
        elif 76 <= numero <= 100:
            self.intervalos["76-100"] += 1

    def contar_intervalos(self):
        while True:
            try:
                numero = int(input("Digite um número positivo (ou um número negativo para encerrar): "))
                if numero < 0:
                    break
                self.adicionar_numero(numero)
            except ValueError:
                print("Valor inválido. Digite um número inteiro válido.")

    def exibir_resultado(self):
        print("\nResultados:")
        for intervalo, quantidade in self.intervalos.items():
            print(f"{intervalo}: {quantidade}")


def main():
    contador = ContadorIntervalos()
    contador.contar_intervalos()
    contador.exibir_resultado()


if __name__ == "__main__":
    main()

