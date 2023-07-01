#Lista de Exercício 3 - Questão 47
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Aparecido Parente
#Nota: 9.9
#Nota: 7.5
#Nota: 9.5
#Nota: 8.5
#Nota: 9.0
#Nota: 8.5
#Nota: 9.7

#Resultado final:
#Atleta: Aparecido Parente
#Melhor nota: 9.9
#Pior nota: 7.5
#Média: 9,04


class Ginasta:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        melhores_notas = sorted(self.notas)[1:-1]  # Remove a melhor e pior nota
        media = sum(melhores_notas) / len(melhores_notas)
        return media


def obter_notas(ginasta):
    for i in range(1, 8):
        while True:
            try:
                nota = float(input(f"Nota {i}: "))
                ginasta.adicionar_nota(nota)
                break
            except ValueError:
                print("Valor inválido! Digite novamente.")


def exibir_resultado_final(ginasta):
    media = ginasta.calcular_media()
    melhor_nota = max(ginasta.notas)
    pior_nota = min(ginasta.notas)

    print("\nResultado final:")
    print(f"Atleta: {ginasta.nome}")
    print(f"Melhor nota: {melhor_nota}")
    print(f"Pior nota: {pior_nota}")
    print(f"Média: {media:.2f}")


def main():
    ginastas = []

    while True:
        nome_ginasta = input("Atleta: ")
        if not nome_ginasta:
            break

        ginasta = Ginasta(nome_ginasta)
        obter_notas(ginasta)
        exibir_resultado_final(ginasta)

        ginastas.append(ginasta)

    print("\nRelatório de todos os ginastas:")
    for ginasta in ginastas:
        media = ginasta.calcular_media()
        print(f"Atleta: {ginasta.nome}")
        print(f"Média: {media:.2f}")
        print()

if __name__ == "__main__":
    main()

