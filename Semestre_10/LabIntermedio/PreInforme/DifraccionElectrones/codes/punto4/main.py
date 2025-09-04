from math import pow, sqrt

def distance(h: int,
             k: int,
             l: int = 0,
             a: float = 0.2461,
             c: float = 0.6708) -> float:
    inv_d = (4/3) * (pow(h, 2) + (h * k) +    pow(k, 2))/pow(a, 2) + pow(l, 2)/pow(c, 2)
    return sqrt(1/inv_d)

values = set()

h = 1
while len(values) < 5:
    for k in range(h + 1):
        values.add(distance(h, k))
    h += 1

print(values)
