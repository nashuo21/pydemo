#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter
from tkinter import *

root = Tk()

btn_ok = Button(master=None)


li = ['c', 'python', 'php', 'html', 'sql', 'java']
movie = ['css', 'jquery', 'bootstrap']
listb = Listbox(root)
listb2 = Listbox(root)
for item in li:
    listb.insert(0, item)
for item in movie:
    listb2.insert(0, item)
listb.pack()
listb2.pack()

root.mainloop()
