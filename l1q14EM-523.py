#Lista de Exercício 1 - Questão 14
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

class Pescador:
    def __init__(self, peso_limite, valor_multa):
        self.peso_limite = peso_limite
        self.valor_multa = valor_multa

    def calcular_multa_excesso_peso(self, peso):
        if peso > self.peso_limite:
            excesso = peso - self.peso_limite
            multa = excesso * self.valor_multa
        else:
            excesso = 0
            multa = 0
        return excesso, multa

    def obter_peso_peixes(self):
        while True:
            try:
                peso = float(input("Digite o peso dos peixes em quilos: "))
                return peso
            except ValueError:
                print("Erro: O peso deve ser um valor numérico válido.")

    def exibir_resultado(self, peso, excesso, multa):
        print("Peso dos peixes:", peso, "quilos")
        print("Excesso de peso:", excesso, "quilos")
        print("Multa a ser paga: R$", multa)

    def executar(self):
        peso = self.obter_peso_peixes()
        excesso, multa = self.calcular_multa_excesso_peso(peso)
        self.exibir_resultado(peso, excesso, multa)


def main():
    peso_limite = 50  # Limite de peso estabelecido em 50 quilos
    valor_multa = 4.00  # Valor da multa por quilo excedente

    pescador = Pescador(peso_limite, valor_multa)
    pescador.executar()


if __name__ == '__main__':
    main()
