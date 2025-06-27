import tkinter as tk
from tkinter import messagebox


def ano():
    
    try:
        ano= int(entry_ano.get())
        
        if ano % 4 ==0 and ano %100 !=0 or ano %400 ==0:
            resultado="O ano é bisexto"
        
        else:
            resultado= "O ano não é bisexto"

                    
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")



janela = tk.Tk()
janela.title("O ANO É BISEXTO?")
janela.geometry("300x200")

label_ano = tk.Label(janela, text="Digite ano:")
label_ano.pack()
entry_ano = tk.Entry(janela)
entry_ano.pack()

btn_ano = tk.Button(janela, text="Verifique:", command=ano)
btn_ano.pack(pady=20)

janela.mainloop()

