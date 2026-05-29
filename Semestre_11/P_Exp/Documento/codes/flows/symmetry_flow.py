import pygraphviz as pgv

def create_main_diagram():
    """Crea el diagrama de flujo principal del método calculate()"""
    G = pgv.AGraph(directed=True, strict=True)
    G.graph_attr.update(
        rankdir='TB',
        label='Diagrama de Flujo - Método calculate() de SymmetryMethod',
        labelloc='t',
        fontname='Arial',
        fontsize='12'
    )
    G.node_attr.update(
        shape='rectangle',
        style='rounded,filled',
        fillcolor='#e1f5fe',
        fontname='Arial',
        fontsize='10'
    )
    
    # Nodos
    nodes = {
        'start': 'INICIO: calculate',
        'query': 'Consultar datos en BD\ncon filtros de rango',
        'get_arrays': 'Obtener arrays dependent\ne independent',
        'check_inverse': 'Aplicar inverso a\nindependent?',
        'apply_inverse': 'Aplicar transformación\ninversa',
        'keep_original': 'Dejar original',
        'create_test': 'Crear función test_maker\ncon threshold',
        'filter_centers': 'Filtrar índices que son\ncentros de picos',
        'create_peaks': 'Crear lista de objetos\nPeak para cada centro',
        'init_expands': 'Inicializar max_expands\n= 1000 * len(peaks)',
        'check_complete': 'Todos los picos\ncompletos?',
        'check_expands': 'max_expands > 0?',
        'expand_all': 'Expandir cada pico\npeak.expand',
        'decrement': 'Decrementar max_expands',
        'calculate_areas': 'Para cada peak:\ncalculate_area',
        'check_image': 'generate_image\nactivado?',
        'generate_img': 'Llamar generate_image_aux',
        'write_csv': 'Escribir resultados\nen archivo CSV',
        'print_peaks': 'Imprimir lista de peaks\nen consola',
        'end': 'FIN'
    }
    
    # Añadir nodos con identificadores
    for key, label in nodes.items():
        G.add_node(key, label=label)
    
    # Conexiones
    edges = [
        ('start', 'query'),
        ('query', 'get_arrays'),
        ('get_arrays', 'check_inverse'),
        ('check_inverse', 'apply_inverse', 'Sí'),
        ('check_inverse', 'keep_original', 'No'),
        ('apply_inverse', 'create_test'),
        ('keep_original', 'create_test'),
        ('create_test', 'filter_centers'),
        ('filter_centers', 'create_peaks'),
        ('create_peaks', 'init_expands'),
        ('init_expands', 'check_complete'),
        ('check_complete', 'check_expands', 'No'),
        ('check_complete', 'calculate_areas', 'Sí'),
        ('check_expands', 'expand_all', 'Sí'),
        ('check_expands', 'calculate_areas', 'No'),
        ('expand_all', 'decrement'),
        ('decrement', 'check_complete'),
        ('calculate_areas', 'check_image'),
        ('check_image', 'generate_img', 'Sí'),
        ('check_image', 'write_csv', 'No'),
        ('generate_img', 'write_csv'),
        ('write_csv', 'print_peaks'),
        ('print_peaks', 'end')
    ]
    
    # Añadir conexiones
    for edge in edges:
        if len(edge) == 2:
            G.add_edge(edge[0], edge[1])
        else:
            G.add_edge(edge[0], edge[1], label=edge[2])
    
    # Guardar diagrama
    G.layout(prog='dot')
    G.draw('../Fig/diagrama_principal.png')
    print("Diagrama principal creado: diagrama_principal.png")

