#
# CS1010A --- Programming Methodology
#
# Side Quest 1.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

def top_bottom_row(pic, n):
    return quarter_turn_right(stackn(n,
                                     quarter_turn_left(pic)))
def middle_rows(pic, n):
    return quarter_turn_right(stack_frac(1/n,
                              quarter_turn_right(stackn(n-2,
                                                        turn_upside_down(pic))),
                              stack_frac(1-1/(n-1),
                                         quarter_turn_left(pic),
                                         quarter_turn_right(stackn(n-2,
                                                                   turn_upside_down(pic))))))
def egyptian(pic, n):
    return stack_frac(1/n,
                      top_bottom_row(pic, n),
                      stack_frac(1-1/(n-1),
                         middle_rows(pic,n),
                         top_bottom_row(pic, n)))

def top_bottom_row(pic, n):
    return quarter_turn_right(stackn(n,
                                     quarter_turn_left(pic)))
def middle_rows(pic, n):
    return quarter_turn_right(stack_frac(1/n,
                              quarter_turn_right(stackn(n-2,
                                                        turn_upside_down(pic))),
                              stack_frac(1-1/(n-1),
                                         quarter_turn_left(pic),
                                         quarter_turn_right(stackn(n-2,
                                                                   turn_upside_down(pic))))))
def egyptian(pic, n):
    return stack_frac(1/n,
                      top_bottom_row(pic, n),
                      stack_frac(1-1/(n-1),
                         middle_rows(pic,n),
                         top_bottom_row(pic, n)))

show(egyptian(make_cross(rcross_bb), 4))
