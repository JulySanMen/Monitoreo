import tkinter as tk
from tkinter import messagebox
import subprocess

# Función para ejecutar un archivo de Python específico
def ejecutar_archivo(archivo):
    try:
        # Ejecuta el archivo en un proceso separado
        subprocess.Popen(["python", archivo])
        messagebox.showinfo("Éxito", f"{archivo} se está ejecutando.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo ejecutar {archivo}: {e}")

# Interfaz gráfica
root = tk.Tk()
root.title("Menú de Ejecución de Scripts")
root.configure(bg="#0f2557")

# Título
titulo = tk.Label(
    root, 
    text="Papel de Ejecucion", 
    font=("Helvetica", 14, "bold"), 
    bg="#0f2557", 
    fg="#e4f34a"
)
titulo.grid(row=0, column=0, columnspan=2, pady=10)  # Usamos columnspan para que ocupe varias columnas

# Hover para botones
def on_enter(e):
    e.widget['bg'] = "#465eff"

def on_leave(e):
    e.widget['bg'] = "#2f4b8f"

# Crear un botón con estilo personalizado
def crear_boton(texto, comando, columna, fila):
    boton = tk.Button(
        root, 
        text=texto, 
        command=comando, 
        font=("Helvetica", 10, "bold"), 
        bg="#2f4b8f", 
        fg="white", 
        width=20,  # Ancho mayor para que todos los botones tengan el mismo tamaño
        height=2,  # Altura mayor para más consistencia
        relief=tk.FLAT, 
        border=0
    )
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)
    boton.grid(row=fila, column=columna, padx=5, pady=5, sticky="ew")  # Alineación horizontal (expandir) con sticky="ew"
    return boton

# Crear botones usando grid para tener un control más flexible del espacio
crear_boton("CLIENTE", lambda: ejecutar_archivo("clientemonitoreo.py"), 0, 1)
crear_boton("SERVIDOR", lambda: ejecutar_archivo("serverm.py"), 1, 1)

# Hacer que las columnas se expandan de manera proporcional
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Inicia la interfaz
root.mainloop()
