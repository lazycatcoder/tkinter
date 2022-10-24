#Shorten link
from tkinter import*
from tkinter import messagebox, Canvas
import pyperclip
import pyshorteners
from pyshorteners import Shortener
from PIL import Image, ImageTk


def main(root):
    
    def copytoclipboard():
        url = res.get()
        pyperclip.copy(url)

    def short(event):
        try:
            res.delete(0, END)
            shorturl = pyshorteners.Shortener()
            short_link=shorturl.tinyurl.short(str(link.get()))
            res.insert(0, str(short_link))
        except:
            messagebox.showerror("short link", "Error link")

    def clear():
        link.delete(0, "end")
        res.delete(0, "end")

    title_text = c.create_text(208, 30, text="SHORTEN LINK", font="Calibri 15 bold", fill="#FFFFFF")

    link_text = c.create_text(200, 60, text="link", font="Calibri 11 italic", fill="#FFFFFF")
    link = Entry(root, width=50)
    link.place(x=50, y=75)

    shorten_link_text = c.create_text(200, 120, text="shorten link", font="Calibri 11 italic", fill="#FFFFFF")
    res= Entry(root, width=50)
    res.place(x=50, y=135)

    but1 = Button(root, text="SHORT", width=10, font="Calibri 9 bold", relief="flat")
    but1.place(x=165, y=165)

    but2 = Button(root, text="COPY", width=10, font="Calibri 9", relief="flat", command=copytoclipboard)
    but2.place(x=165, y=195)

    but2 = Button(root, text="CLEAR", width=10, font="Calibri 9", relief="flat", command=clear)
    but2.place(x=165, y=225)

    link.bind("<Return>", short)
    but1.bind("<Button-4>", short)
    but1.bind("<ButtonRelease-1>", short)

    link.focus_set()


if __name__ == "__main__":
    root = Tk()
    root.title("Shorten link")
    root.iconbitmap(default="link.ico")
    root.geometry("400x280")
    root.resizable(False, False) 

    xx = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 8
    yy = (root.winfo_screenheight() - root.winfo_reqheight()) / 6
    root.wm_geometry("+%d+%d" % (xx, yy))

    src_img = Image.open("img.jpg")
    img_obj = ImageTk.PhotoImage(src_img)
    c = Canvas(root, width=400, height=280)
    c.place(x=0, y=0, relwidth=1, relheight=1)
    c.create_image(0, 0, anchor="nw", image=img_obj)
    
    src_icon = Image.open("link.png")
    img_resize = src_icon.resize((18, 18), Image.LANCZOS)
    icon_png = ImageTk.PhotoImage(img_resize)
    c.create_image(133, 30, image=icon_png)
    
    app = main(root)
    root.mainloop()