#Lista de Exercício 2 - Questão 26
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#a.Álcool:
#b.até 20 litros, desconto de 3% por litro
#c.acima de 20 litros, desconto de 5% por litro
#d.Gasolina:
#e.até 20 litros, desconto de 4% por litro
#f.acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

class PostoCombustivel:
    def __init__(self):
        self.preco_alcool = 1.90
        self.preco_gasolina = 2.50

    def calcular_desconto(self, combustivel, litros):
        if combustivel == 'A':
            if litros <= 20:
                desconto = 0.03
            else:
                desconto = 0.05
        elif combustivel == 'G':
            if litros <= 20:
                desconto = 0.04
            else:
                desconto = 0.06
        else:
            raise ValueError("Combustível inválido.")

        return desconto

    def calcular_valor_a_pagar(self, combustivel, litros):
        if combustivel == 'A':
            preco_litro = self.preco_alcool
        elif combustivel == 'G':
            preco_litro = self.preco_gasolina
        else:
            raise ValueError("Combustível inválido.")

        desconto = self.calcular_desconto(combustivel, litros)
        valor_total = preco_litro * litros
        valor_desconto = valor_total * desconto
        valor_final = valor_total - valor_desconto
        return valor_final


def obter_input_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número válido.")


try:
    posto = PostoCombustivel()

    litros = obter_input_float("Informe a quantidade de litros vendidos: ")
    combustivel = input("Informe o tipo de combustível (A-álcool, G-gasolina): ").upper()

    valor_a_pagar = posto.calcular_valor_a_pagar(combustivel, litros)
    print("Valor a ser pago: R$", valor_a_pagar)

except ValueError as error:
    print(f"Erro: {str(error)}")
