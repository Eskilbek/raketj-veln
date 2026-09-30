import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def angle_calc(x, y):
    target_angle = np.arctan2(60 - y, 80 - x)

    return target_angle + np.pi #För att bränslet skjuts åt motsatt håll





def ode(t, y):
    x, y, vx, vy = y

    mass = 4 if t > 10 else 8 - 0.4*t
    mass_derivative = 0 if mass == 4 else -0.4
    c = 0.05

    if y < 20:
        theta = -(np.pi/2)
    else:
        theta = angle_calc(x, y)

    ux = 700 * np.cos(theta)
    uy = 700 * np.sin(theta)

    length = np.sqrt(vx**2 + vy**2)

    ax = -(c/mass) * length * vx + (mass_derivative/mass) * ux
    ay = -9.82 - (c/mass) * length * vy + (mass_derivative/mass) * uy

    return[vx, vy, ax, ay]


tspan = (0, 20)

y = [0, 0 ,0 ,0]

sol = solve_ivp(ode, tspan, y)

plt.plot(sol.y[0], sol.y[1]) #x och y värden
plt.scatter(80, 60)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
