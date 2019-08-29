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
        self.score = 0
        
    def pressed_up(self):
        self.sety(self.ycor()+20)
        
    def pressed_down(self):
        self.sety(self.ycor()-20)
