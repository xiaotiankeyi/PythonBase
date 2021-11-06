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
        """创建Entry标签"""

        self.btn03 = Label(self, text="用户名",)
        self.btn03.pack()

        v1 = StringVar()
        self.btn01 = Entry(self, textvariable=v1, cursor='arrow')
        self.btn01.pack()
        v1.set('jack')

        self.btn02 = Label(self, text="密码",)
        self.btn02.pack()

        v2 = StringVar()
        self.btn04 = Entry(
            self,
            show='*',
            cursor='arrow',
            stat='normal',
            textvariable=v2,
        )
        self.btn04.pack()

        Button(self, text='登录', command=self.login).pack()

    def login(self):
        username = self.btn01.get()
        password = self.btn04.get()
        print('用户名为:{}\n密码是:{}'.format(username, password))
        if username == "jack" and password == "123456":
            messagebox.showinfo('登录状态', "success 登录成功！！！")
        else:
            messagebox.showinfo('登录状态', "fail 登录失败！！！")


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x200+200+300")
    root.title("一个经典的GUI程序的测试运行")
    app = Application(master=root)
    root.mainloop()
