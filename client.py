import socket
import tkinter as tk
from tkinter import ttk
from cryptography.fernet import Fernet

def receive_file():
   
    sock = socket.socket()
    print ("Socket created successfully.")
    
    port = 8800
    host = 'localhost'
    
    sock.connect((host, port))
    print('Connection Established.')
    
    sock.send('A message from the client'.encode())
    
    file = open(name_entry.get(), 'wb')
    
    line = sock.recv(1024)
    
    while(line):
        file.write(line)
        line = sock.recv(1024)
    
    print('File has been received successfully.')
    
    file.close()
    sock.close()
    print('Connection Closed.')

def decrypt_file(file_path, key_path):
    
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
    
    fernet = Fernet(key)
    
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

    print(f"File '{file_path}' has been decrypted.")

root = tk.Tk()
root.title("File Transfer Application")
root.geometry("600x400")
root.configure(bg='lightblue') 

label = ttk.Label(root, text="SECURE FILE TRANSFER SYSTEM", font=('Arial', 16),background='lightblue')
label.pack(pady=20)

label = ttk.Label(root, text="File name with correct extention:",background='lightblue')
label.pack()

name_entry = ttk.Entry(root)
name_entry.pack()

decryptbutton = ttk.Button(root, text="Decrypt File", command=lambda:decrypt_file(name_entry.get(), 'private_key.txt'))
decryptbutton.pack(pady=20)

receivebutton = ttk.Button(root, text="Receive File", command=receive_file)
receivebutton.pack(pady=20)


root.mainloop()





