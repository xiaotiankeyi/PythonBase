from tkinter import *
from tkinter import messagebox
from tkinter import Checkbutton


class Application(Frame):
    """GUI程序面向对象的经典写法"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        """创建Checkbutton_多选标签，选中还回1，不选中还回0"""

        self.tomato = IntVar()
        self.r1 = Checkbutton(
            self,
            text='西红柿',
            onvalue=1,
            offvalue=0,
            variable=self.tomato)

        self.banana = IntVar()
        self.r2 = Checkbutton(
            self,
            text='香蕉',
            onvalue=1,
            offvalue=0,
            variable=self.banana)

        self.r1.pack(side='left')
        self.r2.pack(side='left')

        Button(self, text='提交', command=self.Popup_window).pack()

    def Popup_window(self):
        if self.tomato.get() == 1 and self.banana.get() == 1:
            messagebox.showinfo(
                "选取食物", "{}.西红柿🍅和{}.香蕉🍌".format(
                    self.tomato.get(), self.banana.get()))
        elif self.tomato.get() == 1:
            messagebox.showinfo("选取食物", "{}.西红柿🍅".format(self.tomato.get()))

        elif self.banana.get() == 1:
            messagebox.showinfo("选取食物", "{}.香蕉🍌".format(self.banana.get()))

        else:
            pass


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x100+200+300")
    root.title("一个经典的GUI程序的测试运行")
    app = Application(master=root)
    root.mainloop()
