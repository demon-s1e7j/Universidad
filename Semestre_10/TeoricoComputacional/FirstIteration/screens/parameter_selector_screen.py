import customtkinter
import matplotlib.pyplot as plt
from methods.simple_method import ExplicitLimits
from methods.symmetry_method import SymmetryMethod


class ParameterSelectorScreen(customtkinter.CTkFrame):
    def __init__(self, master, catalog, table):
        super().__init__(master)
        self.catalog = catalog
        self.table = table
        self.master = master
        self.options = ["Simple Selector", "Symmetry Selector"]
        self.current_method_widget = None  # Referencia al widget actual

        self._setup_grid()
        self._create_widgets()
        print(f"Entraste a Parameter Screen con: {self.table}")

    def _setup_grid(self):
        self.grid_rowconfigure(0, weight=0)  # Title
        self.grid_rowconfigure(1, weight=0)  # Method Selector
        self.grid_rowconfigure(2, weight=1)  # Dynamic widget area
        self.grid_columnconfigure(0, weight=1)

    def _create_widgets(self):
        self._create_title()
        self._create_method_selector()
        self._create_dynamic_widget_area()

    def _create_title(self):
        self.title_label = customtkinter.CTkLabel(
            self,
            text=f"Selector de Parametros para {self.table}",
            font=("Arial", 20, "bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    def _create_method_selector(self):
        self.method_selector = customtkinter.CTkOptionMenu(
            self,
            values=self.options,
            command=self.method_selected
        )
        self.method_selector.grid(row=1, column=0, padx=20, pady=(20, 10))

    def _create_dynamic_widget_area(self):
        # Frame contenedor para widgets dinámicos
        self.dynamic_frame = customtkinter.CTkScrollableFrame(self)
        self.dynamic_frame.grid(
            row=2,
            column=0,
            padx=20,
            pady=20,
            sticky="nsew")
        self.dynamic_frame.grid_columnconfigure(0, weight=1)

    def close_figures(self):
        plt.close("all")

    def method_selected(self, method):
        print(f"Método seleccionado: {method}")

        # Limpiar widget anterior
        if self.current_method_widget:
            self.current_method_widget.destroy()

        # Crear nuevo widget según el método
        if method == "Simple Selector":
            self.current_method_widget = ExplicitLimits(
                self.dynamic_frame, self.catalog, self.table)
            self.current_method_widget.grid(
                row=0, column=0, sticky="nsew", padx=10, pady=10)

        if method == "Symmetry Selector":
            self.current_method_widget = SymmetryMethod(
                self.dynamic_frame, self.catalog, self.table)
            self.current_method_widget.grid(
                row=0, column=0, sticky="nsew", padx=10, pady=10)
