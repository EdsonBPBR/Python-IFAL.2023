#Lista de Exercício 2 - Questão 4
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

class VerificadorLetra:
    def __init__(self, letra):
        self.letra = letra.lower()

    def verificar(self):
        if len(self.letra) != 1:
            raise ValueError("Digite apenas uma letra.")

        if not self.letra.isalpha():
            raise ValueError("Digite apenas letras.")

        if self.letra in 'aeiou':
            return "vogal"
        else:
            return "consoante"

try:
    letra = input("Digite uma letra: ")
    verificador = VerificadorLetra(letra)
    resultado = verificador.verificar()
    print(f"A letra '{letra}' é uma {resultado}.")

except ValueError as e:
    print(f"Erro: {e}")

