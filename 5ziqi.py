from tkinter import *
import time

def sum():
    s = 0
    for i in range(1, 101):
        s += i


def window_show():
    root = Tk()
    label1 = Label(root, text='五子棋', font=('华文中宋', 30), width=30, bg='red')
    label1.pack()
    root.geometry('1280x720')
    root.title('五子棋')
    root.resizable(width=False, height=False)
    root.mainloop()


if __name__ == '__main__':
    # 创建画布
    window_show()
