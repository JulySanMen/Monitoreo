import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import ctypes

def is_admin():
    """Verifica si el script está siendo ejecutado como administrador en Windows."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def solicitar_permisos_admin():
    """Reinicia el script con permisos de administrador si no los tiene."""
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()

def ejecutar_comando(comando):
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    if resultado.returncode != 0:
        print(f"Error: {resultado.stderr}")
        return False
    else:
        print(f"Éxito: {resultado.stdout}")
        return True

def bloquear_ping_desde_ip(ip):
    # Verifica si ya existe una regla de firewall que bloquea el ping desde esta IP
    verificar_comando = f"netsh advfirewall firewall show rule name=\"Bloquear Ping desde {ip}\""
    resultado = subprocess.run(verificar_comando, shell=True, capture_output=True, text=True)
    
    if "No hay coincidencias" in resultado.stdout:
        # Si la regla no existe, la agregamos
        comando = f"netsh advfirewall firewall add rule name=\"Bloquear Ping desde {ip}\" dir=in action=block protocol=icmpv4 remoteip={ip}"
        if ejecutar_comando(comando):
            messagebox.showinfo("Acción completada", f"Ping bloqueado de forma persistente desde {ip}.")
    else:
        messagebox.showinfo("Información", f"El ping ya estaba bloqueado desde {ip}.")

def permitir_ping_desde_ip(ip):
    comando = f"netsh advfirewall firewall delete rule name=\"Bloquear Ping desde {ip}\""
    if ejecutar_comando(comando):
        messagebox.showinfo("Acción completada", f"Ping permitido desde {ip}.")

def pingre(ip):
    resultado_text.delete(1.0, tk.END)
    resultado_text.insert(tk.END, f"Haciendo ping a {ip}...\n")
    resultado = subprocess.run(f"ping {ip}", shell=True, capture_output=True, text=True)
    
    if resultado.returncode == 0:
        resultado_text.insert(tk.END, f"Respuesta de {ip}:\n{resultado.stdout}")
    else:
        resultado_text.insert(tk.END, f"No se pudo llegar a {ip}.\n")

def realizar_accion(accion):
    ip = ip_entry.get()
    if not ip:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una dirección IP.")
        return
    
    if accion == "ping":
        pingre(ip)
    elif accion == "bloquear":
        bloquear_ping_desde_ip(ip)
    elif accion == "permitir":
        permitir_ping_desde_ip(ip)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Menú de Ping para Windows")

tk.Label(root, text="Ingrese la dirección IP:").pack(pady=5)
ip_entry = tk.Entry(root)
ip_entry.pack(pady=5)

ping_button = tk.Button(root, text="Realizar Ping", command=lambda: realizar_accion("ping"))
ping_button.pack(pady=5)

bloquear_button = tk.Button(root, text="Bloquear Ping desde IP", command=lambda: realizar_accion("bloquear"))
bloquear_button.pack(pady=5)

permitir_button = tk.Button(root, text="Permitir Ping desde IP", command=lambda: realizar_accion("permitir"))
permitir_button.pack(pady=5)

resultado_text = tk.Text(root, height=10, width=50)
resultado_text.pack(pady=10)

# Solicitar permisos de administrador si no se tienen
solicitar_permisos_admin()

root.mainloop()
