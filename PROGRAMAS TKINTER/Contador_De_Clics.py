import tkinter as tk # importa la biblioteca tkinter as tk 

# Ventana principal
ventana = tk.Tk() 
ventana.title("Contador de Clics")

# Variable para contar los clics
contador = 0

# Etiqueta para mostrar el número de clics
label_contador = tk.Label(ventana, text=f"Clics: {contador}", font=("Arial", 14)) # crea una etiqueta con el texto inicial
label_contador.pack(pady=10) # el pady es para dar espacio vertical

# Función que aumenta el contador
def aumentar():

    global contador  # usar la variable global, global sirve para modificar variables fuera de la función

    contador += 1  # suma 1 al contador
    
    label_contador.config(text=f"Clics: {contador}")  # .config actualiza el texto de la etiqueta

# Botón que ejecuta la función
boton = tk.Button(ventana, text="Haz clic aquí", command=aumentar, font=("Arial", 12)) # crea un botón que llama a la función aumentar al hacer clic 
boton.pack(pady=10)

# Bucle para mantener la ventana abierta
ventana.mainloop()