import socket
import tkinter as tk
from tkinter import ttk
from cryptography.fernet import Fernet

def encrypt_file(file_path, key_path):
    
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
    
    fernet = Fernet(key)
    
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    encrypted_data = fernet.encrypt(file_data)
    
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

    print(f"File '{file_path}' has been encrypted.")


def transfer_file():

    sock = socket.socket()
    print ("Socket created successfully.")

    port = 8800
    host = ''

    sock.bind((host, port))

    sock.listen(10)
    print('Socket is listening...')

    while True:
        
        con, addr = sock.accept()
        print('Connected with ', addr)
    
        
        data = con.recv(1024)
        print(data.decode())
        
        file = open(name_entry.get(), 'rb')
        line = file.read(1024)
        
        while(line):
            con.send(line)
            line = file.read(1024)
        
        file.close()
        print('File has been transferred successfully.')
    
        con.close()
        sock.close()

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

label = ttk.Label(root, text="File name:",background='lightblue')
label.pack()

name_entry = ttk.Entry(root)
name_entry.pack()

decryptbutton = ttk.Button(root,text="Encrypt File",command=lambda:encrypt_file(name_entry.get(), 'private_key.txt'))
decryptbutton.pack(pady=20)

transferbutton = ttk.Button(root,text="Transfer file",command=transfer_file)
transferbutton.pack(pady=20)

decryptbutton = ttk.Button(root,text="decrypt File",command=lambda:decrypt_file(name_entry.get(), 'private_key.txt'))
decryptbutton.pack(pady=20)

root.mainloop()