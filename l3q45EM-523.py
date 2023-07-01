#Lista de Exercício 3 - Questão 45
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#a.Maior e Menor Acerto;
#b.Total de Alunos que utilizaram o sistema;
#c.A Média das Notas da Turma.
#Gabarito da Prova:

#01 - A
#02 - B
#03 - C
#04 - D
#05 - E
#06 - E
#07 - D
#08 - C
#09 - B
#10 - A
#Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.


class Aluno:
    def __init__(self):
        self.respostas = []
        self.acertos = 0

    def responder_questoes(self):
        for i in range(1, 11):
            resposta = input(f"Resposta da questão {i}: ")
            self.respostas.append(resposta.upper())

    def calcular_acertos(self, gabarito):
        for i in range(10):
            if self.respostas[i] == gabarito[i]:
                self.acertos += 1


def obter_gabarito():
    gabarito = []
    print("Digite as respostas do gabarito:")
    for i in range(1, 11):
        resposta = input(f"Resposta da questão {i}: ")
        gabarito.append(resposta.upper())
    return gabarito


def cadastrar_aluno():
    aluno = Aluno()
    aluno.responder_questoes()
    return aluno


def exibir_relatorio(alunos):
    total_alunos = len(alunos)
    maior_acerto = max(alunos, key=lambda x: x.acertos).acertos
    menor_acerto = min(alunos, key=lambda x: x.acertos).acertos
    soma_notas = sum(aluno.acertos for aluno in alunos)
    media_notas = soma_notas / total_alunos if total_alunos > 0 else 0

    print("\nRelatório Final:")
    print(f"Maior acerto: {maior_acerto}")
    print(f"Menor acerto: {menor_acerto}")
    print(f"Total de alunos: {total_alunos}")
    print(f"Média das notas: {media_notas:.2f}")


def main():
    alunos = []
    continuar = True
    gabarito = obter_gabarito()

    while continuar:
        try:
            aluno = cadastrar_aluno()
            aluno.calcular_acertos(gabarito)
            alunos.append(aluno)

            opcao = input("Deseja cadastrar outro aluno? (S/N): ")
            if opcao.upper() != "S":
                continuar = False

        except ValueError as ve:
            print(f"Erro: {ve}\n")

    exibir_relatorio(alunos)


if __name__ == "__main__":
    main()
