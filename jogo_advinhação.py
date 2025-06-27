import tkinter as tk
from tkinter import messagebox
import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

def verificar_palpite():
    try:
        # Obtém o palpite do usuário
        palpite = int(entry_palpite.get())
        entry_palpite.delete(0, tk.END)  # Limpa o campo de entrada

        if palpite < 1 or palpite > 100:  # Verifica se o palpite está no intervalo válido
            messagebox.showerror("Erro", "Por favor, insira um número entre 1 e 100.")
        else:
            # Compara o palpite com o número secreto
            if palpite < numero_secreto:
                messagebox.showinfo("Dica", "Muito baixo! Tente um número maior.")
            elif palpite > numero_secreto:
                messagebox.showinfo("Dica", "Muito alto! Tente um número menor.")
            else:
                messagebox.showinfo("Parabéns!", f"Você acertou! O número secreto era {numero_secreto}.")
                janela.destroy()  # Fecha a interface ao acertar
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Jogo de Adivinhação")
janela.geometry("400x200")

# Label e entrada para o palpite do usuário
label_palpite = tk.Label(janela, text="Tente adivinhar o número (entre 1 e 100):")
label_palpite.pack()
entry_palpite = tk.Entry(janela)
entry_palpite.pack()

# Botão para verificar o palpite
btn_verificar = tk.Button(janela, text="Verificar Palpite", command=verificar_palpite)
btn_verificar.pack(pady=20)

# Inicia o loop principal da interface
janela.mainloop()
