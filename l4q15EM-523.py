
#Lista de Exercício 4 - Questão 15
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#a.Mostre a quantidade de valores que foram lidos;
#b.Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#c.Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#d.Calcule e mostre a soma dos valores;
#e.Calcule e mostre a média dos valores;
#f.Calcule e mostre a quantidade de valores acima da média calculada;
#g.Calcule e mostre a quantidade de valores abaixo de sete;
#h.Encerre o programa com uma mensagem;


class Notas:
    def __init__(self):
        self.notas = []

    def ler_notas(self):
        while True:
            try:
                valor = float(input("Digite uma nota (-1 para encerrar): "))
                if valor == -1:
                    break
                self.notas.append(valor)
            except ValueError:
                print("Erro: Digite um valor numérico válido.")

    def quantidade_valores(self):
        return len(self.notas)

    def exibir_valores_ordem_insercao(self):
        print("Valores na ordem em que foram informados:", end=" ")
        for nota in self.notas:
            print(nota, end=" ")
        print()

    def exibir_valores_ordem_inversa(self):
        print("Valores na ordem inversa:")
        for nota in reversed(self.notas):
            print(nota)

    def calcular_soma(self):
        return sum(self.notas)

    def calcular_media(self):
        quantidade = self.quantidade_valores()
        if quantidade > 0:
            return self.calcular_soma() / quantidade
        else:
            return 0

    def quantidade_valores_acima_media(self):
        media = self.calcular_media()
        return sum(1 for nota in self.notas if nota > media)

    def quantidade_valores_abaixo_sete(self):
        return sum(1 for nota in self.notas if nota < 7)


def main():
    try:
        notas = Notas()
        notas.ler_notas()

        print("Quantidade de valores lidos:", notas.quantidade_valores())
        notas.exibir_valores_ordem_insercao()
        notas.exibir_valores_ordem_inversa()
        print("Soma dos valores:", notas.calcular_soma())
        print("Média dos valores:", notas.calcular_media())
        print("Quantidade de valores acima da média:", notas.quantidade_valores_acima_media())
        print("Quantidade de valores abaixo de sete:", notas.quantidade_valores_abaixo_sete())
        print("Programa encerrado.")
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print("Ocorreu um erro:", e)


if __name__ == "__main__":
    main()
