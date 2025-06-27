import tkinter as tk
from tkinter import messagebox

numeros = []  # Lista global para armazenar os números

def adicionar_numero():
    try:
        numero = int(entry_numero.get())  # Obtém o número inserido
        entry_numero.delete(0, tk.END)  # Limpa o campo de entrada

        if numero == -1:  # Condição de parada
            calcular_media()  # Calcula a média e encerra
        else:
            numeros.append(numero)  # Adiciona o número à lista
            calcular_media(atualizar=True)  # Calcula a média continuamente
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def calcular_media(atualizar=False):
    if numeros:
        media = sum(numeros) / len(numeros)  # Calcula a média
        if atualizar:
            # Atualiza a média a cada novo número adicionado
            label_resultado.config(text=f"Média atual: {media:.2f}")
        else:
            # Exibe o resultado final e encerra a janela
            messagebox.showinfo("Média", f"A média dos números é: {media:.2f}")
            janela.destroy()
    else:
        messagebox.showinfo("Média", "Nenhum número foi inserido.")
        janela.destroy()

# Criação da janela principal
janela = tk.Tk()
janela.title("Média de Números")
janela.geometry("400x300")

# Label e entrada para números
label_numero = tk.Label(janela, text="Digite um número (-1 para finalizar):")
label_numero.pack()
entry_numero = tk.Entry(janela)
entry_numero.pack()

# Botão para adicionar números
btn_adicionar = tk.Button(janela, text="Adicionar Número", command=adicionar_numero)
btn_adicionar.pack(pady=10)

# Label para exibir a média atual
label_resultado = tk.Label(janela, text="Média atual: 0.00")
label_resultado.pack(pady=10)

# Inicia o loop principal da interface
janela.mainloop()
