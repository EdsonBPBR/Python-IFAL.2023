#Lista de Exercício 1 - Questão 9
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9)

class Temperatura:
    def __init__(self):
        self.temp_fahrenheit = 0

    def converter_fahrenheit_para_celsius(self):
        temp_celsius = 5 * ((self.temp_fahrenheit - 32) / 9)
        return temp_celsius

    def obter_temperatura_fahrenheit(self):
        while True:
            try:
                self.temp_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
                return self.temp_fahrenheit
            except ValueError:
                print("Entrada inválida! Digite um número válido para a temperatura em Fahrenheit.")

    def exibir_temperatura_celsius(self):
        temp_celsius = self.converter_fahrenheit_para_celsius()
        print("A temperatura em graus Celsius é:", temp_celsius)

temperatura = Temperatura()
temperatura.obter_temperatura_fahrenheit()
temperatura.exibir_temperatura_celsius()
