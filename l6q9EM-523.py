#Lista de Exercício 6 - Questão 9
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

class CPF:
    def __init__(self, cpf):
        self.cpf = self._remover_formatacao(cpf)

    def _remover_formatacao(self, cpf):
        return cpf.replace(".", "").replace("-", "")

    def _calcular_digito_verificador(self, digitos):
        soma = 0
        for i, digito in enumerate(digitos):
            soma += int(digito) * (len(digitos) + 1 - i)
        digito = 11 - (soma % 11)
        return digito if digito < 10 else 0

    def _validar_digitos_verificadores(self):
        digitos = self.cpf[:-2]
        digito1 = self._calcular_digito_verificador(digitos)
        digito2 = self._calcular_digito_verificador(digitos + str(digito1))
        return self.cpf[-2:] == str(digito1) + str(digito2)

    def validar_cpf(self):
        try:
            if len(self.cpf) != 11 or not self.cpf.isdigit():
                raise ValueError("CPF deve conter 11 dígitos numéricos.")
            if self.cpf == self.cpf[0] * 11:
                raise ValueError("CPF inválido.")

            if not self._validar_digitos_verificadores():
                raise ValueError("CPF inválido.")

            return True

        except ValueError as error:
            print(f"Erro: {error}")
            return False


# Solicitar o CPF ao usuário
cpf_input = input("Digite o CPF no formato xxx.xxx.xxx-xx: ")

# Criar objeto CPF
cpf = CPF(cpf_input)

# Verificar se o CPF é válido
if cpf.validar_cpf():
    print("CPF válido.")
else:
    print("CPF inválido.")
