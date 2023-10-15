from turtle import Turtle, Screen
import random

class Paddle(Turtle):
    
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.goto(x,y)

    def up(self):
        new_y = self.ycor() + 55
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 55
        self.goto(self.xcor(), new_y)