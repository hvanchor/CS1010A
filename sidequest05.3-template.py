#
# CS1010A --- Programming Methodology
#
# Side Quest 5.3 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def dragonize(order, curve):
    if order == 0:
        return curve
    else:
        # Recursively get the curve of the previous order
        c = dragonize(order - 1, curve)
        # Rotate one curve by 90 degrees and revert the other
        return put_in_standard_position(connect_ends(rotate(-pi/2)(c), revert(c)))

# Example: Drawing the dragon curve of order 12 using the unit line
draw_connected_scaled(4096, dragonize(12, unit_line))
# test:
# draw_connected_scaled(4096, dragonize(12, unit_line))
