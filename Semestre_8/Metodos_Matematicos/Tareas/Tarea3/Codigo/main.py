import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure()

axis = plt.axes(xlim=(-5, 5),
                ylim=(0, 100))

line, = axis.plot([],[], lw = 3)

plt.title(r"Función: $\frac{1}{n\pi}\frac{\sin^2(nx)}{x^2}$")

def func_1(n: int | float, x):
    n = n if n > 0 else 0.0000001
    prim = 1/(n*np.pi)
    num = np.power(np.sin(n * x), 2)
    den = np.power(x, 2)
    return prim*(num/den)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(-5, 5, 2000)
    y = func_1(i, x)
    line.set_data(x, y)

    return line,

anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval = 20)

anim.save('fun3.mp4',  
          writer = 'ffmpeg', fps = 30) 
