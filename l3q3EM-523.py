#Lista de Exercício 3 - Questão 3

#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia e valide as seguintes informações:
#a.Nome: maior que 3 caracteres;
#b.Idade: entre 0 e 150;
#c.Salário: maior que zero;
#d.Sexo: 'f' ou 'm';
#e.Estado Civil: 's', 'c', 'v', 'd';


class Validador:
    def __init__(self, mensagem, validacao):
        self.mensagem = mensagem
        self.validacao = validacao

    def validar(self, valor):
        return self.validacao(valor)


class Pessoa:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.salario = None
        self.sexo = None
        self.estado_civil = None

    def obter_informacao(self, validador):
        while True:
            try:
                valor = input(validador.mensagem)
                validador.validar(valor)
                return valor
            except ValueError as error:
                print("Erro de validação:", str(error))

    def preencher_informacoes(self):
        validadores = [
            Validador("Digite seu nome: ", self.validar_nome),
            Validador("Digite sua idade: ", self.validar_idade),
            Validador("Digite seu salário: ", self.validar_salario),
            Validador("Digite seu sexo (f/m): ", self.validar_sexo),
            Validador("Digite seu estado civil (s/c/v/d): ", self.validar_estado_civil)
        ]

        for validador in validadores:
            valor = self.obter_informacao(validador)

            if validador.mensagem.startswith("Digite seu nome"):
                self.nome = valor
            elif validador.mensagem.startswith("Digite sua idade"):
                self.idade = int(valor)
            elif validador.mensagem.startswith("Digite seu salário"):
                self.salario = float(valor)
            elif validador.mensagem.startswith("Digite seu sexo"):
                self.sexo = valor
            elif validador.mensagem.startswith("Digite seu estado civil"):
                self.estado_civil = valor

    @staticmethod
    def validar_nome(nome):
        if len(nome) <= 3:
            raise ValueError("O nome deve ter mais de 3 caracteres.")

    @staticmethod
    def validar_idade(idade):
        if not 0 <= int(idade) <= 150:
            raise ValueError("A idade deve estar entre 0 e 150.")

    @staticmethod
    def validar_salario(salario):
        if float(salario) <= 0:
            raise ValueError("O salário deve ser maior que zero.")

    @staticmethod
    def validar_sexo(sexo):
        if sexo.lower() not in ['f', 'm']:
            raise ValueError("O sexo deve ser 'f' ou 'm'.")

    @staticmethod
    def validar_estado_civil(estado_civil):
        if estado_civil.lower() not in ['s', 'c', 'v', 'd']:
            raise ValueError("O estado civil deve ser 's', 'c', 'v' ou 'd'.")


pessoa = Pessoa()
pessoa.preencher_informacoes()

print("Informações válidas:")
print("Nome:", pessoa.nome)
print("Idade:", pessoa.idade)
print("Salário:", pessoa.salario)
print("Sexo:", pessoa.sexo)
print("Estado Civil:", pessoa.estado_civil)
