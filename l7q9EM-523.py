#Lista de Exercício 7 - Questão 9
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

#a.Possua uma classe chamada Ponto, com os atributos x e y.
#b.Possua uma classe chamada Retangulo, com os atributos largura e altura.
#c.Possua uma função para imprimir os valores da classe Ponto
#d.Possua uma função para encontrar o centro de um Retângulo.
#e.Você deve criar alguns objetos da classe Retangulo.
#f.Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
#g.A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
#h.O valor do centro do objeto deve ser mostrado na tela
#i.Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Coordenadas do ponto: ({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        return Ponto(x_centro, y_centro)


def imprimir_centro(retangulo):
    centro = retangulo.encontrar_centro()
    print("Centro do retângulo:")
    centro.imprimir()


def alterar_retangulo(retangulo):
    try:
        x = float(input("Digite a coordenada x do ponto inicial: "))
        y = float(input("Digite a coordenada y do ponto inicial: "))
        largura = float(input("Digite a largura do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))

        ponto_inicial = Ponto(x, y)
        retangulo.ponto_inicial = ponto_inicial
        retangulo.largura = largura
        retangulo.altura = altura
    except ValueError:
        print("Valores inválidos. Certifique-se de inserir números.")


def exibir_menu(retangulo):
    opcao = 0
    while opcao != 3:
        print("\n===== Menu =====")
        print("1. Alterar valores do retângulo")
        print("2. Imprimir centro do retângulo")
        print("3. Sair")

        try:
            opcao = int(input("Digite sua opção: "))
        except ValueError:
            print("Opção inválida. Digite um número inteiro.")

        if opcao == 1:
            alterar_retangulo(retangulo)
        elif opcao == 2:
            imprimir_centro(retangulo)
        elif opcao == 3:
            print("Encerrando o programa...")
        else:
            print("Opção inválida. Digite uma opção válida.")


# Testando o programa
def main():
    ponto_inicial = Ponto(0, 0)
    retangulo = Retangulo(ponto_inicial, 5, 3)
    exibir_menu(retangulo)


if __name__ == "__main__":
    main()

