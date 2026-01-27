from turtle import Turtle
import random

POSITION = 280

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()  # Call the refresh method to set initial position

    def refresh(self):
        """
        Move the food to a random position within the specified range.
        """
        x_axis = random.randint(-POSITION, POSITION)
        y_axis = random.randint(-POSITION, POSITION)
        self.goto(x_axis, y_axis)