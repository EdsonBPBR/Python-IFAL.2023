#Lista de Exercício 2 - Questão 3
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


class VerificadorSexo:
	def __init__(self, letra):
    	    self.letra = letra.upper()

	def verificar(self):
            if self.letra == "F":
                return "F - Feminino"
            elif self.letra == "M":
                return "M - Masculino"
            else:
                return "Sexo Inválido"


try:
	entrada = input("Digite uma letra (F/M): ")

	verificador = VerificadorSexo(entrada)
	resultado = verificador.verificar()

	print(resultado)
except ValueError:
	print("Entrada inválida. Digite apenas 'F' ou 'M'.")
