from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=30, bg=THEME_COLOR)
        self.score = 0

        self.score_label = Label(text=f"Score: {self.score}/{self.quiz.question_number}", bg=THEME_COLOR, fg="white",
                                 font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.display = self.canvas.create_text(150, 125, text="Some text", fill=THEME_COLOR, font=("Arial", 20, "italic"
                                                                                                   ), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=30)

        tick_image = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=tick_image, highlightthickness=0, bd=0, command=self.check_for_right_button)
        self.tick_button.grid(row=2, column=0, padx=20, pady=20)

        cross_image = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_image, highlightthickness=0, bd=0, command=self.check_for_wrong_button)
        self.cross_button.grid(row=2, column=1, padx=20, pady=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.display, text=q_text)
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.itemconfig(self.display, text="You've reached the end of the quiz.")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")
            self.canvas.config(bg="white")

    def check_for_wrong_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def check_for_right_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
        if not is_right:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
