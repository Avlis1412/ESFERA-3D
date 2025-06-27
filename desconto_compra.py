import tkinter as tk
from tkinter import messagebox
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def preco():

    try:
        preco = float(entry_preco.get())
        
        
        if preco < 100:
            desconto = preco
            resultado = f"Sem desconto:{locale.currency(desconto, grouping=True)}"

        elif 101 <= preco < 500:
            desaconto= preco * 10/100
            resultado = f"O desconto é de {locale.currency(desconto, grouping=True)}"            

        else:            
            desconto=preco * 20/100
            resultado = f"O desconto é de {locale.currency(desconto, grouping=True)}"
            

        
        messagebox.showinfo("Desconto", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

janela = tk.Tk()
janela.title("QUAL É SEU DESCONTO?")
janela.geometry("300x200")

label_preco = tk.Label(janela, text="PREÇO:")
label_preco.pack()
entry_preco = tk.Entry(janela)
entry_preco.pack()


btn_preco = tk.Button(janela, text="Calcule o desconto:", command=preco)
btn_preco.pack(pady=20)

janela.mainloop()
