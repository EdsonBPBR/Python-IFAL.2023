#Lista de Exercício 3 - Questão 39
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

class Aluno:
    def __init__(self, numero, altura):
        self.numero = numero
        self.altura = altura


def ler_alunos():
    alunos = []

    for i in range(1, 11):
        while True:
            try:
                numero = int(input(f"Digite o número do {i}º aluno: "))
                altura = float(input(f"Digite a altura do {i}º aluno em centímetros: "))
                aluno = Aluno(numero, altura)
                alunos.append(aluno)
                break
            except ValueError:
                print("Erro: Insira valores numéricos válidos.")

    return alunos


def obter_aluno_mais_alto(alunos):
    aluno_mais_alto = max(alunos, key=lambda a: a.altura)
    return aluno_mais_alto


def obter_aluno_mais_baixo(alunos):
    aluno_mais_baixo = min(alunos, key=lambda a: a.altura)
    return aluno_mais_baixo


def exibir_aluno(aluno, posicao):
    print(f"Aluno {posicao}:")
    print(f"Número do aluno: {aluno.numero}, Altura: {aluno.altura} cm")


alunos = ler_alunos()

aluno_mais_alto = obter_aluno_mais_alto(alunos)
aluno_mais_baixo = obter_aluno_mais_baixo(alunos)

exibir_aluno(aluno_mais_alto, "mais alto")
exibir_aluno(aluno_mais_baixo, "mais baixo")
