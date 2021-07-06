from tkinter import *
from tkinter import messagebox
from tkinter import Radiobutton


class Application(Frame):
    """GUI程序面向对象的经典写法"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        """创建Radiobutton_单选标签"""
        self.v = StringVar()
        self.r1 = Radiobutton(self, text='men', value='m', variable=self.v)
        self.r2 = Radiobutton(self, text='women', value='w', variable=self.v)

        self.r1.pack(side='left')
        self.r2.pack(side='left')

        Button(self, text='提交', command=self.Popup_window).pack()

    def Popup_window(self):
        messagebox.showinfo("选取性别", "{}".format(self.v.get()))

if __name__ == "__main__":
    root = Tk()
    root.geometry("400x100+200+300")
    root.title("一个经典的GUI程序的测试运行")
    app = Application(master=root)
    root.mainloop()