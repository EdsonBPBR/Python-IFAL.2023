
#Lista de Exercício 5 - Questão 12
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.


import random

class Embaralhador:
    def __init__(self, palavra):
        self.palavra = palavra.lower()

    def embaralhar(self):
        caracteres = list(self.palavra)
        random.shuffle(caracteres)
        palavra_embaralhada = ''.join(caracteres)
        return palavra_embaralhada.upper()


def embaralhar_palavra(palavra):
    try:
        embaralhador = Embaralhador(palavra)
        return embaralhador.embaralhar()
    except Exception as e:
        print(f"Erro: {e}")
        return None


# Exemplo de uso
palavra = input("Digite uma palavra: ")
palavra_embaralhada = embaralhar_palavra(palavra)
if palavra_embaralhada is not None:
    print(f"Palavra embaralhada: {palavra_embaralhada}")
else:
    print("Não foi possível embaralhar a palavra.")

