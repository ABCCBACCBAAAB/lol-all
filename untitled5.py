# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:00:48 2023

@author: Marcus
"""

string = "HI"

def func2():
    global string
    string = "Bye" 
    print(string)
    
func2()
print(string)

import tkinter as tk

window = tk.Tk()
window.title("Scale")

scale = tk.Scale(window,label="OMG",
                 orient=tk.HORIZONTAL,
                 length=200)
scale.pack()

window.mainloop()