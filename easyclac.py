from tkinter import *
import math


class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x300")
        self.menu = Menu(self.root)
        self.fmenu = Menu(self.menu)
        self.fmenu.add_command(label='标准', command=self.initWidgets)
        self.fmenu.add_command(label='科学', command=self.initWidgets2)
        self.menu.add_cascade(label='计算器', menu=self.fmenu)
        self.p = Frame(self.root)
        self.show = Label(self.root, font=('宋体', 24), width=23)
        self.show.pack()
        self.p.pack()
        self.root['menu'] = self.menu
        self.root.mainloop()

    def initWidgets(self):
        self.show['text'] = ''
        names = ("+", "1", "2", "3", "C", "-", "4", "5", "6", "**", "*", "7", "8", "9", "//", "/", ".", "0", "%", "=")
        for i in range(len(names)):
            b = Button(self.p, text=names[i], font=('Verdana', 20), width=5)
            b.grid(row=i // 5, column=i % 5)
            b.bind('<Button-1>', self.click)

    def initWidgets2(self):
        self.show['text'] = ''
        names = (
            "1/x", "sqrt(x)", "x^2", "|x|", "exp", "mod", "log", "log10", "ln", "1", "2", "3", "4", "5", "6", "7", "8",
            "9",
            "0", "=")
        for i in range(len(names)):
            b = Button(self.p, text=names[i], font=('Verdana', 20), width=5)
            b.grid(row=i // 5, column=i % 5)
            b.bind('<Button-1>', self.click2)

    def click(self, event):
        if event.widget['text'] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'):
            self.show['text'] = self.show['text'] + event.widget['text']
        elif event.widget['text'] in ('+', '-', '*', '/', '%', '**', '//'):
            s1 = self.show['text']
            if s1[-1].isdigit():
                self.show['text'] = self.show['text'] + event.widget['text']
        elif event.widget['text'] == '=' and self.show['text'] is not None:
            s2 = self.show['text']
            if s2[-1].isdigit():
                self.show['text'] = str(eval(self.show['text']))
            else:
                s2 = s2[:len(s2) - 1]
                self.show['text'] = str(eval(s2))
        elif event.widget['text'] == 'C':
            self.show['text'] = ''

    def click2(self, event):
        if event.widget['text'] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'):
            self.show['text'] = self.show['text'] + event.widget['text']
        elif event.widget['text'] == '1/x':
            self.show['text'] = str(1 / (eval(self.show['text'])))
        elif event.widget['text'] == 'sqrt(x)':
            self.show['text'] = str(math.sqrt(eval(self.show['text'])))
        elif event.widget['text'] == 'x^2':
            self.show['text'] = str(eval(self.show['text']) ** 2)
        elif event.widget['text'] == '|x|':
            self.show['text'] = str(abs(eval(self.show['text'])))
        elif event.widget['text'] == 'exp':
            self.show['text'] = str(math.exp(eval(self.show['text'])))
        elif event.widget['text'] == 'mod':
            self.show['text'] = str(eval(self.show['text']) % 1)
        elif event.widget['text'] == 'log':
            self.show['text'] = str(math.log(eval(self.show['text'])))
        elif event.widget['text'] == 'log10':
            self.show['text'] = str(math.log10(eval(self.show['text'])))
        elif event.widget['text'] == 'ln':
            self.show['text'] = str(math.log(eval(self.show['text'])))
        elif event.widget['text'] == '=' and self.show['text'] is not None:
            self.show['text'] = str(eval(self.show['text']))


App()
