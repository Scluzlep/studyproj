from tkinter import *


def create_root():
    root = Tk()
    root.geometry('1280x720')
    root.title('五子棋')
    root.resizable(width=True, height=True)
    return root


def create_label(root):
    label = Label(root, text='五子棋', font=('华文中宋', 30), bg='white')
    label.pack()
    return label


def create_entry(root):
    data = StringVar()
    data.set('')
    entry = Entry(root, textvariable=data)
    entry.pack()
    return entry


def create_button(root, label, entry):
    def factorial(_event=None):
        fact = 1
        for i in range(1, int(entry.get()) + 1):
            fact *= i
        label['text'] = str(fact)

    button = Button(root, text='求阶乘')
    button.bind('<Button-1>', factorial)
    button.pack()


def main():
    root = create_root()
    label = create_label(root)
    entry = create_entry(root)
    create_button(root, label, entry)
    root.mainloop()


if __name__ == '__main__':
    main()
