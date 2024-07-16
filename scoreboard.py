from turtle import Turtle
import pandas as pd
FONT = ('Courier', 5, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')


    def update_map(self, state):
        data = pd.read_csv("50_states.csv")
        state_data = data[data.state == state]
        self.goto(state_data.x.item(), state_data.y.item())
        self.write(state,font=FONT, align='left')






