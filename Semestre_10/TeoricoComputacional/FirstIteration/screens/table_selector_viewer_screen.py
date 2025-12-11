import io
import customtkinter
from tabulate import tabulate
from .type_process import TypeProcess


class TableSelectorViewerScreen(customtkinter.CTkFrame):
    def __init__(self, master, catalog, type: TypeProcess = TypeProcess.VIZIER):
        super().__init__(master)
        self.master = master
        self.type = type
        
        if type == TypeProcess.VIZIER:
            self.tap_service = catalog.get_service("tap")
            self.catalog = catalog
            self.tables = catalog.get_tables()
            self.table_name = ""
        
        if type == TypeProcess.EXCEL:
            self.catalog = catalog
            self.tables = {x : "Local Table" for x in catalog.keys()}

        self._setup_grid()
        self._create_widgets()

    def _setup_grid(self):
        """Configura el grid de la pantalla."""
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Título - peso 0
        self.grid_rowconfigure(1, weight=1)  # Frame de descripción - peso 1
        self.grid_rowconfigure(2, weight=0)  # Menú de opciones - peso 0
        # Frame de visualización de tablas - peso 1
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)

    def _create_widgets(self):
        """Crea y configura los widgets de la pantalla."""
        self._create_title()
        self._create_description_frame()
        self._create_table_selector()
        self._create_table_display()
        self._create_back_button()
        self._create_select_button()

    def _create_title(self):
        """Crea el título de la pantalla."""
        title = f"Visualizador de {self.catalog.res_title if self.type == TypeProcess.VIZIER else "Tablas"}"
        self.title_label = customtkinter.CTkLabel(
            self,
            text=title,
            font=("Arial", 20, "bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    def _create_description_frame(self):
        """Crea el frame con la descripción del catálogo."""
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self)
        self.scrollable_frame.grid(
            row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        description = io.StringIO()
        self.catalog.describe(verbose=True, file=description)
        text_to_display = description.getvalue() if self.type == TypeProcess.VIZIER else "Tabla Local"

        self.text_label = customtkinter.CTkLabel(
            self.scrollable_frame,
            text=text_to_display,
            justify="left",
            wraplength=550
        )
        self.text_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    def _create_table_selector(self):
        """Crea el selector de tablas."""
        self.option_menu = customtkinter.CTkOptionMenu(
            master=self,
            values=[
                f"{table_name}: {
                    table.description}" for table_name,
                table in self.tables.items()],
            command=self.select_table)
        self.option_menu.grid(row=2, column=0, padx=10, pady=10)

    def _create_table_display(self):
        """Crea el área de visualización de tablas."""
        self.table_display_frame = customtkinter.CTkScrollableFrame(
            self, orientation="horizontal")
        self.table_display_frame.grid(
            row=3, column=0, sticky="nsew", padx=10, pady=10)
        self.table_display_frame.grid_columnconfigure(0, weight=1)
        self.table_display_frame.grid_rowconfigure(0, weight=1)

        self.table_info_label = customtkinter.CTkLabel(
            self.table_display_frame,
            text="Selecciona una tabla para ver los detalles.",
            justify="left",
            wraplength=800
        )
        self.table_info_label.grid(
            row=0, column=0, padx=10, pady=10, sticky="nsew")

    def _create_back_button(self):
        """Crea el botón para volver a la pantalla anterior."""
        self.back_button = customtkinter.CTkButton(
            self,
            text="← Volver a Catálogos",
            command=self.master.switch_to_catalog_screen
        )
        self.back_button.grid(row=5, column=0, padx=20, pady=(10, 20))

    def _create_select_button(self):
        self.select_button = customtkinter.CTkButton(
            self, text="Escoger Tabla →", command=(
                lambda: self.master.switch_to_parameter_screen(
                    self.tap_service, self.table_name, self.type)), state="disabled")
        self.select_button.grid(row=4, column=0, padx=20, pady=(10, 20))

    def select_vizier(self):
        try:
            values = self.tap_service.search(
                f'select TOP 3 * from "{self.table_name}"')
            print(values)
            table_display = tabulate(
                values.to_table(),
                headers="keys",
                tablefmt="pretty")
            self.table_info_label.configure(text=table_display)
            self.select_button.configure(state="normal")
        except Exception as e:
            self.table_info_label.configure(
                text=f"Error al cargar la tabla: {str(e)}")
    
    def select_excel(self):
        try:
            if self.table_name in self.catalog:
                self.tap_service = self.catalog[self.table_name]
                table_display = tabulate(self.tap_service.head(3), headers='keys', tablefmt='grid')
                self.table_info_label.configure(text=table_display)
            else:
                self.table_info_label.configure(text=f"Hoja '{self.table_name}' no encontrada")
    
            self.select_button.configure(state="normal")

        except Exception as e:
            self.table_info_label.configure(
                text=f"Error al cargar la tabla: {str(e)}")

    def select_table(self, choice):
        """Maneja la selección de una tabla y muestra sus datos."""

        self.table_name = choice.split(":")[0]

        if type == TypeProcess.VIZIER:
            self.select_vizier()
            return

        if type == TypeProcess.EXCEL:
            self.select_excel()
            return

        self.select_vizier()
        print(f"Tabla seleccionada: {self.table_name}")
