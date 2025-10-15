import tkinter as tk    # Importación de librería
from tkinter import messagebox

# Ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Etiqueta
tk.Label(ventana, text="Escribe una tarea:").grid(row=0, column=0, padx=10, pady=5)

# Entrada de texto
entrada_tarea = tk.Entry(ventana, width=30)
entrada_tarea.grid(row=0, column=1, padx=10, pady=5)

# Listbox para mostrar las tareas
lista_tareas = tk.Listbox(ventana, width=45, height=10)
lista_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Función para agregar tareas
def agregar_tarea():
    tarea = entrada_tarea.get().strip()  # leer lo que escribió el usuario

    # si el campo no está vacío
    if tarea:  

        lista_tareas.insert(tk.END, tarea)  # agregar al final de la lista
        entrada_tarea.delete(0, tk.END)  # limpiar campo de texto

    # Si por lo contrario, el campo está vacío
    else:
        messagebox.showwarning("Atención", "Escribe una tarea antes de agregar")

# Función para eliminar tarea seleccionada
def eliminar_tarea():

    seleccion = lista_tareas.curselection()  # obtener índice seleccionado

    # si hay algo seleccionado
    if seleccion: 

        lista_tareas.delete(seleccion)

    # si no hay algo seleccionado
    else:
        messagebox.showinfo("Aviso", "Selecciona una tarea para eliminar")

# Botones
tk.Button(ventana, text="Agregar", command=agregar_tarea).grid(row=2, column=0, pady=10)
tk.Button(ventana, text="Eliminar", command=eliminar_tarea).grid(row=2, column=1, pady=10)

ventana.mainloop()