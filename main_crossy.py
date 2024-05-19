import time
import turtle
from player_crossy import Player
from car_crossy import Car
from score_crossy import Score
from border_crossy import vertical, horizontal

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = Car()
score = Score()

vertical()
horizontal()
vertical()
horizontal()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            score.increase_level()

screen.exitonclick()
