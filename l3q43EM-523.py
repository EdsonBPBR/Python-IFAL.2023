#Lista de Exercício 3 - Questão 43
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#O cardápio de uma lanchonete é o seguinte:
#Especificação   Código  Preço
#Cachorro Quente 100     R$ 1,20
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,20
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.


class ItemCardapio:
    def __init__(self, codigo, especificacao, preco):
        self.codigo = codigo
        self.especificacao = especificacao
        self.preco = preco


class Lanchonete:
    def __init__(self):
        self.cardapio = {
            100: ItemCardapio(100, "Cachorro Quente", 1.20),
            101: ItemCardapio(101, "Bauru Simples", 1.30),
            102: ItemCardapio(102, "Bauru com ovo", 1.50),
            103: ItemCardapio(103, "Hambúrguer", 1.20),
            104: ItemCardapio(104, "Cheeseburguer", 1.30),
            105: ItemCardapio(105, "Refrigerante", 1.00)
        }

    def fazer_pedido(self):
        total_geral = 0

        while True:
            try:
                codigo = int(input("Digite o código do item (ou um número negativo para encerrar o pedido): "))
                if codigo < 0:
                    break

                if codigo in self.cardapio:
                    quantidade = int(input("Digite a quantidade desejada: "))
                    if quantidade < 0:
                        raise ValueError("Quantidade inválida. Digite um valor positivo.")

                    item = self.cardapio[codigo]
                    preco_item = item.preco
                    valor_a_pagar = preco_item * quantidade
                    total_geral += valor_a_pagar

                    print(f"Item: {item.especificacao}")
                    print(f"Preço unitário: R$ {preco_item:.2f}")
                    print(f"Quantidade: {quantidade}")
                    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}\n")
                else:
                    raise ValueError("Código inválido. Digite um código válido.")

            except ValueError as ve:
                print(f"Erro: {ve}\n")

        print(f"Total geral do pedido: R$ {total_geral:.2f}")


def main():
    lanchonete = Lanchonete()
    lanchonete.fazer_pedido()


if __name__ == "__main__":
    main()
