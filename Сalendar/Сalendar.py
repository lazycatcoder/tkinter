#Calendar
from tkinter import *
from tkcalendar import *
import datetime


root = Tk()
root.title("Calendar")
root.iconbitmap(default="calendar.ico")
root.geometry("400x400")
root.resizable(False, False) 
root.configure(bg="#B9B9B9")


today = datetime.date.today()
cal = Calendar(root, font="Arial 10", selectmode="day", year=today.year, month=today.month, day=today.day)
cal.pack(padx=10, pady=5, fill='both', expand=True)

def grab_date():
    global my_label
    my_label.destroy()  
    my_label = Label(root, font="helvetica 10 italic", background="#B9B9B9", text="")
    my_label.pack(pady=10)
    my_label.config(text=cal.get_date())
    
def clear():
    global my_label
    my_label.destroy()
    my_label = Label(root, background="#B9B9B9")
    my_label.pack(pady=10)

my_button = Button(root, text="GET DATE", font="Arial 8 bold", width=8,relief="flat", command=grab_date)
my_button.pack(padx=10, side=LEFT)

my_button_2 = Button(root, text="CLEAR", font="Arial 8 bold", width=8, relief="flat", command=clear)
my_button_2.pack(padx=10, side=RIGHT)

my_label = Label(root, font="helvetica 10 italic", background="#B9B9B9", text="")
my_label.pack(pady=10)


root.mainloop()