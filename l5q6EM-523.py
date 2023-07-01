#Lista de Exercício 5 - Questão 6
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.


class ConversorHorario:
    def __init__(self):
        self.horas = 0
        self.minutos = 0

    def ler_horario(self):
        while True:
            try:
                horario = input("Digite o horário no formato HH:MM (24 horas): ")
                partes = horario.split(":")
                if len(partes) != 2:
                    raise ValueError("Formato inválido. Digite no formato HH:MM.")

                self.horas = int(partes[0])
                self.minutos = int(partes[1])

                if not (0 <= self.horas <= 23) or not (0 <= self.minutos <= 59):
                    raise ValueError("Horário inválido. Digite horas entre 0 e 23 e minutos entre 0 e 59.")

                break

            except ValueError as e:
                print("Erro:", str(e))

    def converter_para_12_horas(self):
        if self.horas == 0:
            horas_12 = 12
            periodo = 'A.M.'
        elif self.horas < 12:
            horas_12 = self.horas
            periodo = 'A.M.'
        elif self.horas == 12:
            horas_12 = 12
            periodo = 'P.M.'
        else:
            horas_12 = self.horas - 12
            periodo = 'P.M.'

        return horas_12, self.minutos, periodo

    def exibir_resultado(self, horas_12, minutos, periodo):
        print(f"A hora convertida é: {horas_12}:{minutos:02d} {periodo}")


conversor = ConversorHorario()

while True:
    conversor.ler_horario()
    horas_12, minutos, periodo = conversor.converter_para_12_horas()
    conversor.exibir_resultado(horas_12, minutos, periodo)

    repetir = input("Deseja converter outro valor? (S/N) ").upper()
    if repetir != 'S':
        break
