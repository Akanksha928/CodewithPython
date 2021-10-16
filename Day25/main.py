import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
guessed_states = []
states_list = data["state"].tolist()

game_is_on = True
while game_is_on:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 Guessed", prompt="Enter a state's name: ").title()
    if answer in states_list:
        guessed_states.append(answer)
        answer_data = data[data.state == answer]
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(int(answer_data.x), int(answer_data.y))
        state.write(answer)
    if answer == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missed_states.csv")
        game_is_on = False


