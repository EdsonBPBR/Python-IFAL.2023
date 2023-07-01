#O Departamento Estadual de Meteorologia#Lista de Exercício 3 - Questão 33
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
#lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.





class Meteorologia:
    def __init__(self):
        self.temperaturas = []

    def ler_temperaturas(self):
        while True:
            try:
                temperatura = float(input("Digite uma temperatura (ou digite 'sair' para encerrar): "))
                if temperatura == "sair":
                    break
                self.temperaturas.append(temperatura)
            except ValueError:
                print("Valor inválido. Digite um número válido ou 'sair' para encerrar.")

    def obter_maior_temperatura(self):
        if len(self.temperaturas) == 0:
            return None
        return max(self.temperaturas)

    def obter_menor_temperatura(self):
        if len(self.temperaturas) == 0:
            return None
        return min(self.temperaturas)

    def calcular_media_temperaturas(self):
        if len(self.temperaturas) == 0:
            return None
        return sum(self.temperaturas) / len(self.temperaturas)


def main():
    meteorologia = Meteorologia()
    meteorologia.ler_temperaturas()

    maior_temperatura = meteorologia.obter_maior_temperatura()
    menor_temperatura = meteorologia.obter_menor_temperatura()
    media_temperaturas = meteorologia.calcular_media_temperaturas()

    if maior_temperatura is not None:
        print("Maior temperatura: ", maior_temperatura)

    if menor_temperatura is not None:
        print("Menor temperatura: ", menor_temperatura)

    if media_temperaturas is not None:
        print("Média das temperaturas: ", media_temperaturas)


if __name__ == "__main__":
    main()
