import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def concentric(r,n,shrink):
    t.speed(0)
    if n == 0:
        return ""
    else:
        t.penup()
        #print("r is " + str(r) + " r*shrink is " + str(r*shrink))
        t.left(90)
        t.forward(r-shrink*r)
        t.right(90)
        t.pendown()
        t.circle(r)
        return concentric(shrink*r,n-1,shrink)

concentric(100,10,0.9)
