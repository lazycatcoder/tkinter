#Сalculator
from tkinter import*

class main(Frame):
    def __init__(self, root):
        super(main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Arial", 24, "bold"), background="#EDEDED", foreground="#000", width=24, height=2, anchor=W, padx=4)
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "DEL", ".", "*",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "="
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logic(x)
            Button(text=bt, bg="#EDEDED", relief="flat", font=("Arial", 16), command=com).place(x=x, y=y, width=115, height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logic(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "=":
                self.formula = eval(self.formula)
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == "__main__":
    root = Tk()
    root["bg"] = "#FFF"
    root.geometry("486x550")
    root.title("Сalculator")
    root.iconbitmap(default="calc.ico")
    root.resizable(False, False)
    
    app = main(root)
    app.pack()
    
    root.mainloop()