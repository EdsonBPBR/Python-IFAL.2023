# Lista de Exercício 2 - Questão 27
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Uma fruteira está vendendo frutas com a seguinte tabela de preços:


class Fruta:
    def __init__(self, nome, preco_ate_5kg, preco_acima_5kg):
        self.nome = nome
        self.preco_ate_5kg = preco_ate_5kg
        self.preco_acima_5kg = preco_acima_5kg

    def calcular_valor(self, kg):
        if kg <= 5:
            valor = kg * self.preco_ate_5kg
        else:
            valor = kg * self.preco_acima_5kg
        return valor


class Fruteira:
    def __init__(self):
        self.frutas = [
            Fruta("Morango", 2.50, 2.20),
            Fruta("Maçã", 1.80, 1.50)
        ]
        self.desconto_limite_kg = 8
        self.desconto_limite_valor = 25.00
        self.desconto_percentual = 0.10

    def calcular_valor_a_pagar(self, kg_frutas):
        valor_total = sum(fruta.calcular_valor(kg) for fruta, kg in zip(self.frutas, kg_frutas))

        if sum(kg_frutas) > self.desconto_limite_kg or valor_total > self.desconto_limite_valor:
            valor_desconto = valor_total * self.desconto_percentual
            valor_total -= valor_desconto

        return valor_total


def obter_input_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número válido.")


def calcular_valor_a_pagar_cliente():
    fruteira = Fruteira()

    kg_frutas = []
    for fruta in fruteira.frutas:
        kg = obter_input_float(f"Informe a quantidade de {fruta.nome}s em kg: ")
        kg_frutas.append(kg)

    valor_a_pagar = fruteira.calcular_valor_a_pagar(kg_frutas)
    print("Valor a ser pago: R$", valor_a_pagar)


calcular_valor_a_pagar_cliente()
