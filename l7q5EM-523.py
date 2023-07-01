# Lista de Exercício 7 - Questão 5
# Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
# Disciplina: Programação Web
# Professor: Italo Arruda

# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self._numero_conta = None
        self._nome_correntista = None
        self._saldo = None
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    @property
    def numero_conta(self):
        return self._numero_conta

    @numero_conta.setter
    def numero_conta(self, novo_numero_conta):
        if not novo_numero_conta:
            raise ValueError("O número da conta deve ser informado.")
        self._numero_conta = novo_numero_conta

    @property
    def nome_correntista(self):
        return self._nome_correntista

    @nome_correntista.setter
    def nome_correntista(self, novo_nome_correntista):
        if not novo_nome_correntista:
            raise ValueError("O nome do correntista deve ser informado.")
        self._nome_correntista = novo_nome_correntista

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            raise ValueError("O saldo da conta corrente deve ser maior ou igual a zero.")
        self._saldo = novo_saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor


def main():
    try:
        numero_conta = input("Digite o número da conta corrente: ")
        nome_correntista = input("Digite o nome do correntista: ")
        saldo = float(input("Digite o saldo inicial da conta corrente: "))

        conta = ContaCorrente(numero_conta, nome_correntista, saldo)

        print("\nDados iniciais:")
        print("Número da conta:", conta.numero_conta)
        print("Nome do correntista:", conta.nome_correntista)
        print("Saldo:", conta.saldo)

        novo_nome = input("Digite o novo nome do correntista: ")
        conta.alterarNome(novo_nome)

        valor_deposito = float(input("Digite o valor do depósito: "))
        conta.deposito(valor_deposito)

        valor_saque = float(input("Digite o valor do saque: "))
        conta.saque(valor_saque)

        print("\nDados atualizados:")
        print("Número da conta:", conta.numero_conta)
        print("Nome do correntista:", conta.nome_correntista)
        print("Saldo:", conta.saldo)

    except ValueError as e:
        print("Erro:", str(e))


if __name__ == "__main__":
    main()

