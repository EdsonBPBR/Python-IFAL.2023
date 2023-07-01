
#Lista de Exercício 5 - Questão 4
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.


class VerificarPositivoNegativo:
    def __init__(self):
        self.numero = 0

    def obter_numero(self):
        while True:
            try:
                self.numero = float(input("Digite um número: "))
                break
            except ValueError:
                print("Por favor, digite um número válido.")

    def verificar(self):
        if self.numero > 0:
            return 'P'
        elif self.numero <= 0:
            return 'N'


def executar_programa():
    verificador = VerificarPositivoNegativo()
    verificador.obter_numero()
    resultado = verificador.verificar()
    print("O valor é:", resultado)


executar_programa()
