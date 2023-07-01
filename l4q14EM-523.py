#Lista de Exercício 4 - Questão 14
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a."Telefonou para a vítima?"
#b."Esteve no local do crime?"
#c."Mora perto da vítima?"
#d."Devia para a vítima?"
#e."Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

class InvestigacaoCrime:
    def __init__(self):
        self.perguntas = [
            "Telefonou para a vítima?",
            "Esteve no local do crime?",
            "Mora perto da vítima?",
            "Devia para a vítima?",
            "Já trabalhou com a vítima?"
        ]
        self.respostas = []

    def fazer_perguntas(self):
        for pergunta in self.perguntas:
            while True:
                try:
                    resposta = input(pergunta + " (Sim/Não): ")
                    if resposta.lower() == "sim":
                        self.respostas.append(True)
                    elif resposta.lower() == "não":
                        self.respostas.append(False)
                    else:
                        raise ValueError
                    break
                except ValueError:
                    print("Erro: Digite uma resposta válida (Sim/Não).")

    def classificar_participacao(self):
        quantidade_positivas = sum(self.respostas)
        if quantidade_positivas == 2:
            return "Suspeita"
        elif 3 <= quantidade_positivas <= 4:
            return "Cúmplice"
        elif quantidade_positivas == 5:
            return "Assassino"
        else:
            return "Inocente"


def main():
    try:
        print("Responda às seguintes perguntas sobre o crime (Sim/Não):")
        investigacao = InvestigacaoCrime()
        investigacao.fazer_perguntas()
        classificacao = investigacao.classificar_participacao()
        print("\nClassificação: {}".format(classificacao))
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print("Ocorreu um erro:", e)


if __name__ == "__main__":
    main()
