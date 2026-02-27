from typing import Callable, Iterable, List, Tuple
import customtkinter as ctk
from functools import reduce
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from methods.base_method import BaseMethod
from screens.type_process import TypeProcess


def test_maker(heights: list, threshold: float | int) -> Callable:
    def test(number: int):
        if 0 > number or number >= len(heights):
            return False
        height = heights[number]
        left_value = (heights[number - 1]) if number - \
            1 > 0 and number - 1 < len(heights) else 1
        right_value = (heights[number + 1]) if number + \
            1 > 0 and number + 1 < len(heights) else 1
        return height < left_value and height < right_value and height < threshold
    return test


class Peak():
    def __init__(self,
                 center,
                 complete=False,
                 symmetric: Tuple[bool,
                                  str] | None = None,
                 adyacents_left: list | None = None,
                 adyacents_right: list | None = None,
                 total_area=0):
        self.center = center
        self.complete = complete
        self.symmetric = (True, "both") if symmetric is None else symmetric
        self.adyacents_left = [] if adyacents_left is None else adyacents_left
        self.adyacents_right = [] if adyacents_right is None else adyacents_right
        self.total_area = total_area
    
    def __str__(self) -> str:
        return f"Peak(Center: {
            self.center}, Complete: {
            self.complete}, Symmetric: {
            self.symmetric}, Adyacents Left: {
                self.adyacents_left}, Adyacents Right: {
                    self.adyacents_right}, total_area: {
                        self.total_area}"

    def __repr__(self) -> str:
        return f"Peak(Center: {
            self.center}, Complete: {
            self.complete}, Symmetric: {
            self.symmetric}, Adyacents Left: {
                self.adyacents_left}, Adyacents Right: {
                    self.adyacents_right}, total_area: {
                        self.total_area}"
    
    def checkpeak(self, dependent, independent):
        center_idx = self.center
    
        if center_idx <= 0 or center_idx >= len(dependent) - 1:
            print(f"Error: Centro en posición {center_idx} no tiene vecinos adyacentes")
            return
    
        prev_idx = center_idx - 1
        next_idx = center_idx + 1
    
        prev_value = dependent[prev_idx]
        center_value = dependent[center_idx]
        next_value = dependent[next_idx]
    
        is_peak = (center_value > prev_value) and (center_value > next_value)
    
        prev_pos = independent[prev_idx]
        center_pos = independent[center_idx]
        next_pos = independent[next_idx]
    
        print(f"{prev_pos} {center_pos} {next_pos}, {is_peak}")


    def is_complete(self) -> bool:
        return self.complete

    def calculate_area(self, dependent, independent):
        def calculate_segment_area(indices):
            area = 0.0
            for i in range(1, len(indices)):
                x1 = independent[indices[i-1]]
                x2 = independent[indices[i]]
                y1 = dependent[indices[i-1]]
                y2 = dependent[indices[i]]
                area += (x2 - x1) * ((1 - y1) + (1 - y2)) / 2.0
            return area

        if self.symmetric[0]:
            left_indices = list(reversed(self.adyacents_left)) + [self.center]
            right_indices = [self.center] + self.adyacents_right
        
            left_area = calculate_segment_area(left_indices)
            right_area = calculate_segment_area(right_indices)
            self.total_area = left_area + right_area
        else:
            problematic_side = self.symmetric[1]
        
            if problematic_side == "left":
                right_indices = [self.center] + self.adyacents_right
                right_area = calculate_segment_area(right_indices)
                self.total_area = right_area * 2
            else:
                left_indices = list(reversed(self.adyacents_left)) + [self.center]
                left_area = calculate_segment_area(left_indices)
                self.total_area = left_area * 2



    def _calculate_slope(
            self, p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
        x1, y1 = p1
        x2, y2 = p2
        return (y2 - y1) / (x2 - x1)

    def expand(self, heights, positions):
        if self.complete:
            return

        TOLERANCE = 0.5
        MAX_EXPANSION = 50  # Límite máximo de expansión

        def is_acceptable_slope(slope, side):
            if side == "left":
                return abs(slope) < TOLERANCE or slope > 0
            if side == "right":
                return abs(slope) < TOLERANCE or slope < 0

        def check_side(side):
            """Verifica un lado y retorna (slope, es_aceptable, apart)"""
            if side == "left":
                if len(self.adyacents_left) > 0:
                    current_index = self.adyacents_left[-1]
                else:
                    current_index = self.center
                apart = current_index - 1
            else:  # "right"
                if len(self.adyacents_right) > 0:
                    current_index = self.adyacents_right[-1]
                else:
                    current_index = self.center
                apart = current_index + 1

            # Verificar límites
            if apart < 0 or apart >= len(heights):
                return 0.0, True, apart  # Fuera de límites = lado completado

            # Verificar si hemos alcanzado el máximo de expansión
            if (side == "left" and len(self.adyacents_left) >= MAX_EXPANSION) or (
                    side == "right" and len(self.adyacents_right) >= MAX_EXPANSION):
                return 0.0, True, apart

            current_point = (positions[current_index], heights[current_index])
            next_point = (positions[apart], heights[apart])
            slope = self._calculate_slope(current_point, next_point)
            return slope, is_acceptable_slope(slope, side), apart

        # Aplicar la lógica de expansión
        _, left_acceptable, left_apart = check_side("left")
        _, right_acceptable, right_apart = check_side("right")

        # Determinar si debemos expandir
        left_expandable = not left_acceptable and 0 <= left_apart < len(
            heights)
        right_expandable = not right_acceptable and 0 <= right_apart < len(
            heights)

        if not left_expandable and not right_expandable:
            self.complete = True
            return

        # Expandir lados según sea necesario
        if not self.symmetric[0]:
            # Solo expandir el lado problemático
            problematic_side = self.symmetric[1]
            if problematic_side == "left" and left_expandable:
                self.adyacents_left.append(left_apart)
            elif problematic_side == "right" and right_expandable:
                self.adyacents_right.append(right_apart)
            else:
                self.complete = True
        else:
            # Expandir ambos lados
            if left_expandable and right_expandable:
                self.adyacents_left.append(left_apart)
                self.adyacents_right.append(right_apart)
            elif left_expandable:
                self.adyacents_left.append(left_apart)
                self.symmetric = (False, "right")
            elif right_expandable:
                self.adyacents_right.append(right_apart)
                self.symmetric = (False, "left")
            else:
                self.complete = True


def create_peaks(iter: Iterable[int | float]) -> List[Peak]:
    return list(map(lambda x: Peak(x), iter))


class ExplicitPeaksMethod(BaseMethod):
    def __init__(self, master, catalog, table, type):
        super().__init__(master, catalog, table, type)

    def generate_image_aux(self, independent, dependent, peaks):
        fig, ax = plt.subplots(figsize=(10, 6))

        # Graficar datos originales
        ax.plot(independent, dependent, 'b-', label='Datos', alpha=0.7)
        ax.scatter(independent, dependent, color='blue', s=10, zorder=3)

        # Graficar threshold
        threshold = float(self.threshold_entry.get())
        ax.axhline(y=threshold, color='r', linestyle='--', label='Threshold')

        # Resaltar cada pico y su área
        for peak in peaks:
            # Obtener todos los índices del pico (izquierda + centro + derecha)
            indices = peak.adyacents_left + [peak.center] + peak.adyacents_right
            # Ordenar los índices para asegurar continuidad
            indices.sort()
            
            # Extraer las coordenadas del pico
            x_peak = [independent[i] for i in indices]
            y_peak = [dependent[i] for i in indices]
            
            # Sombrear el área del pico
            ax.fill_between(x_peak, y_peak, color='pink', alpha=0.5, 
                          label=f'Área pico {independent[peak.center]:.2f}: {peak.total_area:.4f}')
            
            # Marcar el centro del pico
            ax.scatter(independent[peak.center], dependent[peak.center], 
                      color='red', s=50, zorder=4, marker='x')

        ax.set_xlabel(
            ("Inverse " if self.take_inverse_independent.get() else "") +
            self.independent_variables_selector.get())
        ax.set_ylabel(self.dependent_variables_selector.get())
        ax.set_title('Picos detectados y sus áreas')
        #ax.legend()
        ax.grid(True, alpha=0.3)
        plt.savefig("results.png")

        # Integrar el gráfico en la interfaz
        canvas = FigureCanvasTkAgg(fig, self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        canvas.draw()

    def write_peaks_to_file(self, peaks, independent, file_name="results.csv"):
        with open(file_name, "w") as file:
            file.write(f"{self.independent_variables_selector.get()},Area\n")
            for peak in peaks:
                position = independent[peak.center]
                file.write(f"{position},{peak.total_area}\n")

    
    def _create_inputs(self):
        # Colocar frame en grid
        self.peaks = ctk.CTkTextbox(
            self,
            height=300,
            border_width=2,
            corner_radius=8,
        )

        self.peaks.grid(row=2, column=0, padx=10, pady=10, sticky="nsew", rowspan=3, columnspan=3)

    def begin_end_entry(self):
        # Convertir cada línea en float, ignorando líneas vacías
        numeros = self.get_numbers()
    
        # Encontrar máximo y mínimo
        maximo = max(numeros)
        minimo = min(numeros)
    
        # Aplicar operaciones
        nuevo_maximo = maximo + 1
        nuevo_minimo = minimo - 1
    
        # Devolver tupla con los nuevos valores
        return (nuevo_minimo, nuevo_maximo)

    
    def get_vizier(self):
        begin_entry, end_entry = self.begin_end_entry()
        variables = self.catalog.search(f'''
                                        SELECT
                                            {self.independent_variables_selector.get()}, {self.dependent_variables_selector.get()}
                                        FROM
                                            "{self.table}"
                                        WHERE
                                            "{self.independent_variables_selector.get()}" BETWEEN {float(begin_entry)**(-1 if self.take_inverse_independent.get() else 1)} AND {float(end_entry)**(-1 if self.take_inverse_independent.get() else 1)}
                                            AND {self.dependent_variables_selector.get()} IS NOT NULL
                                            AND {self.independent_variables_selector.get()} IS NOT NULL
                                        ''')
        dependent = variables.getcolumn(self.dependent_variables_selector.get()) 
        independent = (variables.getcolumn(self.independent_variables_selector.get()))**(-1 if self.take_inverse_independent.get() else 1)
        return dependent, independent
    
    def get_pandas(self):
        begin_entry, end_entry = self.begin_end_entry()
        # Obtener nombres de columnas
        independent_col = self.independent_variables_selector.get()
        dependent_col = self.dependent_variables_selector.get()
    
        # Obtener límites
        begin_val = float(begin_entry)
        end_val = float(end_entry)
    
        # Aplicar transformación inversa a los límites si es necesario
        if self.take_inverse_independent.get():
            begin_limit = begin_val ** (-1)
            end_limit = end_val ** (-1)
        else:
            begin_limit = begin_val
            end_limit = end_val
    
        # Filtrar el DataFrame
        filtered_df = self.catalog[
            (self.catalog[independent_col] >= begin_limit) &
            (self.catalog[independent_col] <= end_limit) &
            (self.catalog[dependent_col].notna()) &
            (self.catalog[independent_col].notna())
        ].copy()
    
        # Aplicar transformación a la variable independiente si es necesario
        if self.take_inverse_independent.get():
            filtered_df.loc[:, 'independent_transformed'] = filtered_df[independent_col] ** (-1)
            independent = filtered_df['independent_transformed']
        else:
            independent = filtered_df[independent_col]
    
        dependent = filtered_df[dependent_col]
    
        return dependent, independent
    
    def get_numbers(self):
        contenido = self.peaks.get("1.0", "end")
    
        if contenido.endswith('\n'):
            contenido = contenido[:-1]
    
        if not contenido.strip():
            return []
    
        numeros = []
        lineas = contenido.split('\n')
    
        for i, linea in enumerate(lineas, 1):
            linea = linea.strip()
            if not linea:
                continue
            
            try:
                num = float(linea)
                numeros.append(num)
            except ValueError:
                error_msg = f"Error en línea {i}: '{linea}' no es un número válido"
                print(error_msg)
        return numeros
    
    def inside(self, x, dependent):
        min_diff = float('inf')
        min_idx = 0
    
        for i, val in enumerate(dependent):
            diff = abs(val - x)
            if diff < min_diff:
                min_diff = diff
                min_idx = i
    
        return min_idx

    def calculate(self):
        dependent, independent = self.get_variables()

        print(self.get_numbers())

        peaks = create_peaks([self.inside(x, dependent) for x in self.get_numbers()])

        for peak in peaks:
            peak.checkpeak(dependent, independent)

        max_expands = 1000 * len(peaks)

        while not reduce(
                lambda acc,
                item: acc and item.is_complete(),
                peaks,
                True) and max_expands > 0:
            for peak in peaks:
                peak.expand(dependent, independent)
            max_expands -= 1

        for peak in peaks:
            peak.calculate_area(dependent, independent)

        if self.generate_image.get():
            self.generate_image_aux(independent, dependent, peaks)

        self.write_peaks_to_file(peaks, independent)

        print(peaks)
