#Lista de Exercício 7 - Questão 6
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class Televisor:
    def __init__(self):
        self._canal = 1
        self._volume = 50

    def alterar_canal(self, novo_canal):
        if self._canal_valido(novo_canal):
            self._canal = novo_canal
            print(f"Canal alterado para {self._canal}")
        else:
            raise ValueError("Canal inválido")

    def aumentar_volume(self):
        if self._volume < 100:
            self._volume += 1
            print(f"Volume aumentado para {self._volume}")
        else:
            print("Volume máximo atingido")

    def diminuir_volume(self):
        if self._volume > 0:
            self._volume -= 1
            print(f"Volume diminuído para {self._volume}")
        else:
            print("Volume mínimo atingido")

    def exibir_canal(self):
        print(f"Canal atual: {self._canal}")

    def exibir_volume(self):
        print(f"Volume atual: {self._volume}")

    def _canal_valido(self, canal):
        return 1 <= canal <= 100


# Exemplo de uso
tv = Televisor()
tv.exibir_canal()
tv.exibir_volume()

try:
    tv.alterar_canal(5)
    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.diminuir_volume()
    tv.alterar_canal(150)
    tv.diminuir_volume()
except ValueError as e:
    print(str(e))

tv.exibir_canal()
tv.exibir_volume()

