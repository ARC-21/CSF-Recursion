import turtle

s = turtle.getscreen()
t = turtle.Turtle()


def square(s, color):
    t.color(color)
    t.begin_fill()
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.end_fill()


def geo_art(s, n):
    if n == 0:
        return
    else:
        color = ""
        if n % 2 == 0:
            color = "cyan"
        else:
            color = "white"
        square(s, color)
        t.left(90)
        t.forward(s / 2)
        t.left(45)
        return geo_art(s * (2 ** 0.5) * 0.5, n - 1)


geo_art(300, 20)
