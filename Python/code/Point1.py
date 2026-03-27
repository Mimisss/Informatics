"""This module contains code related to classes and objects.
"""

import math

class Point:
    """Represents a point in 2D space."""

class Rectangle:
    """Represents a rectangle in 2D space."""

class Circle:
    """Represents a circle in 2D space."""
    
def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def distance_between_points(p1, p2):
    """Computes the distance between two Point objects."""
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    distance = math.sqrt(dx**2 + dy**2)
    return distance

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def point_in_circle(circle, p):
    dist = distance_between_points(circle.center, p)
    return dist <= circle.radius

if __name__ == '__main__':
    blank = Point()
    print(blank)
    blank.x = 0
    blank.y = 0
    print_point(blank)    

    grosse = Point()
    grosse.x = 3
    grosse.y = 4
    print_point(grosse)

    print(distance_between_points(grosse, blank))

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0
    
    center = find_center(box)
    print_point(center)
    

    circle = Circle()
    circle.center = Point()
    circle.center.x = 150
    circle.center.y = 100
    circle.radius = 75
    print(point_in_circle(circle, grosse))
