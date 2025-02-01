import matplotlib.pyplot as plt
from scipy.constants import c, pi, h, k
import numpy as np
from typing import Any, Callable

def I_planck_constructor_for_T(T: int) -> Callable[[Any], float]:
    def fun(lamb) -> float:
        first_factor: Callable[[int], float] = lambda x: (2 * pi * c * c * h)/np.pow(x, 5)
        second_factor: Callable[[int], float] = lambda x : 1/(np.exp(np.divide((h*c),(x*k*T))) - 1)
        return first_factor(lamb) * second_factor(lamb)
    return fun

I_100 = I_planck_constructor_for_T(100)
I_5800= I_planck_constructor_for_T(5_800)
I_120000 = I_planck_constructor_for_T(120_000)

if __name__=="__main__":
    values = np.linspace(0, 2_000, 200)
    V_I_100 = I_100(values)
    V_I_5800= I_5800(values)
    V_I_120000 = I_120000(values)

    fig, ax = plt.subplots()
    # ax.plot(values, V_I_100, label="T 100")
    ax.plot(values, V_I_5800, label="T 5800")
    # ax.plot(values, V_I_120000, label="T 120.000")
    plt.show()
