from math import *
from random import *
import warnings
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def warn(*args, **kwargs):
    pass
warnings.warn = warn

# Define representation of a planet
def make_planet(x_pos, y_pos, mass, colour, size, name):
    return (x_pos, y_pos, mass, colour, size, name)

def get_x_coordinate(planet):
    return planet[0]

def get_y_coordinate(planet):
    return planet[1]

def get_mass(planet):
    return planet[2]

def get_colour(planet):
    return planet[3]

def get_size(planet):
    return planet[4]

def get_name(planet):
    return planet[5]

def get_position(planet):
    return (get_x_coordinate(planet), get_y_coordinate(planet))

# Setup constants
G = 6.6743e-11
Mass_of_Earth = 6 * 10**24
Earth = make_planet(0, 0, Mass_of_Earth / 10**13, 'oc', 22, 'Earth')
Mars = make_planet(-0.65, -0.6, 0.11 * Mass_of_Earth / 10**13, 'or', 10, 'Mars')
Moon = make_planet(-0.04, -0.1, 7.348 * 10 ** 22 / 10**13, 'ow', 8, 'Moon')
X_RANGE = (-0.9, 0.3)
Y_RANGE = (-0.8, 0.1)
N_STARS = 35

# Drawing the environment of the simulation
plt.style.use('dark_background')
fig = plt.figure(figsize=(6, 6))
axes = plt.axes(xlim=X_RANGE, ylim=Y_RANGE)
axes.set_aspect('equal')

def planet_plot(planets_list):
    for planet, colour in zip(planets_list, ['cyan', 'white', 'red']):
        # Plot planets
        axes.plot(get_x_coordinate(planet), get_y_coordinate(planet), get_colour(planet),
                  markersize=get_size(planet))
        # Plot labels
        axes.text(get_x_coordinate(planet) + 4e-3 * (get_size(planet) - 2), get_y_coordinate(planet) - 1e-3, get_name(planet),
                  color=colour, fontsize='small', fontweight='bold')

def plot_planets(planets_list, circles):
    planet_plot(planets_list)
    # Add indicator circles
    for planet in circles:
        circle = plt.Circle(get_position(planet), circles[planet][0], color=circles[planet][1], zorder=3)
        circle.fill = False
        axes.add_artist(circle)

def plot_explosion(current_x, current_y):
    num_circles = 200
    # Generate random circles with random colors and random sizes
    ex = np.random.uniform(-2e-2, 2e-2, num_circles) + current_x
    ey = np.random.uniform(-2e-2, 2e-2, num_circles) + current_y
    cols = [choice([
        'orangered', 'lightcoral', 'orange', 'darkorange',
        'gold', 'yellow', 'lightyellow', 'white'
        ]) for _ in range(num_circles)]
    sizes = np.random.uniform(7, 9, num_circles)
    axes.scatter(ex, ey, c=cols, s=sizes)

