import turtle
import paddle, ball, board # Local Files
             
# Window Set-up
window = turtle.Screen()
window.title("Pong")
window.setup(width=800, height=600)
window.bgcolor("white")
window.tracer(0)

# Paddle Set-up
distance = 350
paddles = [
    paddle.Paddle(-distance, ["w", "s"]),
    paddle.Paddle(distance, ["Up", "Down"])
]
window.listen()
for x in range(2):
    window.onkeypress(paddles[x].pressed_up, paddles[x].up_key)
    window.onkeypress(paddles[x].pressed_down, paddles[x].down_key)

# Ball Set-up
ball = ball.Ball(0.2)

# Score board
board = board.Board(225)

while True:
    window.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bounce on borders
    ball.vert_border_check(window.screensize()[1])
    if ball.left_border_check(window.screensize()[0]):
        paddles[1].score += 1
        board.update_score(paddles[0].score, paddles[1].score)
    if ball.right_border_check(window.screensize()[0]):
        paddles[0].score += 1
        board.update_score(paddles[0].score, paddles[1].score)

    # Paddle collisions
    ball.left_player_bounce(paddles[0], distance)
    ball.right_player_bounce(paddles[1], distance)
    
