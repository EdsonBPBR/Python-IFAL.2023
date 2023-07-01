# Lista de Exercício 4 - Questão 20
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.

class Colaborador:
    def __init__(self, salario):
        self.salario = salario
        self.abono = 0

    def calcular_abono(self):
        self.abono = self.salario * 0.2
        if self.abono < 100:
            self.abono = 100


class GastosAbono:
    def __init__(self):
        self.colaboradores = []

    def adicionar_colaborador(self, salario):
        colaborador = Colaborador(salario)
        colaborador.calcular_abono()
        self.colaboradores.append(colaborador)

    def calcular_total_colaboradores(self):
        return len(self.colaboradores)

    def calcular_total_abono(self):
        return sum(colaborador.abono for colaborador in self.colaboradores)

    def calcular_valor_minimo_pago(self):
        return sum(1 for colaborador in self.colaboradores if colaborador.abono == 100)

    def calcular_maior_valor_abono(self):
        return max(colaborador.abono for colaborador in self.colaboradores)

    def exibir_projecao_gastos(self):
        print("Projeção de Gastos com Abono")
        print("============================\n")
        print("Salário\t\t- Abono")

        for colaborador in self.colaboradores:
            print(f"R$ {colaborador.salario:.2f}\t- R$ {colaborador.abono:.2f}")

        total_colaboradores = self.calcular_total_colaboradores()
        total_abono = self.calcular_total_abono()
        valor_minimo_pago = self.calcular_valor_minimo_pago()
        maior_valor_abono = self.calcular_maior_valor_abono()

        print(f"\nForam processados {total_colaboradores} colaboradores")
        print(f"Total gasto com abonos: R$ {total_abono:.2f}")
        print(f"Valor mínimo pago a {valor_minimo_pago} colaboradores")
        print(f"Maior valor de abono pago: R$ {maior_valor_abono:.2f}")


def main():
    gastos_abono = GastosAbono()

    while True:
        try:
            salario = float(input("Salário: "))
            if salario == 0:
                break
            gastos_abono.adicionar_colaborador(salario)
        except ValueError:
            print("Valor inválido! Digite um número válido.")

    gastos_abono.exibir_projecao_gastos()


if __name__ == '__main__':
    main()

