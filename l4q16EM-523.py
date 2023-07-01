#Lista de Exercício 4 - Questão 16
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#a.$200 - $299
#b.$300 - $399
#c.$400 - $499
#d.$500 - $599
#e.$600 - $699
#f.$700 - $799
#g.$800 - $899
#h.$900 - $999
#i.$1000 em diante
#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

class Vendedor:
    def __init__(self, vendas_brutas):
        self.vendas_brutas = vendas_brutas

    def calcular_salario(self):
        return 200 + 0.09 * self.vendas_brutas


class Empresa:
    def __init__(self):
        self.vendedores = []

    def ler_vendas_brutas(self):
        while True:
            try:
                vendas_brutas = float(input("Informe as vendas brutas (-1 para encerrar): "))
                if vendas_brutas == -1:
                    break
                vendedor = Vendedor(vendas_brutas)
                self.vendedores.append(vendedor)
            except ValueError:
                print("Erro: Digite um valor numérico válido.")

    def contar_vendedores_por_intervalo(self):
        intervalos = ["$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599",
                      "$600 - $699", "$700 - $799", "$800 - $899", "$900 - $999",
                      "$1000 em diante"]
        contagem = [0] * len(intervalos)

        for vendedor in self.vendedores:
            salario = vendedor.calcular_salario()
            indice = int(salario / 100) - 2
            if indice >= 0 and indice < len(intervalos):
                contagem[indice] += 1

        return intervalos, contagem


def main():
    try:
        empresa = Empresa()
        empresa.ler_vendas_brutas()

        intervalos, contagem = empresa.contar_vendedores_por_intervalo()

        for i in range(len(intervalos)):
            print("Quantidade de vendedores no intervalo {}: {}".format(intervalos[i], contagem[i]))

        print("Programa encerrado.")
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print("Ocorreu um erro:", e)


if __name__ == "__main__":
    main()
