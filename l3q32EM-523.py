#Lista de Exercício 3 - Questão 32
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5
#5! =  5 . 4 . 3 . 2 . 1 = 120


class FatorialCalculator:
    def calcular_fatorial(self, numero):
        if numero < 0:
            raise ValueError("O número não pode ser negativo.")
        elif numero == 0:
            return 1
        else:
            fatorial = 1
            for i in range(1, numero + 1):
                fatorial *= i
            return fatorial


def obter_numero():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            return numero
        except ValueError:
            print("Valor inválido. Digite novamente.")


def exibir_fatorial(numero):
    calculator = FatorialCalculator()
    fatorial = calculator.calcular_fatorial(numero)
    fatores = " . ".join(str(i) for i in range(numero, 0, -1))
    print(f"Fatorial de: {numero}")
    print(f"{numero}! = {fatores} = {fatorial}")


def calcular_e_exibir_fatorial():
    try:
        numero = obter_numero()
        exibir_fatorial(numero)
    except ValueError as e:
        print(f"Erro: {str(e)}")


# Execução do programa
calcular_e_exibir_fatorial()
