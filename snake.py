from turtle import Turtle

POSITIONS = [(0, 0), (-5, 0), (-10, 0)]
DISTANCE = 13
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in POSITIONS:
            self.segments_body(i)

    def segments_body(self, i):
        new_body = Turtle('square')
        new_body.color('SeaGreen1')
        new_body.shapesize(0.6)
        new_body.penup()
        new_body.goto(i)
        self.segments.append(new_body)

    def add_segments(self):
        self.segments_body(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for s_num in range(len(self.segments) - 1, 0, -1):
            pose = self.segments[s_num - 1].position()
            self.segments[s_num].goto(pose)
        self.head.forward(DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
