# Lista de Exercício 7 - Questão 2
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Classe Quadrado: Crie uma classe que modele um quadrado:
#a.Atributos: Tamanho do lado
#b.Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;


class Quadrado:
    def __init__(self, lado):
        self._lado = None
        self.lado = lado

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, novo_lado):
        if novo_lado <= 0:
            raise ValueError("O lado do quadrado deve ser maior que zero.")
        self._lado = novo_lado

    def calcular_area(self):
        return self.lado ** 2


def main():
    try:
        lado = float(input("Digite o tamanho do lado do quadrado: "))
        meu_quadrado = Quadrado(lado)
        area = meu_quadrado.calcular_area()
        print("Área:", area)
    except ValueError as e:
        print("Erro:", str(e))


if __name__ == "__main__":
    main()
