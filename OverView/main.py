import sqlite3

con = sqlite3.connect('./materias.db')
cur = con.cursor()

def encontrar_bool(valor: str) -> bool:
    return False if valor == 0 else True

continuar = ""

while continuar == "":
    continuar = input("Ultimo? ").strip()
    codigo = input("Ingresa el codigo: ").strip()
    nombre = input("Nombre de la materia: ").strip()
    creditos = int(input("Numero de creditos ").strip())
    cursado = encontrar_bool(input("Ya lo cursaste? ").strip())
    materia = (codigo, nombre, creditos, cursado)
    print(materia)
    cur.execute("""
        INSERT INTO materias VALUES (?, ?, ?, ?)
    """, materia)

value = cur.execute("""
SELECT * FROM materias
""")

for valor in value:
    print(valor)

confirmacion = input("Esta todo bien? [y/N] ").strip().upper()
confirmacion = True if confirmacion == "Y" else False

if confirmacion:
    con.commit()
