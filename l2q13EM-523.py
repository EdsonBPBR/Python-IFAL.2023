
#Lista de Exercício 2 - Questão 13
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

class DiaSemana:
    def __init__(self):
        self.dias_semana = {
            1: "Domingo",
            2: "Segunda",
            3: "Terça",
            4: "Quarta",
            5: "Quinta",
            6: "Sexta",
            7: "Sábado"
        }

    def obter_dia_semana(self, numero):
        try:
            return self.dias_semana[numero]
        except KeyError:
            return "Valor inválido"

    def ler_numero(self):
        while True:
            try:
                numero = int(input("Digite um número de 1 a 7: "))
                return numero
            except ValueError:
                print("Valor inválido! Digite um número inteiro.")

    def exibir_dia_semana(self, numero):
        dia_semana = self.obter_dia_semana(numero)
        print(dia_semana)

dia_semana = DiaSemana()
numero = dia_semana.ler_numero()
dia_semana.exibir_dia_semana(numero)
