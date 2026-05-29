from graphviz import Digraph
import textwrap

def create_uml():
    dot = Digraph('UML', format='png')
    dot.attr(rankdir='TB', splines='ortho')
    dot.attr('node', shape='plaintext')
    
    # BaseMethod (abstract)
    base = '''<
<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
  <tr><td bgcolor="lightgray"><b><i>«abstract»<br/>BaseMethod</i></b></td></tr>
  <tr><td align="left" balign="left">+ __init__(master, catalog, table)</td></tr>
  <tr><td align="left" balign="left">+ calculate()</td></tr>
</table>>'''
    
    # ExplicitLimits
    explicit = '''<
<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
  <tr><td bgcolor="white"><b>ExplicitLimits</b></td></tr>
  <tr><td align="left" balign="left">+ __init__(master, catalog, table)</td></tr>
  <tr><td align="left" balign="left">+ calculate() <font color="green">«override»</font></td></tr>
  <tr><td align="left" balign="left"># generate_image_aux(...)</td></tr>
  <tr><td align="left" balign="left"># write_to_file(...)</td></tr>
</table>>'''
    
    # SymmetryMethod
    symmetry = '''<
<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
  <tr><td bgcolor="white"><b>SymmetryMethod</b></td></tr>
  <tr><td align="left" balign="left">+ __init__(master, catalog, table)</td></tr>
  <tr><td align="left" balign="left">+ calculate() <font color="green">«override»</font></td></tr>
  <tr><td align="left" balign="left"># generate_image_aux(...)</td></tr>
  <tr><td align="left" balign="left"># write_peaks_to_file(...)</td></tr>
</table>>'''
    
    # Peak
    peak = '''<
<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
  <tr><td bgcolor="lightblue"><b>Peak</b></td></tr>
  <tr><td align="left" balign="left">+ __init__(center, complete=False, ...)</td></tr>
  <tr><td align="left" balign="left">+ expand(heights, positions)</td></tr>
  <tr><td align="left" balign="left">+ calculate_area(dependent, independent)</td></tr>
  <tr><td align="left" balign="left">- _calculate_slope(p1, p2)</td></tr>
</table>>'''
    
    # Agregar nodos
    dot.node('BaseMethod', base)
    dot.node('ExplicitLimits', explicit)
    dot.node('SymmetryMethod', symmetry)
    dot.node('Peak', peak)
    
    # Relaciones
    dot.edge('BaseMethod', 'ExplicitLimits', arrowhead='empty', label=' extends')
    dot.edge('BaseMethod', 'SymmetryMethod', arrowhead='empty', label=' extends')
    dot.edge('SymmetryMethod', 'Peak', style='dashed', arrowhead='vee', label=' uses')
    
    # Notas
    dot.node('note1', textwrap.dedent('''\
        Sobreescribe calculate()
        Implementa suma de Riemann
        para límites explícitos'''),
        shape='note', style='filled', fillcolor='lightyellow')
    
    dot.node('note2', textwrap.dedent('''\
        Sobreescribe calculate()
        Detecta picos simétricos
        usando la clase Peak'''),
        shape='note', style='filled', fillcolor='lightyellow')
    
    dot.edge('note1', 'ExplicitLimits', style='dashed', arrowhead='none')
    dot.edge('note2', 'SymmetryMethod', style='dashed', arrowhead='none')
    
    return dot

# Generar diagrama
diagram = create_uml()
diagram.render('../Fig/uml_class', cleanup=True, view=True)
print("Diagrama generado como 'uml_graphviz.png'")
