
#Lista de Exercício 6 - Questão 7
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda


#Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#a.quantos espaços em branco existem na frase.
#b.quantas vezes aparecem as vogais a, e, i, o, u.

class ContadorEspacosVogais:
    def __init__(self):
        self.frase = ""
        self.espacos = 0
        self.vogais = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0
        }

    def obter_frase(self):
        self.frase = input("Digite uma frase: ")

    def contar_espacos(self):
        self.espacos = self.frase.count(' ')

    def contar_vogais(self):
        frase_lower = self.frase.lower()
        for vogal in self.vogais:
            self.vogais[vogal] = frase_lower.count(vogal)

    def exibir_resultados(self):
        print(f"Quantidade de espaços em branco: {self.espacos}")
        print("Quantidade de vogais:")
        for vogal, quantidade in self.vogais.items():
            print(f"{vogal}: {quantidade}")


# Exemplo de uso
contador = ContadorEspacosVogais()
contador.obter_frase()
contador.contar_espacos()
contador.contar_vogais()
contador.exibir_resultados()
