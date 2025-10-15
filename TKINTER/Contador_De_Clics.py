import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Contador de Clics")

# Variable para contar los clics
contador = 0

# Etiqueta para mostrar el número de clics
label_contador = tk.Label(ventana, text=f"Clics: {contador}", font=("Arial", 14))
label_contador.pack(pady=10)

# Función que aumenta el contador
def aumentar():

    global contador  # usar la variable global

    contador += 1  # suma 1 al contador
    
    label_contador.config(text=f"Clics: {contador}")  # actualiza el texto de la etiqueta

# Botón que ejecuta la función
boton = tk.Button(ventana, text="Haz clic aquí", command=aumentar, font=("Arial", 12))
boton.pack(pady=10)

# Bucle para mantener la ventana abierta
ventana.mainloop()