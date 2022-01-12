from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=0.5, stretch_len=7)
        self.goto(0, -250)
    
    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, -250)
    
    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, -250)
    