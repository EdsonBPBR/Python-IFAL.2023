#Lista de Exercício 7 - Questão 11
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

#a.Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
#b.O consumo é especificado no construtor e o nível de combustível inicial é 0.
#c.Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
#d.Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
#e.Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
#meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
#meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
#meuFusca.andar(100);            # anda 100 quilômetros.
#meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        consumo_total = distancia / self.consumo
        if consumo_total <= self.combustivel:
            self.combustivel -= consumo_total
            print(f"O carro andou {distancia} quilômetros.")
        else:
            raise ValueError("Combustível insuficiente. O carro não pode andar essa distância.")

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, quantidade):
        if quantidade < 0:
            raise ValueError("A quantidade de combustível deve ser maior que zero.")
        self.combustivel += quantidade


# Exemplo de uso
try:
    meuFusca = Carro(15)  # 15 quilômetros por litro de combustível.
    meuFusca.adicionarGasolina(20)  # abastece com 20 litros de combustível.
    meuFusca.andar(100)  # anda 100 quilômetros.
    print(f"Combustível restante: {meuFusca.obterGasolina()} litros.")
except ValueError as e:
    print(f"Erro: {str(e)}")
