#Lista de Exercício 2 - Questão 19
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

class NumeroExtenso:
    def __init__(self, numero):
        self.numero = numero

    def validar_numero(self):
        if self.numero >= 1000:
            raise ValueError("Número inválido. Digite um número inteiro menor que 1000.")

    def obter_extenso(self):
        self.validar_numero()

        unidades = self.numero % 10
        dezenas = (self.numero // 10) % 10
        centenas = self.numero // 100

        extenso = ""

        if centenas > 0:
            extenso += f"{centenas} centena{'s' if centenas > 1 else ''}"

        if dezenas > 0:
            if extenso:
                extenso += ", "

            extenso += f"{dezenas} dezena{'s' if dezenas > 1 else ''}"

        if unidades > 0:
            if extenso:
                extenso += " e "

            extenso += f"{unidades} unidade{'s' if unidades > 1 else ''}"

        return extenso


def exibir_extenso(numeros):
    for numero in numeros:
        try:
            numero_extenso = NumeroExtenso(numero)
            resultado = numero_extenso.obter_extenso()
            print(f"{numero} = {resultado}")
        except ValueError as e:
            print(f"Erro: {str(e)}")


numeros = [326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

exibir_extenso(numeros)
