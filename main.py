from turtle import Turtle, Screen
from block import Block
from paddle import Paddle
import random

screen = Screen()
screen.title('Breakout Game')
screen.setup(width=700, height=600)
screen.bgcolor('black')

screen.colormode(255)

# screen.tracer(0)

# ------------------------------- Blocks ------------------------------- #
# TODO: Create blocks class


# TODO: Make multiple blocks (maybe with different colors)

for row in range(50, 300, 65):
    starting_x = -315
    i = 0
    blocks = []
    while starting_x < 275:
        rand_size = random.randint(3, 5)
        rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if i == 0:
            starting_x = starting_x - ((5 - rand_size) * 10)
        else:
            next_x = (blocks[i - 1].block_size * 20)/2 + (rand_size * 20)/2 + 15
            starting_x += next_x
        block = Block((starting_x, row), rand_size)
        block.color(rand_color)
        blocks.append(block)
        i += 1
    # screen.update()

# TODO: Make block disappear when ball hits block


# ------------------------------- Paddle ------------------------------- #
# TODO: Create paddle class


# TODO: Create paddle

paddle = Paddle()

screen.listen()

screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)

# ------------------------------- Ball ------------------------------- #
# TODO: Create ball class


# TODO: Create ball


# TODO: Make ball bounce when it hits the wall, block and paddle.
#  Determine angle based on length of paddle or block.
#  Wall would just be the opposite.


# ------------------------------- Scoreboard ------------------------------- #
# TODO: Create Scoreboard class


# TODO: Update score. One block hit = one point


# TODO: End game when there are no more blocks left.


screen.exitonclick()