def create_expand_diagram():
    """Crea el diagrama de flujo del método expand() de Peak"""
    G = pgv.AGraph(directed=True, strict=True)
    G.graph_attr.update(
        rankdir='TB',
        label='Diagrama de Flujo - Método expand() de Peak',
        labelloc='t',
        fontname='Arial',
        fontsize='12'
    )
    G.node_attr.update(
        shape='rectangle',
        style='rounded,filled',
        fillcolor='#f3e5f5',
        fontname='Arial',
        fontsize='9'
    )
    
    # Nodos
    nodes = {
        'start': 'INICIO: expand',
        'check_complete': 'peak.complete == True?',
        'return': 'RETORNAR inmediatamente',
        'init_params': 'Definir TOLERANCE = 0.5\nMAX_EXPANSION = 50',
        'calc_left': 'Calcular slope y apart\npara lado izquierdo',
        'calc_right': 'Calcular slope y apart\npara lado derecho',
        'check_left_range': 'left_apart en rango\ny expansiones < MAX?',
        'check_right_range': 'right_apart en rango\ny expansiones < MAX?',
        'left_false': 'left_expandable = False',
        'left_check_slope': 'Slope aceptable\npara izquierda?',
        'left_true': 'left_expandable = True',
        'right_false': 'right_expandable = False',
        'right_check_slope': 'Slope aceptable\npara derecha?',
        'right_true': 'right_expandable = True',
        'check_expandable': 'left_expandable OR\nright_expandable?',
        'set_complete': 'peak.complete = True',
        'check_symmetric': 'peak.symmetric[0] == True?',
        'check_both': 'Ambos lados\nexpandibles?',
        'expand_both': 'Expandir ambos lados',
        'check_left_only': 'Solo left_expandable?',
        'expand_left_asym': 'Expandir izquierda\nsymmetric = (False, "right")',
        'expand_right_asym': 'Expandir derecha\nsymmetric = (False, "left")',
        'get_problematic': 'Obtener lado\nproblemático',
        'check_problem_left': 'Lado problemático == "left"\ny left_expandable?',
        'expand_problem_left': 'Expandir izquierda',
        'check_problem_right': 'Lado problemático == "right"\ny right_expandable?',
        'expand_problem_right': 'Expandir derecha',
        'end': 'FIN expand'
    }
    
    # Añadir nodos
    for key, label in nodes.items():
        G.add_node(key, label=label)
    
    # Conexiones
    edges = [
        ('start', 'check_complete'),
        ('check_complete', 'return', 'Sí'),
        ('check_complete', 'init_params', 'No'),
        ('init_params', 'calc_left'),
        ('init_params', 'calc_right'),
        ('calc_left', 'check_left_range'),
        ('calc_right', 'check_right_range'),
        ('check_left_range', 'left_false', 'No'),
        ('check_left_range', 'left_check_slope', 'Sí'),
        ('left_check_slope', 'left_false', 'Sí'),
        ('left_check_slope', 'left_true', 'No'),
        ('check_right_range', 'right_false', 'No'),
        ('check_right_range', 'right_check_slope', 'Sí'),
        ('right_check_slope', 'right_false', 'Sí'),
        ('right_check_slope', 'right_true', 'No'),
        ('left_false', 'check_expandable'),
        ('left_true', 'check_expandable'),
        ('right_false', 'check_expandable'),
        ('right_true', 'check_expandable'),
        ('check_expandable', 'set_complete', 'No'),
        ('check_expandable', 'check_symmetric', 'Sí'),
        ('check_symmetric', 'check_both', 'Sí'),
        ('check_both', 'expand_both', 'Sí'),
        ('check_both', 'check_left_only', 'No'),
        ('check_left_only', 'expand_left_asym', 'Sí'),
        ('check_left_only', 'expand_right_asym', 'No'),
        ('check_symmetric', 'get_problematic', 'No'),
        ('get_problematic', 'check_problem_left'),
        ('check_problem_left', 'expand_problem_left', 'Sí'),
        ('check_problem_left', 'check_problem_right', 'No'),
        ('check_problem_right', 'expand_problem_right', 'Sí'),
        ('check_problem_right', 'set_complete', 'No'),
        ('expand_both', 'end'),
        ('expand_left_asym', 'end'),
        ('expand_right_asym', 'end'),
        ('expand_problem_left', 'end'),
        ('expand_problem_right', 'end'),
        ('set_complete', 'end')
    ]
    
    # Añadir conexiones
    for edge in edges:
        if len(edge) == 2:
            G.add_edge(edge[0], edge[1])
        else:
            G.add_edge(edge[0], edge[1], label=edge[2])
    
    # Guardar diagrama
    G.layout(prog='dot')
    G.draw('../Fig/diagrama_expand.png')
    print("Diagrama expand creado: diagrama_expand.png")

