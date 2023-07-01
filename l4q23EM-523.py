#Lista de Exercício 4 - Questão 23 APARECE A MENSAGEM: Arquivo usuarios.txt não encontrado.
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
#alexandre       456123789
#anderson        1245698456
#antonio         123456456
#carlos          91257581
#cesar           987458
#rosemary        789456125
#Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
#ACME Inc.               Uso do espaço em disco pelos usuários
#------------------------------------------------------------------------
#Nr.  Usuário        Espaço utilizado     % do uso

#1    alexandre       434,99 MB             16,85%
#2    anderson       1187,99 MB             46,02%
#3    antonio         117,73 MB              4,56%
#4    carlos           87,03 MB              3,37%
#5    cesar             0,94 MB              0,04%
#6    rosemary        752,88 MB             29,16%

#Espaço total ocupado: 2581,57 MB
#Espaço médio ocupado: 430,26 MB

#O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

class Usuario:
    def __init__(self, nome, espaco):
        self.nome = nome
        self.espaco = espaco

    def converter_para_mb(self):
        return self.espaco / (1024 * 1024)


class Relatorio:
    def __init__(self, usuarios):
        self.usuarios = usuarios
        self.total_espaco = sum(usuario.espaco for usuario in self.usuarios)

    def gerar_relatorio(self):
        relatorio = "ACME Inc.               Uso do espaço em disco pelos usuários\n"
        relatorio += "-" * 72 + "\n"
        relatorio += "Nr.  Usuário        Espaço utilizado     % do uso\n\n"

        for i, usuario in enumerate(self.usuarios, 1):
            espaco_mb = usuario.converter_para_mb()
            percentual = (usuario.espaco / self.total_espaco) * 100

            relatorio += f"{i:<5}{usuario.nome:<15}{espaco_mb:15.2f} MB{percentual:15.2f}%\n"

        relatorio += "\nEspaço total ocupado: {:.2f} MB\n".format(self.total_espaco / (1024 * 1024))
        relatorio += "Espaço médio ocupado: {:.2f} MB\n".format(self.total_espaco / len(self.usuarios) / (1024 * 1024))

        return relatorio


def ler_usuarios():
    usuarios = []

    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                nome, espaco = linha.split()
                usuarios.append(Usuario(nome, int(espaco)))

    except FileNotFoundError:
        print("Arquivo usuarios.txt não encontrado.")
        return None

    except ValueError:
        print("Formato inválido no arquivo usuarios.txt.")
        return None

    return usuarios


def main():
    usuarios = ler_usuarios()

    if usuarios is not None:
        relatorio = Relatorio(usuarios)
        relatorio_texto = relatorio.gerar_relatorio()

        try:
            with open("relatorio.txt", "w") as arquivo:
                arquivo.write(relatorio_texto)
            print("Relatório gerado com sucesso.")

        except PermissionError:
            print("Sem permissão para escrever no arquivo relatorio.txt.")


if __name__ == "__main__":
    main()
