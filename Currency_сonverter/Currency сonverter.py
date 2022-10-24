#Currency convertet
from tkinter import *
from tkinter import ttk
import requests
import json
from tkinter.messagebox import showerror
from PIL import Image, ImageTk
import pyperclip


root = Tk()
root.geometry("452x300")
root.title("Currency Converter")
root.iconbitmap(default="conv.ico")
root.resizable(height=FALSE, width=FALSE)

primary = "#770D91"
secondary = "#770D91"
white = "#FFFFFF"
dark_bg = "#3b3b3b"
root["bg"] = dark_bg

top_frame = Frame(root, bg=primary, width=402, height=80)
top_frame.grid(row=0, column=0)

bottom_frame = Frame(root, width=330, height=250, bg=dark_bg)
bottom_frame.grid(row=1, column=0)


url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
response = requests.get(url).json()
exchangedate = (response[0].get("exchangedate"))

currency_code = []
currency_rate = []
for dict in response[:-4]:
    currency_code.append(dict["cc"])
    rate = (dict["rate"])
    corrected_rate = float(rate)
    currency_rate.append(corrected_rate)

currencies = {}
currencies.update({"UAH": "1.0"})
for i in range(0, len(currency_code)):
    currencies[currency_code[i]] = currency_rate[i]


def convert_currency(event):
    try:
        global formatted_result
        source = from_currency_combo.get()
        destination = to_currency_combo.get()
        amount = float(amount_entry.get())
        
        if source == "UAH":
            cr_source = float(currencies.get(source))
            cr__destination = float(currencies.get(destination))
            result = (cr_source / cr__destination) * amount
        elif destination == "UAH":
            cr_source = float(currencies.get(source))
            cr__destination = float(currencies.get(destination))
            result = (cr__destination * cr_source) * amount
        elif source == destination:
            cr_source = float(currencies.get(source))
            cr__destination = float(currencies.get(destination))
            result = (cr__destination / cr_source) * amount
        else:
            cr_source = float(currencies.get(source))
            cr__destination = float(currencies.get(destination))
            result = (cr_source / cr__destination) * amount   
            
        converted_result = round(result, 3)
        formatted_result = f"{amount} {source} = {converted_result} {destination}"
        result_label.config(text=formatted_result)
        time_label.config(text = "the exchange rate from bank.gov.ua is valid as of: "  + exchangedate)
    except:
        showerror(title = "Error", message="Something wrong!\nFill all the required field or check your internet connection.")

def limit_size_amount(*args):
    value = amountValue.get()

    if len(value) > 10: 
        amountValue.set(value[:10])
    for i in value:
        if i.isalpha():
            amountValue.set(value="")

def change_currency_code():
    code_currency_source = from_currency_combo.get()
    code_currency_destination = to_currency_combo.get()
    from_currency_combo.set(code_currency_destination)
    to_currency_combo.set(code_currency_source)

def clear():
    global result_label, time_label
    amount_entry.delete(0, END)

    result_label.destroy()
    result_label = Label(bottom_frame, text="", font=("Calibri 12"), bg=dark_bg, fg="white")
    result_label.place(x=-3, y=117)

    time_label.destroy()
    time_label = Label(bottom_frame, text="", font=("Calibri 9 italic"), bg=dark_bg, fg="white", justify=CENTER)
    time_label.place(x=-3, y=145)

def copy():
    res = f"{formatted_result}"
    pyperclip.copy(res)


img = ImageTk.PhotoImage(Image.open("сurrency_сonverter.png"))
name_label = Label(top_frame, image = img, width=452, bg=primary, pady=26, padx=23, justify=CENTER)
name_label.grid(row=0, column=0)

from_currency_label = Label(bottom_frame, text="FROM:", font=("Calibri 10 bold"), bg=dark_bg, fg="white", justify=LEFT)
from_currency_label.place(x=-1, y=10)

to_currency_label = Label(bottom_frame, text="TO:", font=("Calibri 10 bold"), bg=dark_bg, fg="white", justify=RIGHT)
to_currency_label.place(x=200, y=10)

from_currency_combo = ttk.Combobox(bottom_frame, values=list(currencies.keys()), width=14, font=("Calibri 10 bold"))
from_currency_combo.current(26)
from_currency_combo.place(x=1, y=30)

to_currency_combo = ttk.Combobox(bottom_frame, values=list(currencies.keys()), width=14, font=("Calibri 10 bold"))
to_currency_combo.current(33)
to_currency_combo.place(x=202, y=30)

amount_label = Label(bottom_frame, text="AMOUNT:", font=("Calibri 10 bold"), bg=dark_bg, fg="white")
amount_label.place(x=-1, y=60)

amountValue = StringVar()
amountValue.trace("w", limit_size_amount)
amount_entry = Entry(bottom_frame, width=32, font=("Calibri 15 bold"), textvariable=amountValue)
amount_entry.place(x=0, y=80)
amount_entry.focus_set()

result_label = Label(bottom_frame, text="", font=("Calibri 12"), bg=dark_bg, fg="white")
result_label.place(x=-3, y=117)

time_label = Label(bottom_frame, text="", font=("Calibri 9 italic"), bg=dark_bg, fg="white", justify=CENTER)
time_label.place(x=-3, y=145)

change_code_button = Button(bottom_frame, text="↔", bg=secondary, fg=white, font=("Calibri 8 bold"), command=change_currency_code)
change_code_button.place(x=151, y=30)

convert_button = Button(bottom_frame, text="CONVERT", bg=secondary, fg=white, font=("Calibri 10 bold"))
convert_button.place(x=-2, y=180)

copy_button = Button(bottom_frame, text="COPY", bg=secondary, fg=white, font=("Calibri 10 bold"), command=copy)
copy_button.place(x=143, y=180)

clear_button = Button(bottom_frame, text="CLEAR", bg=secondary, fg=white, font=("Calibri 10 bold"), command=clear)
clear_button.place(x=280, y=180)

amount_entry.bind("<Return>", convert_currency)
convert_button.bind("<Button-4>", convert_currency)
convert_button.bind("<ButtonRelease-1>", convert_currency)


root.mainloop()