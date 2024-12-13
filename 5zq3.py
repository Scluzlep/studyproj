from tkinter import *

root = Tk()
label1 = Label(root, text='五子棋', font=('华文中宋', 30), bg='white')
label1.pack()
data = StringVar()
data.set('')
tx = Entry(root, textvariable=data)
tx.pack()


def factorial(_event=None):
    fact = 1
    for i in range(1, int(tx.get()) + 1):
        fact *= i
    label1['text'] = str(fact)


bt = Button(root, text='求阶乘')
bt.bind('<Button-1>', factorial)
bt.pack()
root.geometry('1280x720')
root.title('五子棋')
root.resizable(width=True, height=True)
root.mainloop()
