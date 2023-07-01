#Lista de Exercício 2 - Questão 20
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#a.A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#b.A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#c.A mensagem "Aprovado com Distinção", se a média for igual a 10.

class Aluno:
    def __init__(self):
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        total = sum(self.notas)
        media = total / len(self.notas)
        return media

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media == 10:
            return "Aprovado com Distinção"
        elif media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


def ler_notas():
    aluno = Aluno()
    for i in range(3):
        nota = ler_nota(i + 1)
        aluno.adicionar_nota(nota)
    return aluno


def ler_nota(numero):
    while True:
        try:
            nota = float(input(f"Digite a nota {numero}: "))
            if nota < 0 or nota > 10:
                raise ValueError("Valor inválido. Digite uma nota entre 0 e 10.")
            return nota
        except ValueError as e:
            print(f"Erro: {str(e)}")


def exibir_resultado(media_aluno, situacao):
    print(f"Média alcançada: {media_aluno:.2f}")
    print(f"Situação do aluno: {situacao}")


aluno = ler_notas()
media_aluno = aluno.calcular_media()
situacao_aluno = aluno.verificar_aprovacao()
exibir_resultado(media_aluno, situacao_aluno)
