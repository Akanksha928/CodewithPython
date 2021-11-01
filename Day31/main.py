from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    dictionary = pandas.read_csv("data/to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    dictionary = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
current_card = {}


def show_words():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dictionary)
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(background, image=front_pic)
    flip_timer = window.after(3000, func=flip_card)

# Flipping card mechanism

def flip_card():
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(background, image=back_pic)

# Creating csv file of words to learn

def to_learn():
    dictionary.remove(current_card)
    words_to_learn = pandas.DataFrame(dictionary)
    words_to_learn.to_csv("data/to_learn.csv", index=False)
    show_words()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, highlightthickness=0)
front_pic = PhotoImage(file="images/card_front.png")
background = canvas.create_image(400, 263, image=front_pic)
back_pic = PhotoImage(file="images/card_back.png")

canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, command=to_learn)
tick_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=show_words)
wrong_button.grid(row=1, column=1)

word = canvas.create_text(400, 270, font=("Arial", 60, "bold"))
title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
show_words()
window.mainloop()
