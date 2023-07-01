
#Lista de Exercício 5 - Questão 9
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda


#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.


class NumeroInteiro:
    def __init__(self, numero):
        self.numero = numero

    def calcular_reverso(self):
        try:
            # Verifica se o número é inteiro
            if not isinstance(self.numero, int):
                raise ValueError("O valor fornecido não é um número inteiro.")

            # Converte o número em uma string
            numero_str = str(self.numero)

            # Inverte a string
            numero_reverso_str = numero_str[::-1]

            # Converte o reverso de volta para um número inteiro
            numero_reverso = int(numero_reverso_str)

            # Retorna o reverso do número
            return numero_reverso

        except ValueError as ve:
            print(f"Erro: {ve}")
            return None


# Exemplo de uso
try:
    numero = int(input("Digite um número inteiro: "))
    num_obj = NumeroInteiro(numero)
    reverso = num_obj.calcular_reverso()
    if reverso is not None:
        print(f"O reverso de {numero} é {reverso}.")
except ValueError:
    print("Erro: Você deve fornecer um número inteiro.")
