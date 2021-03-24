#Clock

from tkinter import Tk,Label

from time import strftime
from datetime import date

#function to print the time in label
def Time():
    string=strftime("%H:%M:%S %p")
    today=date.today()

    #setted our label to the given string or format provided
    label.config(text=string)
    #after is used to callback after an delay in milli seconds
    label.after(1000,Time)
    label1.config(text=today)

#-------------------------------
#setup of gui
root=Tk()
root.title("CLOCK")
label=Label(master=root,font=("Helvetica",80),backgroun="black",foreground="blue")
label1=Label(master=root,font=("Helvetica",90),backgroun="black",foreground="blue")
label1.pack()
label.pack()

Time()

root.mainloop()