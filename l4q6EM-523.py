#Lista de Exercício 4 - Questão 6
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda
#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

def main():
    medias = []
    alunos_aprovados = 0

    for i in range(10):
        notas = []
        for j in range(4):
            try:
                nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
                notas.append(nota)
            except ValueError:
                print("Entrada inválida. Digite apenas números.")
                return

        media_aluno = calcular_media(notas)
        medias.append(media_aluno)

        if media_aluno >= 7.0:
            alunos_aprovados += 1

    print("Médias dos alunos:", medias)
    print("Número de alunos com média maior ou igual a 7.0:", alunos_aprovados)


if __name__ == '__main__':
    main()
