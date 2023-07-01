class Enquete:
    def __init__(self):
        self.opcoes = {
            1: "Windows Server",
            2: "Unix",
            3: "Linux",
            4: "Netware",
            5: "Mac OS",
            6: "Outro"
        }
        self.resultados = {opcao: 0 for opcao in self.opcoes.values()}

    def realizar_enquete(self):
        while True:
            try:
                voto = int(input("Digite o número correspondente ao sistema operacional (ou 0 para encerrar): "))
                if voto == 0:
                    break
                elif voto not in self.opcoes:
                    raise ValueError("Voto inválido. Tente novamente.")

                sistema_operacional = self.opcoes[voto]
                self.resultados[sistema_operacional] += 1

            except ValueError as error:
                print(str(error))

    def calcular_percentagens(self):
        total_votos = sum(self.resultados.values())
        percentagens = {sistema: (votos / total_votos) * 100 for sistema, votos in self.resultados.items()}
        return percentagens

    def exibir_resultado(self):
        print("Sistema Operacional     Votos   %")
        print("-------------------     -----   ---")
        percentagens = self.calcular_percentagens()
        for sistema, votos in self.resultados.items():
            percentual = percentagens[sistema]
            print(f"{sistema:<25}{votos:<7}{percentual:.1f}%")
        print("-------------------     -----")
        print(f"Total                    {sum(self.resultados.values())}")
        vencedor = max(self.resultados, key=self.resultados.get)
        print(
            f"\nO Sistema Operacional mais votado foi o {vencedor}, com {self.resultados[vencedor]} votos, correspondendo a {percentagens[vencedor]:.1f}% dos votos.")


# Execução do programa
enquete = Enquete()
enquete.realizar_enquete()
enquete.exibir_resultado()