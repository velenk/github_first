from tkinter import *

root = Tk()
v = IntVar()

position = [('头',1),
            ('身',2),
            ('左',3),
            ('右',4)
        ]
for p,num in position:
    b = Radiobutton(root,text=p,variable=v,value=num,indicatoron=False,padx=80,pady=20,font=('楷体',36))
    l = Label(root,textvariable=v)
    l.pack()
    b.pack(anchor=W,fill=X)
           
mainloop()
