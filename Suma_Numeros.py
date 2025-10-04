import tkinter as tk

# ------ FUNCIONES ------

def sumar():
    try:
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
        resultado.set (numero1 + numero2)
    except ValueError:
        resultado.set("Error")

# ------ VENTANA PRINCIPAL ------

ventana = tk.Tk()
ventana.tittle ("Calculadora básica")

