#
# CS1010A --- Programming Methodology
#
# Side Quest 5.2 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *
from math import pi

##########
# Task 1 #
##########

def kochize(level):
    def koch_curve(curve):
        s_curve = scale(1/3)(curve)
        c1 = s_curve
        c2 = rotate(3.14/3)(s_curve)
        c3 = rotate(-3.14/3)(s_curve)
        return connect_ends(connect_ends(connect_ends(c1,c2),c3),c1)
    curve = unit_line
    for i in range(level):
        curve = koch_curve(curve)
    return curve
    

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))



##########
# Task 2 #
##########

def snowflake():
    curve = kochize(5)
    p1 = rotate(2*pi/3)(curve)
    p2 = curve
    p3 = rotate(-2*pi/3)(curve)
    return connect_ends(connect_ends(p1,p2),p3)


draw_connected_scaled(10000, snowflake())


