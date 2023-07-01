#Lista de Exercício 7 - Questão 7
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

#a.Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        if nova_fome >= 0:
            self.fome = nova_fome
        else:
            raise ValueError("Valor inválido para fome. Deve ser maior ou igual a zero.")

    def alterar_saude(self, nova_saude):
        if nova_saude >= 0:
            self.saude = nova_saude
        else:
            raise ValueError("Valor inválido para saúde. Deve ser maior ou igual a zero.")

    def alterar_idade(self, nova_idade):
        if nova_idade >= 0:
            self.idade = nova_idade
        else:
            raise ValueError("Valor inválido para idade. Deve ser maior ou igual a zero.")

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def calcular_humor(self):
        return self.fome + self.saude


# Exemplo de uso
bichinho = BichinhoVirtual("Fofinho", 5, 8, 2)

print(f"Nome: {bichinho.retornar_nome()}")
print(f"Fome: {bichinho.retornar_fome()}")
print(f"Saúde: {bichinho.retornar_saude()}")
print(f"Idade: {bichinho.retornar_idade()}")
print(f"Humor: {bichinho.calcular_humor()}")

try:
    bichinho.alterar_nome("Fofuxo")
    bichinho.alterar_fome(3)
    bichinho.alterar_saude(7)
    bichinho.alterar_idade(3)
    bichinho.alterar_fome(-1)  # Gerando uma exceção de valor inválido
except ValueError as e:
    print(f"Erro: {str(e)}")

print(f"Nome: {bichinho.retornar_nome()}")
print(f"Fome: {bichinho.retornar_fome()}")
print(f"Saúde: {bichinho.retornar_saude()}")
print(f"Idade: {bichinho.retornar_idade()}")
print(f"Humor: {bichinho.calcular_humor()}")
