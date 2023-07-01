#Lista de Exercício 4 - Questão 22
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
#Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
#necessita da esfera;
#necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
#Quantidade de mouses: 100

#Situação                        Quantidade              Percentual
#1- necessita da esfera                  40                     40%
#2- necessita de limpeza                 30                     30%
#3- necessita troca do cabo ou conector  15                     15%
#4- quebrado ou inutilizado              15                     15%


class Mouse:
    def __init__(self, identificacao, defeito):
        self.identificacao = identificacao
        self.defeito = defeito


class MouseInventory:
    def __init__(self):
        self.mouses = []

    def adicionar_mouse(self, identificacao, defeito):
        mouse = Mouse(identificacao, defeito)
        self.mouses.append(mouse)

    def gerar_relatorio(self):
        total_mouses = len(self.mouses)

        situacoes = {
            "necessita da esfera": 0,
            "necessita de limpeza": 0,
            "necessita troca do cabo ou conector": 0,
            "quebrado ou inutilizado": 0
        }

        for mouse in self.mouses:
            situacoes[mouse.defeito] += 1

        print("Quantidade de mouses:", total_mouses, "\n")
        print("Situação\t\tQuantidade\t\tPercentual")
        for defeito, quantidade in situacoes.items():
            percentual = (quantidade / total_mouses) * 100
            print(defeito, "\t\t", quantidade, "\t\t", percentual, "%")


def main():
    inventory = MouseInventory()

    while True:
        try:
            identificacao = int(input("Digite o número de identificação do mouse (ou 0 para sair): "))
            if identificacao == 0:
                break

            defeito = int(input("Digite o tipo de defeito:\n1 - necessita da esfera\n2 - necessita de limpeza\n3 - necessita troca do cabo ou conector\n4 - quebrado ou inutilizado\n"))

            if defeito < 1 or defeito > 4:
                raise ValueError("Opção inválida!")

            inventory.adicionar_mouse(identificacao, defeito)

        except ValueError as e:
            print("Erro:", e)
            continue

    inventory.gerar_relatorio()


if __name__ == "__main__":
    main()
