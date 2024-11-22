import paramiko
import tkinter as tk
from tkinter import messagebox

def apagar_mac():
    # Obtiene los valores de la interfaz
    ip = ip_entry.get()
    usuario = usuario_entry.get()
    contraseña = contraseña_entry.get()
    
    # Configura la conexión SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Conéctate a la Mac
        ssh.connect(ip, username=usuario, password=contraseña)
        
        # Ejecuta el comando de apagado
        stdin, stdout, stderr = ssh.exec_command('sudo -S shutdown -h now')
        
        # Proporciona la contraseña para el comando sudo
        stdin.write(contraseña + '\n')
        stdin.flush()
        
        # Verifica si hay algún error
        error = stderr.read().decode()
        if error:
            messagebox.showerror("Error", f"No se pudo apagar la Mac: {error}")
        else:
            messagebox.showinfo("Éxito", "La Mac se está apagando.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo apagar la Mac: {e}")
    finally:
        ssh.close()

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Apagar Mac Remota")
root.geometry("300x250")

# Etiquetas y campos de entrada
tk.Label(root, text="IP de la Mac Remota:").pack(pady=5)
ip_entry = tk.Entry(root)
ip_entry.pack()

tk.Label(root, text="Usuario:").pack(pady=5)
usuario_entry = tk.Entry(root)
usuario_entry.pack()

tk.Label(root, text="Contraseña:").pack(pady=5)
contraseña_entry = tk.Entry(root, show="*")
contraseña_entry.pack()

# Botón para ejecutar el comando de apagado
apagar_btn = tk.Button(root, text="Apagar Mac", command=apagar_mac)
apagar_btn.pack(pady=20)

# Inicia la interfaz
root.mainloop()