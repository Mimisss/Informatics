"""This module contains code related to classes and objects
"""

import math
import turtle

class Point:
    """Represents a point in 2D space
    """
    
class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner
    """

class Circle:
    """Represents a circle.

    attributes: center, radius
    """
    
def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.
    """
    dx = p1.x - p2.x
    dy = p2.x - p2.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist

def move_rectangle(rect, dx, dy):
    """Move the Rectangle by modifying its corner object.
    """
    rect.corner.x += dx
    rect.corner.y += dy

def point_in_circle(circle, p):
    """Checks whether a point lies inside a circle.
    """
    d = distance_between_points(p, circle.center)
    return d <= circle.radius

def draw_rect(t, rect):
    t.pu()
    t.goto(rect.corner.x, rect.corner.y)
    t.setheading(0)
    t.pd()

    for length in rect.width, rect.height, rect.width, rect.height:
        t.fd(length)
        t.rt(90)
        
if __name__ == '__main__':
    print(Point)
    blank = Point()
    print(blank)    
    blank.x = 3.0
    blank.y = 4.0
    print_point(blank)
    distance = math.sqrt(blank.x**2 + blank.y**2)
    print(distance)

    #but what about....
    #point = Point()
    #print_point(point)
    
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0
    print(box)
    print(box.width)
    print(box.corner.y)
    center = find_center(box)
    print_point(center)

    circle = Circle()
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    bob = turtle.Turtle()
    draw_rect(bob, box)    
