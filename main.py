from turtle import Screen
from block import Block
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.title('Breakout Game')
screen.setup(width=700, height=600)
screen.bgcolor('black')
screen.colormode(255)
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)

# Created blocks and added blocks to list
total_blocks = []

for row in range(50, 300, 65):
    starting_x = -315
    i = 0
    blocks = []
    while starting_x < 275:
        # Create random size and random color
        rand_size = random.randint(3, 5)
        rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        # Have blocks spaced out evenly
        if i == 0:
            starting_x = starting_x - ((5 - rand_size) * 10)
        else:
            next_x = (blocks[i - 1].block_size * 20)/2 + (rand_size * 20)/2 + 15
            starting_x += next_x
        block = Block((starting_x, row), rand_size)
        block.color(rand_color)
        blocks.append(block)
        i += 1
    total_blocks += blocks

# Make ball move
game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    
    # Detect collision with right or left walls
    if ball.xcor() > 335 or ball.xcor() < -340:
        ball.bounce_x()
    
    # Detect collision with top wall
    if ball.ycor() > 280:
        ball.bounce_y()
    
    # Detect collision with blocks
    for b in total_blocks:
        if abs(ball.xcor() - b.xcor()) < 50 and abs(ball.ycor() - b.ycor()) < 50:
            ball.bounce_y()
            total_blocks.remove(b)
            b.hideturtle()
            scoreboard.point()
    
    # Detect collision with paddle
    if ball.distance(paddle) < 70 and ball.ycor() < -234:
        ball.bounce_y()
        ball.move_speed *= 0.9

    # Game ends when all blocks are hit or ball goes below paddle
    if len(total_blocks) == 0 or ball.ycor() < -280:
        game_on = False


screen.exitonclick()
