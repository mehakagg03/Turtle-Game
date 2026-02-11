from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(width=600,height=400)
screen.bgcolor("beige")
user_input=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Color: ")
colour=["purple", "blue", "green", "yellow", "orange", "red"]
y_cord=[150,90,30,-30,-90,-150]
all_turtle=[]
race_on=False

for turtle_index in range(0,6):
    ron = Turtle(shape="turtle")
    ron.penup()
    ron.color(colour[turtle_index])
    ron.goto(x=-280,y=y_cord[turtle_index])
    all_turtle.append(ron)

if user_input:
    race_on=True

while race_on:
    for turtle in all_turtle:
        dist = random.randint(0, 10)
        turtle.forward(dist)

        if turtle.xcor()>280:
            race_on=False
            winner=turtle.pencolor()
            if user_input==winner:
                print(f"You've won!🏆 The winner is {winner}.")
            else:
                print(f"You've lost!🐀 The winner is {winner}.")


screen.exitonclick()