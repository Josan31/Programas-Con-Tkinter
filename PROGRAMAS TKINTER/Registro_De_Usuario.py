import tkinter as tk    # importación de librería Tkinter
from tkinter import messagebox    # Se usa para mostrar el mensaje emergente de los datos registrados

# Creación de ventana
ventana = tk.Tk()

# Título de la ventana principal
ventana.title("Formulario de Registro")

# Creación de la etiqueta para el nombre
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)

# Creación de la etiqueta para la edad
tk.Label(ventana, text="Edad:").grid(row=1, column=0, padx=10, pady=5)

# Creación de la etiqueta para el correo electrónico
tk.Label(ventana, text="Correo:").grid(row=2, column=0, padx=10, pady=5)

# Se crean las entradas de texto
entrada_nombre = tk.Entry(ventana)
entrada_edad = tk.Entry(ventana)
entrada_correo = tk.Entry(ventana)

# Ubicación de las entradas en la cuadrícula
entrada_nombre.grid(row=0, column=1, padx=10, pady=5)
entrada_edad.grid(row=1, column=1, padx=10, pady=5)
entrada_correo.grid(row=2, column=1, padx=10, pady=5)

# Función que se ejecuta al presionar 'Guardar'
def guardar_datos():

    # Guarda los datos ingresados por el usuario
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    correo = entrada_correo.get()

    # Muestra los datos ingresados por el usuario previamente
    messagebox.showinfo("Datos guardados", f"Nombre: {nombre}\nEdad: {edad}\nCorreo: {correo}")

# Creación del boton guardar
tk.Button(ventana, text="Guardar", command=guardar_datos).grid(row=3, column=0, columnspan=2, pady=10)

# Bucle que ejecuta la ventana constantemente
ventana.mainloop()

