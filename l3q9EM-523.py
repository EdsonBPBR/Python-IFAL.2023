#Lista de Exercício 3 - Questão 9
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

class ImparesPrinter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def imprimir_impares(self):
        try:
            for numero in range(self.start, self.end + 1):
                if numero % 2 != 0:
                    print(numero)
        except TypeError:
            print("Erro: Os valores fornecidos devem ser inteiros.")

def main():
    printer = ImparesPrinter(1, 50)
    printer.imprimir_impares()

if __name__ == "__main__":
    main()
