from __future__ import print_function, division

import turtle

from polygon import arc

def petal(t, r, angle):
    '''Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    '''
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    '''Draws a flower with n petals.
    
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    '''
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)


def move(t, length):
    '''Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    '''
    t.pu()
    t.fd(length)
    t.pd()


if __name__ == '__main__':
    bob = turtle.Turtle()
    
    # draw a sequence of three flowers, as shown in the book.
    move(bob, -100)
    flower(bob, 7, 60, 60)

    move(bob, 100)
    flower(bob, 10, 40, 80)

    move(bob, 100)
    flower(bob, 20, 140, 20)

    bob.hideturtle()
    turtle.mainloop()
