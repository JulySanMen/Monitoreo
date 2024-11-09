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
root.geometry("300x250")

# Título
tk.Label(root, text="Selecciona el script a ejecutar", font=("Helvetica", 14)).pack(pady=10)

# Botones para cada archivo de Python
boton1 = tk.Button(root, text="CHAT", command=lambda: ejecutar_archivo("menuchat.py"))
boton1.pack(pady=5)

boton2 = tk.Button(root, text="PING", command=lambda: ejecutar_archivo("ping.py"))
boton2.pack(pady=5)

boton3 = tk.Button(root, text="TRANSFERENCIA", command=lambda: ejecutar_archivo("menutransfer.py"))
boton3.pack(pady=5)

boton4 = tk.Button(root, text="MONITOREO", command=lambda: ejecutar_archivo("menumo.py"))
boton4.pack(pady=5)

boton5 = tk.Button(root, text="APAGAR", command=lambda: ejecutar_archivo("apagarcompu.py"))
boton5.pack(pady=5)

# Puedes agregar más botones aquí para otros scripts si es necesario
# boton4 = tk.Button(root, text="Ejecutar Script 4", command=lambda: ejecutar_archivo("script4.py"))
# boton4.pack(pady=5)

# Inicia la interfaz
root.mainloop()
