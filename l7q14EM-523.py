#Lista de Exercício 7 - Questão 14
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
#Exemplo de uso:
  #harry=funcionário("Harry",25000)
  #harry.aumentarSalario(10)

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obterNome(self):
        return self.nome

    def obterSalario(self):
        return self.salario

    def aumentarSalario(self, porcentualDeAumento):
        if not isinstance(porcentualDeAumento, (float, int)) or porcentualDeAumento < 0:
            raise ValueError("O porcentual de aumento deve ser um número positivo.")
        aumento = self.salario * (porcentualDeAumento / 100)
        self.salario += aumento


# Exemplo de uso
try:
    harry = Funcionario("Harry", 25000)
    print("Salário atual de Harry:", harry.obterSalario())

    harry.aumentarSalario(10)
    print("Salário após aumento de 10%:", harry.obterSalario())
except ValueError as e:
    print(f"Erro: {str(e)}")
