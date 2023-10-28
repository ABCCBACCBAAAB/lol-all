# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 14:06:52 2023

@author: Marcus
"""

import tkinter as tk
import threading
def thread():
    threading.Thread(target=onClick).start()
    

def onCLick():
    
    golbal var
    var.set(entry.get())
    button.config(state=tk.DISABLED)
    try:
        
        yt = YouTube(var.get(),
                     on_progress_callback=showProgress)
        
        if onlyMusic.get():
            stream = yt.stream.filter(only_audio=True).first()
        else:
            stream = yt.streams.first()
    except:
        pass
    button.config(state=tk.NORMAL)
window = tk.Tk()

window.title("???")
window.geometry("500x150")
window.resizable(False,False) 

onlyMusic = tk.BooleanVar()
check = tk.Checkbutton(window, text = "bla", variable = onlyMusic,
                         onvalue = True, offvalue = False)
check.pack()
button = tk.Button(window, text = "download",
                   command = thread)
button.pack()
window.mainloop()
