import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def equiTri(s, shade):
    t.color(shade*0.1,shade*0.1,shade*0.1)
    t.begin_fill()
    t.forward(s)
    t.left(120)
    t.forward(s)
    t.left(120)
    t.forward(s)
    t.end_fill()

def tricentric2(s,shade):
    if s < 5:
        return ""
    else:
        equiTri(s,shade)
        t.left(120)
        t.forward(s/2)
        t.left(60)
        return tricentric2(s/2,shade+1)

tricentric2(300,0)
