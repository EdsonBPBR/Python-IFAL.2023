#Lista de Exercício 1 - Questão 10
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.


class Temperatura:
    def __init__(self):
        self.temp_celsius = 0

    def converter_celsius_para_fahrenheit(self):
        temp_fahrenheit = (self.temp_celsius * 9/5) + 32
        return temp_fahrenheit

    def obter_temperatura_celsius(self):
        while True:
            try:
                self.temp_celsius = float(input("Digite a temperatura em graus Celsius: "))
                return self.temp_celsius
            except ValueError:
                print("Entrada inválida! Digite um número válido para a temperatura em Celsius.")

    def exibir_temperatura_fahrenheit(self):
        temp_fahrenheit = self.converter_celsius_para_fahrenheit()
        print("A temperatura em graus Fahrenheit é:", temp_fahrenheit)

temperatura = Temperatura()
temperatura.obter_temperatura_celsius()
temperatura.exibir_temperatura_fahrenheit()
