#
# CS1010A --- Programming Methodology
#
# Side Quest 2.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi

##########
# Task 1 #
##########

def tree(n, pic):
    output = pic
    overlay_ratio = 2
    ratio = n - 1
    for i in range(1, n):
        output = overlay_frac(1/overlay_ratio, scale(ratio/n, pic), output)
        overlay_ratio += 1
        ratio -= 1
    return output



##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

def helix(pic, n):
    s_rune = scale(2/n, pic)
    radius = 1/2 - 1/n
    angle = 2/n
    count = 1 
    for i in range(1,n+1):
        x = math.cos(math.pi * angle) * radius
        y = math.sin(math.pi * angle) * radius
        image = translate(-y, x, s_rune)
        if count == 1:
            output = image
        else:
            output = overlay_frac(1 / count, image, output)
        angle += 2/n
        count += 1
    return output



# Test
show(helix(make_cross(rcross_bb), 9))
