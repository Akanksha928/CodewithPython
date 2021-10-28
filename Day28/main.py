import math
from tkinter import *
# ----------------------CONSTANTS-----------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1500
SHORT_BREAK_MIN = 300
LONG_BREAK_MIN = 1200
mark = ""
reps = 0
temp = None

# -----------------------TIMER RESET-----------------------#


def restart_timer():

    window.after_cancel(temp)
    global reps
    global mark
    reps = 0
    mark = ""
    checkmark.config(text=mark)
    start_timer()

# ----------------------TIMER MECHANISM---------------------#


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        clock(LONG_BREAK_MIN)
        timer.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        clock(SHORT_BREAK_MIN)
        timer.config(text="Break", fg=PINK)

    else:
        clock(WORK_MIN)
        timer.config(text="Work")


# --------------------------COUNTDOWN MECHANISM--------------------------#


def clock(count):
    global mark
    global temp
    mins, secs = divmod(count, 60)
    timing = '{:02d}:{:02d}'.format(mins, secs)
    if count >= 0:
        canvas.itemconfig(timer_text, text=timing)
        temp = window.after(1000, clock, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        checkmark.config(text=mark)

# ----------------------------UI SETUP---------------------------- #


window = Tk()
window.title("POMODORO")
window.config(padx=40, pady=40, bg=YELLOW)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer.grid(row=0, column=1)

canvas = Canvas(width=400, height=400, bg=YELLOW, highlightthickness=0)
pic = PhotoImage(file="tomato.png")
canvas.create_image(200, 200, image=pic)
timer_text = canvas.create_text(200, 200, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start = Button(text="Start", bg="white", command=start_timer)
start.grid(row=2, column=0)

checkmark = Label(text=mark, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark.grid(row=2, column=1)

restart = Button(text="Reset", bg="white", command=restart_timer)
restart.grid(row=2, column=2)
window.mainloop()
