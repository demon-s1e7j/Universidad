import numpy as np
import matplotlib.pyplot as plt

class Element():
    def __init__(self, name, A, B) -> None:
        self.name = name
        self.A = A
        self.B = B

    def calculate_n(self):
        space = np.linspace(0.4, 0.7, 100)
        return (space, self.A + (self.B / np.pow(space, 2)))

if __name__=="__main__":
    elements = [
        Element("Silica", 1.4580, 0.00354),
        Element("BK7", 1.5046, 0.00420)
    ]
    plt.figure(figsize=(10, 6))
    for element in elements:
        x, y = element.calculate_n()
        plt.plot(x, y, label=element.name)

    plt.xlabel('Longitud de onda (μm)')
    plt.ylabel('Índice de refracción n(λ)')
    plt.title('Índice de refracción según la ecuación de Cauchy')
    plt.legend()
    plt.grid(True)
    plt.show()
