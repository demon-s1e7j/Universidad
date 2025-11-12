import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from methods.base_method import BaseMethod

class ExplicitLimits(BaseMethod):
    def __init__(self, master, catalog, table):
        super().__init__(master, catalog, table)

    def calculate(self):
        variables = self.catalog.search(f'''
                                        SELECT
                                            {self.independent_variables_selector.get()}, {self.dependent_variables_selector.get()}
                                        FROM
                                            "{self.table}"
                                        WHERE
                                            "{self.independent_variables_selector.get()}" BETWEEN {float(self.begin_entry.get())**(-1 if self.take_inverse_independent.get() else 1)} AND {float(self.end_entry.get())**(-1 if self.take_inverse_independent.get() else 1)}
                                            AND {self.dependent_variables_selector.get()} IS NOT NULL
                                            AND {self.independent_variables_selector.get()} IS NOT NULL
                                        ''')
        dependent = variables.getcolumn(self.dependent_variables_selector.get()) 
        independent = (variables.getcolumn(self.independent_variables_selector.get()))**(-1 if self.take_inverse_independent.get() else 1)

        print(variables)

        riemann_rectangles = []
        riemann_sum = 0

        for i in range(len(independent) - 1):
            base = independent[i + 1] - independent[i]  # Base del rectángulo
            altura = dependent[i]  # Altura usando el punto izquierdo
            area_rectangulo = base * altura
            riemann_sum += area_rectangulo
            riemann_rectangles.append({
                'x': independent[i],
                'base': base,
                'altura': altura,
                'area': area_rectangulo
            })

        if self.generate_image.get():
            self.generate_image_aux(independent, dependent, riemann_rectangles, riemann_sum)

        self.write_to_file(riemann_rectangles)
        
    def generate_image_aux(self, independent, dependent, rectangles, sum):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Gráfico 1: Puntos originales
        ax1.scatter(independent, dependent, color='blue', label='Datos')
        ax1.plot(independent, np.repeat(float(self.threshold_entry.get()), independent.shape), color="red")
        ax1.set_xlabel(("Inverse " if self.take_inverse_independent.get() else "") + self.independent_variables_selector.get())
        ax1.set_ylabel(self.dependent_variables_selector.get())
        ax1.set_title(f'{self.dependent_variables_selector.get()} vs {self.independent_variables_selector.get()}')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Gráfico 2: Suma de Riemann con rectángulos
        ax2.scatter(independent, dependent, color='blue', label='Datos', zorder=3)
        
        # Dibujar rectángulos de Riemann
        for rect in rectangles:
            ax2.add_patch(plt.Rectangle(
                (rect['x'], 0),           # Esquina inferior izquierda
                rect['base'],              # Ancho
                rect['altura'],            # Alto
                fill=True,
                color='pink',
                alpha=0.5,                 # Transparencia
                edgecolor='red',
                linewidth=0.5,
                zorder=2
            ))
        
        # Conectar puntos con líneas
        ax2.plot(independent, dependent, 'b-', alpha=0.7, linewidth=1, label='Especter', zorder=3)
        ax2.plot(independent, np.repeat(float(self.threshold_entry.get()), independent.shape), color="red")
        
        ax2.set_xlabel(("Inverse " if self.take_inverse_independent.get() else "") + self.independent_variables_selector.get())
        ax2.set_ylabel(self.dependent_variables_selector.get())
        ax2.set_title(f'Suma de Riemann: {sum:.4f}')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Ajustar layout
        plt.tight_layout()
        
        # Integrar el gráfico en la interfaz de CustomTkinter
        canvas = FigureCanvasTkAgg(fig, self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        canvas.draw()
    
    def write_to_file(self, riemann_rectangles, file_name="results.csv"):
        with open(file_name, "w") as file:
            file.write(f"{self.independent_variables_selector.get()},Area\n")
            for i, rect in enumerate(riemann_rectangles):
                if rect["altura"] < float(self.threshold_entry.get()):
                    continue
                total_area = rect["area"] + (riemann_rectangles[(i -1)]["area"] if (i - 1) >= 0 else 0)
                position = rect["x"]
                file.write(f"{position}, {total_area}\n")
