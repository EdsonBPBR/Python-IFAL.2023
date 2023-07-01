# Lista de Exercício 3 - Questão 5
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.


class Pais:
    def __init__(self, nome):
        self.nome = nome
        self.populacao = None
        self.taxa_crescimento = None

    def ler_dados(self):
        while True:
            try:
                self.populacao = int(input(f"Informe a população do país {self.nome}: "))
                if self.populacao <= 0:
                    raise ValueError("A população deve ser um valor positivo.")

                self.taxa_crescimento = float(
                    input(f"Informe a taxa de crescimento do país {self.nome} (em decimal): "))
                if self.taxa_crescimento <= 0:
                    raise ValueError("A taxa de crescimento deve ser um valor positivo.")

                break

            except ValueError as error:
                print("Erro:", str(error))
                print("Por favor, informe valores válidos.")

    def calcular_anos_ultrapassagem(self, outro_pais):
        anos = 0

        while self.populacao < outro_pais.populacao:
            self.populacao += self.populacao * self.taxa_crescimento
            outro_pais.populacao += outro_pais.populacao * outro_pais.taxa_crescimento
            anos += 1

            if anos > 1000:
                raise ValueError(
                    f"A população do país {self.nome} não ultrapassará ou igualará a população do país {outro_pais.nome} em até 1000 anos.")

        return anos


def executar_calculo_populacional():
    pais_a = Pais("A")
    pais_b = Pais("B")

    pais_a.ler_dados()
    pais_b.ler_dados()

    try:
        anos = pais_a.calcular_anos_ultrapassagem(pais_b)
        print(
            f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")

    except ValueError as error:
        print("Erro:", str(error))

    resposta = input("Deseja repetir a operação? (s/n): ")
    if resposta.lower() == "s":
        executar_calculo_populacional()


executar_calculo_populacional()
