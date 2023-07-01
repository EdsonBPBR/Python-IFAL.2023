#Lista de Exercício 2 - Questão 2
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo


class VerificadorValor:
	def __init__(self, valor):
    	    self.valor = valor

	def verificar(self):
    	    if self.valor > 0:
        	    return "positivo"
    	    elif self.valor < 0:
        	    return "negativo"
    	    else:
        	    return "zero"


try:
	entrada = input("Digite um valor: ")
	valor = float(entrada)

	verificador = VerificadorValor(valor)
	resultado = verificador.verificar()

	print(f"O valor é {resultado}.")
except ValueError:
	print("Entrada inválida. Por favor, digite um valor numérico.")
