import tkinter as tk
from tkinter import messagebox
import locale

def idade():

    try:
        idade = int(entry_idade.get())

        if idade <=12:
            resultado = "Classificação etária: CRIANÇA"
            
        elif 13 <= idade < 18:
            resultado = "Classificação etária: ADOLESCENTE"
        else:
            resultado="Classificação etária: ADULTO"

        
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

janela = tk.Tk()
janela.title("QUAL É SUA CLASSIFICAÇÃO ETÁRIA?")
janela.geometry("380x200")

label_idade = tk.Label(janela, text="Digite sua idade:")
label_idade.pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()



btn_idade = tk.Button(janela, text="Determine faixa etária:", command=idade)
btn_idade.pack(pady=20)

janela.mainloop()
