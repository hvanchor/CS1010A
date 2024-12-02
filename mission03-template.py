#
# CS1010A --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########
def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))


# Your answer here:
# n =


###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2




###########
# Task 2a #
###########

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def smiley_sum(t):
    def f(x):
        ...

    def op(x, y):
        ...

    n = ...

    # Do not modify this return statement
    return combine(f, op, n)

###########
# Task 2b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def new_fib(n):
    def f(x):
        if x == 0 or x == 1:
            return x
        else:
            return new_fib(x-2)

    def op(x, y):
        return x + y

    # Do not modify this return statement
    return combine(f, op, n+1)

# Your answer here:

print(new_fib(10))
print(fib(10))

