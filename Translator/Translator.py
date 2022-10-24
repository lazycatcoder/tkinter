#Translator
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import googletrans
import textblob


root = Tk()
root.title("Translator")
root.iconbitmap(default="translate.ico")
root.geometry("845x260")
root.resizable(False, False) 

src_img = Image.open("tag.png")
img_obj = ImageTk.PhotoImage(src_img)
c = Canvas(root)
c.place(x=0, y=0, relwidth=1, relheight=1)
c.create_image(0, 0, anchor="nw", image=img_obj)

def translate():
	translated_text.delete(1.0, END)
	try:
		for key, value in languages.items():
			if (value == original_lang.get()):
				from_language_key = key

		for key, value in languages.items():
			if (value == translated_lang.get()):
				to_language_key = key

		words = textblob.TextBlob(original_text.get(1.0, END))
		words = words.translate(from_lang=from_language_key , to=to_language_key)
		translated_text.insert(1.0, words)
	except Exception as ex:
		messagebox.showerror("Translator", ex)

def clear():
	original_text.delete(1.0, END)
	translated_text.delete(1.0, END)

def change():
	index_original = original_lang.get()
	index_translated = translated_lang.get()
	original_lang.set(index_translated)
	translated_lang.set(index_original)

	get_text_original = original_text.get(1.0, END)
	get_text_translated = translated_text.get(1.0, END)
	original_text.delete(1.0, END)
	translated_text.delete(1.0, END)
	original_text.insert(1.0, get_text_translated)
	translated_text.insert(1.0, get_text_original)

	
languages = googletrans.LANGUAGES
lang_list = list(languages.values())

original_text = Text(root, height=10, width=40, font="Helvetica 11", borderwidth=2, fg="#0088aa")
original_text.grid(row=0, column=0, pady=20, padx=10)

style = ttk.Style()
style.configure("translate.TButton", font=('Helvetica', 14, 'bold'))
style.configure("clear.TButton", font=('Helvetica', 8, 'bold'))
style.configure("change.TButton", font=('Helvetica', 8, 'bold'))

translate_button = ttk.Button(root, text="TRANSLATE", style="translate.TButton", command=translate)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40, font="Helvetica 11", borderwidth=2, fg="#0088aa")
translated_text.grid(row=0, column=2, pady=20, padx=10)

original_lang = ttk.Combobox(root, width=43, font="Tahoma 8 bold", value=lang_list)
original_lang.current(21)
original_lang.grid(row=1, column=0)

translated_lang = ttk.Combobox(root, width=43, font="Tahoma 8 bold", value=lang_list)
translated_lang.current(97)
translated_lang.grid(row=1, column=2)

clear_button = ttk.Button(root, text="clear", style="clear.TButton", command=clear)
clear_button.place(x=383, y=160)

change_button = ttk.Button(root, text="change lang", style="change.TButton", command=change)
change_button.grid(row=1, column=1)


root.mainloop()