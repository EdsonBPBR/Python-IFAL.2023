#Lista de Exercício 4 - Questão 11
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

class VetorIntercale:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.vetores = []
        self.vetor_intercalado = []

    def ler_vetores(self):
        for i in range(3):
            vetor = []
            print(f"Digite os elementos do vetor {i+1}:")
            try:
                for j in range(self.tamanho):
                    elemento = int(input(f"Elemento {j+1}: "))
                    vetor.append(elemento)
                self.vetores.append(vetor)
            except ValueError:
                print("Erro: Digite um número inteiro válido.")
                return

    def intercalar_vetores(self):
        for i in range(self.tamanho):
            for vetor in self.vetores:
                self.vetor_intercalado.append(vetor[i])

    def exibir_vetor_intercalado(self):
        print("\nVetor intercalado:")
        for elemento in self.vetor_intercalado:
            print(elemento)


def main():
    try:
        tamanho_vetor = 10
        intercaler = VetorIntercale(tamanho_vetor)
        intercaler.ler_vetores()
        intercaler.intercalar_vetores()
        intercaler.exibir_vetor_intercalado()
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print("Ocorreu um erro:", e)


if __name__ == "__main__":
    main()
