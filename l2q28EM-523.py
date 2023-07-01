
#Lista de Exercício 2 - Questão 28 NÃO RODOU
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                     Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

class Carne:
    def __init__(self, tipo, preco_ate_5kg, preco_acima_5kg):
        self.tipo = tipo
        self.preco_ate_5kg = preco_ate_5kg
        self.preco_acima_5kg = preco_acima_5kg


class Carne:
    def __init__(self, nome, preco_ate_5kg, preco_acima_5kg):
        self.nome = nome
        self.preco_ate_5kg = preco_ate_5kg
        self.preco_acima_5kg = preco_acima_5kg


class Fruteira:
    def __init__(self):
        self.carnes = [
            Carne("File Duplo", 4.90, 5.80),
            Carne("Alcatra", 5.90, 6.80),
            Carne("Picanha", 6.90, 7.80)
        ]

    def obter_carne_por_nome(self, nome):
        for carne in self.carnes:
            if carne.nome.lower() == nome.lower():
                return carne
        return None


class CupomFiscal:
    def __init__(self, carne, quantidade, tipo_pagamento):
        self.carne = carne
        self.quantidade = quantidade
        self.tipo_pagamento = tipo_pagamento

    def calcular_preco_total(self):
        if self.quantidade <= 5:
            return self.quantidade * self.carne.preco_ate_5kg
        else:
            return self.quantidade * self.carne.preco_acima_5kg

    def calcular_desconto(self):
        if self.tipo_pagamento == "cartao_tabajara":
            preco_total = self.calcular_preco_total()
            return preco_total * 0.05
        else:
            return 0

    def calcular_valor_a_pagar(self):
        preco_total = self.calcular_preco_total()
        desconto = self.calcular_desconto()
        return preco_total - desconto

    def imprimir_cupom_fiscal(self):
        preco_total = self.calcular_preco_total()
        desconto = self.calcular_desconto()
        valor_a_pagar = self.calcular_valor_a_pagar()

        print("Cupom Fiscal")
        print("Tipo de carne: {}".format(self.carne.nome))
        print("Quantidade: {} Kg".format(self.quantidade))
        print("Preço total: R$ {:.2f}".format(preco_total))
        print("Tipo de pagamento: {}".format(self.tipo_pagamento))
        print("Desconto: R$ {:.2f}".format(desconto))
        print("Valor a pagar: R$ {:.2f}".format(valor_a_pagar))


def main():
    fruteira = Fruteira()

    tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ")
    quantidade = float(input("Digite a quantidade em Kg: "))
    tipo_pagamento = input("Digite o tipo de pagamento (cartao_tabajara ou outro): ")

    carne = fruteira.obter_carne_por_nome(tipo_carne)
    if carne:
        cupom = CupomFiscal(carne, quantidade, tipo_pagamento)
        cupom.imprimir_cupom_fiscal()
    else:
        print("Tipo de carne inválido!")


if __name__ == "__main__":
    main()
