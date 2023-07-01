#Lista de Exercício 5 - Questão 5
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_preco_com_imposto(self, taxa_imposto):
        if taxa_imposto < 0:
            raise ValueError("A taxa de imposto deve ser um valor não negativo.")
        imposto = self.preco * taxa_imposto / 100
        preco_com_imposto = self.preco + imposto
        return preco_com_imposto


# Função auxiliar para ler um número float do usuário
def ler_numero_float(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")


# Exemplo de uso do objeto Produto e tratamento de exceções
try:
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = ler_numero_float("Digite o preço do produto: ")
    taxa_imposto = ler_numero_float("Digite a taxa de imposto (em %): ")

    produto = Produto(nome_produto, preco_produto)
    preco_com_imposto = produto.calcular_preco_com_imposto(taxa_imposto)

    print(f"O preço do produto {produto.nome} com imposto é: R${preco_com_imposto:.2f}")

except ValueError as e:
    print("Erro:", str(e))
