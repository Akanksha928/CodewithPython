from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []

for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

brain = QuizBrain(question_bank)
while brain.still_has_questions():
    brain.next_question()

print("Your quiz is complete!")
print(f"Congrats! Your final score is {brain.score}/12.")

