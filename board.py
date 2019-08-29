import turtle

class Board (turtle.Turtle):

    
    def __init__(self, distanceFromTop):
        super(Board, self).__init__()

        self.speed(0)
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(0, distanceFromTop)

        self.board_font = ("Courier", 45, "bold")
        self.write("0\t0", align="center", font=self.board_font)

    def update_score(self, left_score, right_score):
        updated_score = "{}\t{}".format(left_score, right_score)
        self.clear()
        self.write(updated_score, align="center", font=self.board_font)
