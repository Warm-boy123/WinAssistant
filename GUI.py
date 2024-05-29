import learnTkinter
from learnTkinter import messagebox, Frame, Button


# 定义类继承于画纸对象，然后把画纸放到画板上
class Application(Frame):
    """经典的GUI程序类的写法"""

    def __init__(self, master=None):  # master模板容器，画纸放到哪
        # 继承方法，父类的重新定义
        super().__init__(master)  # 定义属性
        self.master = master
        self.pack()  # 画纸几何布局，默认摆放
        self.CreatWidget()  # 创建示例对象时，自动进行调用

    def CreatWidget(self):
        """创建组件"""
        self.bt = Button(self)
        # self.bt = Button(self,text='按钮说明')
        self.bt['text'] = '按钮说明'  # 与上一行代码等同
        self.bt.pack()  # 默认布局
        # 事件绑定
        self.bt.bind('<Button-1>', self.massage_1)  # 绑定，方法里必须的有形参
        # self.bt['command'] = self.massage_1  # 用此方法的时候massage_1内不能有形参
        # 如果有形参，调用时候得进行传参，否则方法里就不能有形参 def massage_1(self)

    def massage_1(self, event):
        messagebox.showinfo('Message', '文档说明信息，点击关闭')


if __name__ == '__main__':  # 程序入口，里面的本文件内调用，其他程序访问不到
    root = tkinter.Tk()  # 创建主窗口
    root.title('标题-经典GUI程序类的测试')
    root.geometry('300x300+900+300')

    # 创建画纸对象放到root画板上
    Application(master=root)
    root.mainloop()  # 消息循环
