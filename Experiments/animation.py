import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# x = np.arange(0, 2*np.pi, 0.01)
# line, = ax.plot(x, np.sin(x))
l = 2
nx = 41
dx = l / (nx - 1)
nt = 25
dt = 0.025
c = 1

u = np.ones(nx)
u[int(.5 / dx):int(1 / dx + 1)] = 2
print(u)

plt.plot(np.linspace(0, 2, nx), u)
plt.show()

# def animate(i):
#     line.set_ydata(np.sin(x + i/10.0))  # update the data
#     return line,

# # Init only required for blitting to give a clean slate.
# def init():
#     line.set_ydata(np.ma.array(x, mask=True))
#     return line,

# ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
#                               interval=25, blit=True)
# plt.show()