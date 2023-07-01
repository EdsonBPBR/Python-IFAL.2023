#Lista de Exercício 7 - Questão 17
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.

import random

class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 10)
        self.tedio = random.randint(0, 10)

    def alimentar(self):
        self.fome -= 1
        if self.fome < 0:
            self.fome = 0

    def brincar(self):
        self.tedio -= 1
        if self.tedio < 0:
            self.tedio = 0

    def ouvir(self):
        print(f"{self.nome} diz: Estou feliz!")

    def __str__(self):
        return f"{self.nome}: Fome({self.fome}), Tédio({self.tedio})"


class FazendaBichinhos:
    def __init__(self):
        self.fazenda = []

    def adicionar_bichinho(self, nome):
        bichinho = Bichinho(nome)
        self.fazenda.append(bichinho)

    def alimentar_todos(self):
        for bichinho in self.fazenda:
            bichinho.alimentar()
        print("Todos os bichinhos foram alimentados!")

    def brincar_todos(self):
        for bichinho in self.fazenda:
            bichinho.brincar()
        print("Todos os bichinhos brincaram!")

    def ouvir_todos(self):
        for bichinho in self.fazenda:
            bichinho.ouvir()

    def mostrar_todos(self):
        for bichinho in self.fazenda:
            print(bichinho)


def obter_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número inteiro válido.")


def exibir_menu():
    print("\n--- Fazenda de Bichinhos ---")
    print("1. Alimentar todos os bichinhos")
    print("2. Brincar com todos os bichinhos")
    print("3. Ouvir todos os bichinhos")
    print("4. Mostrar todos os bichinhos")
    print("0. Sair")


def main():
    fazenda = FazendaBichinhos()
    quantidade_bichinhos = obter_inteiro("Digite a quantidade de bichinhos na fazenda: ")

    for i in range(quantidade_bichinhos):
        nome_bichinho = input(f"Digite o nome do bichinho {i+1}: ")
        fazenda.adicionar_bichinho(nome_bichinho)

    while True:
        exibir_menu()
        opcao = obter_inteiro("Digite a opção desejada: ")

        if opcao == 1:
            fazenda.alimentar_todos()
        elif opcao == 2:
            fazenda.brincar_todos()
        elif opcao == 3:
            fazenda.ouvir_todos()
        elif opcao == 4:
            fazenda.mostrar_todos()
        elif opcao == 0:
            print("Até mais!")
            break
        else:
            print("Opção inválida. Digite novamente.")


if __name__ == "__main__":
    main()
