#Lista de Exercício 6 - Questão 4
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

#F
#FU
#FUL
#FULA
#FULAN
#FULANO


class NomeEscada:
    def __init__(self):
        self.nome = ""

    def obter_nome(self):
        self.nome = input("Digite o seu nome: ")

    def imprimir_escada(self):
        try:
            escada = ""
            for letra in self.nome:
                escada += letra.upper()
                print(escada)
        except TypeError:
            print("Erro: nome inválido.")


# Exemplo de uso
nome_escada = NomeEscada()
nome_escada.obter_nome()
nome_escada.imprimir_escada()
