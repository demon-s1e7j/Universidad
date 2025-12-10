import customtkinter
import os
import pandas as pd
import matplotlib.pyplot as plt
import atexit
from screens.catalog_screen import CatalogScreen
from screens.table_selector_viewer_screen import TableSelectorViewerScreen
from screens.parameter_selector_screen import ParameterSelectorScreen
from screens.type_process import TypeProcess
import sys

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Catálogos de VizieR")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.current_frame = None
        self.change_to_first_screen()
        self.protocol("WM_DELETE_WINDOW", self.force_quit)

    def change_to_first_screen(self):
        if len(sys.argv) <= 1:
            self.switch_to_catalog_screen()
            return
        if ".csv" in sys.argv[1]:
            self.switch_to_parameter_screen(pd.read_csv(sys.argv[1]), "TABLA CSV", type=TypeProcess.CSV)
            return
        if ".xlsx" in sys.argv[1]:
            self.switch_to_viewer_screen(pd.read_excel(sys.argv[1], sheet_name=None), type=TypeProcess.EXCEL)
            return
        self.switch_to_catalog_screen()

    def force_quit(self):
        """Cierre forzoso de la aplicación"""
        print("Cerrando aplicación...")

        # Cerrar todas las figuras de matplotlib
        plt.close('all')

        # Limpiar frame actual
        if self.current_frame:
            if hasattr(self.current_frame, 'destroy_figures'):
                self.current_frame.destroy_figures()
            self.current_frame.destroy()

        # Destruir ventana principal
        self.quit()
        self.destroy()

        # Forzar salida del proceso
        os._exit(0)

    def on_closing(self):
        """Maneja el cierre correcto de la aplicación"""
        plt.close('all')  # Cierra todas las figuras de matplotlib
        self.quit()
        self.destroy()

    def switch_to_catalog_screen(self):
        """Muestra la pantalla de búsqueda de catálogos."""
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = CatalogScreen(self)
        self.current_frame.pack(fill="both", expand=True)

    def switch_to_viewer_screen(self, catalog, type=TypeProcess.VIZIER):
        """Muestra la pantalla del visualizador de posibilidades."""
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = TableSelectorViewerScreen(self, catalog, type)
        self.current_frame.pack(fill="both", expand=True)

    def switch_to_parameter_screen(self, catalog, table, type):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = ParameterSelectorScreen(self, catalog, table, type)
        self.current_frame.pack(fill="both", expand=True)

    def _cleanup_current_frame(self):
        """Limpia el frame actual y las figuras de matplotlib"""
        if self.current_frame:
            # Cierra cualquier figura de matplotlib en el frame actual
            if hasattr(self.current_frame, 'close_figures'):
                self.current_frame.close_figures()
            self.current_frame.pack_forget()
            self.current_frame.destroy()
        plt.close('all')  # Cierra todas las figuras


def close_application():
    """Función para cerrar la aplicación en caso de que se llame desde atexit"""
    plt.close('all')


atexit.register(close_application)

if __name__ == "__main__":
    import signal
    import sys

    def signal_handler(sig, frame):
        plt.close('all')
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    app = App()
    try:
        app.mainloop()
    finally:
        plt.close("all")
