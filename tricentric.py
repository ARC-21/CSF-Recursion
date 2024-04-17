import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def equiTri(s):
    t.forward(s)
    t.left(120)
    t.forward(s)
    t.left(120)
    t.forward(s)

def tricentric(s):
    if s < 5:
        return ""
    else:
        equiTri(s)
        t.left(120)
        t.forward(s/2)
        t.left(60)
        return tricentric(s/2)

tricentric(300)
