#Lista de Exercício 3 - Questão 2

#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda


#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

class Autenticacao:
    def __init__(self):
        self.nome_usuario = None
        self.senha = None

    def solicitar_informacoes(self):
        # Solicita as informações de usuário e senha
        self.nome_usuario = input("Digite o nome de usuário: ")
        self.senha = input("Digite a senha: ")

    def verificar_senha(self):
        # Verifica se a senha é igual ao nome de usuário
        if self.senha == self.nome_usuario:
            raise ValueError("Erro: a senha não pode ser igual ao nome de usuário.")

    def cadastrar_usuario(self):
        while True:
            try:
                self.solicitar_informacoes()
                self.verificar_senha()
                print("Cadastro realizado com sucesso!")
                break
            except ValueError as error:
                print(error)
            except Exception as error:
                print("Ocorreu um erro durante o cadastro:", str(error))


# Programa principal
if __name__ == "__main__":
    autenticacao = Autenticacao()
    autenticacao.cadastrar_usuario()
