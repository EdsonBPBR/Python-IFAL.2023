import tkinter as tk
from tkinter import ttk
import subprocess
import glob
import re
import sys

def executar_questao(questao):
    comando = [sys.executable, questao]
    subprocess.run(comando)

def pesquisar_questao():
    arquivo = entry_pesquisa.get()
    for botao in botoes:
        if arquivo == botao["text"]:
            executar_questao(arquivo)
            return
    label_status.configure(text="Questão inexistente")

janela = tk.Tk()
janela.title("Lista de Exercícios")
janela.configure(bg="green")

frame_principal = tk.Frame(janela, bg="green")
frame_principal.pack(fill="both", expand=True, padx=10, pady=10)

frame_pesquisa = tk.Frame(frame_principal, bg="green")
frame_pesquisa.pack(fill="x")

entry_pesquisa = tk.Entry(frame_pesquisa)
entry_pesquisa.pack(side="left", padx=5, pady=5)

botao_executar = ttk.Button(frame_pesquisa, text="Executar", command=pesquisar_questao)
botao_executar.pack(side="left", padx=5, pady=5)

label_status = tk.Label(frame_pesquisa, bg="green", fg="red", font=("Arial", 10))
label_status.pack(side="right", padx=5, pady=5)

canvas = tk.Canvas(frame_principal, bg="green")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

frame_botoes = tk.Frame(canvas, bg="green")
canvas.create_window((0, 0), window=frame_botoes, anchor="nw")

# Obter a lista de arquivos .py no diretório atual e ordená-los
arquivos = sorted(glob.glob("*.py"))

# Ordenar os botões de acordo com os números da questão
arquivos.sort(key=lambda x: int(re.search(r"l\dq(\d+)", x).group(1)) if re.search(r"l\dq(\d+)", x) else float('inf'))

num_colunas = 3

botoes = []  # Lista para armazenar os botões

# Configurar botões
linha = 0
coluna = 0
for arquivo in arquivos:
    botao = ttk.Button(frame_botoes, text=arquivo, command=lambda q=arquivo: executar_questao(q))
    botao.grid(row=linha, column=coluna, padx=5, pady=5, sticky="ew")
    botoes.append(botao)  # Adicionar botão à lista
    coluna += 1
    if coluna == num_colunas:
        coluna = 0
        linha += 1

janela.mainloop()