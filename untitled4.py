# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 14:07:39 2023

@author: Marcus
"""

from pytube import YouTube

progress = 0
def showProgress(stream,chunk,bytes_remaining):
    global progress
    preProgress = progress
    size = stream.filesize
    currentProgress = int((size - bytes_remaining)*100) // size
    progress = currentProgress
    
    if progress == 100:
        print("finish")
        return
    
    if preProgress != progress:
        print("progress: " + str(currentProgress) + "%")
    
yt = YouTube("https://www.youtube.com/watch?v=8QDRT1aGDkI",on_progress_callback=showProgress)
stream = yt.streams.filter(res="720p").first()
print (stream)
stream.download("youtube", "test.3gpp")