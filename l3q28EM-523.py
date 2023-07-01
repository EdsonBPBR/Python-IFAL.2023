#Lista de Exercício 3 - Questão 28
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda


#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.


class CD:
    def __init__(self, valor):
        self.valor = valor


class ColecaoCDs:
    def __init__(self):
        self.cds = []

    def adicionar_cd(self, cd):
        self.cds.append(cd)

    def calcular_valor_total(self):
        valor_total = 0
        for cd in self.cds:
            valor_total += cd.valor
        return valor_total

    def calcular_valor_medio(self):
        quantidade_cds = len(self.cds)
        if quantidade_cds == 0:
            return 0
        valor_total = self.calcular_valor_total()
        return valor_total / quantidade_cds


def obter_quantidade_cds():
    while True:
        try:
            quantidade_cds = int(input("Informe a quantidade de CDs na coleção: "))
            if quantidade_cds < 0:
                raise ValueError
            return quantidade_cds
        except ValueError:
            print("Quantidade inválida. Digite um número inteiro positivo.")


def obter_valor_cd(numero_cd):
    while True:
        try:
            valor_cd = float(input(f"Informe o valor gasto no CD {numero_cd}: "))
            if valor_cd < 0:
                raise ValueError
            return valor_cd
        except ValueError:
            print("Valor inválido. Digite um número positivo.")


def main():
    colecao = ColecaoCDs()
    quantidade_cds = obter_quantidade_cds()

    for i in range(quantidade_cds):
        valor_cd = obter_valor_cd(i + 1)
        cd = CD(valor_cd)
        colecao.adicionar_cd(cd)

    valor_total = colecao.calcular_valor_total()
    valor_medio = colecao.calcular_valor_medio()

    print(f"O valor total investido na coleção é R$ {valor_total:.2f}")
    print(f"O valor médio gasto em cada CD é R$ {valor_medio:.2f}")


if __name__ == "__main__":
    main()
