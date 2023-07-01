#Lista de Exercício 3 - Questão 36
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7

#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

class TabuadaGenerator:
    def __init__(self, numero, inicio, fim):
        self.numero = numero
        self.inicio = inicio
        self.fim = fim

    def gerar_tabuada(self):
        """Gera a tabuada do número no intervalo especificado."""
        if self.fim < self.inicio:
            raise ValueError("O valor final não pode ser menor que o valor inicial.")

        tabuada = []
        for i in range(self.inicio, self.fim + 1):
            resultado = self.numero * i
            tabuada.append(f"{self.numero} X {i} = {resultado}")

        return tabuada


try:
    # Solicitar o número para a tabuada
    numero = int(input("Montar a tabuada de: "))

    # Solicitar os valores inicial e final
    inicio = int(input("Começar por: "))
    fim = int(input("Terminar em: "))

    # Criar instância da classe TabuadaGenerator
    tabuada_generator = TabuadaGenerator(numero, inicio, fim)

    # Gerar a tabuada
    tabuada = tabuada_generator.gerar_tabuada()

    # Exibir a tabuada
    print(f"Vou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:")
    for item in tabuada:
        print(item)

except ValueError as e:
    print(f"Erro: {str(e)}")
