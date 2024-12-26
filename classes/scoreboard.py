from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.levelControl()

    def levelControl(self):
        self.penup()
        self.hideturtle()
        self.goto(x=-270, y=260)
        self.write(f"Level: {self.score}", font=FONT)

    def levelUp(self):
        self.clear()
        self.score += 1
        self.levelControl()

    def gameOver(self):
        self.penup()
        self.hideturtle()
        self.home()
        self.write("Game over!", False, align=ALIGNMENT, font=FONT)
