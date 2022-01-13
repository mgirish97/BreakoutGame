from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, -100)
        self.move_x = 3
        self.move_y = 3
        self.move_speed = 0.01
    
    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)
    
    def bounce_x(self):
        self.move_x *= -1
    
    def bounce_y(self):
        self.move_y *= -1
