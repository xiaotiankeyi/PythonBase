# GUI实现计算器的功能

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """GUI程序面向对象的经典写法"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        """calculator界面布局"""

        Entry(self, bd=3).grid(row=0, column=0, columnspan=4, sticky='NSEW')

        element = (
            ('AC', '±', '%', '÷'),
            (7, 8, 9, 'x'),
            (4, 5, 6, '-'),
            (1, 2, 3, '+'),
            (0, '.', '='),
        )
        for index, ele in enumerate(element):
            for i, val in enumerate(ele):
                if val == 0:
                    Button(
                        self,
                        text=val,
                        width=6,
                        height=3).grid(
                        row=index + 1,
                        column=i,
                        rowspan=1,
                        sticky=NSEW,
                        columnspan=2)
                elif val == '.':
                    Button(
                        self,
                        text=val,
                        width=6,
                        height=3).grid(
                        row=index + 1,
                        column=i + 1,
                        rowspan=1,
                        sticky=NSEW)
                elif val == '=':
                    Button(
                        self,
                        text=val,
                        width=6,
                        height=3).grid(
                        row=index + 1,
                        column=i + 1,
                        rowspan=1,
                        sticky=NSEW)
                else:
                    Button(
                        self,
                        text=val,
                        width=6,
                        height=3).grid(
                        row=index + 1,
                        column=i,
                        rowspan=1,
                        sticky=NSEW)

    def Popup_window(self):
        messagebox.showinfo("alert show", "这个是弹出的警告弹窗！！！！")


if __name__ == "__main__":
    root = Tk()
    root.geometry("230x290")
    root.title("计算器")
    app = Application(master=root)
    root.mainloop()
