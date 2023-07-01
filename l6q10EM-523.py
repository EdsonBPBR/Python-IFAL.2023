
#Lista de Exercício 6 - Questão 10
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

class NumeroPorExtenso:
    def __init__(self):
        self.unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
        self.especiais = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
        self.dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

    def obter_extenso(self, numero):
        if not isinstance(numero, int) or numero < 0 or numero > 99:
            raise ValueError("O número deve ser um inteiro entre 0 e 99.")

        if numero < 10:
            return self.unidades[numero]
        elif numero < 20:
            return self.especiais[numero - 10]
        else:
            dezena = numero // 10
            unidade = numero % 10
            extenso = self.dezenas[dezena - 2]
            if unidade != 0:
                extenso += ' e ' + self.unidades[unidade]
            return extenso


try:
    numero = int(input("Digite um número até 99: "))
    extenso = NumeroPorExtenso().obter_extenso(numero)
    print(f'O número {numero} por extenso é: {extenso}')
except ValueError as error:
    print("Erro:", str(error))
