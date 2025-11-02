from scipy.constants import Avogadro
from math import cbrt, sqrt

class Element():
    def __init__(self, n: int = 8, m: int | float = 12, density: float = 3.515):
        self.n = n
        self.m = m
        self.d = density

    def side(self) -> float:
        return cbrt((self.n * self.m)/(self.d * Avogadro))

    def distance(self) -> float:
        return (sqrt(3)/4) * self.side()

if __name__=="__main__":
    carbono = Element()
    silicio = Element(m = 28, density=2.329)
    germanio = Element(m = 72.63, density=5.323)
    print(f"Carbono: {carbono.distance()}")
    print(f"Silicio: {silicio.distance()}")
    print(f"Germanio: {germanio.distance()}")
