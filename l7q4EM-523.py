# Lista de Exercício 7 - Questão 4
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Classe Pessoa: Crie uma classe que modele uma pessoa:


#Classe Pessoa: Crie uma classe que modele uma pessoa:

#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self._nome = None
        self._idade = None
        self._peso = None
        self._altura = None
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome da pessoa deve ser informado.")
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            raise ValueError("A idade da pessoa deve ser maior ou igual a zero.")
        self._idade = nova_idade

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, novo_peso):
        if novo_peso < 0:
            raise ValueError("O peso da pessoa deve ser maior ou igual a zero.")
        self._peso = novo_peso

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, nova_altura):
        if nova_altura < 0:
            raise ValueError("A altura da pessoa deve ser maior ou igual a zero.")
        self._altura = nova_altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, quantidade):
        self.peso += quantidade

    def emagrecer(self, quantidade):
        self.peso -= quantidade

    def crescer(self, quantidade):
        self.altura += quantidade


def main():
    try:
        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))
        peso = float(input("Digite o peso da pessoa: "))
        altura = float(input("Digite a altura da pessoa: "))

        pessoa = Pessoa(nome, idade, peso, altura)

        print("\nDados iniciais:")
        print("Nome:", pessoa.nome)
        print("Idade:", pessoa.idade)
        print("Peso:", pessoa.peso)
        print("Altura:", pessoa.altura)

        pessoa.envelhecer()
        pessoa.engordar(5)
        pessoa.emagrecer(2)

        print("\nDados atualizados:")
        print("Nome:", pessoa.nome)
        print("Idade:", pessoa.idade)
        print("Peso:", pessoa.peso)
        print("Altura:", pessoa.altura)

    except ValueError as e:
        print("Erro:", str(e))


if __name__ == "__main__":
    main()

