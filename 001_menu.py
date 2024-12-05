import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

# Función para ejecutar un archivo de Python específico
def ejecutar_archivo(archivo):
    try:
        subprocess.Popen(["python", archivo])  # Ejecuta el archivo como un proceso en segundo plano
        messagebox.showinfo("Éxito", f"{archivo} se está ejecutando.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo ejecutar {archivo}: {e}")

# Interfaz gráfica
root = tk.Tk()
root.title("Menú de Ejecución de Scripts")
root.configure(bg="#0f2557")

# Ejecutar el servidor de bloqueo al abrir el menú
def iniciar_servidor_bloqueo():
    subprocess.Popen(["python", "bloqmouse.py"])  # Ejecuta el servidor del socket en segundo plano

# Ejecutar otro servidor al abrir el menú
def iniciar_servidor():
    subprocess.Popen(["python", "recibir.py"])

# Iniciar los servidores
iniciar_servidor_bloqueo()
iniciar_servidor()

# Título
titulo = tk.Label(
    root, 
    text="Mr. Witcher", 
    font=("Arial Rounded MT Bold", 24, "bold"), 
    bg="#0f2557", 
    fg="#e4f34a"
)
titulo.grid(row=0, column=0, columnspan=4, pady=10)  # Usamos columnspan para que ocupe varias columnas

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
crear_boton("Observar", lambda: ejecutar_archivo("menumo.py"), 0, 1)
crear_boton("Transferencia", lambda: ejecutar_archivo("menutransfer.py"), 0, 2)
crear_boton("Chat", lambda: ejecutar_archivo("menuchat.py"), 0, 3)
crear_boton("Exhibir", lambda: ejecutar_archivo("monitoreo/menumo.py"), 0, 4)
crear_boton("Mostrar Serv", lambda: ejecutar_archivo("recibir.py"), 1, 1)

crear_boton("Bloquear", lambda: ejecutar_archivo("bloqmouse.py"), 1, 2)
crear_boton("Apagar", lambda: ejecutar_archivo("apagarcompu.py"), 1, 3)
crear_boton("Denegar Páginas", lambda: ejecutar_archivo("bloquearpagserv.py"), 1, 4)
crear_boton("Denegar Ping", lambda: ejecutar_archivo("pingserv.py"), 2, 1)

# Cargar y colocar la imagen del gato
try:
    gato_img = Image.open("gatow.png") 
    gato_img = gato_img.resize((100, 100), Image.LANCZOS)
    gato_photo = ImageTk.PhotoImage(gato_img)
    gato_label = tk.Label(root, image=gato_photo, bg="#0f2557")
    gato_label.grid(row=5, column=2, columnspan=2, padx=10, pady=20)  # Colocamos la imagen en una nueva fila
except FileNotFoundError:
    messagebox.showerror("Error", "No se encontró la imagen 'gat.png'.")

# Hacer que las columnas se expandan de manera proporcional
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

# Inicia la interfaz
root.mainloop()
