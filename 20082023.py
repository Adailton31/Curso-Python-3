import tkinter as tk
from tkinter import messagebox
import random

def update_fixed_numbers():
    fixed_numbers_text = fixed_numbers_input.get()
    fixed_numbers_array = [int(number.strip()) for number in fixed_numbers_text.split(",")]

    if len(fixed_numbers_array) == 20 and all(isinstance(num, int) for num in fixed_numbers_array):
        fixed_numbers_output.config(text="Números Fixos: " + ", ".join(map(str, fixed_numbers_array)))
    else:
        fixed_numbers_output.config(text="Números fixos inválidos")

def generate_boleta():
    selected_numbers = get_selected_numbers()

    if not selected_numbers or len(selected_numbers) != 20:
        messagebox.showerror("Erro", "Selecione exatamente 20 números válidos!")
        return

    random_numbers = generate_random_numbers(selected_numbers)
    total_games = calculate_total_games(selected_numbers, random_numbers)

    update_random_numbers(random_numbers)
    update_total_games(total_games)
    display_games_list(selected_numbers, random_numbers)

def get_selected_numbers():
    fixed_numbers_text = fixed_numbers_input.get()
    selected_numbers = [int(number.strip()) for number in fixed_numbers_text.split(",")]
    return selected_numbers

def generate_random_numbers(selected_numbers):
    random_numbers = []
    ends_count = {digit: 0 for digit in range(10)}

    while len(random_numbers) < 30:
        random_number = random.randint(1, 100)
        if random_number not in random_numbers and random_number not in selected_numbers:
            last_digit = random_number % 10
            if ends_count[last_digit] < 5:
                random_numbers.append(random_number)
                ends_count[last_digit] += 1

    return random_numbers

def calculate_total_games(fixed_numbers, random_numbers):
    total_numbers = len(fixed_numbers) + len(random_numbers)
    return -(-total_numbers // 6)  # Ceil division

def update_random_numbers(random_numbers):
    random_numbers_output.config(text="Números Gerados: " + ", ".join(map(str, random_numbers)))

def update_total_games(total_games):
    total_games_output.config(text="Total de Jogos: " + str(total_games))

def display_games_list(fixed_numbers, random_numbers):
    games_list.delete(0, tk.END)

    total_numbers = fixed_numbers + random_numbers
    total_games = len(total_numbers) // 6

    for i in range(total_games):
        game_numbers = total_numbers[i * 6: (i + 1) * 6]
        games_list.insert(tk.END, f"Jogo {i + 1}: {', '.join(map(str, game_numbers))}")

root = tk.Tk()
root.title("Boleta de Números")
root.geometry("400x600")  # Tamanho da tela única

fixed_numbers_input_label = tk.Label(root, text="Digite 20 números fixos separados por vírgula:")
fixed_numbers_input_label.grid(row=0, column=0, padx=10, pady=(10, 0), columnspan=2)

fixed_numbers_input = tk.Entry(root, width=30)  # Largura do campo de entrada
fixed_numbers_input.grid(row=1, column=0, padx=10, pady=(0, 10), columnspan=2)

update_button = tk.Button(root, text="Atualizar Números Fixos", command=update_fixed_numbers)
update_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

fixed_numbers_output = tk.Label(root, text="", wraplength=300)
fixed_numbers_output.grid(row=3, column=0, columnspan=2, padx=10, pady=(0, 10))

generate_button = tk.Button(root, text="Gerar Boleta", command=generate_boleta)
generate_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

random_numbers_output = tk.Label(root, text="")
random_numbers_output.grid(row=5, column=0, padx=10, pady=(0, 10), columnspan=2)

total_games_output = tk.Label(root, text="")
total_games_output.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

games_list_label = tk.Label(root, text="Boleta de Números:")
games_list_label.grid(row=7, column=0, padx=10, pady=(0, 10), columnspan=2)

games_list = tk.Listbox(root, width=50, height=10)  # Ajuste a largura e altura da lista
games_list.grid(row=8, column=0, padx=10, pady=10, columnspan=2)

root.mainloop()
