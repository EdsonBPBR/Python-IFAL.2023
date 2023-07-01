#Lista de Exercício 6 - Questão 5
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda


#Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

#FULANO
#FULAN
#FULA
#FUL
#FU
#F

class EscadaInvertida:
    def __init__(self):
        self.nome = ""

    def obter_nome(self):
        self.nome = input("Digite o seu nome: ")

    def imprimir_escada_invertida(self):
        try:
            escada = ""
            for letra in self.nome:
                escada = letra.upper() + escada
                print(escada)
        except TypeError:
            print("Erro: nome inválido.")


# Exemplo de uso
escada_invertida = EscadaInvertida()
escada_invertida.obter_nome()
escada_invertida.imprimir_escada_invertida()
