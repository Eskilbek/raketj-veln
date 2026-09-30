import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

target_coordinates = (80, 60)

def angle_calc(x, y, target_coordinates):
    target_x, target_y = target_coordinates

    target_angle = np.arctan2(target_y - y, target_x - x)

    return target_angle + np.pi #För att bränslet skjuts åt motsatt håll

def angle_calc2(x, y, target_coordinates):
    target_x, target_y = target_coordinates
    return (np.pi) / 2 + 1.67

def angle_calc3(x, y):
    return (-52.98*np.pi)/100


def ode(t, y):
    x, y, vx, vy = y

    mass = 4 if t > 10 else 8 - 0.4*t
    mass_derivative = 0 if mass == 4 else -0.4
    c = 0.05

    if y < 20:
        theta = -(np.pi/2)
    else:
<<<<<<< HEAD
        theta = angle_calc2(x, y, target_coordinates)

    ux = 700 * np.cos(theta)
    uy = 700 * np.sin(theta)

    length = np.sqrt(vx**2 + vy**2)

    ax = -(c/mass) * length * vx + (mass_derivative/mass) * ux
    ay = -9.82 - (c/mass) * length * vy + (mass_derivative/mass) * uy

    return[vx, vy, ax, ay]


tspan = (0, 10)

y = [0, 0 ,0 ,0]

sol = solve_ivp(ode, tspan, y)

plt.plot(sol.y[0], sol.y[1]) #x och y värden
plt.scatter(80, 60)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