def create_calculate_area_diagram():
    """Crea el diagrama de flujo del método calculate_area()"""
    G = pgv.AGraph(directed=True, strict=True)
    G.graph_attr.update(
        rankdir='TB',
        label='Diagrama de Flujo - Método calculate_area() de Peak',
        labelloc='t',
        fontname='Arial',
        fontsize='12'
    )
    G.node_attr.update(
        shape='rectangle',
        style='rounded,filled',
        fillcolor='#e8f5e8',
        fontname='Arial',
        fontsize='9'
    )
    
    # Nodos
    nodes = {
        'start': 'INICIO: calculate_area',
        'check_symmetric': 'peak.symmetric[0] == True?',
        'calc_left_indices': 'Calcular left_indices\nreversed(adyacents_left) + center',
        'calc_right_indices': 'Calcular right_indices\ncenter + adyacents_right',
        'calc_left_area': 'Calcular left_area\ncon calculate_segment_area',
        'calc_right_area': 'Calcular right_area\ncon calculate_segment_area',
        'sum_areas': 'total_area = left_area + right_area',
        'get_problematic': 'Obtener lado\nproblemático',
        'check_left_side': 'lado problemático == "left"?',
        'calc_right_only': 'Calcular right_indices\ncenter + adyacents_right',
        'calc_right_area_only': 'Calcular right_area\ncon calculate_segment_area',
        'double_right': 'total_area = right_area * 2',
        'calc_left_only': 'Calcular left_indices\nreversed(adyacents_left) + center',
        'calc_left_area_only': 'Calcular left_area\ncon calculate_segment_area',
        'double_left': 'total_area = left_area * 2',
        'end': 'FIN calculate_area'
    }
    
    # Añadir nodos
    for key, label in nodes.items():
        G.add_node(key, label=label)
    
    # Conexiones
    edges = [
        ('start', 'check_symmetric'),
        ('check_symmetric', 'calc_left_indices', 'Sí'),
        ('calc_left_indices', 'calc_right_indices'),
        ('calc_right_indices', 'calc_left_area'),
        ('calc_left_area', 'calc_right_area'),
        ('calc_right_area', 'sum_areas'),
        ('sum_areas', 'end'),
        ('check_symmetric', 'get_problematic', 'No'),
        ('get_problematic', 'check_left_side'),
        ('check_left_side', 'calc_right_only', 'Sí'),
        ('calc_right_only', 'calc_right_area_only'),
        ('calc_right_area_only', 'double_right'),
        ('double_right', 'end'),
        ('check_left_side', 'calc_left_only', 'No'),
        ('calc_left_only', 'calc_left_area_only'),
        ('calc_left_area_only', 'double_left'),
        ('double_left', 'end')
    ]
    
    # Añadir conexiones
    for edge in edges:
        if len(edge) == 2:
            G.add_edge(edge[0], edge[1])
        else:
            G.add_edge(edge[0], edge[1], label=edge[2])
    
    # Guardar diagrama
    G.layout(prog='dot')
    G.draw('../Fig/diagrama_calculate_area.png')
    print("Diagrama calculate_area creado: diagrama_calculate_area.png")

