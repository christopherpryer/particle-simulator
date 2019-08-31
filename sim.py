from matplotlib import pyplot as plt
from matplotlib import animation
from random import uniform
import numpy as np

class Particle:
    __slots__ = ('x', 'y', 'ang_vel')

    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel

class Simulator:
    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        r_i = np.array([[p.x, p.y] for p in self.particles])
        ang_vel_i = np.array([p.ang_vel for p in self.particles])
        for i in range(nsteps):
            norm_i = np.sqrt((r_i ** 2).sum(axis=1))
            v_i = r_i[:, [1, 0]]
            v_i[:, 0] *= -1
            v_i /= norm_i[:, np.newaxis]
            d_i = timestep * ang_vel_i[:, np.newaxis] * v_i
            r_i += d_i
            for i, p in enumerate(self.particles):
                p.x, p.y = r_i[i]


def visaulize(sim):
    X = [p.x for p in sim.particles]
    Y = [p.y for p in sim.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        sim.evolve(0.01)

        X = [p.x for p in sim.particles]
        Y = [p.y for p in sim.particles]

        line.set_data(X, Y)
        return line,

    anim = animation.FuncAnimation(
        fig, animate, init_func=init, blit=True, interval=10)
    plt.show()

if __name__ == '__main__':
    particles = [Particle(0.3, 0.5, 1),
                Particle(0.0, -0.5, -1),
                Particle(-0.1, -0.4, 3)]
    sim = Simulator(particles)
    visaulize(sim)
