#Lista de Exercício 2 - Questão 24
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda


#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#a.par ou ímpar;
#b.positivo ou negativo;
#c.inteiro ou decimal.

class Numero:
    def __init__(self, valor):
        self.valor = valor

    def verificar_paridade(self):
        if self.valor % 2 == 0:
            return "par"
        else:
            return "ímpar"

    def verificar_sinal(self):
        if self.valor > 0:
            return "positivo"
        elif self.valor < 0:
            return "negativo"
        else:
            return "zero"

    def verificar_tipo(self):
        arredondado = round(self.valor)
        if arredondado == self.valor:
            return "inteiro"
        else:
            return "decimal"


class Calculadora:
    def __init__(self):
        self.numero1 = None
        self.numero2 = None

    def obter_numero(self, mensagem):
        while True:
            try:
                valor = float(input(mensagem))
                return Numero(valor)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")

    def obter_operacao(self):
        operacoes_validas = ["+", "-", "*", "/"]
        while True:
            operacao = input("Escolha uma operação (+, -, *, /): ")
            if operacao in operacoes_validas:
                return operacao
            else:
                print("Operação inválida. Por favor, escolha uma operação válida.")

    def realizar_operacao(self, numero1, numero2, operacao):
        try:
            if operacao == "+":
                resultado = numero1.valor + numero2.valor
            elif operacao == "-":
                resultado = numero1.valor - numero2.valor
            elif operacao == "*":
                resultado = numero1.valor * numero2.valor
            elif operacao == "/":
                resultado = numero1.valor / numero2.valor
            else:
                raise ValueError("Operação inválida.")
        except ZeroDivisionError:
            print("Erro: Divisão por zero.")
            return None
        except ValueError as error:
            print(f"Erro: {str(error)}")
            return None

        tipo_resultado = Numero(resultado).verificar_tipo()
        paridade_resultado = Numero(resultado).verificar_paridade()
        sinal_resultado = Numero(resultado).verificar_sinal()

        return resultado, tipo_resultado, paridade_resultado, sinal_resultado

    def exibir_resultado(self, resultado):
        if resultado is not None:
            valor, tipo, paridade, sinal = resultado
            print(f"O resultado da operação é: {valor}")
            print(f"O resultado é {paridade}, {sinal}, {tipo}.")

    def executar_calculadora(self):
        self.numero1 = self.obter_numero("Digite o primeiro número: ")
        self.numero2 = self.obter_numero("Digite o segundo número: ")

        if self.numero1 is not None and self.numero2 is not None:
            operacao = self.obter_operacao()

            resultado = self.realizar_operacao(self.numero1, self.numero2, operacao)

            self.exibir_resultado(resultado)


calculadora = Calculadora()
calculadora.executar_calculadora()

