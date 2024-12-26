import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def levelUp(self):
        self.car_speed += MOVE_INCREMENT

    def makeCar(self):
        if random.randint(1, 10) == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            y_location = random.randint(-250, 240)
            car.goto(300, y_location)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.setx(car.xcor() - self.car_speed)