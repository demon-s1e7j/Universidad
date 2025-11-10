import io
from astropy.table import column
from astropy.units.function.units import _description
import customtkinter
from tabulate import tabulate
from pyvo import registry

# Definimos la ventana principal que gestionará las pantallas
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
            self.current_frame.pack_forget() # Oculta la pantalla actual
        self.current_frame = CatalogScreen(self)
        self.current_frame.pack(fill="both", expand=True)

    def switch_to_viewer_screen(self, catalog_name):
        """Muestra la pantalla del visualizador de posibilidades."""
        self.current_frame.pack_forget() # Oculta la pantalla de catálogos
        self.current_frame = TableSelectorViewerScreen(self, catalog_name)
        self.current_frame.pack(fill="both", expand=True)

# ----------------------------------------------------------------------------------------------------------------------
# CLASE DE PANTALLA 1: Búsqueda de Catálogos
# ----------------------------------------------------------------------------------------------------------------------
class CatalogScreen(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        # Simulación de datos de catálogos

        # Encabezado
        self.title_label = customtkinter.CTkLabel(self, text="Catálogos de VizieR", font=("Arial", 20, "bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.search_entry = customtkinter.CTkEntry(self, placeholder_text="Escribe algo para buscar")
        self.search_entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.search_button = customtkinter.CTkButton(self, text="Buscar", command=self.create_catalog_buttons)
        self.search_button.grid(row=1, column=1, padx=20, pady=10)
        
        # Frame para los resultados
        self.results_frame = customtkinter.CTkScrollableFrame(self)
        self.results_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew", columnspan=2)
        self.results_frame.grid_columnconfigure(0, weight=1)

    def create_catalog_buttons(self):
        """Crea un botón para cada catálogo y lo empaqueta en el frame de resultados."""
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        query = self.search_entry.get() if self.search_entry.get() != "" else "J/A+A/587/A65"
        self.search_entry.delete(0, customtkinter.END)
        catalogue_ivoid = f"ivo://CDS.VizieR/{query}"
        self.catalogs = registry.search(ivoid=catalogue_ivoid)

        if len(self.catalogs) <= 0:
            error_message = f"❌ No se encontraron resultados para '{query}'."
            error_label = customtkinter.CTkLabel(self.results_frame, text=error_message, font=("Arial", 14), text_color="red")
            error_label.pack(anchor="center", pady=20)
            return

        for _, catalog in enumerate(self.catalogs):
            # El comando del botón llama a la función para cambiar de pantalla y le pasa el nombre del catálogo.
            button = customtkinter.CTkButton(self.results_frame, 
                                             text=f"Abrir: {catalog.res_title}",
                                             command=lambda c=catalog: self.master.switch_to_viewer_screen(c))
            button.pack(fill="x", padx=10, pady=5)

# ----------------------------------------------------------------------------------------------------------------------
# CLASE DE PANTALLA 2: Visualizador de Posibilidades
# ----------------------------------------------------------------------------------------------------------------------
class TableSelectorViewerScreen(customtkinter.CTkFrame):
    def __init__(self, master, catalog):
        super().__init__(master)

        self.tap_service = catalog.get_service("tap")

        self.master = master
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Título - peso 0
        self.grid_rowconfigure(1, weight=1)  # Frame de descripción - peso 1
        self.grid_rowconfigure(2, weight=0)  # Menú de opciones - peso 0
        self.grid_rowconfigure(3, weight=1)  # Frame de visualización de tablas - peso 1
        self.grid_rowconfigure(4, weight=0) 

        # Título dinámico
        self.title_label = customtkinter.CTkLabel(self, text=f"Visualizador de {catalog.res_title}", font=("Arial", 20, "bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        description = io.StringIO()
        catalog.describe(verbose=True, file=description)
        text_to_display = description.getvalue()
        
        self.text_label = customtkinter.CTkLabel(
            self.scrollable_frame, 
            text=text_to_display, # Usa la variable con el texto limpio
            justify="left",
            wraplength=550
        )
        self.text_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.tables = catalog.get_tables()
        self.option_menu = customtkinter.CTkOptionMenu(
            master=self,
            values=[f"{table_name}: {table.description}" for table_name, table in self.tables.items()],
            command=self.select_table
        )
        self.option_menu.grid(row=2, column=0, padx=10, pady=10)

        # Botón para volver a la pantalla de catálogos
        self.table_display_frame = customtkinter.CTkScrollableFrame(self, orientation="horizontal")
        self.table_display_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)
        self.table_display_frame.grid_columnconfigure(0, weight=1)
        self.table_display_frame.grid_rowconfigure(0, weight=1)
        self.table_display_frame.grid(row=3, column=0, padx=10, pady=10)

        self.table_info_label = customtkinter.CTkLabel(
            self.table_display_frame, 
            text="Selecciona una tabla para ver los detalles.", 
            justify="left",
            wraplength=800
        )
        self.table_info_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.back_button = customtkinter.CTkButton(self, 
                                                  text="← Volver a Catálogos", 
                                                  command=self.master.switch_to_catalog_screen)
        self.back_button.grid(row=4, column=0, padx=20, pady=(10, 20))


    def select_table(self, choice):
        table_name = choice.split(":")[0]
        values = self.tap_service.search(f'select TOP 3 * from "{table_name}"')
        self.table_info_label.configure(text=tabulate(values.to_table(), headers="keys", tablefmt="pretty"))
        print(f"La opción seleccionada es: {choice}, lo que implica que es la tabla {table_name}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
