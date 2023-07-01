# Lista de Exercício 1 - Questão 4
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

class CalculadoraMedia:
    def __init__(self):
        self.notas = []

    def solicitar_notas(self):
        for i in range(4):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i + 1}: "))
                    if nota < 0 or nota > 10:
                        raise ValueError("A nota deve estar entre 0 e 10.")
                    self.notas.append(nota)
                    break
                except ValueError as e:
                    print("Erro:", str(e))

    def calcular_media(self):
        soma = sum(self.notas)
        media = soma / len(self.notas)
        return media


def main():
    calculadora = CalculadoraMedia()
    calculadora.solicitar_notas()
    media = calculadora.calcular_media()
    print("A média das notas é:", media)


if __name__ == '__main__':
    main()
