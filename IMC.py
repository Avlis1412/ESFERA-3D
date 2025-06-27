import tkinter as tk
from tkinter import messagebox
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')



def imc():

    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / altura ** 2

        if imc < 18.5:
            resultado = "Classificação: Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            resultado = "Classificação: Peso normal"
        elif 25.0 <= imc < 29.9:
            resultado = "Classificação: Sobrepeso"
        elif 30.0 <= imc < 34.9:
            resultado = "Classificação: Obesidade grau 1"
        elif 35.0 <= imc < 39.9:
           resultado = "Classificação: Obesidade grau 2"
        else:
            resultado="Classificação: Obesidade grau 3 (mórbida)"

        
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

janela = tk.Tk()
janela.title("QUAL É O SEU IMC?")
janela.geometry("400x200")

label_peso = tk.Label(janela, text="Digite peso:")
label_peso.pack()
entry_peso = tk.Entry(janela)
entry_peso.pack()

label_altura = tk.Label(janela, text="Digite sua altura:")
label_altura.pack()
entry_altura = tk.Entry(janela)
entry_altura.pack()


btn_imc = tk.Button(janela, text="Calcule o IMC:", command=imc)
btn_imc.pack(pady=20)

janela.mainloop()
