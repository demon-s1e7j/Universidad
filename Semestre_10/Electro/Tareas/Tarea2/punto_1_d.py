import numpy as np
import matplotlib.pyplot as plt
from enum import Enum

class DegType(Enum):
    Degree = 1
    Radians = 2

def T(n1, n2, theta1, deg_type: DegType = DegType.Degree):
    theta1 = theta1 if deg_type == DegType.Radians else np.radians(theta1)
    theta2 = n1/n2 * np.sin()
