#Lista de Exercício 3 - Questão 35
#Dupla: 2021327310 - Maria Raissa e 2021314590 - Edson Barros
#Disciplina: Programação Web
#Professor: Italo Arruda

#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.


class PrimeGenerator:
    def __init__(self,_number):
        self.max_number = max_number

    def is_prime(self, number):
        """Verifica se um número é primo."""
        if number < 2:
            return False

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False

        return True

    def generate_prime_list(self):
        """Gera uma lista de números primos até o número max_number."""
        primes = []
        for i in range(2, self.max_number + 1):
            if self.is_prime(i):
                primes.append(i)

        return primes


try:
    # Solicitar o número máximo ao usuário
    max_number = int(input("Digite um número inteiro: "))

    # Criar instância da classe PrimeGenerator
    prime_generator = PrimeGenerator(max_number)

    # Gerar a lista de números primos
    prime_list = prime_generator.generate_prime_list()

    # Exibir a lista de números primos
    print("Números primos até", max_number, ":")
    print(prime_list)

except ValueError:
    print("Erro: Você deve fornecer um número inteiro válido.")
