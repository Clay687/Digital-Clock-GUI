from tkinter import *
from time import strftime
import win32gui , win32con

root = Tk()
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide,win32con.SW_HIDE)

root.title("Digital Clock")
root.geometry("300x72")
root.minsize(300,72)
root.maxsize(300,72)
root.wm_iconbitmap("C:\\Users\\prince\\Desktop\\GUI\\Required files\\Clock.ico")

hour =strftime('%H')
if int(hour)>12:
    final_hour = int(hour)-12
else:
    final_hour = hour

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font='calibri 40 bold',background='purple',foreground='white')

lbl.pack(anchor='center')
time()

root.mainloop()
