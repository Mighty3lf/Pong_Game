from turtle import Turtle, Screen
from paddle import Paddle
from pong_ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

l_paddle = Paddle(-350,0)
r_paddle = Paddle(350, 0)
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()
scoreboard = Scoreboard()
game_is_on = True
speed = 0.05


while game_is_on:
    screen.update()
    ball.move()
    time.sleep(speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed -= 0.005
    
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.increase_score_r()
        speed = 0.05
    
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.increase_score_l()
        speed = 0.05
       







screen.exitonclick()