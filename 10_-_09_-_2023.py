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
  

# Função para obter os números selecionados
def get_selected_numbers():
    fixed_numbers_text = fixed_numbers_input.get()
    selected_numbers = [int(number.strip()) for number in fixed_numbers_text.split(",")]
    return selected_numbers
      
def numero_natural(lim_minimo, lim_maximo):
    
    #Gerar 20 numeros aleatorios de 0 a 100 garatindo que haja no minimo X numeros terminados em cada numeros natural(0 a 9)

    numeros = [0] * 10 # Inicializa uma lista com contadores para cada dígito natural de 0 a 9.

    resultado = []

    # Gera X números terminados em cada dígito natural de 0 a 9.
    for digito in range(10):
        for _ in range(x):
            x = ''
            numero_aleatorio = random.randint(lim_minimo, lim_maximo)
            while numero_aleatorio % 10 != digito:
                numero_aleatorio = numero_aleatorio(lim_minimo, lim_maximo)
            resultado.append(numero_aleatorio)
            numeros[digito] += 1

    numeros_restantes = 20 - 10 * x 
    for _ in range(numeros_restantes):
        numero_aleatorio = random.randint(lim_minimo, lim_maximo)
        resultado.append(numero_aleatorio) # Embaralha a lista de resultados.

        return resultado
    
    # TODO:
    # Criar uma lista que contenha os numeros de 0 a 9 e aleatorizar todas as vezes que a função for chamada
    
    
def lista_aleatoria():
    numeros = list(range(10))  # Cria uma lista de 0 a 9
    random.shuffle(numeros)   # Embaralhando a lista
    return numeros

minha_lista = lista_aleatoria()
print(minha_lista)


    # TODO: 
    # Para cada numero natural (0,9) adquirir a quantida minima de numeros de 0 a 50 terminados no numero natural
        
def numeros_terminados_em(n, max_num):
    numeros = []
    for i in range(max_num + 1):  # Gere números de 0 a max_num
        if i % 10 == n:  # Verifique se o número termina com o valor desejado
            numeros.append(i)
            if len(numeros) == 6:  # Se encontrou 2 números que terminam em n, pare
                break
    return numeros

numeros_naturais = list(range(10))  # Cria uma lista de números naturais de 0 a 9
max_num = 50  # Defina o número máximo para a busca

resultados = {}

for num in numeros_naturais:
    resultados[num] = numeros_terminados_em(num, max_num)

# Exemplo :
for num, terminados_em_num in resultados.items():
    print(f"Números terminados em {num}: {terminados_em_num}")

    
    # TODO: 
    # Garantir que quando atingido 20 numeros a execução seja finalizada e retornada o novo jogo

def novo_jogo():
    numeros_naturais = list(range(10))
    max_num = 50
    resultados = {}

    for num in numeros_naturais:
        resultados[num] = numeros_terminados_em(num, max_num)

    return resultados

    
    
def gerar_jogos():
    #chamar a funçao novo_jogo 8 vezes e armazenar todos os jogos retornados em um dicinario para mostrar na tela
    
    ...
    
root = tk.Tk()
root.title("Boleta de Números")


fixed_numbers_label = tk.Label(root, text="Números Fixos (20 números separados por vírgula):")
fixed_numbers_input = tk.Entry(root, width=50)
update_button = tk.Button(root, text="Atualizar Números Fixos", command=update_fixed_numbers)
#generate_button = tk.Button(root, text="Gerar Boleta", command=generate_boleta)
fixed_numbers_output = tk.Label(root, text="", wraplength=400)
random_numbers_output = tk.Label(root, text="", wraplength=400)
total_games_output = tk.Label(root, text="", wraplength=400)
games_list = tk.Listbox(root, width=160, height=18)

# Organização dos elementos na interface
fixed_numbers_label.pack()
fixed_numbers_input.pack()
update_button.pack()
fixed_numbers_output.pack()
#generate_button.pack()
random_numbers_output.pack()
total_games_output.pack()
games_list.pack()

# Inicialização da interface gráfica
root.mainloop()
