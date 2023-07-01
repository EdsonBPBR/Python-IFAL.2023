
#Lista de Exercício 5 - Questão 11
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.


class Data:
    def __init__(self, data):
        self.dia, self.mes, self.ano = self.validar_data(data)

    def validar_data(self, data):
        partes_data = data.split('/')
        if len(partes_data) != 3:
            raise ValueError("Formato de data inválido.")

        dia, mes, ano = partes_data

        try:
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
        except ValueError:
            raise ValueError("Valores de dia, mês ou ano inválidos.")

        meses = {
            1: 'janeiro',
            2: 'fevereiro',
            3: 'março',
            4: 'abril',
            5: 'maio',
            6: 'junho',
            7: 'julho',
            8: 'agosto',
            9: 'setembro',
            10: 'outubro',
            11: 'novembro',
            12: 'dezembro'
        }

        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido.")

        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido.")

        if mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if dia > 29:
                    raise ValueError("Dia inválido para o mês de fevereiro em ano bissexto.")
            elif dia > 28:
                raise ValueError("Dia inválido para o mês de fevereiro.")

        if mes in [4, 6, 9, 11] and dia > 30:
            raise ValueError("Dia inválido para o mês informado.")

        return dia, mes, ano

    def formatar_data_extenso(self):
        meses = {
            1: 'janeiro',
            2: 'fevereiro',
            3: 'março',
            4: 'abril',
            5: 'maio',
            6: 'junho',
            7: 'julho',
            8: 'agosto',
            9: 'setembro',
            10: 'outubro',
            11: 'novembro',
            12: 'dezembro'
        }

        return f"{self.dia} de {meses[self.mes]} de {self.ano}"


def obter_data_extenso(data):
    try:
        data_obj = Data(data)
        return data_obj.formatar_data_extenso()
    except ValueError as ve:
        print(f"Erro: {ve}")
        return None


# Exemplo de uso
data = input("Digite uma data no formato DD/MM/AAAA: ")
data_extenso = obter_data_extenso(data)
if data_extenso is not None:
    print(data_extenso)
else:
    print("Data inválida.")

