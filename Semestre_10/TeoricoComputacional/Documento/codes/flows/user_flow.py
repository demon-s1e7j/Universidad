from graphviz import Digraph

dot = Digraph(comment='Flujo de Usuario')
dot.node('A', 'Inicio')
dot.node('B', 'Selección de datos, con ID de Vizier')
dot.node('C', 'Selección de la tabla necesaria')
dot.node('D', 'Selección del metodo a usar')
dot.node('E', 'Completado de los inputs necesarios')
dot.node('F', '¿Se esta satisfecho con los resultados?')
dot.node('G', 'Aprobado, continuar con la interpretación')

dot.edges(['AB', 'BC', 'CD', 'DE', 'EF'])
dot.edge('F', 'G', label='Sí')
dot.edge('F', 'D', label='No')
dot.render('../Fig/user_diagram', format='png', view=True)
