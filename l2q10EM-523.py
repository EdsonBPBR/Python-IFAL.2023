#Lista de Exercício 2 - Questão 10
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


class Saudacao:
    def __init__(self, turno):
        self.turno = turno.lower()

    def obter_saudacao(self):
        if self.turno == "m":
            return "Bom Dia!"
        elif self.turno == "v":
            return "Boa Tarde!"
        elif self.turno == "n":
            return "Boa Noite!"
        else:
            raise ValueError("Valor Inválido!")

try:
    turno = input("Em que turno você estuda? Digite M para Matutino, V para Vespertino ou N para Noturno: ")

    saudacao = Saudacao(turno)
    mensagem = saudacao.obter_saudacao()
    print(mensagem)

except ValueError as e:
    print(f"Erro: {e}")

