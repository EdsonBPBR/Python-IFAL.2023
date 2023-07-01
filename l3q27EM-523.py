#Lista de Exercício 3 - Questão 27
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

class Turma:
    def __init__(self):
        self.quantidade_alunos = 0

    def adicionar_alunos(self, quantidade):
        if quantidade <= 0 or quantidade > 40:
            raise ValueError("Quantidade inválida. A turma deve ter entre 1 e 40 alunos.")
        self.quantidade_alunos = quantidade

    def obter_quantidade_alunos(self):
        return self.quantidade_alunos


def calcular_media_alunos_por_turma():
    total_turmas = int(input("Digite a quantidade de turmas: "))
    total_alunos = 0

    for i in range(1, total_turmas + 1):
        turma = Turma()
        while True:
            try:
                quantidade_alunos = int(input("Digite a quantidade de alunos na turma {}: ".format(i)))
                turma.adicionar_alunos(quantidade_alunos)
                total_alunos += turma.obter_quantidade_alunos()
                break
            except ValueError as e:
                print("Erro:", str(e))

    media_alunos_por_turma = total_alunos / total_turmas
    return media_alunos_por_turma


media = calcular_media_alunos_por_turma()
print("A média de alunos por turma é: {:.2f}".format(media))

