
#Lista de Exercício 4 - Questão 12
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


class Aluno:
    def __init__(self, idade, altura):
        self.idade = idade
        self.altura = altura


def contar_alunos(alunos):
    # Contadores para alunos com mais de 13 anos e altura inferior à média
    count = 0

    # Calculando a média de altura dos alunos com mais de 13 anos
    total_altura = 0
    qtd_alunos = 0
    for aluno in alunos:
        if aluno.idade > 13:
            total_altura += aluno.altura
            qtd_alunos += 1
    if qtd_alunos > 0:
        media_altura = total_altura / qtd_alunos
    else:
        media_altura = 0

    # Contando alunos com mais de 13 anos e altura inferior à média
    for aluno in alunos:
        if aluno.idade > 13 and aluno.altura < media_altura:
            count += 1

    return count


def main():
    try:
        # Inicializando lista de alunos
        alunos = []

        # Lendo as idades e alturas dos alunos
        for i in range(30):
            idade = int(input("Digite a idade do aluno {}: ".format(i + 1)))
            altura = float(input("Digite a altura do aluno {}: ".format(i + 1)))
            alunos.append(Aluno(idade, altura))

        # Chamando a função para contar os alunos com mais de 13 anos e altura inferior à média
        resultado = contar_alunos(alunos)
        print("Número de alunos com mais de 13 anos e altura inferior à média:", resultado)
    except ValueError:
        print("Erro: Digite um valor válido para idade ou altura.")
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print("Ocorreu um erro:", e)


if __name__ == "__main__":
    main()
