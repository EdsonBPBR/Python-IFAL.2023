#Lista de Exercício 2 - Questão 18
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

class Data:
    def __init__(self, data_str):
        self.data_str = data_str
        self.dia, self.mes, self.ano = self.obter_valores()

    def obter_valores(self):
        try:
            return map(int, self.data_str.split('/'))
        except (ValueError, IndexError):
            return None, None, None

    def validar_data(self):
        if self.dia is None or self.mes is None or self.ano is None:
            return False

        if self.dia < 1 or self.dia > 31:
            return False
        if self.mes < 1 or self.mes > 12:
            return False
        if self.ano < 1:
            return False

        if (self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11) and self.dia > 30:
            return False

        if self.mes == 2:
            if (self.ano % 4 == 0 and self.ano % 100 != 0) or self.ano % 400 == 0:
                if self.dia > 29:
                    return False
            elif self.dia > 28:
                return False

        return True


def verificar_data():
    try:
        data_str = input("Digite uma data no formato dd/mm/aaaa: ")
        data = Data(data_str)

        if data.validar_data():
            print("A data é válida.")
        else:
            print("A data é inválida.")

    except Exception as error:
        print("Ocorreu um erro:", str(error))


verificar_data()
