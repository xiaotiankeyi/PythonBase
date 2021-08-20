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
        """创建Label标签"""

        self.btn03 = Label(self, text="字节跳动", width=10, height=2, bg='yellow', fg='black', font=("黑体", 20))
        self.btn03.pack()

        """添加图片"""
        global img
        img = PhotoImage(file="")
        self.btn04 = Label(self, image=img)
        self.btn04.pack()


    def Popup_window(self):
        messagebox.showinfo("alert show", "这个是弹出的警告弹窗！！！！")
if __name__ == "__main__":
    root = Tk()
    root.geometry("400x100+200+300")
    root.title("一个经典的GUI程序的测试运行")
    app = Application(master=root)
    root.mainloop()