#Lista de Exercício 3 - Questão 1

#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

# Enunciado: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

class NotaInvalidaError(Exception):
    """Exceção personalizada para notas inválidas."""
    pass

def obter_nota():
    """Função para solicitar e retornar uma nota válida."""
    while True:
        try:
            nota = float(input("Digite uma nota entre zero e dez: "))
            if nota < 0 or nota > 10:
                raise NotaInvalidaError
            return nota
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
        except NotaInvalidaError:
            print("Valor inválido. Digite uma nota entre zero e dez.")

try:
    nota = obter_nota()
    print("Valor válido informado:", nota)
except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

