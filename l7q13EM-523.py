#Lista de Exercício 7 - Questão 13
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

class Funcionario:
    def __init__(self, nome, salario):
        if not isinstance(nome, str) or nome == "":
            raise ValueError("O nome do funcionário deve ser uma string não vazia.")
        if not isinstance(salario, float) and not isinstance(salario, int) or salario < 0:
            raise ValueError("O salário do funcionário deve ser um número positivo.")
        self.nome = nome
        self.salario = float(salario)

    def obterNome(self):
        return self.nome

    def obterSalario(self):
        return self.salario


# Exemplo de uso
try:
    funcionario = Funcionario("João", 2000.0)
    print("Nome do funcionário:", funcionario.obterNome())
    print("Salário do funcionário:", funcionario.obterSalario())
except ValueError as e:
    print(f"Erro: {str(e)}")
