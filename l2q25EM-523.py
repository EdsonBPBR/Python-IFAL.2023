#Lista de Exercício 2 - Questão 25
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a."Telefonou para a vítima?"
#b."Esteve no local do crime?"
#c."Mora perto da vítima?"
#d."Devia para a vítima?"
#e."Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

class InvestigacaoCrime:
    def __init__(self):
        self.respostas = []

    def fazer_perguntas(self):
        perguntas = [
            "Telefonou para a vítima?",
            "Esteve no local do crime?",
            "Mora perto da vítima?",
            "Devia para a vítima?",
            "Já trabalhou com a vítima?"
        ]

        for pergunta in perguntas:
            while True:
                resposta = self.obter_resposta(pergunta)
                if resposta is not None:
                    self.respostas.append(resposta)
                    break

    def obter_resposta(self, pergunta):
        try:
            resposta = input(pergunta + " (Sim/Não): ")
            resposta = resposta.lower()
            if resposta in ["sim", "não"]:
                return resposta
            else:
                raise ValueError("Resposta inválida. Digite 'Sim' ou 'Não'.")
        except ValueError as error:
            print(f"Erro: {str(error)}")
            return None

    def classificar_participacao(self):
        respostas_positivas = self.respostas.count("sim")

        if respostas_positivas == 2:
            return "Suspeita"
        elif 3 <= respostas_positivas <= 4:
            return "Cúmplice"
        elif respostas_positivas == 5:
            return "Assassino"
        else:
            return "Inocente"

    def exibir_classificacao(self, classificacao):
        print("Classificação:", classificacao)

    def executar_investigacao(self):
        self.fazer_perguntas()
        classificacao = self.classificar_participacao()
        self.exibir_classificacao(classificacao)


investigacao = InvestigacaoCrime()
investigacao.executar_investigacao()
