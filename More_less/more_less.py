#How much less/more
from tkinter import *
import tkinter

root = Tk()
root.title("MORE ± LESS")
root.geometry("350x208")
root.iconbitmap(default="more_less.ico")
root.resizable(height=FALSE, width=FALSE)

result=Label(root)

def func(event):
   global result
   result.destroy()  
   result = Label(root, text="", font=("Calibri 9 bold"), fg="#800000")
   result.place(x=117, y=162)

   a1=float(a.get())
   b1=float(b.get())
   if a1 > b1:
      ab = float(((a1-b1)/a1)*100)
      res="A more than B by: "+'{:.3f}'.format(ab)+"%"
   elif a1 < b1:
      ba = float(((b1-a1)/b1)*100)
      res="A less than B by: "+'{:.3f}'.format(ba)+"%"
   elif a1 == b1:
      res="0%"
   result.config(text=res)  

def limit_size_a(*args):
   value = a.get()  
   if len(value) > 10: 
        a.set(value[:10]) 
   for i in value:
        if i.isalpha():
            a.set(value="")

def limit_size_b(*args):
   value = b.get()  
   if len(value) > 10: 
        b.set(value[:10]) 
   for i in value:
        if i.isalpha():
            b.set(value="")    


title_label = Label(root, text="MORE ± LESS", font=("Helvetica 18 bold"), width=20, pady=20, padx=23, justify=CENTER, fg="white", bg="#333")
title_label.grid(row=0, column=0, sticky="w") 

a_label = Label(root, text="input А: ", font=("Helvetica 10 italic"))
a_label.place(x=50, y=90)

b_label = Label(root, text="input В: ", font=("Helvetica 10 italic"))
b_label.place(x=50, y=120)

a = StringVar()
a.trace("w", limit_size_a)
a_entry = Entry(root, width=28, textvariable=a)
a_entry.place(x=120, y=89)
a_entry.focus_set()

b = StringVar()
b.trace("w", limit_size_b)
b_entry = Entry(root, width=28, textvariable=b)
b_entry.place(x=120, y=119)

result = Label(root, text="", font=("Calibri 11 bold"), fg="#800000")
result.place(x=117, y=162) 
 
calculate_button = Button(root, text="calculate", font=("Calibri 9 bold"), bg="#333", fg="white")
calculate_button.place(x=50, y=160)

a_entry.bind("<Return>", func)
b_entry.bind("<Return>", func)
calculate_button.bind("<Button-4>", func)
calculate_button.bind("<ButtonRelease-1>", func)


root.mainloop()