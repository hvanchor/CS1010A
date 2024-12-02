#
# CS1010A --- Programming Methodology
#
# Side Quest 8.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from planets import *

##########
# Task 1 #
##########
# a)
# Follows trigonometry angle.
# E.g. 0 degree -> East
# E.g. 90 degree -> North
def get_velocity_component(angle, velocity):
    x_velocity = velocity * np.cos(np.radians(angle))
    y_velocity = velocity * np.sin(np.radians(angle))
    return (x_velocity, y_velocity)


# print(get_velocity_component(30, 50)) # (43.30127018922194, 24.999999999999996)
# note that the exact values of each component may differ slightly due to differences in precision

# b)
def calculate_total_acceleration(planets, current_x, current_y):
    total_acceleration_x = 0
    total_acceleration_y = 0
    for planet in planets:
        x_coord = get_x_coordinate(planet)
        y_coord = get_y_coordinate(planet)
        planet_mass = get_mass(planet)

        r_x = x_coord - current_x
        r_y = y_coord - current_y
        r = sqrt(r_x**2 + r_y**2)

        acceleration_x = (G*planet_mass*r_x/r**3)
        acceleration_y = (G*planet_mass*r_y/r**3)

        total_acceleration_x += acceleration_x
        total_acceleration_y += acceleration_y
    return (total_acceleration_x, total_acceleration_y)



# c)
# Do not change the return statement
def f(t, Y):
    rx, ry, vx, vy = Y
    ax, ay = calculate_total_acceleration(planets, rx, ry)
    return np.array([vx, vy, ax, ay])

np.set_printoptions(precision=5)
# print(f(0.5, [0.1, 0.1, 15.123, 20.211])) # [15.123  20.211  -1423.61135  -1425.42972]

##########
# Task 2 #
##########

# Uncomment and change the input parameters to alter the path of the spacecraft
vx, vy = get_velocity_component(-45, 100)


##############################################################################################
# Uncomment the following line to start the plot
start_spacecraft_animation(vx, vy, f)

