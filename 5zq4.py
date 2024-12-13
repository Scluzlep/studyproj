from tkinter import *

root = Tk()

Label(root, text='1').grid(row=0, column=0)
Label(root, text='2').grid(row=1, column=0)
entry1 = Entry(root)
entry2 = Entry(root)
button = Button(root, text='计算', height=2)
button.grid(row=0, column=2, rowspan=2)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.geometry('600x400')
root.title('五子棋')
root.resizable(width=True, height=True)
root.mainloop()