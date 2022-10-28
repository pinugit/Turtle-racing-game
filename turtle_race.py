import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Enter your bet",
                              prompt="which turtle do you think will winn")
y_cord = -150
colors = ["red", "yellow", "green", "orange", "purple", "blue"]
all_turtles = []
is_race_on = True
for turtle_index in range(0, 6):
    tim = Turtle()
    tim.shape("turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_cord)
    y_cord = y_cord + 50
    all_turtles.append(tim)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            tu_color = turtle.fillcolor()
            if user_input.lower() == tu_color.lower():
                screen.textinput(
                    title="Youuu winn!!", prompt="What are your thoughts?")
            else:
                screen.textinput(
                    title=f"{tu_color} wins!! you loose!", prompt="how do you feel loosig to a computer XD XD")

            is_race_on = False
            break
        rand_distance = random.randint(0, 8)
        turtle.forward(rand_distance)


screen.exitonclick()
