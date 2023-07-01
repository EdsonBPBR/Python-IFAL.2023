#Lista de Exercício 3 - Questão 13
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

class PotenciaCalculator:
    def __init__(self):
        self.base = 0
        self.expoente = 0

    def obter_valores(self):
        try:
            self.base = float(input("Digite o número base: "))
            self.expoente = int(input("Digite o número expoente: "))
        except ValueError:
            print("Erro: Os valores fornecidos devem ser numéricos.")

    def calcular_potencia(self):
        resultado = 1

        for _ in range(self.expoente):
            resultado *= self.base

        return resultado


def main():
    potencia_calc = PotenciaCalculator()
    potencia_calc.obter_valores()

    resultado = potencia_calc.calcular_potencia()
    print(f"O resultado de {potencia_calc.base} elevado a {potencia_calc.expoente} é: {resultado}")


if __name__ == "__main__":
    main()