def setup_spacecraft(vx, vy, f):
    # Initial Time
    t0 = 0
    
    # Iteration speed
    dt = 1e-3

    def rungekutta4(f, y0, t):
        n = len(t)
        y = np.zeros((n, len(y0)))
        y[0] = y0
        for i in range(n - 1):
            h = t[i+1] - t[i]
            k1 = f(t[i], y[i])
            k2 = f(t[i] + h / 2., y[i] + k1 * h / 2.)
            k3 = f(t[i] + h / 2., y[i] + k2 * h / 2.)
            k4 = f(t[i] + h, y[i] + k3 * h)
            y[i+1] = y[i] + (h / 6.) * (k1 + 2*k2 + 2*k3 + k4)
        return y

    # Vector with the spacecraft's initial position and speed
    y0 = np.array([0.1, 0, vx, vy])
    t = np.arange(0, 400*dt, dt)
    final_path = rungekutta4(f, y0, t)

    # Initial animation state, indicators, and stars
    pause = False
    mars_passed, earth_reached, moon_compromised = False, False, False
    sx = np.random.uniform(X_RANGE[0] - 0.08, X_RANGE[1] + 0.08, N_STARS)
    sy = np.random.uniform(Y_RANGE[0] - 0.08, Y_RANGE[1] + 0.08, N_STARS)
    sc = [choice(['yellow']*17 + ['white']) for _ in range(N_STARS)]
    path_x, path_y = [], []
    counter = 0
    
    # This function will plot out the path of the spacecraft
    def animate(i):
        nonlocal pause, final_path, counter, t0, mars_passed, earth_reached, moon_compromised, sx, sy, path_x, path_y
        if not pause:
            day = round(1000*t0)
            current_x = final_path[counter][0]
            current_y = final_path[counter][1]
            counter += 1
            axes.clear()
            axes.set_xlim(*X_RANGE)
            axes.set_ylim(*Y_RANGE)
            axes.set_title(f"Mars Mission: Day {day} of 365")
            if day % 7 == 0:
                sx += np.random.uniform(-0.003, 0.003, N_STARS)
                sy += np.random.uniform(-0.003, 0.003, N_STARS)
            axes.scatter(sx, sy, s=3, marker='*', c=sc)
            if not mars_passed:
                plot_planets(planets, {Mars: [0.05, 'white']})
            elif not earth_reached and not moon_compromised:
                plot_planets(planets, {Mars: [0.05, 'lime'],
                                       Earth: [0.025, 'white'],
                                       Moon: [0.07, 'yellow']})
            elif not earth_reached and moon_compromised:
                plot_planets(planets, {Mars: [0.05, 'lime'],
                                       Earth: [0.025, 'white'],
                                       Moon: [0.07, 'red']})
            else:
                plot_planets(planets, {Mars: [0.05, 'lime'],
                                       Earth: [0.025, 'lime'],
                                       Moon: [0.07, 'lime']})
            axes.scatter(path_x, path_y, s=5, c=range(len(path_y)), cmap="hot")
            if day >= 365:
                axes.set_title("Simulation stopped! You ran out of time :(")
                pause = True
            elif not (X_RANGE[0] - 0.2 <= current_x <= X_RANGE[1] + 0.2) or not (Y_RANGE[0] - 0.2 <= current_y <= Y_RANGE[1] + 0.2):
                axes.set_title("Simulation stopped! You are out of bounds!")
                pause = True
            elif mars_passed and earth_reached and not moon_compromised:
                axes.set_title("Simulation finished! Good job!")
                pause = True
            elif moon_compromised:
                axes.set_title("Simulation stopped! You hit the Moon's vicinity!")
                pause = True
            elif (current_x - get_x_coordinate(Mars))**2 + (current_y - get_y_coordinate(Mars))**2 <= 0.034**2:
                axes.set_title("Simulation stopped! You crashed on Mars!")
                plot_explosion(current_x, current_y)
                pause = True
            elif (current_x - get_x_coordinate(Moon))**2 + (current_y - get_y_coordinate(Moon))**2 <= 0.018**2:
                axes.set_title("Simulation stopped! You crashed on the Moon!")
                plot_explosion(current_x, current_y)
                pause = True
            elif not mars_passed and (current_x - get_x_coordinate(Earth))**2 + (current_y - get_y_coordinate(Earth))**2 <= 0.025**2:
                axes.set_title("Simulation stopped! You crashed on the Earth!")
                plot_explosion(current_x, current_y)
                pause = True
            else:
                if not mars_passed and (current_x - get_x_coordinate(Mars))**2 + (current_y - get_y_coordinate(Mars))**2 <= 0.05**2:
                    mars_passed = True
                if mars_passed and (current_x - get_x_coordinate(Earth))**2 + (current_y - get_y_coordinate(Earth))**2 <= 0.025**2:
                    earth_reached = True
                elif mars_passed and (current_x - get_x_coordinate(Moon))**2 + (current_y - get_y_coordinate(Moon))**2 <= 0.07**2:
                    moon_compromised = True
                path_x = (path_x + [current_x])[-50:]
                path_y = (path_y + [current_y])[-50:]
                axes.plot(path_x[-10:], path_y[-10:], c='white', lw=2)
            t0 += dt
    
    # Setup matplotlib's animator
    return animation.FuncAnimation(fig, animate, interval=10, blit=False, save_count=365)

def start_spacecraft_animation(initial_vx, initial_vy, f):
    anim = setup_spacecraft(initial_vx, initial_vy, f)
    plt.show()

planets = (Earth, Moon, Mars)
