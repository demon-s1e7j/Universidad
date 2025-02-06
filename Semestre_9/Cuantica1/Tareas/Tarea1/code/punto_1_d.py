import os
import matplotlib.pyplot as plt
from scipy.constants import c, pi, h, k
import numpy as np
from typing import Any, Callable

DIR_NAME = "../img"

def I_planck_constructor_for_T(T: int) -> Callable[[Any], float]:
    def fun(lamb) -> float:
        first_factor: Callable[[float], float] = lambda wavelength : np.divide( (2 * pi * np.pow(c, 2) * h), np.pow(wavelength, 5))
        second_factor: Callable[[float], float] = lambda wavelength: np.divide( 1, (np.exp(np.divide((h * c), (wavelength * k * T))) - 1))
        return first_factor(lamb) * second_factor(lamb)
    return fun

def plot_generator(function: Callable[[Any], float], ax, fig, l ,limit=13e-5, color="#cc241d"):
    ax.grid()
    values = np.linspace(0, limit, 20_000)
    ax.plot(values, function(values), color=color, label=f"{l}K")

def create_dir():
    ubication = "/".join(DIR_NAME.split("/")[:-1])
    print(os.listdir(ubication))
    dir_name = DIR_NAME.split("/")[-1]
    if dir_name not in os.listdir(ubication):
        os.mkdir(DIR_NAME)

I_100 = I_planck_constructor_for_T(100)
I_5800 = I_planck_constructor_for_T(5_800)
I_120000 = I_planck_constructor_for_T(120_000)

if __name__ == "__main__":
    create_dir()
    

    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(10, 10))
    fig.suptitle("Graficas de Intensidad respecto a Longitud de onda")
    fig.supxlabel("Longitud de Onda")
    fig.supylabel("Intensidad")
    plot_generator(I_100, ax1, fig, "100")
    plot_generator(I_5800, ax2, fig, "5800", limit=5e-6, color="#98971a")
    plot_generator(I_120000, ax3, fig, "120.000", limit=2e-7, color="#b16286")
    fig.legend()
    plt.savefig(f"{DIR_NAME}/General.png")
    # plt.close()
    plt.show()
