
import random
import art

print(art.logo)

print("Welcome to the Number Guessing Game!")
level = input("Choose a level to begin with. Type 'easy' or 'hard': ")
if level == "easy":
    attempts = 10
else:
    attempts = 5

num = random.randint(1,101)
print(f"You get {attempts} attempts")

while attempts > 0:

    answer_guessed = False
    guess = int(input("Guess a number: "))
    if guess == num:
        print("You guessed the answer!")
        answer_guessed = True
        break
    elif num > guess:
        print("Too low")
        attempts -=1
    elif num < guess:
        print("Too high")
        attempts -=1

if answer_guessed == False:
    print("Sorry, you used up all your attempts :( ")



    

