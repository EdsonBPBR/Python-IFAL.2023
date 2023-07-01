#Lista de Exercício 3 - Questão 40
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#Código da cidade;
#Número de veículos de passeio (em 1999);
#Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#Qual a média de veículos nas cinco cidades juntas;
#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.


class Cidade:
    def __init__(self, codigo, veiculos, acidentes):
        self.codigo = codigo
        self.veiculos = veiculos
        self.acidentes = acidentes


def ler_dados_cidades():
    cidades = []

    for i in range(1, 6):
        while True:
            try:
                codigo = int(input(f"Digite o código da {i}ª cidade: "))
                veiculos = int(input(f"Digite o número de veículos de passeio em 1999 da {i}ª cidade: "))
                acidentes = int(input(f"Digite o número de acidentes de trânsito com vítimas em 1999 da {i}ª cidade: "))
                cidade = Cidade(codigo, veiculos, acidentes)
                cidades.append(cidade)
                break
            except ValueError:
                print("Erro: Insira valores numéricos válidos.")

    return cidades


def obter_maior_indice_acidentes(cidades):
    cidade_maior_indice = max(cidades, key=lambda c: c.acidentes)
    return cidade_maior_indice


def obter_menor_indice_acidentes(cidades):
    cidade_menor_indice = min(cidades, key=lambda c: c.acidentes)
    return cidade_menor_indice


def calcular_media_veiculos(cidades):
    total_veiculos = sum(cidade.veiculos for cidade in cidades)
    media_veiculos = total_veiculos / len(cidades)
    return media_veiculos


def calcular_media_acidentes_menos_2000_veiculos(cidades):
    cidades_menos_2000 = [cidade for cidade in cidades if cidade.veiculos < 2000]
    if len(cidades_menos_2000) == 0:
        return 0

    total_acidentes = sum(cidade.acidentes for cidade in cidades_menos_2000)
    media_acidentes = total_acidentes / len(cidades_menos_2000)
    return media_acidentes


def exibir_resultados(cidade_maior_indice, cidade_menor_indice, media_veiculos, media_acidentes_menos_2000_veiculos):
    print("Maior índice de acidentes de trânsito:")
    print(f"Cidade: {cidade_maior_indice.codigo}, Índice: {cidade_maior_indice.acidentes}")

    print("Menor índice de acidentes de trânsito:")
    print(f"Cidade: {cidade_menor_indice.codigo}, Índice: {cidade_menor_indice.acidentes}")

    print("Média de veículos nas cinco cidades:")
    print(f"Média: {media_veiculos}")

    print("Média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio:")
    print(f"Média: {media_acidentes_menos_2000_veiculos}")


cidades = ler_dados_cidades()

cidade_maior_indice = obter_maior_indice_acidentes(cidades)
cidade_menor_indice = obter_menor_indice_acidentes(cidades)

media_veiculos = calcular_media_veiculos(cidades)
media_acidentes_menos_2000_veiculos = calcular_media_acidentes_menos_200
