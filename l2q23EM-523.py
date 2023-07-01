
#Lista de Exercício 2 - Questão 23
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

class Numero:
    def __init__(self, valor):
        self.valor = valor

    def verificar_tipo(self):
        arredondado = round(self.valor)
        if arredondado == self.valor:
            return "inteiro"
        else:
            return "decimal"


def obter_numero():
    try:
        valor = float(input("Digite um número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return None
    else:
        return Numero(valor)


def main():
    numero = obter_numero()
    if numero is not None:
        tipo_numero = numero.verificar_tipo()
        print(f"O número é do tipo {tipo_numero}.")


main()
