import tkinter as tk
from tkinter import messagebox



def verificar_par_ou_impar():
    try:
        numero = int(entry_numero.get())  
        if numero % 2 == 0:
            resultado = "O número é par."
        else:
            resultado = "O número é ímpar."
                
        messagebox.showinfo("Resultado", resultado)
    except ValueError:        
        messagebox.showerror("Erro", "Por favor, insira um número válido.")



janela = tk.Tk()
janela.title("PAR OU ÍMPAR")
janela.geometry("500x200")

label_numero = tk.Label(janela, text="Digite o número:")
label_numero.pack()
entry_numero= tk.Entry(janela)
entry_numero.pack()


btn_numero = tk.Button(janela, text="Verificar", command=verificar_par_ou_impar)
btn_numero.pack(pady=20)

janela.mainloop()
