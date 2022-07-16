import turtle as t
from random import *



t.speed(100)
colors = ["red", "green", "yellow", "blue"]

while True:
    color = choice(colors)
    t.color(color)
    randpx = randint(1, 90)
    randgr = choice([40, 50, 60, 70, 80, 90])
    randwh = randint(1, 10)
    randsp = choice([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    t.fd(randpx)
    t.width(randwh)
    t.left(randgr)
