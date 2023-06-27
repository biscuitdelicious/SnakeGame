from turtle import Turtle, Screen
from snake import Snake
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('LightCoral')
        self.speed('fastest')
        self.screen = Screen()
        self.refresh()

    def refresh(self):
        self.random_x = random.randint(-int(self.screen.window_width() / 2 - 25),
                                       int(self.screen.window_width() / 2 - 25))
        self.random_y = random.randint(-int(self.screen.window_height() / 2 - 25),
                                       int(self.screen.window_height() / 2 - 25))
        self.goto(self.random_x, self.random_y)