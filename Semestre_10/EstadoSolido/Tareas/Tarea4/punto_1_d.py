import numpy as np
import matplotlib.pyplot as plt
import os

os.system("clear")

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
            raise TypeError(f"unsupported operand type(s) for ==: 'Point' and '{other.__class__.__name__}'")
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"unsupported operand type(s) for +:'Point' and '{other.__class__.__name__}'")
        return Point(self.x + other.x, self.y + other.y)
    
    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def __div__(self, other):
        return Point(self.x / other, self.y / other)
    
    def __sub__(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"unsupported operand type(s) for +:'Point' and '{other.__class__.__name__}'")
        return Point(self.x - other.x, self.y - other.y)
    
    def __pow__(self, pow):
        return Point(self.x**pow , self.y**pow)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __lt__(self, other) -> bool:
        if not isinstance(other, Point):
            raise TypeError(f"unsupported operand type(s) for <:'Point' and '{other.__class__.__name__}'")
        return (self.x < other.x) and (self.y < other.y)

    def __gt__(self, other) -> bool:
        if not isinstance(other, Point):
            raise TypeError(f"unsupported operand type(s) for >:'Point' and '{other.__class__.__name__}'")
        return (self.x > other.x) and (self.y > other.y)

    def __le__(self, other) -> bool:
        if not isinstance(other, Point):
            raise TypeError(f"unsupported operand type(s) for <:'Point' and '{other.__class__.__name__}'")
        return (self < other) or (self.x == other.x and self.y < other.y) or (self.y == other.y and self.x < other.x)

    def __ge__(self, other) -> bool:
        if not isinstance(other, Point):
            raise TypeError(f"unsupported operand type(s) for >:'Point' and '{other.__class__.__name__}'")
        return (self > other) or (self.x == other.x and self.y > other.y) or (self.y == other.y and self.x > other.x)

    def _sum(self) -> float:
        return self.x + self.y
    
    def distance(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"unsupported operand type(s) for +:'Point' and '{other.__class__.__name__}'")
        return np.sqrt(((other - self)**2)._sum())

    @classmethod
    def zero(cls):
        return cls(0, 0)

a1 = (2 * 1e-8)
a2 = (4 * 1e-8)
b1 = (np.pi) / a1
b2 = (np.pi) / a2

radius = (np.sqrt(np.pi / 4) * 10**8)

def circumference(x, c: Point = Point.zero(), r: float = radius) -> float:
    return c.y + np.sqrt(r**2 - (x - c.x)**2)

### PRIMERA ZONA
centers = [(i/2) * b2 for i in range(8) if i % 2 != 0]

spaces = [np.linspace(i*b2, (i + 1)*b2, 100) for i in range(len(centers))]

for i, x in enumerate(spaces):
    plt.plot(x, circumference(x, c=Point(centers[i], 0)), 'b')
    plt.plot(x, -circumference(x, c=Point(centers[i], 0)), 'b')

plt.axis("equal")
plt.ylim(-b1, b1)
plt.xlim(0, 4*b2)
plt.savefig("./punto_1_d_primera_zona.png")

plt.close()


### SEGUNDA ZONA
spaces = [np.linspace((i - radius), (i + radius), 100) for i in centers]

for i, x in enumerate(spaces):
    plt.plot(x, circumference(x, c=Point(centers[i], 0)), 'r')
    plt.plot(x, -circumference(x, c=Point(centers[i], 0)), 'r')


plt.axis("equal")
plt.savefig("./punto_1_d_segunda_zona.png")

