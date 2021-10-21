from tkinter import *

window = Tk()
window.title("Mile to Kilometre Converter")
window.config(padx=20, pady=20)


def convert():
    miles_input = float(entry.get())
    km = round(miles_input*0.62137, 2)
    zero.config(text=km)


entry = Entry()
entry.config(width=7)
entry.grid(row=0, column=1)

miles = Label(text="Miles", font=("Arial", 10))
miles.grid(row=0, column=2)
miles.config(padx=10, pady=10)

equal = Label(text="is equal to", font=("Arial", 10))
equal.grid(row=1, column=0)

zero = Label(text="0", font=("Arial", 10))
zero.grid(row=1, column=1)
zero.config(padx=10, pady=10)

km = Label(text="km", font=("Arial", 10))
km.grid(row=1, column=2)

calculate = Button(text="Calculate", command=convert)
calculate.grid(row=2, column=1)
window.mainloop()
