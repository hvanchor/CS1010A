#
# CS1010A --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn),rotate(-theta)(curve_fn)))
    return inner_gosperize


# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(10)(0.1), 50)

# Choose a significant level for testing for all three sets of functions.

def average_five(function):
    total = 0
    for i in range(0,5):
        x = function
        print(x)
        total += x
    return total/5

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

print(profile_fn(lambda: gosper_curve(10)(0.1), 50))

# Time measurements
print('average: ' + str(average_five(profile_fn (lambda: gosper_curve(10)(0.1), 10))))


# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

print(profile_fn(lambda: gosper_curve_with_angle(10, lambda lvl: pi/4)(0.1), 50))

# Time measurements
print('average: ' + str(average_five(profile_fn (lambda: gosper_curve_with_angle(10, lambda lvl: pi/4)(0.1), 10))))

#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

print(profile_fn(lambda: your_gosper_curve_with_angle(10, lambda lvl: pi/4)(0.1), 50))

# Time measurements
print('average: ' + str(average_five(profile_fn (lambda: your_gosper_curve_with_angle(10, lambda lvl: pi/4)(0.1), 10))))


# Conclusion:
# Functions that are more customized (average 0.21s and 0.17s) have the speed advantage over more customizable functions (average 2.64s)

##########
# Task 2 #
##########

#  1) Yes, joe_rotate will still achieve the same purpose.


#  2) joe_rotate would evaluates curve(t) twice while rotate evaluates it once. If the curve(t) is a function that contains recursive
#     calls, this would lead to a doubling effect and therefore an exponential increase in the number of calls as the level increases.
#     If we use the name pt for the value of curve(t), we would be able to store it as a value instead of a recursive call where each
#     call to curve(t) would recursively call itself twice.
#     Therefore, time complexity for joe_rotate becomes exponential instead of linear




##########
# Task 3 #
##########

#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1         <...>         <...>
#                      2         <...>         <...>
#                      3         <...>         <...>
#                      4         <...>         <...>
#                      5         <...>         <...>
#
#  Evidence of exponential growth in joe_rotate.

