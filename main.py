import time
from turtle import Screen
from classes.player import Player
from classes.car_manager import CarManager
from classes.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle game")
screen.tracer(0)

score = Scoreboard()
car_manager = CarManager()
player = Player()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    car_manager.move()
    car_manager.makeCar()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            score.gameOver()
            game_is_on = False

    if player.ycor() > 270:
        player.reset()
        car_manager.levelUp()
        score.levelUp()

screen.exitonclick()