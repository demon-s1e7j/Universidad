import pygraphviz as pgv

# Crear un nuevo grafo
G = pgv.AGraph(directed=True, name="calculate_flowchart")

# Configurar propiedades del grafo
G.graph_attr.update(
    rankdir="TB",
    splines="ortho"
)

G.node_attr.update(
    shape="rectangle",
    style="rounded,filled",
    fillcolor="#e0f7fa",
    fontname="Arial"
)

G.edge_attr.update(
    fontname="Arial",
    fontsize=10
)

# Crear nodos
G.add_node("start", 
           label="Inicio función calculate()", 
           shape="ellipse", 
           fillcolor="#ffccbc")

G.add_node("query", 
           label="Ejecutar consulta SQL:\n- Seleccionar variables independiente y dependiente\n- Filtrar por rango y valores no nulos\n- Aplicar inversa si take_inverse_independent está activado",
           shape="box",
           fillcolor="#fff3e0")

G.add_node("get_data",
           label="Obtener columnas:\n- dependent = columna dependiente\n- independent = columna independiente\n  (aplicar inversa si take_inverse_independent)",
           fillcolor="#f3e5f5")

G.add_node("print_var",
           label="Imprimir variables",
           fillcolor="#e8f5e8")

G.add_node("init",
           label="Inicializar:\n- riemann_rectangles = []\n- riemann_sum = 0",
           fillcolor="#e1f5fe")

G.add_node("loop_start",
           label="Bucle for i=0 hasta len(independent)-2",
           shape="diamond",
           fillcolor="#ffe0b2")

G.add_node("calc_rect",
           label="Calcular rectángulo:\n- base = independent[i+1] - independent[i]\n- altura = dependent[i]\n- área = base × altura",
           fillcolor="#fce4ec")

G.add_node("accumulate",
           label="Acumular:\n- riemann_sum += área\n- Añadir diccionario a riemann_rectangles",
           fillcolor="#f1f8e9")

G.add_node("loop_end",
           label="i++",
           fillcolor="#fff8e1")

G.add_node("check_image",
           label="¿generate_image = True?",
           shape="diamond",
           fillcolor="#e8eaf6")

G.add_node("gen_image",
           label="Llamar generate_image_aux(independent,\n dependent, riemann_rectangles,\n riemann_sum)",
           fillcolor="#fff3e0")

G.add_node("write_file",
           label="Llamar write_to_file(riemann_rectangles)",
           fillcolor="#e0f2f1")

G.add_node("end",
           label="Fin función",
           shape="ellipse",
           fillcolor="#ffccbc")

# Crear conexiones (edges)
edges = [
    ("start", "query"),
    ("query", "get_data"),
    ("get_data", "print_var"),
    ("print_var", "init"),
    ("init", "loop_start"),
    ("loop_start", "calc_rect", "Sí (i ≤ n-2)"),
    ("calc_rect", "accumulate"),
    ("accumulate", "loop_end"),
    ("loop_end", "loop_start"),
    ("loop_start", "check_image", "No (fin del bucle)"),
    ("check_image", "gen_image", "Sí"),
    ("gen_image", "write_file"),
    ("check_image", "write_file", "No"),
    ("write_file", "end")
]

# Agregar edges con etiquetas
for edge in edges:
    if len(edge) == 3:
        G.add_edge(edge[0], edge[1], label=edge[2])
    else:
        G.add_edge(edge[0], edge[1])

# Crear un subgrafo para agrupar los nodos del bucle
subgraph = G.add_subgraph(
    name="cluster_loop",
    label="Cálculo de suma de Riemann (rectángulos izquierdos)",
    style="dashed",
    color="gray",
    fillcolor="#f5f5f5"
)

subgraph.add_nodes_from(["calc_rect", "accumulate", "loop_end"])

# Aplicar layout
G.layout(prog="dot")

# Guardar en diferentes formatos
G.draw("../Fig/diagrama_calculate.png")  # Para PNG
G.draw("diagrama_calculate.pdf")  # Para PDF
G.draw("diagrama_calculate.svg")  # Para SVG (vectorial)

# Para mostrar en Jupyter Notebook (opcional)
# G.draw(format="png")  # Esto mostraría la imagen en Jupyter

print("Diagrama generado exitosamente")
