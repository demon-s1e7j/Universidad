import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExplicitLimits(customtkinter.CTkFrame):
    def __init__(self, master, catalog, table):
        super().__init__(master)

        self.catalog = catalog
        self.table = table

        self._setup_grid()
        self._create_widgets()
    
    def _setup_grid(self):
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
    
    def _create_widgets(self):
        self._create_variables_selector()
        self._create_inputs()
        self._create_generate_image()
        self._create_calculate_button()

    def _create_variables_selector(self):
        variables = self.catalog.search(f'SELECT TOP 3 * FROM "{self.table}"').fieldnames
        self.independent_variables_selector_label = customtkinter.CTkLabel(self, text="Variable Independiente: ")
        self.independent_variables_selector = customtkinter.CTkOptionMenu(
            self,
            values=variables,
        )
        self.independent_variables_selector_label.grid(row=0, column=0, padx=5, pady=5)
        self.independent_variables_selector.grid(row=0, column=1, padx=5, pady=5)

        self.dependent_variables_selector_label = customtkinter.CTkLabel(self, text="Variable Dependiente: ")
        self.dependent_variables_selector = customtkinter.CTkOptionMenu(
            self,
            values=variables,
        )
        self.dependent_variables_selector_label.grid(row=1, column=0, padx=5, pady=5)
        self.dependent_variables_selector.grid(row=1, column=1, padx=5, pady=5)
    
    def _create_inputs(self):
        self._create_begin_point()
        self._create_end_point()

    def _create_begin_point(self):
        self.begin_label = customtkinter.CTkLabel(self, text="Punto Inicio: ")
        self.begin_label.grid(row=2, column=0, padx=5, pady=5)
        self.begin_entry = customtkinter.CTkEntry(self)
        self.begin_entry.grid(row=2, column=1, padx=5, pady=5)

    def _create_end_point(self):
        self.end_label = customtkinter.CTkLabel(self, text="Punto Final: ")
        self.end_label.grid(row=3, column=0, padx=5, pady=5)
        self.end_entry = customtkinter.CTkEntry(self)
        self.end_entry.grid(row=3, column=1, padx=5, pady=5)

    def _create_generate_image(self):
        self.generate_image = customtkinter.CTkCheckBox(
            self,
            text ="Generar Imagen"
        )

        self.generate_image.grid(row=4, column=0, padx=5, pady=5)

    def _create_calculate_button(self):
        self.calculate_buttons = customtkinter.CTkButton(
            self,
            text="Calcular",
            command=self.calculate)
        self.calculate_buttons.grid(row=4, column=1, padx=5, pady=5)
    
    def calculate(self):
        variables = self.catalog.search(f'''
                                        SELECT
                                            {self.independent_variables_selector.get()}, {self.dependent_variables_selector.get()}
                                        FROM
                                            "{self.table}"
                                        WHERE
                                            "{self.independent_variables_selector.get()}" BETWEEN {self.begin_entry.get()} AND {self.end_entry.get()}
                                            AND {self.dependent_variables_selector.get()} IS NOT NULL
                                            AND {self.independent_variables_selector.get()} IS NOT NULL
                                        ''')
        dependent = variables.getcolumn(self.dependent_variables_selector.get())
        independent = variables.getcolumn(self.independent_variables_selector.get())

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
        
    def generate_image_aux(self, independent, dependent, rectangles, sum):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Gráfico 1: Puntos originales
        ax1.scatter(independent, dependent, color='blue', label='Datos')
        ax1.set_xlabel(self.independent_variables_selector.get())
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
        ax2.plot(independent, dependent, 'b-', alpha=0.7, linewidth=1, label='Función', zorder=3)
        
        ax2.set_xlabel(self.independent_variables_selector.get())
        ax2.set_ylabel(self.dependent_variables_selector.get())
        ax2.set_title(f'Suma de Riemann: {sum:.4f}')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Ajustar layout
        plt.tight_layout()
        
        # Integrar el gráfico en la interfaz de CustomTkinter
        canvas = FigureCanvasTkAgg(fig, self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        canvas.draw()