def create_segment_area_diagram():
    """Crea el diagrama de flujo de calculate_segment_area()"""
    G = pgv.AGraph(directed=True, strict=True)
    G.graph_attr.update(
        rankdir='TB',
        label='Diagrama de Flujo - Función calculate_segment_area()',
        labelloc='t',
        fontname='Arial',
        fontsize='12'
    )
    G.node_attr.update(
        shape='rectangle',
        style='rounded,filled',
        fillcolor='#fff3e0',
        fontname='Arial',
        fontsize='9'
    )
    
    # Nodos
    nodes = {
        'start': 'INICIO: calculate_segment_area',
        'init_area': 'Inicializar area = 0.0',
        'for_loop': 'Para i = 1 hasta len(indices)',
        'get_coords': 'Obtener x1, y1, x2, y2\nde indices[i-1] e indices[i]',
        'calc_segment': 'Calcular segmento:\n(x2 - x1) * ((1 - y1) + (1 - y2)) / 2.0',
        'add_to_area': 'Sumar a area',
        'loop_end': 'Terminado',
        'return': 'RETORNAR area'
    }
    
    # Añadir nodos
    for key, label in nodes.items():
        G.add_node(key, label=label)
    
    # Conexiones
    edges = [
        ('start', 'init_area'),
        ('init_area', 'for_loop'),
        ('for_loop', 'get_coords'),
        ('get_coords', 'calc_segment'),
        ('calc_segment', 'add_to_area'),
        ('add_to_area', 'for_loop'),
        ('for_loop', 'loop_end', 'Terminado'),
        ('loop_end', 'return')
    ]
    
    # Añadir conexiones
    for edge in edges:
        if len(edge) == 2:
            G.add_edge(edge[0], edge[1])
        else:
            G.add_edge(edge[0], edge[1], label=edge[2])
    
    # Guardar diagrama
    G.layout(prog='dot')
    G.draw('../Fig/diagrama_segment_area.png')
    print("Diagrama segment_area creado: diagrama_segment_area.png")

def create_detection_flow_diagram():
    """Crea el diagrama de flujo de detección de picos"""
    G = pgv.AGraph(directed=True, strict=True)
    G.graph_attr.update(
        rankdir='LR',
        label='Flujo de Detección de Picos',
        labelloc='t',
        fontname='Arial',
        fontsize='12'
    )
    G.node_attr.update(
        shape='rectangle',
        style='rounded,filled',
        fillcolor='#fce4ec',
        fontname='Arial',
        fontsize='10'
    )
    
    # Nodos
    nodes = {
        'original': 'Datos originales',
        'apply_threshold': 'Aplicar threshold',
        'identify_minima': 'Identificar mínimos locales\nheight < left AND height < right\nAND height < threshold',
        'create_peaks': 'Crear Peak en cada mínimo',
        'expand_peaks': 'Expandir hasta encontrar\npendiente aceptable',
        'calculate_area': 'Calcular área bajo curva\nentre límites del pico',
        'generate_results': 'Generar resultados'
    }
    
    # Añadir nodos
    for key, label in nodes.items():
        G.add_node(key, label=label)
    
    # Conexiones
    edges = [
        ('original', 'apply_threshold'),
        ('apply_threshold', 'identify_minima'),
        ('identify_minima', 'create_peaks'),
        ('create_peaks', 'expand_peaks'),
        ('expand_peaks', 'calculate_area'),
        ('calculate_area', 'generate_results')
    ]
    
    # Añadir conexiones
    for edge in edges:
        G.add_edge(edge[0], edge[1])
    
    # Guardar diagrama
    G.layout(prog='dot')
    G.draw('../Fig/diagrama_deteccion_picos.png')
    print("Diagrama detección picos creado: diagrama_deteccion_picos.png")

def create_all_diagrams():
    """Crea todos los diagramas de flujo"""
    print("Creando diagramas de flujo...")
    create_main_diagram()
    create_expand_diagram()
    create_calculate_area_diagram()
    create_segment_area_diagram()
    create_detection_flow_diagram()
    print("\nTodos los diagramas han sido creados exitosamente!")
    print("Archivos generados:")
    print("1. diagrama_principal.png - Diagrama principal del método calculate()")
    print("2. diagrama_expand.png - Método expand() de Peak")
    print("3. diagrama_calculate_area.png - Método calculate_area()")
    print("4. diagrama_segment_area.png - Función calculate_segment_area()")
    print("5. diagrama_deteccion_picos.png - Flujo de detección de picos")

# Ejecutar la creación de diagramas
if __name__ == "__main__":
    try:
        create_all_diagrams()
    except Exception as e:
        print(f"Error al crear diagramas: {e}")
        print("Asegúrate de tener instalado:")
        print("1. pygraphviz: pip install pygraphviz")
        print("2. Graphviz: https://graphviz.org/download/")
