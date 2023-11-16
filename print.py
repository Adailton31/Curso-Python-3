import random

import tkinter as tk
from tkinter import messagebox
import random

def update_fixed_numbers():
    fixed_numbers_text = fixed_numbers_input.get()
    fixed_numbers_array = [int(number.strip()) for number in fixed_numbers_text.split(",")]

    # Verifica se há exatamente 20 números válidos entre 1 e 100
    if len(fixed_numbers_array) == 20 and all(1 <= num <= 100 for num in fixed_numbers_array):
        fixed_numbers_output.config(text="Números Fixos: " + ", ".join(map(str, fixed_numbers_array)))
    else:
        messagebox.showerror("Erro", "Insira exatamente 20 números válidos (entre 1 e 100) separados por vírgula.")

def lista_aleatoria():
    numeros = list(range(10))  # Cria uma lista de 0 a 9
    random.shuffle(numeros)   # Embaralhando a lista
    return numeros

def numeros_terminados_em(n, max_num, quantidade=6):
    numeros = []
    for i in range(max_num + 1):  # Gere números de 0 a max_num
        if i % 10 == n:  # Verifique se o número termina com o valor desejado
            numeros.append(i)
            if len(numeros) == quantidade:  # Se encontrou a quantidade desejada de números que terminam em n, pare
                break
    return numeros

def novo_jogo():
    numeros_naturais = list(range(10))
    max_num = 50
    resultados = {}

    for num in numeros_naturais:
        resultados[num] = numeros_terminados_em(num, max_num)

    return resultados

def gerar_jogos():
    jogos = {}
    for _ in range(8):
        novo_jogo_result = novo_jogo()
        jogos[f"Jogo {_+1}"] = novo_jogo_result

    return jogos

root = tk.Tk()
root.title("Boleta de Números")

fixed_numbers_label = tk.Label(root, text="Números Fixos (20 números separados por vírgula):")
fixed_numbers_input = tk.Entry(root, width=50)
update_button = tk.Button(root, text="Atualizar Números Fixos", command=update_fixed_numbers)
fixed_numbers_output = tk.Label(root, text="", wraplength=400)
random_numbers_output = tk.Label(root, text="", wraplength=400)
total_games_output = tk.Label(root, text="", wraplength=400)
games_list = tk.Listbox(root, width=160, height=18)

fixed_numbers_label.pack()
fixed_numbers_input.pack()
update_button.pack()
fixed_numbers_output.pack()
random_numbers_output.pack()
total_games_output.pack()
games_list.pack()

root.mainloop()
