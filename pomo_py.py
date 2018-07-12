# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:46:18 2018

@author: bhavyas
"""
import tkinter as Tk

win = Tk.Tk()
win.geometry('1080x720')
win.title("Welcome to LikeGeeks app")
lbl = Tk.Label(win, text="Har Har Mahadev", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
win.mainloop()