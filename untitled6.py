# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:22:58 2023

@author: Marcus
"""

from pytube import YouTube
import tkinter as tk
def onClick():
    
    global var
    var.set(entry.get())
    
    yt = YouTube(var.get(),
                     on_progress_callback=showProgress)
    
    stream = yt.streams.first()
    stream.download()
window = tk.Tk()

window.title("Youtube download")
window.geometry("500x150")
window.resizable(False,False)
label = tk.Label(window,
                 text = "chose a youtube web")
label.pack()

var = tk.StringVar()
entry = tk.Entry(window, width = 50)
entry.pack()

button = tk.Button(window, text = "download",
                   command = onClick)
button.pack()
scale = tk.Scale(window, label='load',
                 from_=0, to=100,
                 orient=tk.HORIZONTAL,
                 length=200, showvalue=False,
                 tickinterval=0)
scale.pack()

window.mainloop()
