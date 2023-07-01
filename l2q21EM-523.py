#Lista de Exercício 2 - Questão 21
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#a.Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#b.Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

class CaixaEletronico:
    def __init__(self):
        self.notas = [100, 50, 10, 5, 1]

    def calcular_notas(self, saque):
        quantidade_notas = [0, 0, 0, 0, 0]

        while saque > 0:
            for i, nota in enumerate(self.notas):
                if saque >= nota:
                    quantidade_notas[i] += 1
                    saque -= nota
                    break

        return quantidade_notas

    def realizar_saque(self, saque):
        resultado = self.calcular_notas(saque)

        print("Notas fornecidas:")
        for quantidade, nota in zip(resultado, self.notas):
            if quantidade > 0:
                print(f"{quantidade} nota(s) de R${nota}.")


def main():
    valor_minimo = 10
    valor_maximo = 600

    try:
        saque = int(input("Digite o valor do saque (entre R$10 e R$600): "))
        if saque < valor_minimo or saque > valor_maximo:
            raise ValueError("Valor inválido.")
    except ValueError as e:
        print(str(e))
        return

    caixa = CaixaEletronico()
    caixa.realizar_saque(saque)


main()
