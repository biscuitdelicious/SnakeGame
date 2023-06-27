from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor('gray30')
screen.title('Snake game')
screen.tracer(0)
snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'Right')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.up, 'Up')

scoreboard_score = 0
scoreboard = Turtle()
scoreboard.penup()
scoreboard.color('SteelBlue1')
scoreboard.hideturtle()
scoreboard.setposition(-10, 320)
scoreboard.write('Score: 0', False, align='Center', font=('Avenir', 20, 'bold'))


def game_over():
    scoreboard.goto(-20, 0)
    scoreboard.color('LightSkyBlue2')
    scoreboard.write(f'Game over', align='Center', font=('Creepster', 60, 'normal'))


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(10 / (scoreboard_score * 10 + 300))  # ~ to t.speed()
    snake.move()
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.add_segments()
        scoreboard_score += 1
        scoreboard.clear()
        scoreboard.write(f'Score: {scoreboard_score} ', False, align='Center', font=('Avenir', 20, 'bold'))

    if snake.head.xcor() > screen.window_width() / 2 - 20 or snake.head.ycor() > screen.window_height() / 2 - 20 or \
            snake.head.xcor() < -screen.window_width() / 2 + 10 or snake.head.ycor() < -screen.window_height() / 2 + 10:
        game_is_on = False
        game_over()
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 8:
            game_is_on = False
            game_over()


screen.exitonclick()
