import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
correct_guesses = []


def determine_title():
    if len(correct_guesses) == 0:
        return "Guess the State"
    else:
        return f"{len(correct_guesses)}/50 States Correct"


def gen_csv():
    states_to_learn = []
    for state in all_states:
        if state not in correct_guesses:
            states_to_learn.append(state)
    new_data = pandas.DataFrame(states_to_learn)
    new_data.to_csv('states_to_learn.csv')


while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=determine_title(), prompt="What's another state's name?").title()
    if answer_state == "Exit":
        gen_csv()
        break
    if answer_state in all_states and answer_state not in correct_guesses:
        correct_state = data[data.state == answer_state]
        correct_guesses.append(answer_state)
        coordinates = (int(correct_state.x), int(correct_state.y))

        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        text.goto(coordinates)
        text.write(answer_state)


