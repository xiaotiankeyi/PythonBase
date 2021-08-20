# grid布局管理器

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

        self.btn03 = Label(self, text="username",)
        self.btn03.grid(row=0, column=0)
        Label(self, text='telephone and e-mail').grid(row=0, column=2)

        v1 = StringVar()
        self.btn01 = Entry(self, textvariable=v1, cursor='arrow')
        self.btn01.grid(row=0, column=1)
        v1.set('jack')

        self.btn02 = Label(self, text="password",)
        self.btn02.grid(row=1, column=0)

        v2 = StringVar()
        self.btn04 = Entry(
            self,
            show='*',
            cursor='arrow',
            stat='normal',
            textvariable=v2,
        )
        self.btn04.grid(row=1, column=1)

        Button(
            self,
            text='login',
            command=self.login).grid(
            row=3,
            column=1,
            sticky=EW)
        Button(self, text='close', command=self.colse).grid(row=3, column=2)

    def login(self):
        username = self.btn01.get()
        password = self.btn04.get()
        print('用户名为:{}\n密码是:{}'.format(username, password))
        if username == "jack" and password == "123456":
            messagebox.showinfo('登录状态', "success 登录成功！！！")
        else:
            messagebox.showinfo('登录状态', "fail 登录失败！！！")

    def colse(self):
        self.btn05 = Label(self)
        self.quit()


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x200+200+300")
    root.title("一个经典的GUI程序的测试运行")
    app = Application(master=root)
    root.mainloop()
