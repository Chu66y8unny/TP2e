import math
import turtle

def pie(t, radius, n):
    theta = 360.0 / n
    beta = (180.0 - theta)/2
    side = 2 * radius * math.sin(theta/2.0/180.0 * math.pi)
    for i in range(n):
        t.fd(radius)
        t.lt(theta + beta)
        t.fd(side)
        t.lt(theta + beta) 
        move(t, radius)
        t.lt(180.0)
 

def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()
 

if __name__ == '__main__':
    bob = turtle.Turtle()
    move(bob, -160)
    pie(bob, 75, 5)

    move(bob, 160)
    pie(bob, 75, 6)

    move(bob, 160)
    pie(bob, 75, 7)

    bob.hideturtle()
    turtle.mainloop()
