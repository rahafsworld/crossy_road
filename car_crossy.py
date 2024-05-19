from turtle import Turtle
import random

COLOURS = ["palegreen", "lawngreen", "aliceblue", "lightblue", "honeydew"]
STARTING_MOVE = 5
MOVE_INC = 20


class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            random_y = random.randint(-240, 250)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):

        for car in self.all_cars:
            car.backward(self.car_speed)

            if car.xcor() < -280:
                car.hideturtle()
                self.all_cars.remove(car)

    def level_up(self):
        self.car_speed += MOVE_INC