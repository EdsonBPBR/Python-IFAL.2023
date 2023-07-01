#Lista de Exercício 7 - Questão 12
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.

class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        if taxa_juros < 0:
            raise ValueError("A taxa de juros não pode ser negativa.")
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros

    def adicioneJuros(self):
        juros = self.saldo * self.taxa_juros / 100
        self.saldo += juros

    def obterSaldo(self):
        return self.saldo


# Exemplo de uso
try:
    poupanca = ContaInvestimento(1000.00, 10)  # Saldo inicial de R$1000,00 e taxa de juros de 10%

    for _ in range(5):
        poupanca.adicioneJuros()

    saldo_resultante = poupanca.obterSaldo()
    print(f"Saldo resultante: R${saldo_resultante:.2f}")
except ValueError as e:
    print(f"Erro: {str(e)}")
