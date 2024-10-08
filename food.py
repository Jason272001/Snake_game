import random
from turtle import  Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("blue")
        self.speed("fastest")

    def refresh(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 380)
        self.goto(random_x, random_y)
