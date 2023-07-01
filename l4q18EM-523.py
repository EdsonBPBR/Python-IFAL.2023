#Lista de Exercício 4 - Questão 18
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:

#a.O total de votos computados;
#b.Os númeos e respectivos votos de todos os jogadores que receberam votos;
#c.O percentual de votos de cada um destes jogadores;
#d.O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
#Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.

#Enquete: Quem foi o melhor jogador?

#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 11
#Número do jogador (0=fim): 10
#Número do jogador (0=fim): 50
#Informe um valor entre 1 e 23 ou 0 para sair!
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 9
#Número do jogador (0=fim): 0

#Resultado da votação:

#Foram computados 8 votos.

#Jogador Votos           %
#9               4               50,0%
#10              3               37,5%
#11              1               12,5%
#O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.


class Enquete:
    def __init__(self):
        self.votos = [0] * 24

    def computar_voto(self, numero_jogador):
        if 1 <= numero_jogador <= 23:
            self.votos[numero_jogador] += 1
        else:
            raise ValueError("Número do jogador inválido!")

    def calcular_percentual(self, votos_jogador):
        total_votos = sum(self.votos)
        percentual = (votos_jogador / total_votos) * 100
        return percentual

    def obter_resultado(self):
        resultado = []
        for jogador, votos_jogador in enumerate(self.votos):
            if votos_jogador > 0:
                percentual = self.calcular_percentual(votos_jogador)
                resultado.append((jogador, votos_jogador, percentual))
        resultado.sort(key=lambda x: x[0])  # Ordena o resultado pelo número do jogador
        return resultado

    def obter_melhor_jogador(self):
        resultado = self.obter_resultado()
        melhor_jogador = max(resultado, key=lambda x: x[1])
        return melhor_jogador

    def gravar_resultado(self):
        resultado = self.obter_resultado()
        total_votos = sum(self.votos)

        with open('resultado_enquete.txt', 'w') as arquivo:
            arquivo.write("Resultado da votação:\n\n")
            arquivo.write("Foram computados {} votos.\n\n".format(total_votos))
            arquivo.write("Jogador\tVotos\t\t%\n")
            arquivo.write("==========================\n")
            for jogador, votos_jogador, percentual in resultado:
                arquivo.write("{}\t\t{}\t\t{:.1f}%\n".format(jogador, votos_jogador, percentual))


def main():
    enquete = Enquete()

    print("Enquete: Quem foi o melhor jogador?\n")

    while True:
        try:
            numero_jogador = int(input("Número do jogador (0=fim): "))
            if numero_jogador == 0:
                break
            enquete.computar_voto(numero_jogador)
        except ValueError as error:
            print(str(error))

    print("\nResultado da votação:\n")
    print("Foram computados {} votos.\n".format(sum(enquete.votos)))
    print("Jogador\tVotos\t\t%")
    print("==========================")
    for jogador, votos_jogador, percentual in enquete.obter_resultado():
        print("{}\t\t{}\t\t{:.1f}%".format(jogador, votos_jogador, percentual))

    melhor_jogador, votos_melhor_jogador, percentual_melhor_jogador = enquete.obter_melhor_jogador()

    print("\nO melhor jogador foi o número {}, com {} votos, correspondendo a {:.1f}% do total de votos.".format(
        melhor_jogador, votos_melhor_jogador, percentual_melhor_jogador))

    enquete.gravar_resultado()


if __name__ == '__main__':
    main()
