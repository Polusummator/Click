from cryptography.fernet import Fernet
from tkinter import*
import os.path


def error():
    root1 = Tk()
    root1.geometry('300x110+630+300')
    root1.title('ERROR')
    label1 = Label(root1, text='Ошибка!', font='Fixedays 18', fg='brown')
    label2 = Label(root1, text='Проверьте, есть ли у вас папка C:/Click\nПроверьте, есть ли у вас в этой папке файлы\nLogin.txt и Click.txt', font='Fixedays 10', fg='AntiqueWhite4')
    label1.pack()
    label2.pack()
    root1.mainloop()


def error2():
    root1 = Tk()
    root1.geometry('300x80+630+300')
    root1.title('ERROR')
    label1 = Label(root1, text='Ошибка!', font='Fixedays 18', fg='brown')
    label2 = Label(root1, text='В имени пользователя присутствует пробел!', font='Fixedays 10', fg='AntiqueWhite4')
    label1.pack()
    label2.pack()
    root1.mainloop()


def crypto(text):
    cipher_key = Fernet.generate_key()
    cipher = Fernet(cipher_key)
    text = bytes(text, encoding='utf-8')
    encrypted_text = cipher.encrypt(text)
    text2 = encrypted_text + b' ' + cipher_key
    return text2


def nice():
    root1 = Tk()
    root1.geometry('450x100+630+300')
    root1.title('UPGRADE')
    label1 = Label(root1, text='Подготовка системы завершена!', font='Fixedays 18', fg='brown')
    label2 = Label(root1, text='Для начала игры откройте последнюю версию приложения\nУстановите последнюю версию приложения в папку C:/Click_Game\nПоследующие версии также устанавливайте в эту папку', font='Fixedays 10', fg='AntiqueWhite4')
    label1.pack()
    label2.pack()
    root1.mainloop()


path_drk = r'C:\Click'
pr1 = os.path.exists(path_drk)
if not pr1:
    error()
else:
    path_Log = r'C:\Click\Login.txt'
    pr2 = os.path.exists(path_Log)
    if not pr2:
        error()
    else:
        log = open(r'C:\Click\Login.txt')
        login = log.readline().strip()
        log.close()
        if ' ' in login:
            error2()
        else:
            login_2 = crypto(login)
            log = open(r'C:\Click\Login.txt', 'wb+')
            log.write(login_2)
            log.close()
            boost = open(r'C:\Click\Boost.txt', 'wb+')
            b = '1'
            b_cr = crypto(b)
            boost.write(b_cr)
            boost.close()
            path = r'C:\Click_Game'
            os.mkdir(path)
            nice()
