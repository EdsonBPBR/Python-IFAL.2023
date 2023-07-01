#Lista de Exercício 7 - Questão 8
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        if isinstance(alimento, str):
            self.bucho.append(alimento)
        else:
            raise ValueError("O alimento deve ser uma string.")

    def verBucho(self):
        if self.bucho:
            print(f"O bucho do macaco {self.nome} contém: {', '.join(self.bucho)}")
        else:
            print(f"O bucho do macaco {self.nome} está vazio.")

    def digerir(self):
        if self.bucho:
            print(f"O macaco {self.nome} está digerindo...")
            self.bucho = []
        else:
            print(f"O bucho do macaco {self.nome} já está vazio.")


def testar_macacos():
    macaco1 = Macaco("Bob")
    macaco2 = Macaco("Alice")

    try:
        macaco1.comer("banana")
        macaco1.comer("maçã")
        macaco1.comer(123)  # Tentando comer um alimento inválido (número)
    except ValueError as e:
        print(e)

    macaco1.verBucho()
    macaco2.verBucho()

    macaco2.comer("cenoura")
    macaco2.comer("uva")
    macaco2.comer("morango")

    macaco1.verBucho()
    macaco2.verBucho()

    macaco1.digerir()
    macaco2.digerir()

    macaco1.verBucho()
    macaco2.verBucho()

    macaco1.comer(macaco2.nome)

    macaco1.verBucho()
    macaco2.verBucho()

    macaco1.digerir()
    macaco1.verBucho()


# Executa o programa de teste
testar_macacos()

