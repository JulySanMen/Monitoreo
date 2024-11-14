import socket
import os
import tkinter as tk
from tkinter import filedialog

def send_file(filename, host='192.168.138.91', port=5001):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Enviar el nombre del archivo
    client_socket.send(os.path.basename(filename).encode('utf-8'))

    # Esperar confirmación de recepción del nombre del archivo
    confirmation = client_socket.recv(1024)
    if confirmation != b"Filename received":
        print("Error al enviar el nombre del archivo.")
        client_socket.close()
        return

    # Enviar el archivo en binario
    with open(filename, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.send(data)

    print(f'Archivo {filename} enviado')
    client_socket.close()

def select_file():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    filename = filedialog.askopenfilename()  # Abre el cuadro de diálogo de selección de archivos
    return filename

if __name__ == '__main__':
    filename = select_file()  # Llama a la función para seleccionar el archivo
    if filename:  # Verifica que se haya seleccionado un archivo
        send_file(filename)
    else:
        print("No se ha seleccionado ningún archivo.")
