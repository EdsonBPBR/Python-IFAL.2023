#Lista de Exercício 6 - Questão 12
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

#Valida e corrige número de telefone
#Telefone: 461-0133
#Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
#Telefone corrigido sem formatação: 34610133
#Telefone corrigido com formatação: 3461-0133

class Telefone:
    def __init__(self, numero):
        self.numero = numero

    def corrigir_numero(self):
        numero_sem_formatacao = self.numero.replace("-", "")

        if len(numero_sem_formatacao) == 7:
            numero_corrigido = "3" + numero_sem_formatacao
            numero_formatado = numero_corrigido[:4] + "-" + numero_corrigido[4:]
            return numero_corrigido, numero_formatado

        return None

def main():
    numero_telefone = input("Telefone: ")

    telefone = Telefone(numero_telefone)
    resultado = telefone.corrigir_numero()

    if resultado:
        numero_corrigido, numero_formatado = resultado
        print("Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.")
        print("Telefone corrigido sem formatação:", numero_corrigido)
        print("Telefone corrigido com formatação:", numero_formatado)
    else:
        print("O número de telefone informado não precisa de correção.")

if __name__ == "__main__":
    main()
