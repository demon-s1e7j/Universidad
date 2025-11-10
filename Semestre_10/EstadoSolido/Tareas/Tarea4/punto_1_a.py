import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal
import os

os.system('clear')

class Point:
    def __init__(self, x: Decimal, y: Decimal) -> None:
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

    def _sum(self) -> Decimal:
        return self.x + self.y
    
    def distance(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"unsupported operand type(s) for +:'Point' and '{other.__class__.__name__}'")
        return ((other - self)**2)._sum().sqrt()

    @classmethod
    def zero(cls):
        return cls(Decimal(0), Decimal(0))

a1 = Decimal(2 * 1e-8)
a2 = Decimal(4 * 1e-8)
b1 = Decimal(2 * np.pi) / a1
b2 = Decimal(2 * np.pi) / a2

def pendiente(punto_1: Point, punto_2: Point) -> Decimal | None:
    if punto_1.x == punto_2.x:
        return None
    return (punto_2.y - punto_1.y)/(punto_2.x - punto_1.x)

def intercepto(punto: Point, pendiente: Decimal | None) -> Decimal:
    if pendiente is None:
        return punto.x
    return (punto.y - (pendiente * punto.x))

def punto_medio(punto_1: Point, punto_2: Point) -> Point:
    return (punto_1 + punto_2) / 2

def distancia(punto_1: Point, punto_2: Point) -> Decimal:
    return ((punto_2.x - punto_1.x)**2 + (punto_2.y - punto_1.y)**2).sqrt()

def inverso_pendiente(m: Decimal | None) -> Decimal | None:
    if m is None:
        return Decimal(0)
    if m == 0:
        return None
    return - (1 / m)

def interseccion_rectas(recta1, recta2):
    m1, b1 = recta1
    m2, b2 = recta2
    
    if m1 is None and m2 is None:
        return None
    
    if m1 is None:
        x = b1
        y = m2 * x + b2
        return Point(x, y)
    
    if m2 is None:
        x = b2
        y = m1 * x + b1
        return Point(x, y)
    
    if m1 == m2:
        return None
    
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return Point(x, y)

plano = [Point(b1 * a, b2 * b) for a in range(3) for b in range(3)]
objetivo = Point(b1, b2)
puntos = [p for p in plano if p != objetivo]

pendientes = [pendiente(p, objetivo) for p in puntos]
interceptos = [intercepto(objetivo, m) for m in pendientes]
rectas = list(zip(pendientes, interceptos))

puntos_medios = [punto_medio(p, objetivo) for p in puntos]
pendientes_medios = [inverso_pendiente(m) for m in pendientes]
interceptos_medios = [intercepto(p, m) for p, m in zip(puntos_medios, pendientes_medios)]
rectas_perpendiculares = list(zip(pendientes_medios, interceptos_medios))

conexiones_esquinas = [
    (plano[0], plano[2]),
    (plano[0], plano[6]),
    (plano[2], plano[8]),
    (plano[6], plano[8])
]
pendientes_esquinas = [pendiente(p1, p2) for p1, p2 in conexiones_esquinas]
interceptos_esquinas = [intercepto(p[0], m) for p, m in zip(conexiones_esquinas, pendientes_esquinas)]
rectas_esquinas = list(zip(pendientes_esquinas, interceptos_esquinas))


x, y = zip(*[(float(point.x), float(point.y)) for point in plano])

x_min, x_max = min(x), max(x)
y_min, y_max = min(y), max(y)

intersecciones = set(interseccion_rectas(p1, p2) for p1 in rectas_perpendiculares for p2 in rectas_perpendiculares)
intersecciones = intersecciones.union(set(interseccion_rectas(p1, p2) for p1 in rectas_perpendiculares for p2 in rectas_esquinas))
clean_intersecciones = [p for p in intersecciones if (p is not None) and Point(x_min, y_min) <= p and Point(x_max, y_max) >= p]

x_interseccion = [float(point.x) for point in clean_intersecciones]
y_interseccion = [float(point.y) for point in clean_intersecciones]

