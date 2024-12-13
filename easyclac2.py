from tkinter import *


class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x300")
        self.show = Label(self.root, font=('宋体', 24), width=23)
        self.show.grid(row=0, column=0, columnspan=5)
        self.initWidgets()
        self.root.mainloop()

    def initWidgets(self):
        self.show['text'] = ''
        names = ("+", "1", "2", "3", "C", "-", "4", "5", "6", "**", "*", "7", "8", "9", "//", "/", ".", "0", "%", "=")
        for i in range(len(names)):
            b = Button(self.root, text=names[i], font=('Verdana', 20), width=5)
            b.grid(row=(i // 5) + 1, column=i % 5)
            b.bind('<Button-1>', self.click)

    def click(self, event):
        if event.widget['text'] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'):
            self.show['text'] = self.show['text'] + event.widget['text']
        elif event.widget['text'] in ('+', '-', '*', '/', '%', '**', '//'):
            s1 = self.show['text']
            if s1 and s1[-1].isdigit():
                self.show['text'] = self.show['text'] + event.widget['text']
        elif event.widget['text'] == '=' and self.show['text']:
            s2 = self.show['text']
            if s2[-1].isdigit():
                self.show['text'] = str(eval(self.show['text']))
            else:
                s2 = s2[:len(s2) - 1]
                self.show['text'] = str(eval(s2))
        elif event.widget['text'] == 'C':
            self.show['text'] = ''


App()
