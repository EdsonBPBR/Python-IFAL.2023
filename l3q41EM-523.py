#Lista de Exercício 3 - Questão 41
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#   Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#1       0
#3       10
#6       15
#9       20
#12      25
#Exemplo de saída do programa:
#Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#R$ 1.000,00     0               1                       R$  1.000,00
#R$ 1.100,00     100             3                       R$    366,00
#R$ 1.150,00     150             6                       R$    191,67


class Divida:
    def __init__(self, valor):
        self.valor_divida = valor

    def calcular_parcelas(self):
        tabela = []
        parcelas = [
            {"quantidade": 1, "juros": 0},
            {"quantidade": 3, "juros": 10},
            {"quantidade": 6, "juros": 15},
            {"quantidade": 9, "juros": 20},
            {"quantidade": 12, "juros": 25}
        ]

        for parcela in parcelas:
            quantidade_parcelas = parcela["quantidade"]
            percentual_juros = parcela["juros"]
            valor_juros = (self.valor_divida * percentual_juros) / 100
            valor_total = self.valor_divida + valor_juros
            valor_parcela = valor_total / quantidade_parcelas

            tabela.append({
                "Valor da Dívida": f"R$ {valor_total:.2f}",
                "Valor dos Juros": f"R$ {valor_juros:.2f}",
                "Quantidade de Parcelas": quantidade_parcelas,
                "Valor da Parcela": f"R$ {valor_parcela:.2f}"
            })

        return tabela


def obter_valor_divida():
    while True:
        try:
            valor = float(input("Digite o valor da dívida: R$ "))
            if valor <= 0:
                print("O valor da dívida deve ser maior que zero.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Digite um número válido.")


def exibir_tabela(tabela):
    print("Valor da Dívida\tValor dos Juros\tQuantidade de Parcelas\tValor da Parcela")

    for linha in tabela:
        print(f"{linha['Valor da Dívida']}\t{linha['Valor dos Juros']}\t\t\t{linha['Quantidade de Parcelas']}\t\t\t\t{linha['Valor da Parcela']}")


def main():
    valor_divida = obter_valor_divida()
    divida = Divida(valor_divida)
    tabela_parcelas = divida.calcular_parcelas()
    exibir_tabela(tabela_parcelas)


if __name__ == "__main__":
    main()
