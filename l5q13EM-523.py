
#Lista de Exercício 5 - Questão 13
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.


class MolduraRetangulo:
    def __init__(self, linhas=1, colunas=1):
        self.linhas = self.validar_valor(linhas, 1, 20)
        self.colunas = self.validar_valor(colunas, 1, 20)

    def validar_valor(self, valor, valor_min, valor_max):
        try:
            valor = int(valor)
            valor = max(valor_min, min(valor_max, valor))
        except ValueError:
            valor = valor_min
        return valor

    def desenhar(self):
        print('+' + '-' * self.colunas + '+')
        for _ in range(self.linhas):
            print('|' + ' ' * self.colunas + '|')
        print('+' + '-' * self.colunas + '+')


def desenhar_moldura(linhas=1, colunas=1):
    try:
        moldura = MolduraRetangulo(linhas, colunas)
        moldura.desenhar()
    except Exception as e:
        print(f"Erro: {e}")


# Exemplo de uso
linhas = input("Informe o número de linhas (entre 1 e 20): ")
colunas = input("Informe o número de colunas (entre 1 e 20): ")
desenhar_moldura(linhas, colunas)



