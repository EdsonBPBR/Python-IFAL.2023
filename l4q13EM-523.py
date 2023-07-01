#Lista de Exercício 4 - Questão 13
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda


#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

class TemperaturaAnual:
    def __init__(self):
        self.meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        self.temperaturas = []

    def ler_temperaturas(self):
        for i in range(12):
            while True:
                try:
                    temperatura = float(input("Digite a temperatura média de {} (em graus Celsius): ".format(self.meses[i])))
                    self.temperaturas.append(temperatura)
                    break
                except ValueError:
                    print("Erro: Digite um valor válido para temperatura.")

    def calcular_media_anual(self):
        if self.temperaturas:
            return sum(self.temperaturas) / len(self.temperaturas)
        else:
            return 0

    def mostrar_temperaturas_acima_media(self, media_anual):
        print("\nTemperaturas acima da média anual:")
        for i in range(12):
            if self.temperaturas[i] > media_anual:
                print("{} - {:.1f}°C".format(self.meses[i], self.temperaturas[i]))


def main():
    try:
        temperatura_anual = TemperaturaAnual()
        temperatura_anual.ler_temperaturas()
        media_anual = temperatura_anual.calcular_media_anual()
        temperatura_anual.mostrar_temperaturas_acima_media(media_anual)
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print("Ocorreu um erro:", e)


if __name__ == "__main__":
    main()
