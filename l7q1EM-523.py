#Lista de Exercício 7 - Questão 1
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

# Classe Bola: Crie uma classe que modele uma bola:
#a.Atributos: Cor, circunferência, material
#b.Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor


def main():
    try:
        cor = input("Digite a cor da bola: ")
        circunferencia = float(input("Digite a circunferência da bola: "))
        material = input("Digite o material da bola: ")

        bola = Bola(cor, circunferencia, material)

        print("Cor da bola:", bola.mostraCor())

        nova_cor = input("Digite a nova cor da bola: ")
        bola.trocaCor(nova_cor)

        print("Cor da bola após troca:", bola.mostraCor())

    except ValueError:
        print("Erro: Valor inválido para a circunferência.")
    except Exception as e:
        print("Ocorreu um erro:", str(e))


if __name__ == '__main__':
    main()

