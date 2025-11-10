import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from methods.base_method import BaseMethod

class SymmetryMethod(BaseMethod):
    def __init__(self, master, catalog, table):
        super().__init__(master, catalog, table)