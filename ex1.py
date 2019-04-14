from tkinter import *


def toFixed(numObj, digits=3):
    return f"{numObj:.{digits}f}"


def click(event):
    coin.config(text=str(toFixed(float(coin.cget('text')) + 0.001)))


def main():
    global coin
    root = Tk()
    root.title('Coins')
    root.geometry('300x350')
    lab = Label(root, text='Your score:', font='Fixedays 12', fg='AntiqueWhite4')
    coin = Label(root, text='0.000', font='Fixedays 17', fg='black')
    cnopka = PhotoImage(file="but.png")
    but = Label(root, image=cnopka)
    but.bind('<Button-1>', click)
    lab.pack()
    coin.pack()
    but.pack(side='bottom')
    root.mainloop()

main()




