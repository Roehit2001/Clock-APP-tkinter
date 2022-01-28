from curses import window
from tkinter import *
from tkinter import ttk, font
from datetime import datetime


def timeloop():
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    txt.set(current_time)
    window.after(1000, timeloop)


# creating window
window = Tk()

photo = PhotoImage(file="logo.png")
window.iconphoto(False, photo)
window.tk.call('tk', 'scaling', 2.0)
font.families()
window.configure(background='#121212')
style = ttk.Style()
style.theme_use('winnative')
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
# print(width)
window.title("Clock")
window.after(1000, timeloop)
# but = Button(window, text="X", fg="white", bg="#121212",
#              command=window.quit, font=("Comic Sans MS", 15, font.BOLD)).place(x=int(width-50), y=10)
txt = StringVar()
label = Label(window, textvariable=txt,
              fg="white", bg="#121212", font=("Comic Sans MS", int(height/8), font.BOLD))
label.config(anchor=CENTER)
label.pack(pady=(height/3))
window.mainloop()
