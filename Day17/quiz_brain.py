class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def check_answer(self, choice, current_question):
        if choice.lower() == current_question.answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"You got it wrong, your current score is {self.score}/12")

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):

        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number} {current_question.question}. True/False? ")
        answer = current_question.answer
        self.check_answer(choice, current_question)


