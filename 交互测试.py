from tkinter import *
root = Tk()


v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()

button1 = Checkbutton(root, text = '头部',indicatoron=False,variable=v1,padx=25,pady=10)
button2 = Checkbutton(root, text = '躯干',indicatoron=False,variable=v2,padx=25,pady=10)
button3 = Checkbutton(root, text = '下盘',indicatoron=False,variable=v3,padx=25,pady=10)
button4 = Checkbutton(root, text = '左侧',indicatoron=False,variable=v4,padx=25,pady=10)
button5 = Checkbutton(root, text = '右侧',indicatoron=False,variable=v5,padx=25,pady=10)
                  # 将小部件放置到主窗口中
button1.place(x=100, y=0, anchor=NW)
button2.place(x=100, y=50, anchor=NW)
button3.place(x=100, y=100, anchor=NW)
button4.place(x=0, y=50, anchor=NW)
button5.place(x=200, y=50, anchor=NW)

root.mainloop()                 # 进入消息循环
