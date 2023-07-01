# Lista de Exercício 7 - Questão 15
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.tedio = 0

    def alimentar(self, quantidade):
        if not isinstance(quantidade, int) or quantidade <= 0:
            raise ValueError("A quantidade de comida fornecida deve ser um número inteiro positivo.")

        self.fome -= quantidade
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo):
        if not isinstance(tempo, int) or tempo <= 0:
            raise ValueError("O tempo de brincadeira deve ser um número inteiro positivo.")

        self.tedio -= tempo
        if self.tedio < 0:
            self.tedio = 0

    def humor(self):
        if self.fome == 0 and self.tedio == 0:
            return "Feliz"
        elif self.fome == 0:
            return "Faminto"
        elif self.tedio == 0:
            return "Entediado"
        else:
            return "Triste"


# Exemplo de uso
try:
    bichinho = BichinhoVirtual("Fofinho")
    print("Bichinho:", bichinho.nome)
    print("Humor inicial:", bichinho.humor())

    quantidade_comida = int(input("Digite a quantidade de comida fornecida: "))
    tempo_brincadeira = int(input("Digite o tempo de brincadeira em minutos: "))

    bichinho.alimentar(quantidade_comida)
    bichinho.brincar(tempo_brincadeira)

    print("Humor atual:", bichinho.humor())
except ValueError as e:
    print(f"Erro: {str(e)}")
