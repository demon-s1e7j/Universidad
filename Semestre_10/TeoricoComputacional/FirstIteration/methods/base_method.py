import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class BaseMethod(customtkinter.CTkFrame):
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
        self.grid_rowconfigure(5, weight=0)

    def _create_widgets(self):
        self._create_variables_selector()
        self._create_inputs()
        self._create_generate_image()
        self._create_calculate_button()

    def _create_variables_selector(self):
        variables = self.catalog.search(
            f'SELECT TOP 3 * FROM "{self.table}"').fieldnames
        self.independent_variables_selector_label = customtkinter.CTkLabel(
            self, text="Variable Independiente: ")
        self.independent_variables_selector = customtkinter.CTkOptionMenu(
            self,
            values=variables,
        )
        self.independent_variables_selector_label.grid(
            row=0, column=0, padx=5, pady=5)
        self.independent_variables_selector.grid(
            row=0, column=1, padx=5, pady=5)
        self.take_inverse_independent = customtkinter.CTkCheckBox(
            self,
            text="Take Inverse"
        )

        self.take_inverse_independent.grid(row=0, column=2, padx=5, pady=5)

        self.dependent_variables_selector_label = customtkinter.CTkLabel(
            self, text="Variable Dependiente: ")
        self.dependent_variables_selector = customtkinter.CTkOptionMenu(
            self,
            values=variables,
        )
        self.dependent_variables_selector_label.grid(
            row=1, column=0, padx=5, pady=5)
        self.dependent_variables_selector.grid(row=1, column=1, padx=5, pady=5)

    def _create_inputs(self):
        self._create_begin_point()
        self._create_end_point()
        self._create_threshold()

    def _create_begin_point(self):
        self.begin_label = customtkinter.CTkLabel(self, text="Begin Point: ")
        self.begin_label.grid(row=2, column=0, padx=5, pady=5)
        self.begin_entry = customtkinter.CTkEntry(self)
        self.begin_entry.grid(row=2, column=1, padx=5, pady=5)

    def _create_end_point(self):
        self.end_label = customtkinter.CTkLabel(self, text="Final Point: ")
        self.end_label.grid(row=4, column=0, padx=5, pady=5)
        self.end_entry = customtkinter.CTkEntry(self)
        self.end_entry.grid(row=4, column=1, padx=5, pady=5)

    def _create_threshold(self):
        self.threshold_label = customtkinter.CTkLabel(self, text="Threshold: ")
        self.threshold_label.grid(row=3, column=0, padx=5, pady=5)
        self.threshold_entry = customtkinter.CTkEntry(self)
        self.threshold_entry.grid(row=3, column=1, padx=5, pady=5)

    def _create_generate_image(self):
        self.generate_image = customtkinter.CTkCheckBox(
            self,
            text="Generate Imagen"
        )
        self.generate_image.grid(row=5, column=0, padx=5, pady=5)

    def _create_calculate_button(self):
        self.calculate_buttons = customtkinter.CTkButton(
            self,
            text="Calcular",
            command=self.calculate)
        self.calculate_buttons.grid(row=5, column=1, padx=5, pady=5)

    def calculate(self):
        print(f"""
        Select
        {self.independent_variables_selector.get()}, {self.dependent_variables_selector.get()}
        FROM
            "{self.table}"
        WHERE
            "{self.independent_variables_selector.get()}" BETWEEN {self.begin_entry.get()} AND {self.end_entry.get()}
            AND {self.dependent_variables_selector.get()} IS NOT NULL
            AND {self.independent_variables_selector.get()} IS NOT NULL

        Inverso: {self.take_inverse_independent.get()}
        Generate Image: {self.generate_image.get()}
        Threshold: {self.threshold_entry.get()}
""")
