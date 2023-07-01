#Lista de Exercício 3 - Questão 44
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
#1 , 2, 3, 4  - Votos para os respectivos candidatos
#(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.



class Candidato:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.votos = 0


class Eleicao:
    def __init__(self):
        self.candidatos = {
            1: Candidato(1, "José"),
            2: Candidato(2, "João"),
            3: Candidato(3, "Maria"),
            4: Candidato(4, "Ana")
        }
        self.votos_nulos = 0
        self.votos_em_branco = 0
        self.total_votos = 0

    def receber_votos(self):
        while True:
            try:
                voto = int(input("Digite o código do candidato (ou 5 para voto nulo, 6 para voto em branco, ou 0 para encerrar): "))

                if voto == 0:
                    break

                if voto in self.candidatos:
                    self.candidatos[voto].votos += 1
                elif voto == 5:
                    self.votos_nulos += 1
                elif voto == 6:
                    self.votos_em_branco += 1
                else:
                    raise ValueError("Código inválido. Digite um código válido.")

                self.total_votos += 1

            except ValueError as ve:
                print(f"Erro: {ve}\n")

    def exibir_resultados(self):
        print("\nResultados:")
        for candidato in self.candidatos.values():
            votos = candidato.votos
            percentual = (votos / self.total_votos) * 100 if self.total_votos > 0 else 0
            print(f"{candidato.nome}: {votos} voto(s) - {percentual:.2f}%")

        percentual_nulos = (self.votos_nulos / self.total_votos) * 100 if self.total_votos > 0 else 0
        percentual_brancos = (self.votos_em_branco / self.total_votos) * 100 if self.total_votos > 0 else 0

        print(f"Votos nulos: {self.votos_nulos} voto(s) - {percentual_nulos:.2f}%")
        print(f"Votos em branco: {self.votos_em_branco} voto(s) - {percentual_brancos:.2f}%")
        print(f"Total de votos: {self.total_votos}")


def main():
    eleicao = Eleicao()
    eleicao.receber_votos()
    eleicao.exibir_resultados()


if __name__ == "__main__":
    main()
