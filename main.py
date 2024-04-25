from tkinter import *
from pytube import YouTube

def Download_Video():
    url = YouTube(str(link.get()))
    video = url.streams.filter(res=str(resolution.get())).first()
    video.download()
    link.set('')

def Download_Only_Audio():
    url = YouTube(str(link.get()))
    audio = url.streams.filter(only_audio=True).first()
    audio.download()
    link.set('')

root = Tk()
root.tk.call('tk', 'scaling', 2.0)
root.geometry('590x500')
root.resizable(0, 0)
root.title('YT Downloader v2.0')
root.configure(bg='#7D2181') 

Label(root, text='YT Video Downloader', font='arial 20', bg='#7D2181').place(x=90, y=30)

link = StringVar()
Label(root, text='Enter the link here', font='arial 12', bg='#7D2181').place(x=190, y=90)
link_enter = Entry(root, width=50, textvariable=link).place(x=32, y=120)

resolution = StringVar(root)
resolution.set('720p')
resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p']
Label(root, text='Choose the resolution', font='arial 12', bg='#7D2181').place(x=190, y=150)
resolution_menu = OptionMenu(root, resolution, *resolutions).place(x=230, y=180)

Button(root, text='Download Video', font='arial 13', bg='#B57199', padx=2, command=Download_Video).place(x=180, y=240)
Button(root, text='Download Audio', font='arial 13', bg='#B57199', padx=2, command=Download_Only_Audio).place(x=180, y=300)

root.mainloop()