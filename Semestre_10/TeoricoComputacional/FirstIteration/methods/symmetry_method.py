from typing import Callable, Iterable, List, Tuple
from functools import reduce
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from methods.base_method import BaseMethod


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


def create_peaks(iter: Iterable[int]) -> List[Peak]:
    return list(map(lambda x: Peak(x), iter))


class SymmetryMethod(BaseMethod):
    def __init__(self, master, catalog, table):
        super().__init__(master, catalog, table)

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

        dependent = variables.getcolumn(
            self.dependent_variables_selector.get())
        independent = (variables.getcolumn(self.independent_variables_selector.get(
        )))**(-1 if self.take_inverse_independent.get() else 1)

        peaks = create_peaks(
            filter(
                test_maker(
                    dependent, float(
                        self.threshold_entry.get())), range(
                    len(independent))))

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