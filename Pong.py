import turtle

class Paddle (turtle.Turtle):
    def __init__ (self, starting_x, controls):
        super (Paddle, self).__init__()

        # Standard Attributes
        self.speed(0)
        self.shape("square")
        self.color("black")
        self.shapesize(5,1)
        self.penup()
        self.goto(starting_x, 0)

        self.up_key = controls[0]
        self.down_key = controls[1]
        
    def pressed_up(self):
        self.sety(self.ycor()+20)
        
    def pressed_down(self):
        self.sety(self.ycor()-20)

class Ball (turtle.Turtle):
    def __init__(self, speed):
        super (Ball, self).__init__()
        
        self.speed(0)
        self.shape("square")
        self.color("red")
        self.penup()
        self.goto(0, 0)
        self.dx = speed
        self.dy = speed

# Window Set-up
window = turtle.Screen()
window.title("Pong")
window.setup(width=800, height=600)
window.bgcolor("white")
window.tracer(0)

# Paddle Set-up
distance = 350
paddles = [
    Paddle(-distance, ["w", "s"]),
    Paddle(distance, ["Up", "Down"])
]
window.listen()
for x in range(2):
    window.onkeypress(paddles[x].pressed_up, paddles[x].up_key)
    window.onkeypress(paddles[x].pressed_down, paddles[x].down_key)

# Ball Set-up
ball = Ball(0.2)

while True:
    window.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

