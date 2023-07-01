#Lista de Exercício 3 - Questão 37
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes


class Cliente:
    def __init__(self, codigo, altura, peso):
        self.codigo = codigo
        self.altura = altura
        self.peso = peso


def realizar_senso():
    clientes = []

    while True:
        try:
            codigo = input("Digite o código do cliente (ou 0 para encerrar): ")
            if codigo == '0':
                break

            altura = float(input("Digite a altura do cliente em metros: "))
            peso = float(input("Digite o peso do cliente em kg: "))

            cliente = Cliente(codigo, altura, peso)
            clientes.append(cliente)

        except ValueError:
            print("Erro: Insira valores numéricos válidos.")

    return clientes


def obter_cliente_mais_alto(clientes):
    mais_alto = max(clientes, key=lambda c: c.altura)
    return mais_alto


def obter_cliente_mais_baixo(clientes):
    mais_baixo = min(clientes, key=lambda c: c.altura)
    return mais_baixo


def obter_cliente_mais_gordo(clientes):
    mais_gordo = max(clientes, key=lambda c: c.peso)
    return mais_gordo


def obter_cliente_mais_magro(clientes):
    mais_magro = min(clientes, key=lambda c: c.peso)
    return mais_magro


def calcular_media_alturas(clientes):
    if len(clientes) == 0:
        return 0

    soma_alturas = sum(c.altura for c in clientes)
    media_alturas = soma_alturas / len(clientes)
    return media_alturas


def calcular_media_pesos(clientes):
    if len(clientes) == 0:
        return 0

    soma_pesos = sum(c.peso for c in clientes)
    media_pesos = soma_pesos / len(clientes)
    return media_pesos


clientes = realizar_senso()

cliente_mais_alto = obter_cliente_mais_alto(clientes)
cliente_mais_baixo = obter_cliente_mais_baixo(clientes)
cliente_mais_gordo = obter_cliente_mais_gordo(clientes)
cliente_mais_magro = obter_cliente_mais_magro(clientes)

media_alturas = calcular_media_alturas(clientes)
media_pesos = calcular_media_pesos(clientes)

print("Cliente mais alto:")
print(f"Código: {cliente_mais_alto.codigo}, Altura: {cliente_mais_alto.altura}, Peso: {cliente_mais_alto.peso}")

print("Cliente mais baixo:")
print(f"Código: {cliente_mais_baixo.codigo}, Altura: {cliente_mais_baixo.altura}, Peso: {cliente_mais_baixo.peso}")

print("Cliente mais gordo:")
print(f"Código: {cliente_mais_gordo.codigo}, Altura: {cliente_mais_gordo.altura}, Peso: {cliente_mais_gordo.peso}")

print("Cliente mais magro:")
print(f"Código: {cliente_mais_magro.codigo}, Altura: {cliente_mais_magro.altura}, Peso: {cliente_mais_magro.peso}")

print("Média das alturas dos clientes:", media_alturas)
print("Média dos pesos dos clientes:", media_pesos)

