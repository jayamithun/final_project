

# pip install freegames

# Click on screen to control ball

# import modules
from random import *
import turtle as t
from freegames import vector

# Set window title, color and icon
t.title("Flappy Ball")
root = t.Screen()._root
root.iconbitmap("logo-ico.ico")
t.bgcolor('#80ffd4')


bird = vector(0, 0)
balls = []


   # Functions
# Move bird up in response to screen tap
def tap(x, y):
    up = vector(0, 30)
    bird.move(up)

# Return True if point on screen
def inside(point):
    return -200 < point.x < 200 and -200 < point.y < 200

# Draw screen objects
def draw(alive):
    t.clear()

    t.goto(bird.x, bird.y)

    if alive:
        t.dot(13, 'green')
    else:
        t.dot(13, 'red')

    for ball in balls:
        t.goto(ball.x, ball.y)
        t.dot(20, '#862d2d')

    t.update()

def move():
   # Update object positions
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    t.ontimer(move, 50)


t.setup(420, 420, 370, 0)
t.hideturtle()
t.up()
t.tracer(False)
t.onscreenclick(tap)
move()
t.done()