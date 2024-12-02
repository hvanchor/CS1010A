#
# CS1010A --- Programming Methodology
#
# Mission 7 - Sidequest 1
#
########################################################

from lazy_susan import *

##########
# Task 1 #
##########

def solve_trivial_2(table):
    table_state = get_table_state(table)
    flip = ()
    for coin in table_state:
        if coin == 0:
            flip += (1,)
        else:
            flip += (0,)
    return flip_coins(table, flip)

# test:
t2_1 = create_table(2)
solve_trivial_2(t2_1)
print(check_solved(t2_1))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t2_1_run = create_table(2)
# run(t2_1_run, solve_trivial_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_1_susan = create_table(2)
# Susan(t2_1_susan)

########################################################





##########
# Task 2 #
##########

def solve_trivial_4(table):
    table_state = get_table_state(table)
    flip = ()
    for coin in table_state:
        if coin == 0:
            flip += (1,)
        else:
            flip += (0,)
    return flip_coins(table, flip)
# test:
t4_2 = create_table(4)
solve_trivial_4(t4_2)
print(check_solved(t4_2))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t4_2_run = create_table(4)
# run(t4_2_run, solve_trivial_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_2_susan = create_table(4)
# Susan(t4_2_susan)

########################################################





##########
# Task 3 #
##########

def solve_2(table):
    if not check_solved(table):
        # If not solved, flip one coin
        flip_coins(table, (1, 0))

# test:
t2_3 = create_table(2)
solve_2(t2_3)
print(check_solved(t2_3))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t2_3_run = create_table(2)
# run(t2_3_run, solve_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_3_susan = create_table(2)
# Susan(t2_3_susan)

########################################################





##########
# Task 4 #
##########

def solve_4(table):
    """ Write your code here """
    pass

# test:
# t4_4 = create_table(4)
# solve_4(t4_4)
# print(check_solved(t4_4))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t4_4_run = create_table(4)
# run(t4_4_run, solve_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_4_susan = create_table(4)
# Susan(t4_4_susan)

########################################################


x = 7
y = 11
def f(y):
    return y - x
def g(x):
    x = 5
    return f(x*y)
print(g(y))



##########
# Task 5 #
##########

def solve(table):
    table_size = get_table_size(table)
    n = 0

    # Calculate the power of 2 for the table size
    while table_size > 1:
        table_size = table_size / 2  # Floating-point division
        n += 1

    # Base moves for smallest problem size (2 elements)
    A, B = (1, 1), (1, 0)
    moves = (A, B)

    # Generate moves for larger sizes using recursive ABACABA pattern
    while n > 1:
        # Use map and lambda to maintain the style
        moves = tuple(map(lambda x: x * 2, moves)) + (moves[0],) + tuple(map(lambda x: x * 2, moves[::-1]))
        n -= 1

    # Correct move sequence construction
    sequence = ()
    for i in range(1, get_table_size(table)):
        sequence = sequence + (i,) + sequence

    # Apply the generated moves to the table
    for i in sequence:
        if not check_solved(table):
            flip_coins(table, moves[i - 1])

# Test case
t4 = create_table(4)
solve(t4)
print("Table size 4 solved:", check_solved(t4))

t8 = create_table(8)
solve(t8)
print("Table size 8 solved:", check_solved(t8))

t16 = create_table(16)
solve(t16)
print("Table size 16 solved:", check_solved(t16))




        

# test:
t4_5 = create_table(4)
solve(t4_5)
print(check_solved(t4_5))

t8_5 = create_table(8)
solve(t8_5)
print(check_solved(t8_5))

t16_5 = create_table(16)
solve(t16_5)
print(check_solved(t16_5))

# Note: It is not advisable to execute run() if the table is large.
