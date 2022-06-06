"""
Created on Fri Mar 25 10:48:48 2022

@author: Samson N.

pip install tkinter

"""

from tkinter import Label, Tk
import time

app_clock = Tk()
app_clock.iconbitmap('logoClock.ico')
app_clock.title("Digital Clock")
app_clock.geometry('420x150')
app_clock.resizable(1,1)
font_size = ('Boulder', 72, 'bold')
bg = '#f2e750'
fg = '#363529'
border = 20
label = Label(app_clock, font = font_size, bg = bg, fg = fg, bd = border)
label.grid(row = 0, column = 1)
def digi_clock():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(200, digi_clock)

digi_clock()
app_clock.mainloop()
