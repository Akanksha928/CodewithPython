import tkinter.messagebox
from tkinter import *
import random
import pyperclip
import json

# --------------GENERATE PASSWORD ------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def search():
    website_name = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        tkinter.messagebox.showerror(title="Error", message="No data file found :(")

    if website_name in data:
        tkinter.messagebox.showinfo(title=website_name, message=f"Email: {data[website_name]['Email']}\nPassword:"
                                                                f" {data[website_name]['Password']}")
    else:
        tkinter.messagebox.showerror(title="Error", message="The data you are looking for doesn't exist.")


def generate():

    letters_pwd = [random.choice(letters) for _ in range(random.randint(6, 8))]
    symbols_pwd = [random.choice(symbols) for _ in range(random.randint(1, 3))]
    numbers_pwd = [random.choice(numbers) for _ in range(random.randint(1, 3))]

    pwd = letters_pwd + symbols_pwd + numbers_pwd

    random.shuffle(pwd)
    gen_password = "".join(pwd)
    password_entry.delete(0, END)
    password_entry.insert(0, gen_password)
    pyperclip.copy(gen_password)

# --------------SAVE PASSWORD-------------#


def submit():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password_name = password_entry.get()
    new_data = {
        website_name:
            {
                "Email": email_name,
                "Password": password_name,
            }
    }

    if len(website_name) == 0 or len(password_name) == 0:
        tkinter.messagebox.showerror(title="Error", message="Don't leave any of the fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# -----------------UI SETUP----------------#


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(height=200, width=200)
pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pic)
canvas.grid(row=0, column=1)

website = Label(text="Website")
website.grid(row=1)
email = Label(text="Email/Username")
email.grid(row=2)
password = Label(text="Password")
password.grid(row=3)

website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, padx=5, pady=5)
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=2)
email_entry.insert(0, "akanksha@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, padx=5, pady=5)

generate_pwd = Button(text="Generate Password", command=generate)
generate_pwd.grid(row=3, column=2, padx=5, pady=5)

add = Button(text="Add", width=44, command=submit)
add.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

search = Button(text="Search", width=15, command=search)
search.grid(row=1, column=2, padx=5, pady=5)

window.mainloop()
