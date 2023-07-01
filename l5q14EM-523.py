#Lista de Exercício 5 - Questão 14
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

#8  3  4
#1  5  9
#6  7  2
#Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.


class QuadradoMagico:
    def __init__(self):
        self.numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.combinacoes = self.gerar_combinacoes(self.numeros, 9)
        self.quadrados_magicos = []

    def mostrar_quadrados_magicos(self):
        for combinacao in self.combinacoes:
            if self.verificar_quadrado_magico(combinacao):
                self.quadrados_magicos.append(combinacao)

        if self.quadrados_magicos:
            for quadrado in self.quadrados_magicos:
                self.mostrar_quadrado(quadrado)
        else:
            print("Nenhum quadrado mágico encontrado.")

    def gerar_combinacoes(self, numeros, tamanho):
        if tamanho == 0:
            return [[]]

        combinacoes = []
        for i in range(len(numeros)):
            numero = numeros[i]
            restantes = numeros[:i] + numeros[i+1:]
            subcombinacoes = self.gerar_combinacoes(restantes, tamanho - 1)

            for subcombinacao in subcombinacoes:
                combinacoes.append([numero] + subcombinacao)

        return combinacoes

    def verificar_quadrado_magico(self, quadrado):
        soma_alvo = sum(quadrado[:3])

        # Verificar linhas
        for i in range(0, 9, 3):
            if sum(quadrado[i:i+3]) != soma_alvo:
                return False

        # Verificar colunas
        for i in range(3):
            if sum(quadrado[i::3]) != soma_alvo:
                return False

        # Verificar diagonais
        if quadrado[0] + quadrado[4] + quadrado[8] != soma_alvo:
            return False

        if quadrado[2] + quadrado[4] + quadrado[6] != soma_alvo:
            return False

        return True

    def mostrar_quadrado(self, quadrado):
        for i in range(0, 9, 3):
            print(quadrado[i:i+3])
        print()


# Exemplo de uso
quadrado_magico = QuadradoMagico()
quadrado_magico.mostrar_quadrados_magicos()
