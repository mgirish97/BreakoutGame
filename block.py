from turtle import Turtle


class Block(Turtle):
    
    def __init__(self, position, size):
        super().__init__()
        self.speed('fastest')
        self.block_size = size
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=size)
        self.goto(position)
