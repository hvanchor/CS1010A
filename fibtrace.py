from diagnostic import *
from hi_graph_connect_ends import *

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def joe_rotate ( angle ):
    def transform ( curve ):
        def rotated_curve ( t ):
            x , y = x_of ( curve ( t )) , y_of ( curve ( t ))
            cos_a , sin_a = cos ( angle ) , sin ( angle )
            return make_point ( cos_a * x - sin_a *y , sin_a * x + cos_a * y )
        return rotated_curve
    return transform

def rotate ( angle ):
    def transform ( curve ):
        def rotated_curve ( t ):
            pt = curve ( t )
            x , y = x_of ( pt ) , y_of ( pt )
            cos_a , sin_a = cos ( angle ) , sin ( angle )
            return make_point ( cos_a * x - sin_a *y , sin_a * x + cos_a * y )
        return rotated_curve
    return transform

trace(rotate)
rotate(5)
untrace(joe_rotate)
joe_rotate(5)
