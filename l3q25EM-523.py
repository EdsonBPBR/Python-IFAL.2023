#Lista de Exercício 3 - Questão 25
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda


#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada

class Turma:
    def __init__(self):
        self.idades = []

    def adicionar_idade(self, idade):
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        self.idades.append(idade)

    def calcular_media(self):
        if not self.idades:
            raise ValueError("A lista de idades está vazia.")
        soma = sum(self.idades)
        media = soma / len(self.idades)
        return media

    def verificar_faixa_etaria(self, media):
        if media >= 0 and media <= 25:
            return "jovem"
        elif media >= 26 and media <= 60:
            return "adulta"
        else:
            return "idosa"


def main():
    turma = Turma()
    try:
        n = int(input("Quantas pessoas na turma? "))
        for i in range(n):
            idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
            turma.adicionar_idade(idade)

        media = turma.calcular_media()
        faixa_etaria = turma.verificar_faixa_etaria(media)

        print("A média de idade da turma é: {:.2f}".format(media))
        print("A turma é considerada", faixa_etaria)

    except ValueError as e:
        print("Erro:", str(e))

if __name__ == "__main__":
    main()
