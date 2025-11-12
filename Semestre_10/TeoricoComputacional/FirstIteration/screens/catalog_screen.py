import customtkinter
from pyvo import registry


class CatalogScreen(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self._create_widgets()

    def _create_widgets(self):
        """Crea y configura los widgets de la pantalla de catálogos."""
        # Encabezado
        self.title_label = customtkinter.CTkLabel(
            self, text="Catálogos de VizieR", font=(
                "Arial", 20, "bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Búsqueda
        self.search_entry = customtkinter.CTkEntry(
            self, placeholder_text="Escribe algo para buscar")
        self.search_entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.search_button = customtkinter.CTkButton(
            self, text="Buscar", command=self.create_catalog_buttons)
        self.search_button.grid(row=1, column=1, padx=20, pady=10)

        # Frame para los resultados
        self.results_frame = customtkinter.CTkScrollableFrame(self)
        self.results_frame.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
            sticky="nsew",
            columnspan=2)
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
            error_label = customtkinter.CTkLabel(
                self.results_frame, text=error_message, font=(
                    "Arial", 14), text_color="red")
            error_label.pack(anchor="center", pady=20)
            return

        for _, catalog in enumerate(self.catalogs):
            button = customtkinter.CTkButton(
                self.results_frame,
                text=f"Abrir: {
                    catalog.res_title}",
                command=lambda c=catalog: self.master.switch_to_viewer_screen(c))
            button.pack(fill="x", padx=10, pady=5)
