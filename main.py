
from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_postion = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle", )
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_postion[turtle_index])
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You won! The {winning_color} turtle is a winner!")
            else:
                print(f"You lost! The {winning_color} turtle is a winner!  ")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()







#
#
# def move_forward():
#     m.forward(20)
# def move_backward():
#     m.backward(20)
# def move_clock():
#     m.left(10)
# def move_on_clock():
#     m.right(10)
# def clear():
#     m.clear()
#     m.penup()
#     m.home()
#     m.pendown()
#
#
# screen.listen()
#
#
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(move_clock, "a")
# screen.onkey(move_on_clock, "d")
# screen.onkey(clear, "c")
# screen.exitonclick()