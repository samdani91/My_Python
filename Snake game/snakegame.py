import turtle
import random

wn = turtle.Screen()
wn.bgcolor('black')
wn.title("Snake game")
wn.setup(400, 400)
wn.tracer(0)

# create snake
snake = turtle.Turtle()
snake.speed(0)  # animation speed
snake.shape("square")
snake.color("yellow")
snake.penup()
snake.goto(0, 0)
snake.dx = 0.03
snake.dy = 0.03

# create goal
goal = turtle.Turtle()
goal.speed(0)
goal.shape("circle")
goal.color("red")
goal.penup()

goal_x = random.randint(-180, 180)
goal_y = random.randint(-180, 180)

goal.goto(goal_x, goal_y)


def snake_right():
    while True:
        wn.update()
        x = snake.xcor()
        x += snake.dx
        if x > 200:
            break
        snake.setx(x)


def snake_left():
    while True:
        wn.update()
        x = snake.xcor()
        x -= snake.dx
        if x < -200:
            break
        snake.setx(x)


def snake_up():
    while True:
        wn.update()
        y = snake.ycor()
        y += snake.dy
        if y > 200:
            break
        snake.sety(y)


def snake_down():
    while True:
        wn.update()
        y = snake.ycor()
        y -= snake.dy
        snake.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(snake_right, "Right")
wn.onkeypress(snake_left, "Left")
wn.onkeypress(snake_up, "Up")
wn.onkeypress(snake_down, "Down")

while True:
    wn.update()

    if snake.ycor() < -200:
        # snake.sety(snake.ycor())
        break
