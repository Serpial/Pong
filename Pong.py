import turtle


class Paddle (turtle.Turtle):
    up_key = ""
    down_key = ""

    
    def __init__ (self, starting_x, controls):
        super (Paddle, self).__init__()

        # Standard Attributes
        self.speed(0)
        self.shape("square")
        self.color("black")
        self.shapesize(1,1)
        self.penup()
        self.goto(starting_x, 0)

        up_button = controls[0]
        down_button = controls[0]
        

    def pressed_up(self):
        print("Up")
        

    def pressed_down(self):
        print("Down")        


window = turtle.Screen()
window.title("Pong")
window.setup(width=800, height=600)
window.bgcolor("white")
window.tracer(0)


distance = 350
paddles = [
    Paddle(-distance, ["w", "s"]),
    Paddle(distance, ["Up", "Down"])
]


window.listen()
for x in range(2):
    window.onkeypress(paddles[x].pressed_up(), paddles[x].up_key)
    window.onkeypress(paddles[x].pressed_down(), paddles[x].down_key)
    pass

while True:
    window.update()

    
