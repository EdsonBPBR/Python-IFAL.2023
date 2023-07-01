#Lista de Exercício 1 - Questão 18
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
class DownloadManager:
    def __init__(self, tamanho_arquivo, velocidade_internet):
        self.tamanho_arquivo = tamanho_arquivo
        self.velocidade_internet = velocidade_internet

    def calcular_tempo_download(self):
        if self.tamanho_arquivo <= 0:
            raise ValueError("O tamanho do arquivo deve ser um valor positivo.")

        if self.velocidade_internet <= 0:
            raise ValueError("A velocidade da Internet deve ser um valor positivo.")

        # Converte a velocidade para MBps (Megabytes por segundo)
        velocidade_mbps = self.velocidade_internet / 8
        # Calcula o tempo aproximado de download em segundos
        tempo_segundos = self.tamanho_arquivo / velocidade_mbps
        # Calcula o tempo aproximado de download em minutos
        tempo_minutos = tempo_segundos / 60

        return tempo_minutos

def main():
    try:
        tamanho_arquivo = float(input("Informe o tamanho do arquivo para download (em MB): "))
        velocidade_internet = float(input("Informe a velocidade do link de Internet (em Mbps): "))

        download_manager = DownloadManager(tamanho_arquivo, velocidade_internet)
        tempo_minutos = download_manager.calcular_tempo_download()

        print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos")

    except ValueError as e:
        print(f"Erro: {str(e)}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {str(e)}")

# Executa o programa
if __name__ == "__main__":
    main()
