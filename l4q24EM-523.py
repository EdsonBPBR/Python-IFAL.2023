# Lista de Exercício 4 - Questão 24
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random


class Dado:
    def __init__(self, lados=6):
        self.lados = lados

    def lancar(self):
        return random.randint(1, self.lados)


class LancamentoDados:
    def __init__(self, quantidade_lancamentos, dado):
        self.quantidade_lancamentos = quantidade_lancamentos
        self.dado = dado
        self.resultados = []
        self.contadores = [0] * dado.lados

    def executar_lancamentos(self):
        for _ in range(self.quantidade_lancamentos):
            resultado = self.dado.lancar()
            self.resultados.append(resultado)
            self.contadores[resultado - 1] += 1

    def exibir_resultados(self):
        for i in range(self.dado.lados):
            print(f"O valor {i + 1} foi obtido {self.contadores[i]} vezes.")


# Obter a quantidade de lançamentos desejada
try:
    quantidade_lancamentos = int(input("Digite a quantidade de lançamentos desejada: "))
except ValueError:
    print("Valor inválido. A quantidade de lançamentos será definida como 100.")
    quantidade_lancamentos = 100

# Criar um objeto Dado com 6 lados
dado = Dado(6)

# Criar um objeto LancamentoDados com a quantidade de lançamentos desejada e o dado
lancamento = LancamentoDados(quantidade_lancamentos, dado)

# Executar os lançamentos
lancamento.executar_lancamentos()

# Exibir os resultados
lancamento.exibir_resultados()

