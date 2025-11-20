import tkinter as tk    # importa la librería tkinter
from tkinter import messagebox # importa el módulo de cuadros de diálogo

# Ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

tk.Label(ventana, text="Escribe una tarea:").grid(row=0, column=0, padx=10, pady=5) # etiqueta para la entrada de texto

# Entrada de texto
entrada_tarea = tk.Entry(ventana, width=30) # campo para escribir la tarea
entrada_tarea.grid(row=0, column=1, padx=10, pady=5) # campo para escribir la tarea

# Listbox para mostrar las tareas
lista_tareas = tk.Listbox(ventana, width=45, height=10) # litsbox nos permite mostrar una lista de elementos
lista_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Función para agregar tareas
def agregar_tarea():
    tarea = entrada_tarea.get().strip()  # leer lo que escribió el usuario

    # si el campo no está vacío
    if tarea:  

        lista_tareas.insert(tk.END, tarea)  # tk.End indica que se agregue al final de la lista
        entrada_tarea.delete(0, tk.END)  # limpia el campo de entrada

    # Si por lo contrario, el campo está vacío
    else:
        messagebox.showwarning("Atención", "Escribe una tarea antes de agregar") # usa messagebox para mostrar una advertencia

# Función para eliminar tarea seleccionada
def eliminar_tarea():

    seleccion = lista_tareas.curselection()  # obtiene el índice de la tarea seleccionada

    # si hay algo seleccionado
    if seleccion: 

        lista_tareas.delete(seleccion)

    # si no hay algo seleccionado
    else:
        messagebox.showinfo("Aviso", "Selecciona una tarea para eliminar")

# Botones para agregar y eliminar tareas
tk.Button(ventana, text="Agregar", command=agregar_tarea).grid(row=2, column=0, pady=10) # botón para agregar tarea
tk.Button(ventana, text="Eliminar", command=eliminar_tarea).grid(row=2, column=1, pady=10) # botón para eliminar tarea

ventana.mainloop() # inicia el bucle principal de la interfaz gráfica