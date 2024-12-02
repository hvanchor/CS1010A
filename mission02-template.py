#
# CS1010A --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(pic, n):
    if n == 1:
        return pic
    else:
        return stack(pic, quarter_turn_right(stackn(2, quarter_turn_left(fractal(pic, n-1)))))

###########
# Task 1b #
###########

def fractal_iter(pic, n):
    output = pic
    for i in range(1, n):
        output = stack(pic, quarter_turn_right(stackn(2, quarter_turn_left(output))))
    return output


###########
# Task 1c #
###########

def dual_fractal(p1, p2, n):
    if n==1:
        return p1
    else:
        return stack(p1, quarter_turn_right(stackn(2, quarter_turn_left(dual_fractal(p2, p1, n-1)))))

show(dual_fractal(rcross_bb, nova_bb, 6))

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(p1, p2, n):
    if n%2 == 0:
        output = p2
    else:
        output = p1
        p1, p2 = p2, p1
    for i in range(1, n):
        output = stack(p1, quarter_turn_right(stackn(2, quarter_turn_left(output))))
        p1, p2 = p2, p1
    return output
        

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########

def steps(p1, p2, p3, p4):
    layer1 = beside(blank_bb, stack(p1, blank_bb))
    layer2 = beside(blank_bb, stack(blank_bb, p2))
    layer3 = beside(stack(blank_bb, p3), blank_bb)
    layer4 = beside(stack(p4, blank_bb), blank_bb)
    return overlay(overlay(layer4, layer3), overlay(layer2, layer1))


