#Lista de Exercício 2 - Questão 8
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

class Produto:
    def __init__(self, preco):
        self.preco = preco

def determinar_produto_mais_barato(produtos):
    produto_mais_barato = min(produtos, key=lambda p: p.preco)
    return produto_mais_barato

try:
    produtos = []
    for i in range(3):
        preco = float(input(f"Digite o preço do produto {i+1}: "))
        produtos.append(Produto(preco))

    produto_mais_barato = determinar_produto_mais_barato(produtos)

    print(f"Você deve comprar o produto com preço R${produto_mais_barato.preco:.2f}.")

except ValueError as e:
    print(f"Erro: {e}. Certifique-se de digitar apenas números.")
