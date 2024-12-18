from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt') as data:
            self.highscore=int(data.read())
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score:{self.score} High Score:{self.highscore}', align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt',mode='w') as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_score()


    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()
