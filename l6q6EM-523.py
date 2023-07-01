#Lista de Exercício 6 - Questão 6
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda



#Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

#Data de Nascimento: 29/10/1973
#Você nasceu em  29 de Outubro de 1973.

class DataPorExtenso:
    def __init__(self):
        self.data_nascimento = ""

    def obter_data_nascimento(self):
        self.data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

    def imprimir_data_por_extenso(self):
        try:
            dia, mes, ano = map(int, self.data_nascimento.split('/'))
            meses = [
                'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
            ]

            if 1 <= dia <= 31 and 1 <= mes <= 12:
                mes_extenso = meses[mes - 1]
                print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")
            else:
                print("Data de nascimento inválida.")
        except ValueError:
            print("Formato de data inválido.")


# Exemplo de uso
data_por_extenso = DataPorExtenso()
data_por_extenso.obter_data_nascimento()
data_por_extenso.imprimir_data_por_extenso()

