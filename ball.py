import turtle
import paddle 

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

    def vert_border_check(self, vert_window_size):
        if self.ycor() > (vert_window_size-10):
            self.sety(vert_window_size-10)
            self.dy *= -1
        elif self.ycor() < ((vert_window_size-10) *-1):
            self.sety((vert_window_size-10) * -1)
            self.dy *= -1
        else:
            return False
        return True
    
    def left_border_check(self, horz_window_size):
        if self.xcor() < ((horz_window_size-10) *-1):
            self.goto(0, 0)
            self.dx *= -1
        else:
            return False
        return True
    
    def right_border_check(self, horz_window_size):
        if self.xcor() > (horz_window_size-10):
            self.goto(0, 0)
            self.dx *= -1
        else:
            return False
        return True

    def left_player_bounce(self, l_paddle, distance):
        if self.xcor() < (distance-10)*-1 and self.xcor() > distance*-1:
            if self.ycor() < l_paddle.ycor() + 40 and self.ycor() > l_paddle.ycor()-50:
                    self.setx((distance-10)*-1)
                    self.dx *= -1

    def right_player_bounce(self, r_paddle, distance):
        if self.xcor() > distance-10 and self.xcor() < distance:
            if self.ycor() < r_paddle.ycor() + 40 and self.ycor() > r_paddle.ycor()-50:
                    self.setx(distance-10)
                    self.dx *= -1
