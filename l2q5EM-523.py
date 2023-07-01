
#Lista de Exercício 2 - Questão 5
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

class Aluno:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        if self.nota1 < 0 or self.nota1 > 10 or self.nota2 < 0 or self.nota2 > 10:
            raise ValueError("As notas devem estar entre 0 e 10.")

        media = (self.nota1 + self.nota2) / 2
        return media

    def verificar_aprovacao(self):
        media = self.calcular_media()

        if media == 10:
            return "Aprovado com Distinção"
        elif media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    aluno = Aluno(nota1, nota2)
    resultado = aluno.verificar_aprovacao()

    print(resultado)

except ValueError as e:
    print(f"Erro: {e}")
