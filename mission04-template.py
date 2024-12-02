#
# CS1010A --- Programming Methodology
#
# Mission 4
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########


# (a)
# Input: Number
# Output: Point

# (b)
# Input: Number
# Output: Point

# (c)
def vertical_line(point, length):
    x_coord = x_of(point)
    y_coord = y_of(point)
    return lambda t: make_point(x_coord, y_coord + length*t) 
    


# (d)
# Input: Point, Number
# Output: Curve

# (e)
#midpoint = (0.5, 0.5)

##########
# Task 2 #
##########

# (a)
# your answer here

# (b)
def reflect_through_y_axis(curve):
    def reflected_curve(t):
        point = curve(t)
        x_coord = x_of(point)
        y_coord = y_of(point)
        return make_point(-x_coord, y_coord)
    return reflected_curve
	
draw_connected_scaled(200, arc)
draw_connected_scaled(200, reflect_through_y_axis(arc))

