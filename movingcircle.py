import turtle

# Setup
ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()

speed = 5

while True:
    ball.forward(speed)
    
    # If the ball goes too far right or left, turn around
    if ball.xcor() > 200 or ball.xcor() < -200:
        speed = speed * -1  # Reverse direction