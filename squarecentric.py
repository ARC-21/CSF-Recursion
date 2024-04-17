import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def square(s):
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.left(90)
    t.forward(s)

def squarecentric(s):
    if s < 5:
        return
    else:
        square(s)
        t.left(90)
        t.forward(s/2)
        t.left(45)
        return squarecentric(s*(2**(0.5))*0.5)

squarecentric(300)
