#Lista de Exercício 5 - Questão 8
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.


class NumeroInteiro:
    def __init__(self, numero):
        self.numero = numero

    def contar_digitos(self):
        try:
            # Verifica se o número é inteiro
            if not isinstance(self.numero, int):
                raise ValueError("O valor fornecido não é um número inteiro.")

            # Converte o número em uma string
            numero_str = str(self.numero)

            # Retorna a quantidade de caracteres na string (quantidade de dígitos)
            return len(numero_str)

        except ValueError as ve:
            print(f"Erro: {ve}")
            return -1


# Exemplo de uso
try:
    numero = int(input("Digite um número inteiro: "))
    num_obj = NumeroInteiro(numero)
    quantidade_digitos = num_obj.contar_digitos()
    if quantidade_digitos != -1:
        print(f"O número {numero} possui {quantidade_digitos} dígitos.")
except ValueError:
    print("Erro: Você deve fornecer um número inteiro.")
