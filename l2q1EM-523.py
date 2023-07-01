#Lista de Exercício 2 - Questão 1
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça dois números e imprima o maior deles.

class Numero:
	def __init__(self, valor):
            self.valor = valor

	def solicitar_numero(self, mensagem):
		while True:
			try:
				numero = float(input(mensagem))
				return numero
			except ValueError:
				print("Entrada inválida. Certifique-se de inserir um número válido.")

	def obter_valor(self):
    	    return self.valor

	def definir_valor(self, novo_valor):
    	    self.valor = novo_valor

	def encontrar_maior_numero(self, outro_numero):
    	    if self.valor > outro_numero.obter_valor():
        	    return self.valor
    	    elif outro_numero.obter_valor() > self.valor:
        	    return outro_numero.obter_valor()
    	    else:
        	    return None


numero1 = Numero(0)
numero2 = Numero(0)

numero1.definir_valor(numero1.solicitar_numero("Digite o primeiro número: "))
numero2.definir_valor(numero2.solicitar_numero("Digite o segundo número: "))

maior_numero = numero1.encontrar_maior_numero(numero2)

if maior_numero is not None:
	print(f"O maior número é: {maior_numero}")
else:
	print("Os números são iguais.")

