import customtkinter
from screens.catalog_screen import CatalogScreen
from screens.table_selector_viewer_screen import TableSelectorViewerScreen
from screens.parameter_selector_screen import ParameterSelectorScreen

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Catálogos de VizieR")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.current_frame = None
        self.switch_to_catalog_screen()

    def switch_to_catalog_screen(self):
        """Muestra la pantalla de búsqueda de catálogos."""
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = CatalogScreen(self)
        self.current_frame.pack(fill="both", expand=True)

    def switch_to_viewer_screen(self, catalog):
        """Muestra la pantalla del visualizador de posibilidades."""
        self.current_frame.pack_forget()
        self.current_frame = TableSelectorViewerScreen(self, catalog)
        self.current_frame.pack(fill="both", expand=True)

    def switch_to_parameter_screen(self, catalog, table):
        self.current_frame.pack_forget()
        self.current_frame = ParameterSelectorScreen(self, catalog, table)
        self.current_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
