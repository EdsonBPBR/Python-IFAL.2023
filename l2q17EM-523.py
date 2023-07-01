#Lista de Exercício 2 - Questão 17
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

class AnoBissexto:
    def __init__(self, ano):
        self.ano = ano

    def eh_bissexto(self):
        if self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0):
            return True
        else:
            return False

    def verificar_ano(self):
        try:
            if self.ano < 0:
                raise ValueError("Ano inválido. Digite um valor positivo.")

            if self.eh_bissexto():
                print(self.ano, "é um ano bissexto.")
            else:
                print(self.ano, "não é um ano bissexto.")

        except ValueError as error:
            print("Erro:", str(error))


ano = int(input("Digite um ano: "))
verificador = AnoBissexto(ano)
verificador.verificar_ano()
