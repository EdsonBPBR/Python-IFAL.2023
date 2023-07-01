#Lista de Exercício 4 - Questão 21
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#a.O modelo do carro mais econômico;
#b.Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
#Comparativo de Consumo de Combustível

#Veículo 1
#Nome: fusca
#Km por litro: 7
#Veículo 2
#Nome: gol
#Km por litro: 10
#Veículo 3
#Nome: uno
#Km por litro: 12.5
#Veículo 4
#Nome: Vectra
#Km por litro: 9
#Veículo 5
#Nome: Peugeout
#Km por litro: 14.5

#Relatório Final
# 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
# 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
# 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
# 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
# 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
#O menor consumo é do peugeout.

class Carro:
    def __init__(self, modelo, consumo):
        self.modelo = modelo
        self.consumo = consumo

    def calcular_litros_percorridos(self, distancia):
        return distancia / self.consumo

    def calcular_custo_combustivel(self, litros, preco_litro):
        return litros * preco_litro


class RelatorioConsumo:
    def __init__(self):
        self.carros = []

    def adicionar_carro(self, modelo, consumo):
        carro = Carro(modelo, consumo)
        self.carros.append(carro)

    def calcular_total_carros(self):
        return len(self.carros)

    def calcular_litros_percorridos(self, distancia):
        litros_percorridos = []
        for carro in self.carros:
            litros = carro.calcular_litros_percorridos(distancia)
            litros_percorridos.append(litros)
        return litros_percorridos

    def calcular_custo_combustivel(self, litros, preco_litro):
        custo_combustivel = []
        for litro in litros:
            custo = Carro.calcular_custo_combustivel(None, litro, preco_litro)
            custo_combustivel.append(custo)
        return custo_combustivel

    def obter_carro_mais_economico(self):
        return min(self.carros, key=lambda x: x.consumo)


def main():
    relatorio = RelatorioConsumo()

    for i in range(5):
        modelo = input(f"Veículo {i+1}\nNome: ")
        while True:
            try:
                consumo = float(input("Km por litro: "))
                break
            except ValueError:
                print("Valor inválido! Digite um número válido.")
        relatorio.adicionar_carro(modelo, consumo)
        print()

    print("Relatório Final")
    litros_percorridos = relatorio.calcular_litros_percorridos(1000)
    custo_combustivel = relatorio.calcular_custo_combustivel(litros_percorridos, 2.25)

    for i, carro in enumerate(relatorio.carros):
        print(f"{i+1} - {carro.modelo:15s} - {carro.consumo:4.1f} - {litros_percorridos[i]:6.1f} litros - R$ {custo_combustivel[i]:.2f}")

    carro_mais_economico = relatorio.obter_carro_mais_economico()
    print(f"\nO menor consumo é do {carro_mais_economico.modelo}.")


if __name__ == '__main__':
    main()
