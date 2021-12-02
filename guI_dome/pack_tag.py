# pack布局管理

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
        """pack布局管理应用"""

        self.f1 = Frame(self.master, bg=None, height=15)
        self.f1.pack()
        self.f2 = Frame(self.master, bg=None)
        self.f2.pack()

        f1_text = ("中国风", '摇滚', '流行', '爵士')
        for i in f1_text:
            Button(self.f1, text=i).pack(side='left', padx=10)

        for j in range(1, 15):
            Label(
                self.f2,
                width=5,
                height=20,
                borderwidth=1,
                relief="solid",
                bg='black' if j %
                2 == 0 else 'white').pack(
                side='left',
                padx=2)

    def Popup_window(self):
        messagebox.showinfo("alert show", "这个是弹出的警告弹窗！！！！")


if __name__ == "__main__":
    root = Tk()
    root.geometry("700x220")
    root.title("一个经典的GUI程序的测试运行")
    app = Application(master=root)
    root.mainloop()
