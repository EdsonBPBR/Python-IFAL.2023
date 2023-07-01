#Lista de Exercício 3 - Questão 29
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
#Lojas Quase Dois - Tabela de preços
#1 - R$ 1.99
#2 - R$ 3.98
#...
#50 - R$ 99.50

class TabelaPrecos:
    def __init__(self):
        self.preco_unitario = 1.99

    def gerar_tabela(self, quantidade_maxima):
        tabela = []
        for i in range(1, quantidade_maxima + 1):
            preco_total = self.calcular_preco_total(i)
            tabela.append((i, preco_total))
        return tabela

    def calcular_preco_total(self, quantidade):
        if quantidade < 1 or quantidade > 50:
            raise ValueError("A quantidade de produtos deve estar entre 1 e 50.")
        return quantidade * self.preco_unitario


def exibir_tabela_precos(tabela):
    print("Lojas Quase Dois - Tabela de preços")
    for quantidade, preco_total in tabela:
        print(f"{quantidade} - R$ {preco_total:.2f}")


# Exemplo de uso
try:
    tabela_precos = TabelaPrecos()
    tabela = tabela_precos.gerar_tabela(50)
    exibir_tabela_precos(tabela)
except ValueError as e:
    print(f"Erro: {str(e)}")
