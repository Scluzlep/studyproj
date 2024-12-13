from tkinter import *


def initWidgets():
    global show
    show['text'] = ''
    names = ("+", "1", "2", "3", "C", "-", "4", "5", "6", "**", "*", "7", "8", "9", "//", "/", ".", "0", "%", "=")
    for i in range(len(names)):
        b = Button(p, text=names[i], font=('Verdana', 20), width=5)
        b.grid(row=i // 5, column=i % 5)
        b.bind('<Button-1>', click)


def click(event):
    global show
    if event.widget['text'] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'):
        show['text'] = show['text'] + event.widget['text']
    elif event.widget['text'] in ('+', '-', '*', '/', '%', '**', '//'):
        s1 = show['text']
        if s1[-1].isdigit():
            show['text'] = show['text'] + event.widget['text']
    elif event.widget['text'] == '=' and show['text'] is not None:
        s2 = show['text']
        if s2[-1].isdigit():
            show['text'] = str(eval(show['text']))
        else:
            s2 = s2[:len(s2) - 1]
            show['text'] = str(eval(s2))
    elif event.widget['text'] == 'C':
        show['text'] = ''


root = Tk()
root.geometry('500x300')
show = Label(root, width=23, bg='white')
show.pack()

p = Frame(root)
p.pack()

initWidgets()
root.mainloop()