if __name__ == "__main__":
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='red', s=50, zorder=5)


    for m, b in rectas:
        if m is None:
            x_val = float(b)
            y_vals = np.linspace(y_min - 1e8, y_max + 1e8, 100)
            x_vals = np.full_like(y_vals, x_val)
            plt.plot(x_vals, y_vals, 'b--', linewidth=0.8, alpha=0.7)
        else:
            x_vals = np.linspace(x_min - 1e8, x_max + 1e8, 100)
            y_vals = float(m) * x_vals + float(b)
            plt.plot(x_vals, y_vals, 'b--', linewidth=0.8, alpha=0.7)

    distancias = [p.distance(objetivo) for p in puntos]

    for i, (m, b) in enumerate(rectas_perpendiculares):
        punto_medio_actual = puntos_medios[i]
        pm_x = float(punto_medio_actual.x)
        pm_y = float(punto_medio_actual.y)
    
        if m is None:
            longitud_perp = float(min(distancias)) * 1.2
            x_vals = [pm_x, pm_x]
            y_vals = [pm_y - longitud_perp, pm_y + longitud_perp]
            plt.plot(x_vals, y_vals, 'g-', linewidth=1.5, alpha=0.8, label='Rectas perpendiculares' if i == 0 else "")
        elif m == 0:
            longitud_perp = float(min(distancias)) * 1.2
            x_vals = np.linspace(pm_x - longitud_perp, pm_x + longitud_perp, 10)
            y_vals = float(m) * x_vals + float(b)
            plt.plot(x_vals, y_vals, 'g-', linewidth=1.5, alpha=0.8, label='Rectas perpendiculares' if i == 0 else "")
        elif abs(float(m)) < 1e10:
            longitud_perp = float(min(distancias)) * 0.4
            x_vals = np.linspace(pm_x - longitud_perp, pm_x + longitud_perp, 10)
            y_vals = float(m) * x_vals + float(b)
            plt.plot(x_vals, y_vals, 'g-', linewidth=1.5, alpha=0.8, label='Rectas perpendiculares' if i == 0 else "")
        else:
            longitud_perp = float(min(distancias)) * 1
            x_vals = [pm_x, pm_x]
            y_vals = [pm_y - longitud_perp, pm_y + longitud_perp]
            plt.plot(x_vals, y_vals, 'g-', linewidth=1.5, alpha=0.8, label='Rectas perpendiculares' if i == 0 else "")
        
        plt.scatter(pm_x, pm_y, color='orange', s=30, zorder=6, marker='o')
    
    for i, (m, b) in enumerate(rectas_esquinas):
        if m is None:
            x_val = float(b)
            y_vals = np.linspace(y_min, y_max, 100)
            x_vals = np.full_like(y_vals, x_val)
            plt.plot(x_vals, y_vals, 'm-', linewidth=2, alpha=0.8, label='Bordes del plano' if i == 0 else "")
        else:
            x_vals = np.linspace(x_min, x_max, 100)
            y_vals = float(m) * x_vals + float(b)
            plt.plot(x_vals, y_vals, 'm-', linewidth=2, alpha=0.8, label='Bordes del plano' if i == 0 else "")
    
    distancias_intersecciones = []
    for (i, j) in [(6, 17), (17, 23), (23, 15), (15,20), (20, 17), (6, 20), (23, 10), (10, 15), (20, 13), (15, 18), (13, 18)]:
        p1 = clean_intersecciones[i]
        p2 = clean_intersecciones[j]
        dist = p1.distance(p2)
        distancias_intersecciones.append((p1, p2, dist))
    
    # Dibujar las líneas de distancia
    for p1, p2, dist in distancias_intersecciones:
        plt.plot([float(p1.x), float(p2.x)], 
                [float(p1.y), float(p2.y)], 
                'purple', linewidth=1.5, alpha=0.6)
    
        # Añadir etiqueta con la distancia
        medios = punto_medio(p1, p2)
        plt.annotate(f'{float(dist):.2e}', 
                    (float(medios.x), float(medios.y)),
                    textcoords="offset points",
                    xytext=(0,5),
                    ha='center',
                    fontsize=6,
                    color='darkblue')
    
    plt.scatter(x_interseccion, y_interseccion, color='yellow', s=50, zorder=5)
    
    plt.axis("equal")
    plt.xlabel('', fontsize=12)
    plt.ylabel('', fontsize=12)
    plt.title('Red Reciproca y Primera y Segunda Celda de Brillouin', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.margins(0.1)
    
    plt.savefig("punto_1_a.png")
