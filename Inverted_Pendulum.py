import numpy as np
import math
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation

m = 1
l = 1
g = 9.8
mu = 0.01
dt = 0.01
origin = [0, 0]
points = []


class Dynamics:
    def __init__(self, theta, theta_dot, theta_dot_dot, action):
        self.action = action
        self.theta = theta  # initial angle
        self.theta_dot = theta_dot  # initial angular velocity
        self.theta_dot_dot = theta_dot_dot  # initial angular acceleration

    def update_state(self):
        theta_dot_dot_new = (m*g*l*math.sin(self.theta) - mu*self.theta_dot + self.action) / (m*l**2)
        theta_dot_new = self.theta_dot + dt*theta_dot_dot_new
        theta_new = self.theta + dt*theta_dot_new + 0.5*(dt**2)*theta_dot_dot_new
        return theta_new, theta_dot_new, theta_dot_dot_new


def get_new_point(theta):
    x = l*np.sin(theta)
    y = l*np.cos(theta)
    return [x, y]


def main():
    timer = 0
    theta, theta_dot, theta_dot_dot = np.pi, 0, 0
    while timer <= 500:
        torque = random.randrange(-25, 25, 1)/5  # take random actions
        theta, theta_dot, theta_dot_dot = Dynamics(theta, theta_dot, theta_dot_dot, torque).update_state()
        tail = get_new_point(theta)
        points.append(tail)
        timer += 0.1

    fig = plt.figure()  # initialise la figure
    line, = plt.plot([], [])
    plt.xlim(-l - 0.5, l + 0.5)
    plt.ylim(-l - 0.5, l + 0.5)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        x = np.linspace(0, points[i][0], 1000)
        y = np.linspace(0, points[i][1], 1000)
        line.set_data(x, y)
        return line,

    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=5000, blit=True, interval=0.1, repeat=False)

    plt.show()

    # for point in points:
    #     plt.plot(point[0], point[1], 'bo', markersize=20)
    #     plt.plot([origin[0], point[0]], [origin[1], point[1]])
    #     plt.xlim(-l-0.5, l+0.5)
    #     plt.ylim(-l - 0.5, l + 0.5)
    #     plt.xlabel('X-Direction')
    #     plt.ylabel('Y-Direction')
    #     plt.pause(0.01)
    # plt.show()

        # x_values = [origin[0], tail[0]]
        # y_values = [origin[1], tail[1]]
        # plt.plot(x_values, y_values, color='b')
        #
        # plt.pause(0.1)
        #plt.clf()


if __name__ == "__main__":
    main()