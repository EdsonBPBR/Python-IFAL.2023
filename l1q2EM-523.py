#Lista de Exercício 1 - Questão 2
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda



#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].


class MensagemNumero:
    def __init__(self):
        self.numero = None

    def solicitar_numero(self):
        try:
            self.numero = input("Digite um número: ")
            self.numero = float(self.numero)
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")
        except Exception as error:
            print("Ocorreu um erro:", error)

    def exibir_mensagem(self):
        if self.numero is not None:
            print("O número informado foi", self.numero)
        else:
            print("Nenhum número foi informado.")

mensagem = MensagemNumero()
mensagem.solicitar_numero()
mensagem.exibir_mensagem()
