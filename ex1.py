# -*- coding: utf-8 -*-

from tkinter import *
import os.path
from cryptography.fernet import Fernet


def drk():
    drk_path = r"C:\Click"
    pr = os.path.exists(drk_path)
    return pr


def file():
    file_path = r"C:\Click\Click.txt"
    pr = os.path.exists(file_path)
    return pr


def crypto(text):
    cipher_key = Fernet.generate_key()
    cipher = Fernet(cipher_key)
    text = bytes(text, encoding='utf-8')
    encrypted_text = cipher.encrypt(text)
    text2 = encrypted_text + b' ' + cipher_key
    return text2


def decrypto(text, key):
    decrypted_text = key.decrypt(text)
    return decrypted_text


def toFixed(numObj):
    return f"{numObj:.{3}f}"


def click(event):
    global cl
    coin.config(text=str(toFixed(float(coin.cget('text')) + 0.001)))


def on_close(event):
    global coin
    f = open(r'C:\Click\Click.txt', 'wb+')
    score = toFixed(float(coin.cget('text')))
    text = crypto(score)
    f.write(text)
    f.close()
    root.destroy()


def main():
    global coin
    global root
    z = True
    if not file():
        path = r'C:\Click'
        if not drk():
            os.mkdir(path)
        z = False
        f = open(r'C:\Click\Click.txt', 'wb+')
    else:
        f = open(r'C:\Click\Click.txt', 'rb')
    if z:
        a = f.readline()
        a = a.decode('utf-8')
        A = a.split(' ')
        key = Fernet(bytes(A[1], encoding='utf-8'))
        text = bytes(A[0], encoding='utf-8')
        s = key.decrypt(text).decode('utf-8')
        score = float(s)
    else:
        score = 0.000
    f.close()
    root = Tk()
    root.title('Coins')
    root.geometry('300x350')
    lab = Label(root, text='Your score:', font='Fixedays 12', fg='AntiqueWhite4')
    coin = Label(root, text=str(toFixed(score)), font='Fixedays 17', fg='black')
    close = Button(root, text='Close & Save', font='Fixedays 12', fg='white', width=10, height=1, bg='brown')
    cnopka = PhotoImage(file="but.png")
    but = Label(root, image=cnopka)
    but.bind('<Button-1>', click)
    lab.pack()
    coin.pack()
    close.pack()
    but.pack(side='bottom')
    close.bind('<Button-1>', on_close)
    root.mainloop()


main()




