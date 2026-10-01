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
    return (np.pi) / 2 + 1.663

def angle_calc3(x, y, target_coordinates):
    return (-52.98*np.pi)/100



def ode(t, y, angle):
        
    x, y, vx, vy = y

    mass = 4 if t > 10 else 8 - 0.4*t
    mass_derivative = 0 if mass == 4 else -0.4
    c = 0.05

    if y < 20:
        theta = -(np.pi/2)
    else:
        theta = angle

    ux = 700 * np.cos(theta)
    uy = 700 * np.sin(theta)

    length = np.sqrt(vx**2 + vy**2)

    ax = -(c/mass) * length * vx + (mass_derivative/mass) * ux
    ay = -9.82 - (c/mass) * length * vy + (mass_derivative/mass) * uy

    return np.array([vx, vy, ax, ay])


tspan = (0, 4)

y = [0, 0 ,0 ,0]

# sol = solve_ivp(ode, tspan, y)

# plt.plot(sol.y[0], sol.y[1]) #x och y värden
# plt.scatter(80, 60)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid()
# plt.show()

def heuns(func, span, begin, angle, h, timer):
    target_x, target_y = target_coordinates
    arr_t= []
    arr_y = []
    arr_y.append(begin)
    y = np.array(begin, dtype=float)
    t = span[0]

    

    while(t < (span[-1])):
        k1 = np.array(func(t, y, angle))
        
        k2 = np.array(func(t + h/2, y + (h/2)* k1, angle))

        k3 = np.array(func(t + h/2, y + h*(k2/2), angle))

        k4 = np.array(func(t + h, y + h*k3, angle))

        t = t + h
        k_true_final_version = (k1 + 2*k2 + 2* k3 + k4)/6

        y_true = y + h*k_true_final_version
        y = y_true
        arr_y.append(y_true)

        if (y_true[0] < target_x + 0.1 and y_true[0] > target_x - 0.1) and (y_true[1] < target_y + 0.1 and y_true[1] > target_y - 0.1):
            return ((np.array(arr_t), np.array(arr_y)), 
                     True)

    print("span reached", timer)
    return ((np.array(arr_t), np.array(arr_y)), False)

global_h = 0.001

#spamma heuns, få real angle
start_angle = -(np.pi) + np.deg2rad(4)
timer = 1
while True:
    print (timer)
    hit_target = heuns(ode, tspan, y, start_angle, global_h, timer)
    print(hit_target[1])
    print(np.rad2deg(start_angle))
    if hit_target[1] == True or start_angle > -(np.pi)/2:
        break
    else:
        start_angle = start_angle + 0.001

    timer += 1
#sol:true heuns(ode, real angle)
sol_true_final_real_version_v3 = heuns(ode, tspan, y, start_angle, global_h, timer)

plt.plot(sol_true_final_real_version_v3[0][1][:,0], sol_true_final_real_version_v3[0][1][:,1])
plt.scatter(80, 60)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()