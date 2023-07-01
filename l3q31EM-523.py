#Lista de Exercício 3 - Questão 31
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
#Lojas Tabajara
#Produto 1: R$ 2.20
#Produto 2: R$ 5.80
#Produto 3: R$ 0
#Total: R$ 9.00
#Dinheiro: R$ 20.00
#Troco: R$ 11.00


class CaixaRegistradora:
    def __init__(self):
        self.total = 0

    def registrar_compra(self, preco):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        self.total += preco

    def finalizar_compra(self, dinheiro):
        if dinheiro < self.total:
            raise ValueError("Dinheiro insuficiente para pagar a compra.")
        troco = dinheiro - self.total
        self.total = 0
        return troco


def obter_preco():
    while True:
        try:
            preco = float(input("Informe o preço do produto (ou 0 para finalizar): R$ "))
            return preco
        except ValueError:
            print("Valor inválido. Digite novamente.")


def obter_valor_em_dinheiro():
    while True:
        try:
            valor = float(input("Digite o valor em dinheiro fornecido pelo cliente: R$ "))
            return valor
        except ValueError:
            print("Valor inválido. Digite novamente.")


# Função principal
def caixa_registradora():
    caixa = CaixaRegistradora()

    while True:
        try:
            preco = obter_preco()
            if preco == 0:
                break
            caixa.registrar_compra(preco)
        except ValueError as e:
            print(f"Erro: {str(e)}")

    print("Lojas Tabajara")
    print(f"Total: R$ {caixa.total:.2f}")

    dinheiro = obter_valor_em_dinheiro()
    try:
        troco = caixa.finalizar_compra(dinheiro)
        print(f"Dinheiro: R$ {dinheiro:.2f}")
        print(f"Troco: R$ {troco:.2f}")
    except ValueError as e:
        print(f"Erro: {str(e)}")


# Execução do programa
caixa_registradora()
