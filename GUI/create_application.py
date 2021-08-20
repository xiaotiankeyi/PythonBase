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
        """创建组建"""
        self.btn01 = Button(self)
        self.btn01['text'] = "点击弹出弹窗"
        self.btn01.pack()
        self.btn01['command'] = self.Popup_window

        """创建推出按钮"""
        self.btnquit = Button(self, text="quit", command=root.destroy)
        self.btnquit.pack()

    def Popup_window(self):
        messagebox.showinfo("alert show", "这个是弹出的警告弹窗！！！！")


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x100+200+300")
    root.title("一个经典的GUI程序的测试运行")
    app = Application(master=root)
    # 进入消息循环
    root.mainloop()
