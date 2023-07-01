#Lista de Exercício 3 - Questão 30
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
#Preço do pão: R$ 0.18
#Panificadora Pão de Ontem - Tabela de preços
#1 - R$ 0.18
#2 - R$ 0.36
#...
#50 - R$ 9.00



class TabelaPrecos:
    def __init__(self, preco_pao):
        if preco_pao <= 0:
            raise ValueError("O preço do pão deve ser maior que zero.")
        self.preco_pao = preco_pao

    def gerar_tabela(self, quantidade_maxima):
        tabela = []
        for i in range(1, quantidade_maxima + 1):
            preco_total = i * self.preco_pao
            tabela.append((i, preco_total))
        return tabela

    def exibir_tabela_precos(self, tabela):
        print("Panificadora Pão de Ontem - Tabela de preços")
        for quantidade, preco_total in tabela:
            print(f"{quantidade} - R$ {preco_total:.2f}")


def obter_preco_pao():
    while True:
        try:
            preco_pao = float(input("Digite o preço do pão: R$ "))
            return preco_pao
        except ValueError:
            print("Valor inválido. Digite novamente.")


# Exemplo de uso
try:
    preco_pao = obter_preco_pao()

    tabela_precos = TabelaPrecos(preco_pao)
    tabela = tabela_precos.gerar_tabela(50)
    tabela_precos.exibir_tabela_precos(tabela)

except ValueError as e:
    print(f"Erro: {str(e)}")
