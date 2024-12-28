from tkinter import *
from tkinter.messagebox import *
import itertools
import time

class Game:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("550x510")
        self.pic = PhotoImage(file='wuziqi2.png')
        self.r = Canvas(self.root, width=520, height=460)
        self.r.pack()
        self.r.create_image(290, 200, image=self.pic)
        b1 = Button(self.root, text="开始", width=10)
        b1.pack()
        b1.place(x=150, y=480)
        b1.bind('<Button-1>', self.start)
        b2 = Button(self.root, text="退出 ", command=self.root.destroy)
        b2.pack()
        b2.place(x=300, y=480)
        self.root.mainloop()

    def callback1(self, event):
        u, v = event.x, event.y
        for i in range(1, 16):
            if 15 * i < u < 15 * (2 * i + 1):
                zx = i - 1
                break
        for i in range(1, 16):
            if 15 * i < v < 15 * (2 * i + 1):
                zy = i - 1
                break
        self.matrix[zx][zy] = 1
        print('实际落子位置是', (u, v))
        print(f'实际生成棋子的坐标为({zx},{zy})')
        self.c.create_oval((zx + 1) * 30 - 12, (zy + 1) * 30 - 12, (zx + 1) * 30 + 12, (zy + 1) * 30 + 12, fill="black")
        win = self.panfen(zx, zy)
        if win == 1:
            answer = showinfo("Game over", "黑子赢！")
            self.start(event)

    def callback2(self, event):
        u, v = event.x, event.y
        for i in range(1, 16):
            if 15 * i < u < 15 * (2 * i + 1):
                zx = i - 1
                break
        for i in range(1, 16):
            if 15 * i < v < 15 * (2 * i + 1):
                zy = i - 1
                break
        if self.matrix[zx][zy] == 0:
            self.matrix[zx][zy] = -1
            print(f'坐标({zx},{zy})的值为{self.matrix[zx][zy]}')
            self.c.create_oval((zx + 1) * 30 - 12, (zy + 1) * 30 - 12, (zx + 1) * 30 + 12, (zy + 1) * 30 + 12,
                               fill="white")
        else:
            showinfo("error", "落子位置被占，请重新落子")
        win = self.panfen(zx, zy)
        if win == -1:
            answer = showinfo("Game over", "White wins!")
            self.start(event)

    def panfen(self, x, y):

        four_direction = []
        # 获取水平和竖直方向的列表
        four_direction.append([self.matrix[i][y] for i in range(15)])
        four_direction.append([self.matrix[x][j] for j in range(15)])
        # 获取向左下斜方向的列表
        print('水平竖直方向的值为:', four_direction)
        zuox = []
        for i in range(15):
            for j in range(15):
                if i + j == x + y:
                    zuox.append(self.matrix[i][j])
        four_direction.append(zuox)
        # print('左斜为',zuox)
        # 获取向右下斜方向的列表
        youx = []
        if x < y:
            for i in range(15 - (y - x)):
                youx.append(self.matrix[i][i + (y - x)])
        else:
            for i in range(15 - (x - y)):
                youx.append(self.matrix[i + (x - y)][i])
        four_direction.append(youx)
        # print('右斜为',youx)
        # 判断列表four_direction分组数据中1和-1连续的个数是否为5个
        black, white = [0], [0]
        for i in four_direction:
            for k, v in itertools.groupby(i):
                if k == 1:
                    black.append(len(list(v)))
                elif k == -1:
                    white.append(len(list(v)))
            # print('黑白分别为',black,white)
            if max(black) >= 5:
                return 1
            elif max(white) >= 5:
                return -1

    def start(self, event):
        self.label = Label(self.root, text='游戏开始', fg='red')
        self.label.pack()
        self.r.destroy()
        self.c = Canvas(self.root, width=460, height=460, bg="yellow")
        self.c.pack()
        self.c.place(x=20, y=20)
        for i in range(1, 16):
            self.c.create_line(30, 30 * i, 450, 30 * i)
            self.c.create_line(30 * i, 30, 30 * i, 450)
        for i in range(30, 451, 30):
            for j in range(30, 451, 30):
                self.c.create_oval(i - 2, j - 2, i + 2, j + 2, fill="blue")
        self.c.bind("<Button-1>", self.callback1)
        self.c.bind("<Button-3>", self.callback2)
        self.matrix = [[0 for y in range(15)] for x in range(15)]
        self.c.mainloop()

Game()
