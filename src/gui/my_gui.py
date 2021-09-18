# -*- coding:utf-8 -*-
# @Project ：get_novel
# @File: my_gui.py
# @Time: 2021/9/13 16:02
# @Author: zyxhangzhou


from tkinter import *
from src.const.const_value import *


def selection():
    lb.config(text=WEB_INFO[WEB_NAMES[v.get()]][0])


master = Tk()
fm1 = Frame(master)
fm1.pack(fill=BOTH, expand=YES)
v = IntVar()
for i in range(0, len(WEB_NAMES_CN)):
    b = Radiobutton(fm1, text=WEB_NAMES_CN[i], variable=v, value=i, command=selection)
    b.pack(side='left', fill='both', expand=True)
lb = Label(fm1, text=WEB_INFO[WEB_NAMES[0]][0])
lb.pack(side='right')
Label(fm1, text='默认网址：', bg='gray').pack(side='right')
fm2 = Frame(master)
fm2.pack(fill=BOTH, expand=YES)
Label(fm2, text='请输入第一章的网址：', bg='gray', relief=RIDGE, bd=3).pack(side=LEFT, fill=BOTH, expand=YES)
Entry(fm2).pack(side=RIGHT, fill=BOTH, expand=YES)
master.mainloop()
