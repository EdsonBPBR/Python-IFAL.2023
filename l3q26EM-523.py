#Lista de Exercício 3 - Questão 26
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.


class Candidato:
    def __init__(self, nome):
        self.nome = nome
        self.votos = 0

    def adicionar_voto(self):
        self.votos += 1


class Eleicao:
    def __init__(self):
        self.candidatos = {}

    def adicionar_candidato(self, numero, nome):
        if numero in self.candidatos:
            raise ValueError("Número de candidato já existe.")
        candidato = Candidato(nome)
        self.candidatos[numero] = candidato

    def votar(self, numero_candidato):
        if numero_candidato not in self.candidatos:
            raise ValueError("Candidato inválido.")
        candidato = self.candidatos[numero_candidato]
        candidato.adicionar_voto()

    def exibir_resultados(self):
        print("Resultados da eleição:")
        for candidato in self.candidatos.values():
            print("{}: {} voto(s)".format(candidato.nome, candidato.votos))


def main():
    eleicao = Eleicao()

    try:
        n = int(input("Digite o número total de eleitores: "))
        for i in range(n):
            print("Eleitor", i+1)
            candidato = int(input("Digite o número do candidato: "))
            eleicao.votar(candidato)

        eleicao.exibir_resultados()

    except ValueError as e:
        print("Erro:", str(e))

if __name__ == "__main__":
    main()

