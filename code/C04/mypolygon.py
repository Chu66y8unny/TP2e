from __future__ import print_function, division

import math
import turtle


def square(t, length):
    '''Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    '''
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    '''Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    '''
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    '''Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    '''
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    '''Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    '''
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    '''Draws a circle with the given radius.

    t: Turtle
    r: radius
    '''
    arc(t, r, 360)


if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw a circle centered on the origin
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)
    
    # wait for the user to close the window
    turtle.mainloop()

