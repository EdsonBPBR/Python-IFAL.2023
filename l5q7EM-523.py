#Lista de Exercício 5 - Questão 7
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.


class Prestacao:
    def __init__(self, valor, dias_atraso):
        self.valor = valor
        self.dias_atraso = dias_atraso

    def calcular_valor_pago(self):
        if self.dias_atraso == 0:
            return self.valor
        else:
            multa = self.valor * 0.03
            juros = self.valor * (0.001 * self.dias_atraso)
            return self.valor + multa + juros


def ler_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                raise ValueError("O valor não pode ser negativo.")
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico válido.")


def ler_dias_atraso():
    while True:
        try:
            dias_atraso = int(input("Digite o número de dias em atraso: "))
            if dias_atraso < 0:
                raise ValueError("O número de dias em atraso não pode ser negativo.")
            return dias_atraso
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor inteiro válido.")


total_prestacoes = 0
total_valor_pago = 0

while True:
    valor_prestacao = ler_valor("Digite o valor da prestação (ou 0 para encerrar): ")
    if valor_prestacao == 0:
        break

    dias_atraso = ler_dias_atraso()

    prestacao = Prestacao(valor_prestacao, dias_atraso)
    valor_pago = prestacao.calcular_valor_pago()

    total_prestacoes += 1
    total_valor_pago += valor_pago

    print(f"Valor a ser pago: R${valor_pago:.2f}\n")

print("\nRelatório do dia:")
print(f"Quantidade de prestações pagas: {total_prestacoes}")
print(f"Valor total pago: R${total_valor_pago:.2f}")
