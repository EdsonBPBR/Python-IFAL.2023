# Lista de Exercício 7 - Questão 16
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.

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

    def __str__(self):
        return f"Bichinho: {self.nome}\nNível de fome: {self.fome}\nNível de tédio: {self.tedio}"


def exibir_menu():
    print("\nOpções:")
    print("1 - Alimentar")
    print("2 - Brincar")
    print("3 - Mostrar humor")
    print("4 - Opção secreta")


# Exemplo de uso
try:
    nome_bichinho = input("Digite o nome do bichinho virtual: ")
    bichinho = BichinhoVirtual(nome_bichinho)

    print(f"Bem-vindo(a) ao {nome_bichinho} - Bichinho Virtual!")

    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            quantidade_comida = int(input("Digite a quantidade de comida fornecida: "))
            bichinho.alimentar(quantidade_comida)
        elif opcao == 2:
            tempo_brincadeira = int(input("Digite o tempo de brincadeira em minutos: "))
            bichinho.brincar(tempo_brincadeira)
        elif opcao == 3:
            print("Humor atual:", bichinho.humor())
        elif opcao == 4:
            print(bichinho)  # Porta escondida: Mostra os valores exatos dos atributos do objeto
        else:
            print("Opção inválida. Escolha novamente.")

except ValueError as e:
    print(f"Erro: {str(e)}")
