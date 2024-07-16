import turtle
import pandas as pd
from scoreboard import ScoreBoard

score = ScoreBoard()
screen = turtle.Screen()
screen.title(f'U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")
correct_answers = []
unguessed_states = []
while len(correct_answers) < 50:
    answer = screen.textinput(title=f"{len(correct_answers)}/50 Guess The State",
                              prompt="What's another state's name?").title()

    if answer == 'Exit':
        for state in data.state.values:
            if state not in correct_answers:
                unguessed_states.append(state)
        df = pd.DataFrame(unguessed_states, columns=['State'])
        df.to_csv('states_to_learn')
        break
    elif answer in data.state.values:
        score.update_map(state=answer)
        correct_answers.append(answer)


turtle.mainloop()