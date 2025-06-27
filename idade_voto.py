import tkinter as tk
from tkinter import messagebox



def verificar_idade():
    try:
        idade = int(entry_idade.get())  
        if idade <= 17:
            resultado = "Você não é obrigado(a) votar."
        elif idade <=70:
            resultado = "Você é obrigado a votar."
        else:
            resultado= "Você não é obrigado a votar."
                
        messagebox.showinfo("Resultado", resultado)
    except ValueError:        
        messagebox.showerror("Erro", "Por favor, insira uma idade válida.")



janela = tk.Tk()
janela.title("IDADE PARA VOTAR")
janela.geometry("300x200")

label_idade = tk.Label(janela, text="Digite a sua idade:")
label_idade.pack()
entry_idade= tk.Entry(janela)
entry_idade.pack()


btn_idade = tk.Button(janela, text="Verificar", command=verificar_idade)
btn_idade.pack(pady=20)

janela.mainloop()
