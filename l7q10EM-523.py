#Lista de Exercício 7 - Questão 10
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

#a.Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#i.tipoCombustivel.
#ii.valorLitro
#iii.quantidadeCombustivel
#b.Possua no mínimo esses métodos:
#i.abastecerPorValor( ) – método onde é informado o valor a ser
#abastecido e mostra a quantidade de litros que foi colocada no veículo

#ii.abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.3

#iii.alterarValor( ) – altera o valor do litro do combustível.

#iv.alterarCombustivel( ) – altera o tipo do combustível.

#v.alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
#OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor_abastecido):
        try:
            quantidade_abastecida = valor_abastecido / self.valor_litro
            if quantidade_abastecida <= self.quantidade_combustivel:
                self.quantidade_combustivel -= quantidade_abastecida
                return quantidade_abastecida
            else:
                raise Exception("Não há combustível suficiente na bomba")
        except ZeroDivisionError:
            raise Exception("O valor do litro de combustível não pode ser zero")

    def abastecer_por_litro(self, quantidade_litros):
        try:
            valor_pagar = quantidade_litros * self.valor_litro
            if quantidade_litros <= self.quantidade_combustivel:
                self.quantidade_combustivel -= quantidade_litros
                return valor_pagar
            else:
                raise Exception("Não há combustível suficiente na bomba")
        except ZeroDivisionError:
            raise Exception("O valor do litro de combustível não pode ser zero")

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade


def main():
    bomba = BombaCombustivel("Gasolina", 4.50, 1000)

    try:
        litros_abastecidos = bomba.abastecer_por_valor(50)
        print(f"Foram abastecidos {litros_abastecidos:.2f} litros de {bomba.tipo_combustivel}")
    except Exception as e:
        print(str(e))

    try:
        valor_pagar = bomba.abastecer_por_litro(30)
        print(f"O valor a ser pago é de R$ {valor_pagar:.2f}")
    except Exception as e:
        print(str(e))

    bomba.alterar_valor(4.80)
    bomba.alterar_combustivel("Álcool")
    bomba.alterar_quantidade_combustivel(1500)


if __name__ == "__main__":
    main()

